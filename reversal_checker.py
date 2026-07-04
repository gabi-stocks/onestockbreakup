#!/usr/bin/env python3
"""
reversal_checker.py
-------------------
Daily trend-reversal scanner based on a 6-parameter checklist.

Checks per ticker:
  1. Price structure  -> Higher Low + break of last swing High (Higher High)
  2. Moving averages  -> close above MA10 & MA20, MA10 rising
  3. MACD (12,26,9)   -> MACD above Signal AND histogram rising
  4. RSI (14)         -> RSI > 50  OR  bullish divergence with RSI rising
  5. Volume / RVOL    -> reversal day on high RVOL  OR  up-volume > down-volume
  6. Volume Profile   -> close holding above the POC (heaviest-volume price)

BUY trigger only if >= MIN_SIGNALS confirm AND (#1 structure) AND (#5 volume).

Optional email (Gmail SMTP) + optional MORNING_MODE.
Analysis tooling, not investment advice.
"""

import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

# ---------------- Config (via env / GitHub Secrets) ----------------
TICKERS = [t.strip().upper() for t in os.environ.get("TICKERS", "ORCL").split(",") if t.strip()]
PERIOD = "1y"
MIN_SIGNALS = int(os.environ.get("MIN_SIGNALS", "4"))
MORNING_MODE = os.environ.get("MORNING_MODE", "false").lower() == "true"
EMAIL_ONLY_ON_TRIGGER = os.environ.get("EMAIL_ONLY_ON_TRIGGER", "false").lower() == "true"
PIVOT_L, PIVOT_R = 3, 3
REPORT_DIR = "reports"
TICKERS_FILE = "tickers.txt"


def load_tickers():
    """Priority: tickers.txt (one symbol per line, '#'=comment) -> TICKERS env -> ORCL."""
    if os.path.exists(TICKERS_FILE):
        syms = []
        for line in open(TICKERS_FILE, encoding="utf-8"):
            line = line.split("#")[0].strip().upper()
            if line:
                syms.append(line)
        if syms:
            return syms
    return [t.strip().upper() for t in os.environ.get("TICKERS", "ORCL").split(",") if t.strip()]


# ---------------- Indicators ----------------
def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def macd(series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    line = ema_fast - ema_slow
    sig = line.ewm(span=signal, adjust=False).mean()
    return line, sig, line - sig


def pivots(values, left, right, kind="low"):
    out = []
    n = len(values)
    for i in range(left, n - right):
        seg = values[i - left:i + right + 1]
        if kind == "low" and values[i] == seg.min():
            out.append(i)
        if kind == "high" and values[i] == seg.max():
            out.append(i)
    return out


def volume_profile_poc(close, volume, bins=50):
    lo, hi = float(close.min()), float(close.max())
    if hi <= lo:
        return float(close.iloc[-1])
    edges = np.linspace(lo, hi, bins + 1)
    idx = np.clip(np.digitize(close.values, edges) - 1, 0, bins - 1)
    vol_bin = np.zeros(bins)
    for b, v in zip(idx, volume.values):
        vol_bin[b] += v
    poc = int(vol_bin.argmax())
    return float((edges[poc] + edges[poc + 1]) / 2)


def intraday_context(ticker):
    """Best-effort: today's open -> latest price (delayed). Used in morning mode."""
    try:
        intra = yf.Ticker(ticker).history(period="1d", interval="5m")
        if len(intra):
            o = float(intra["Open"].iloc[0])
            cur = float(intra["Close"].iloc[-1])
            return f"  [today so far: open {o:.2f} -> {cur:.2f} ({(cur/o-1)*100:+.2f}%) | DELAYED]"
    except Exception:
        pass
    return ""


# ---------------- Core analysis ----------------
def analyze(ticker, morning=False):
    df = yf.Ticker(ticker).history(period=PERIOD, auto_adjust=False).dropna()
    if len(df) < 60:
        return {"ticker": ticker, "error": "not enough data"}

    ctx = ""
    if morning:
        # Drop today's PARTIAL daily bar so we analyze only completed candles.
        try:
            today_et = datetime.now(ZoneInfo("America/New_York")).date()
            if df.index[-1].date() == today_et:
                df = df.iloc[:-1]
        except Exception:
            pass
        ctx = intraday_context(ticker)

    close, high, low, vol, op = df["Close"], df["High"], df["Low"], df["Volume"], df["Open"]
    last_close = float(close.iloc[-1])

    ma10, ma20, ma50 = close.rolling(10).mean(), close.rolling(20).mean(), close.rolling(50).mean()
    rsi_s = rsi(close)
    macd_line, sig_line, hist = macd(close)
    rvol = vol / vol.rolling(20).mean()

    plows = pivots(low.values, PIVOT_L, PIVOT_R, "low")
    phighs = pivots(high.values, PIVOT_L, PIVOT_R, "high")

    checks, detail = {}, {}

    # 1) Price structure
    higher_low = broke_high = False
    if len(plows) >= 2:
        higher_low = low.iloc[plows[-1]] > low.iloc[plows[-2]]
    last_swing_high = float(high.iloc[phighs[-1]]) if phighs else float("nan")
    if phighs:
        broke_high = last_close > last_swing_high
    checks["1_price_structure"] = bool(higher_low and broke_high)
    detail["1_price_structure"] = f"HigherLow={higher_low}, brokeSwingHigh={broke_high} (last swing high={last_swing_high:.2f})"

    # 2) Moving averages
    above_short = last_close > ma10.iloc[-1] and last_close > ma20.iloc[-1]
    ma10_rising = ma10.iloc[-1] > ma10.iloc[-3]
    golden_short = ma10.iloc[-1] > ma50.iloc[-1]
    checks["2_moving_averages"] = bool(above_short and ma10_rising)
    detail["2_moving_averages"] = (f"close>{ma10.iloc[-1]:.2f}(MA10) & >{ma20.iloc[-1]:.2f}(MA20)={above_short}, "
                                   f"MA10 rising={ma10_rising}, MA10>MA50={golden_short}")

    # 3) MACD
    hist_rising = hist.iloc[-1] > hist.iloc[-2] > hist.iloc[-3]
    macd_above = macd_line.iloc[-1] > sig_line.iloc[-1]
    checks["3_macd"] = bool(macd_above and hist_rising)
    detail["3_macd"] = (f"MACD={macd_line.iloc[-1]:.2f} vs Signal={sig_line.iloc[-1]:.2f} (above={macd_above}), "
                        f"hist={hist.iloc[-1]:.2f} rising={hist_rising}")

    # 4) RSI (+ bullish divergence)
    bull_div = False
    if len(plows) >= 2:
        p1, p2 = plows[-2], plows[-1]
        bull_div = (low.iloc[p2] < low.iloc[p1]) and (rsi_s.iloc[p2] > rsi_s.iloc[p1])
    rsi_now = float(rsi_s.iloc[-1])
    rsi_rising = rsi_s.iloc[-1] > rsi_s.iloc[-2]
    checks["4_rsi"] = bool(rsi_now > 50 or (bull_div and rsi_rising))
    detail["4_rsi"] = f"RSI={rsi_now:.2f} rising={rsi_rising}, bullishDivergence={bull_div}"

    # 5) Volume / RVOL
    rvol_today = float(rvol.iloc[-1]) if not np.isnan(rvol.iloc[-1]) else 0.0
    latest_up = last_close > float(op.iloc[-1])
    recent = df.tail(10)
    up_vol = recent.loc[recent["Close"] >= recent["Open"], "Volume"].mean()
    down_vol = recent.loc[recent["Close"] < recent["Open"], "Volume"].mean()
    up_gt_down = np.nan_to_num(up_vol) > np.nan_to_num(down_vol)
    checks["5_volume"] = bool((latest_up and rvol_today > 1.5) or up_gt_down)
    detail["5_volume"] = f"day up={latest_up}, RVOL={rvol_today:.2f}, up>downVol={up_gt_down}"

    # 6) Volume Profile POC
    poc = volume_profile_poc(close, vol)
    checks["6_volume_profile"] = bool(last_close > poc)
    detail["6_volume_profile"] = f"close={last_close:.2f} vs POC={poc:.2f} (above={last_close > poc})"

    n_conf = sum(checks.values())
    mandatory = checks["1_price_structure"] and checks["5_volume"]
    buy = n_conf >= MIN_SIGNALS and mandatory

    # --- Proximity score per parameter (0..1, higher = closer to passing) ---
    # Based on how many sub-conditions are met + light momentum credit.
    def c01(x):
        return max(0.0, min(1.0, float(x)))

    progress = {
        "1_price_structure": np.mean([bool(higher_low), bool(broke_high)]),
        "2_moving_averages": np.mean([last_close > ma10.iloc[-1],
                                      last_close > ma20.iloc[-1], bool(ma10_rising)]),
        "3_macd": np.mean([bool(macd_above), bool(hist_rising)]),
        "4_rsi": np.mean([rsi_now > 50, bool(rsi_rising), bool(bull_div)]),
        "5_volume": np.mean([bool(latest_up and rvol_today > 1.5),
                             bool(up_gt_down), rvol_today > 1.2]),
        "6_volume_profile": 1.0 if last_close > poc else 0.5 * c01(last_close / poc),
    }
    progress = {k: round(float(v), 3) for k, v in progress.items()}
    # closest FAILING parameter (what to watch next)
    failing = {k: progress[k] for k in checks if not checks[k]}
    closest = max(failing, key=failing.get) if failing else None

    return {
        "ticker": ticker,
        "date": df.index[-1].strftime("%Y-%m-%d"),
        "close": round(last_close, 2),
        "rsi": round(rsi_now, 1),
        "confirmed": n_conf,
        "mandatory_met": mandatory,
        "BUY_TRIGGER": buy,
        "context": ctx,
        "checks": checks,
        "detail": detail,
        "progress": progress,
        "closest": closest,
    }


# ---------------- Email ----------------
def send_email(subject, text_body, html_body=None):
    user = os.environ.get("GMAIL_USER")
    pw = os.environ.get("GMAIL_APP_PASSWORD")
    to = os.environ.get("MAIL_TO", user)
    if not (user and pw):
        print("Email skipped: GMAIL_USER / GMAIL_APP_PASSWORD not set.")
        return
    if html_body:
        msg = MIMEMultipart("alternative")
        msg.attach(MIMEText(text_body, "plain", "utf-8"))   # fallback
        msg.attach(MIMEText(html_body, "html", "utf-8"))     # preferred
    else:
        msg = MIMEText(text_body, "plain", "utf-8")
    msg["Subject"], msg["From"], msg["To"] = subject, user, to
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(user, pw)
            s.sendmail(user, [a.strip() for a in to.split(",")], msg.as_string())
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Email FAILED: {e}")


# ---------------- Reporting ----------------
def render(r):
    if "error" in r:
        return f"## {r['ticker']}\n  ERROR: {r['error']}\n"
    names = {
        "1_price_structure": "1. Price structure (HL+HH)",
        "2_moving_averages": "2. Moving averages",
        "3_macd": "3. MACD",
        "4_rsi": "4. RSI",
        "5_volume": "5. Volume / RVOL",
        "6_volume_profile": "6. Volume Profile POC",
    }
    lines = [f"## {r['ticker']}  ({r['date']})  close={r['close']}  RSI={r['rsi']}{r['context']}"]
    for k, label in names.items():
        mark = "PASS" if r["checks"][k] else "----"
        lines.append(f"  [{mark}] {label}\n         {r['detail'][k]}")
    verdict = "BUY TRIGGER - reversal confirmed" if r["BUY_TRIGGER"] else "NO ENTRY - wait for confirmation"
    lines.append(f"  >> {r['confirmed']}/6 confirmed | mandatory(structure+volume)={r['mandatory_met']}")
    lines.append(f"  >> {verdict}\n")
    return "\n".join(lines)


# ---- Hebrew labels + explanations for the HTML email table ----
HE = {
    "1_price_structure": ("מבנה מחיר (שפל/פסגה עולים)",
        "עובר רק כשנוצר שפל גבוה מהקודם ונשברת פסגה קודמת. זה הסימן היחיד להיפוך אמיתי — חובה."),
    "2_moving_averages": ("ממוצעים נעים 10/20/50",
        "עובר כשהמחיר סוגר מעל MA10 ו-MA20 וה-MA10 מתחיל לעלות (ביטול המבנה היורד)."),
    "3_macd": ("MACD (12,26,9)",
        "עובר כש-MACD חוצה מעל הסיגנל וההיסטוגרמה עולה. היסטוגרמה שעולה לבדה = האטה בלבד, לא אישור."),
    "4_rsi": ("RSI (14)",
        "עובר כש-RSI מעל 50 או שיש דיברגנס שורי. RSI נמוך (oversold) לבדו אינו אות קנייה."),
    "5_volume": ("נפח / RVOL",
        "עובר ביום היפוך במחזור גבוה (RVOL מעל 1.5) או כשמחזור העליות גובר על הירידות. חובה."),
    "6_volume_profile": ("פרופיל נפח (POC)",
        "עובר כשהמחיר מחזיק מעל אזור הנפח הכבד — כלומר יש קרקע (תמיכה) מתחת לרגליים."),
}

# Short "what to watch next" hint for the closest-to-passing parameter
CLOSEST_HINT = {
    "1_price_structure": "המבנה היורד עדיין שולט — צריך שפל גבוה יותר ושבירת פסגה קודמת.",
    "2_moving_averages": "המחיר מתחת לממוצעים — צריך סגירה מעל MA10 ואז MA20.",
    "3_macd": "ההיסטוגרמה מתחילה להאט — האזהרה המוקדמת. עקוב אחר חציית MACD מעל הסיגנל.",
    "4_rsi": "ה-RSI עוד לא מתאושש — צריך עלייה מעל 50 או דיברגנס שורי.",
    "5_volume": "הנפח כמעט מספיק — צריך יום עלייה במחזור גבוה (RVOL מעל 1.5).",
    "6_volume_profile": "המחיר מתקרב לאזור הנפח הכבד — צריך סגירה מעליו כדי לקבל תמיכה.",
}


def render_html(r):
    if "error" in r:
        return f"<h3>{r['ticker']}</h3><p style='color:#b00'>שגיאה: {r['error']}</p>"

    rows = ""
    for k, (label, expl) in HE.items():
        ok = r["checks"][k]
        pill_bg = "#0a7d33" if ok else "#b02a2a"
        pill_txt = "עבר ✓" if ok else "נכשל ✗"
        rows += (
            "<tr>"
            f"<td style='padding:10px;border-bottom:1px solid #eee;font-weight:600'>{label}</td>"
            f"<td style='padding:10px;border-bottom:1px solid #eee;text-align:center;white-space:nowrap'>"
            f"<span style='background:{pill_bg};color:#fff;border-radius:12px;padding:3px 10px;font-size:13px'>{pill_txt}</span></td>"
            f"<td style='padding:10px;border-bottom:1px solid #eee;direction:ltr;text-align:left;"
            f"font-family:monospace;font-size:12px;color:#333'>{r['detail'][k]}</td>"
            f"<td style='padding:10px;border-bottom:1px solid #eee;color:#444;font-size:13px'>{expl}</td>"
            "</tr>"
        )

    buy = r["BUY_TRIGGER"]
    banner_bg = "#0a7d33" if buy else "#b02a2a"
    banner_txt = (f"טריגר כניסה — ההיפוך אושר ({r['confirmed']}/6)"
                  if buy else
                  f"אין כניסה — להמתין לאישור ({r['confirmed']}/6 בלבד)")

    # "closest to passing" strip
    if buy:
        strip = "<b>כל הפרמטרים תומכים בהיפוך.</b>"
    elif r.get("closest"):
        ck = r["closest"]
        pct = int(round(r["progress"][ck] * 100))
        strip = (f"🔎 <b>הכי קרוב לעבור:</b> {HE[ck][0]} "
                 f"(~{pct}%) — {CLOSEST_HINT[ck]}")
    else:
        strip = "אף פרמטר עדיין לא קרוב — הטרנד היורד חזק."

    return f"""
    <div style="border:1px solid #ddd;border-radius:10px;overflow:hidden;margin-bottom:18px">
      <div style="background:#111;color:#fff;padding:14px 16px">
        <span style="font-size:20px;font-weight:700">{r['ticker']}</span>
        <span style="opacity:.8;font-size:13px">&nbsp;·&nbsp;נכון ל-{r['date']}</span>
        <span style="float:left;direction:ltr;font-family:monospace">close {r['close']} | RSI {r['rsi']}</span>
      </div>
      <div style="background:#fff7e6;border-bottom:1px solid #eee;padding:10px 16px;font-size:13px;color:#7a5900">
        {strip}
      </div>
      <table style="border-collapse:collapse;width:100%;background:#fff">
        <thead>
          <tr style="background:#f4f4f4;font-size:13px;color:#555">
            <th style="padding:8px 10px;text-align:right">פרמטר</th>
            <th style="padding:8px 10px;text-align:center">סטטוס</th>
            <th style="padding:8px 10px;text-align:right">ערכים בפועל</th>
            <th style="padding:8px 10px;text-align:right">מה זה אומר</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
      <div style="background:{banner_bg};color:#fff;padding:12px 16px;font-size:16px;font-weight:700;text-align:center">
        {banner_txt}
      </div>
    </div>
    """


def build_html(results, mode_he):
    body = "".join(render_html(r) for r in results)
    stamp = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC"
    return f"""<!DOCTYPE html>
<html dir="rtl" lang="he"><head><meta charset="utf-8"></head>
<body style="font-family:Arial,Helvetica,sans-serif;background:#fafafa;margin:0;padding:18px;direction:rtl;text-align:right">
  <div style="max-width:760px;margin:0 auto">
    <h2 style="margin:0 0 4px">דוח בודק היפוך מגמה</h2>
    <p style="color:#666;margin:0 0 16px;font-size:13px">
      {stamp} · מצב: {mode_he} · תנאי כניסה: לפחות {MIN_SIGNALS} מתוך 6, וחובה מבנה מחיר + נפח.
    </p>
    {body}
    <p style="color:#999;font-size:11px;margin-top:16px">
      כלי ניתוח אוטומטי, אינו ייעוץ השקעות. ✓=הפרמטר תומך בהיפוך, ✗=עדיין לא.
    </p>
  </div>
</body></html>"""


def main():
    tickers = load_tickers()
    results = [analyze(t, morning=MORNING_MODE) for t in tickers]
    mode = "MORNING (through last completed close)" if MORNING_MODE else "END-OF-DAY"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = (f"# Reversal Checker — {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} [{mode}]\n"
            f"(needs >= {MIN_SIGNALS}/6 + mandatory structure & volume)\n\n"
            + "\n".join(render(r) for r in results))
    print(text)

    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(os.path.join(REPORT_DIR, f"reversal_{stamp}.md"), "w") as f:
        f.write(text)
    with open(os.path.join(REPORT_DIR, "latest.md"), "w") as f:
        f.write(text)
    with open(os.path.join(REPORT_DIR, "latest.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)

    mode_he = "בוקר (עד סגירה מלאה אחרונה)" if MORNING_MODE else "סוף יום"
    html = build_html(results, mode_he)
    with open(os.path.join(REPORT_DIR, "latest.html"), "w") as f:
        f.write(html)

    trigger = any(r.get("BUY_TRIGGER") for r in results)
    if not EMAIL_ONLY_ON_TRIGGER or trigger:
        tag = "TRIGGER" if trigger else "report"
        send_email(f"[Reversal] {tag} {stamp} - {','.join(tickers)}", text, html_body=html)


if __name__ == "__main__":
    main()
