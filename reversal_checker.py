#!/usr/bin/env python3
"""
reversal_checker.py
-------------------
Daily trend-reversal scanner based on a 6-parameter checklist.

Checks per ticker:
  1. Price structure  -> Higher Low + break of last swing High (Higher High)
  2. Moving averages  -> close above MA10 & MA20, MA10 rising
  3. MACD (12,26,9)   -> MACD above Signal AND histogram rising
  4. RSI (14)         -> RSI > RSI_THRESHOLD  OR  bullish divergence with RSI rising
  5. Volume / RVOL    -> reversal day on high RVOL  OR  up-volume > down-volume (with an RVOL floor)
  6. Volume Profile   -> close holding above the POC (heaviest-volume price)

BUY trigger only if >= MIN_SIGNALS confirm AND (#1 structure) AND (#5 volume)
AND (if REQUIRE_MARKET_REGIME) SPY is above its 200d MA.
All thresholds are env-configurable -- see the Config section below for current
defaults and reports/backtest_results.md for why they're set where they are.

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

# --- Backtested thresholds (2026-08-01, backtest.py on 6 tickers / 5y) ---
# Defaults below match the "IMPROVED" variant, which beat the original
# ("BASELINE": RSI_THRESHOLD=50, RVOL_SOFT_FLOOR=0, POC_WINDOW=full-history,
# REQUIRE_MARKET_REGIME=false) on 10d/20d winrate and avg forward return,
# at the cost of ~fewer, more selective signals. See reports/backtest_results.md
# for the numbers and rerun backtest.py if tickers.txt changes materially.
# Set any of these env vars in the workflow to override / revert to baseline.
RSI_THRESHOLD = float(os.environ.get("RSI_THRESHOLD", "55"))
RVOL_THRESHOLD = float(os.environ.get("RVOL_THRESHOLD", "1.5"))
RVOL_SOFT_FLOOR = float(os.environ.get("RVOL_SOFT_FLOOR", "1.1"))
_poc_window_env = os.environ.get("POC_WINDOW", "120")
POC_WINDOW = int(_poc_window_env) if _poc_window_env.strip() else None
REQUIRE_MARKET_REGIME = os.environ.get("REQUIRE_MARKET_REGIME", "true").lower() == "true"


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


MAX_NEWS_ITEMS = int(os.environ.get("MAX_NEWS_ITEMS", "3"))
NEWS_LOOKBACK_DAYS = int(os.environ.get("NEWS_LOOKBACK_DAYS", "30"))


def fetch_recent_headlines(ticker, max_items=MAX_NEWS_ITEMS, lookback_days=NEWS_LOOKBACK_DAYS):
    """Free headline pull from Yahoo Finance via yfinance -- no API key, no cost.
    Returns a list of {title, publisher, link, date} for the most recent items
    within lookback_days, newest first (sorted by exact publish timestamp, not
    just by day, so same-day items are still ordered correctly). Returns [] on
    any failure (format changes, network hiccup, no news available) so this
    never blocks the run. yfinance's .news shape has changed across versions,
    so this handles both the flat dict format and the newer nested 'content'
    format defensively."""
    try:
        raw = yf.Ticker(ticker).news or []
    except Exception as e:
        print(f"WARNING: headline fetch failed for {ticker} ({e}); skipping.")
        return []

    cutoff = datetime.now(timezone.utc).timestamp() - lookback_days * 86400
    items = []
    for entry in raw:
        node = entry.get("content", entry) if isinstance(entry, dict) else {}
        title = node.get("title") or entry.get("title")
        if not title:
            continue
        publisher = (
            (node.get("provider") or {}).get("displayName")
            or node.get("publisher")
            or entry.get("publisher")
            or ""
        )
        link = (
            (node.get("canonicalUrl") or {}).get("url")
            or (node.get("clickThroughUrl") or {}).get("url")
            or entry.get("link")
            or ""
        )
        ts = entry.get("providerPublishTime")
        pub_date = node.get("pubDate") or node.get("displayTime")
        epoch = None
        if isinstance(ts, (int, float)):
            epoch = ts
        elif isinstance(pub_date, str):
            try:
                epoch = datetime.fromisoformat(pub_date.replace("Z", "+00:00")).timestamp()
            except Exception:
                epoch = None
        if epoch is not None and epoch < cutoff:
            continue
        date_str = (
            datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            if epoch is not None else ""
        )
        # Items with no timestamp sort last (treated as oldest) rather than
        # landing wherever the API happened to return them.
        items.append({"title": title, "publisher": publisher, "link": link,
                       "date": date_str, "_epoch": epoch if epoch is not None else -1})

    items.sort(key=lambda x: x["_epoch"], reverse=True)
    for it in items:
        del it["_epoch"]
    return items[:max_items]


def fetch_market_regime():
    """True if SPY is above its 200d MA (the 'IMPROVED' backtest variant's
    market-regime filter). Falls back to True (i.e. don't block) if the SPY
    fetch fails, so a network hiccup on the index never crashes the whole run."""
    if not REQUIRE_MARKET_REGIME:
        return True
    try:
        spy = yf.Ticker("SPY").history(period="1y", auto_adjust=False).dropna()
        if len(spy) < 200:
            return True
        ma200 = spy["Close"].rolling(200).mean()
        return bool(spy["Close"].iloc[-1] > ma200.iloc[-1])
    except Exception as e:
        print(f"WARNING: market regime check failed ({e}); not gating on it this run.")
        return True


BACKTEST_RESULTS_FILE = os.path.join(REPORT_DIR, "backtest_results.json")


def load_reliability():
    """Per-ticker historical reliability from the last backtest.py run, read from
    the IMPROVED variant (it matches the thresholds actually in use here). Returns
    {ticker: {n_triggers, winrate_20d_%, avg_fwd_20d_%, ...}}, or {} if no backtest
    has been run yet / the file can't be read."""
    if not os.path.exists(BACKTEST_RESULTS_FILE):
        return {}
    try:
        with open(BACKTEST_RESULTS_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"WARNING: could not read {BACKTEST_RESULTS_FILE} ({e}); skipping reliability tags.")
        return {}
    out = {}
    for row in data.get("per_ticker", []):
        if row.get("variant") == "IMPROVED":
            out[row["ticker"]] = row
    return out


def reliability_label(row):
    """(short tier label, one-line explanation) from a ticker's backtested stats.
    Always names the actual n and win rate behind the label -- never just a bare
    tier -- so the reader can judge the label's own reliability too."""
    if not row or not row.get("n_triggers"):
        return ("אין נתוני בקטסט",
                "לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).")
    n = row["n_triggers"]
    win20 = row.get("winrate_20d_%")
    avg20 = row.get("avg_fwd_20d_%")
    if n < 5:
        return (f"מדגם קטן מדי ({n} עסקאות)",
                f"רק {n} טריגרים היסטוריים נמצאו בבקטסט — מעט מדי כדי לשפוט אמינות. התייחס לטריגר בזהירות כפולה.")
    if win20 is None:
        return (f"נתונים חלקיים ({n} עסקאות)", "לא היה מספיק דאטה קדימה כדי לחשב win rate.")
    if win20 >= 55 and n >= 10:
        tier = "אמינות גבוהה יחסית"
    elif win20 >= 50:
        tier = "אמינות בינונית"
    else:
        tier = "אמינות נמוכה"
    detail = (f"בבקטסט (5 שנים אחורה): {n} עסקאות בלתי-תלויות, "
              f"win rate ל-20 יום={win20}%, תשואה ממוצעת ל-20 יום={avg20}%.")
    return (tier, detail)


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
def analyze(ticker, morning=False, market_ok=True):
    try:
        df = yf.Ticker(ticker).history(period=PERIOD, auto_adjust=False).dropna()
    except Exception as e:
        return {"ticker": ticker, "error": f"data fetch failed: {e}"}
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
    checks["4_rsi"] = bool(rsi_now > RSI_THRESHOLD or (bull_div and rsi_rising))
    detail["4_rsi"] = f"RSI={rsi_now:.2f} rising={rsi_rising}, bullishDivergence={bull_div}"

    # 5) Volume / RVOL
    rvol_today = float(rvol.iloc[-1]) if not np.isnan(rvol.iloc[-1]) else 0.0
    latest_up = last_close > float(op.iloc[-1])
    recent = df.tail(10)
    up_vol = recent.loc[recent["Close"] >= recent["Open"], "Volume"].mean()
    down_vol = recent.loc[recent["Close"] < recent["Open"], "Volume"].mean()
    up_gt_down = np.nan_to_num(up_vol) > np.nan_to_num(down_vol)
    checks["5_volume"] = bool(
        (latest_up and rvol_today > RVOL_THRESHOLD)
        or (up_gt_down and rvol_today > RVOL_SOFT_FLOOR)
    )
    detail["5_volume"] = f"day up={latest_up}, RVOL={rvol_today:.2f}, up>downVol={up_gt_down}"

    # 6) Volume Profile POC (rolling window if POC_WINDOW is set, else full history)
    poc_close = close.tail(POC_WINDOW) if POC_WINDOW else close
    poc_vol = vol.tail(POC_WINDOW) if POC_WINDOW else vol
    poc = volume_profile_poc(poc_close, poc_vol)
    checks["6_volume_profile"] = bool(last_close > poc)
    detail["6_volume_profile"] = f"close={last_close:.2f} vs POC={poc:.2f} (above={last_close > poc})"

    n_conf = sum(checks.values())
    mandatory = checks["1_price_structure"] and checks["5_volume"]
    buy = n_conf >= MIN_SIGNALS and mandatory and market_ok

    # --- Proximity score per parameter (0..1, higher = closer to passing) ---
    # Based on how many sub-conditions are met + light momentum credit.
    def c01(x):
        return max(0.0, min(1.0, float(x)))

    progress = {
        "1_price_structure": np.mean([bool(higher_low), bool(broke_high)]),
        "2_moving_averages": np.mean([last_close > ma10.iloc[-1],
                                      last_close > ma20.iloc[-1], bool(ma10_rising)]),
        "3_macd": np.mean([bool(macd_above), bool(hist_rising)]),
        "4_rsi": np.mean([rsi_now > RSI_THRESHOLD, bool(rsi_rising), bool(bull_div)]),
        "5_volume": np.mean([bool(latest_up and rvol_today > RVOL_THRESHOLD),
                             bool(up_gt_down), rvol_today > RVOL_SOFT_FLOOR]),
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
        "market_regime_ok": market_ok,
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
    tier, rel_detail = reliability_label(r.get("reliability"))
    lines.append(f"  [אמינות היסטורית: {tier}] {rel_detail}")
    if r.get("headlines"):
        lines.append("  [חדשות אחרונות, מהחדש לישן]")
        for h in r["headlines"]:
            date_part = f"{h['date']} " if h["date"] else ""
            lines.append(f"         - {date_part}{h['title']} ({h['publisher']})")
    for k, label in names.items():
        mark = "PASS" if r["checks"][k] else "----"
        lines.append(f"  [{mark}] {label}\n         {r['detail'][k]}")
    verdict = "BUY TRIGGER - reversal confirmed" if r["BUY_TRIGGER"] else "NO ENTRY - wait for confirmation"
    lines.append(f"  >> {r['confirmed']}/6 confirmed | mandatory(structure+volume)={r['mandatory_met']}")
    if not r.get("market_regime_ok", True) and r["mandatory_met"] and r["confirmed"] >= MIN_SIGNALS:
        lines.append("  >> (would have triggered, but blocked: SPY below its 200d MA)")
    lines.append(f"  >> {verdict}\n")
    return "\n".join(lines)


# ---- Hebrew labels + explanations for the HTML email table ----
# Built dynamically (not a static dict) so the explanation text always matches
# the thresholds actually in effect (RSI_THRESHOLD etc.), even if you tune them
# via env vars later without touching this file.
def build_he():
    poc_desc = f"{POC_WINDOW} הימים האחרונים" if POC_WINDOW else "כל ההיסטוריה הזמינה"
    return {
        "1_price_structure": ("מבנה מחיר (שפל/פסגה עולים)",
            "עובר רק כשנוצר שפל גבוה מהקודם ונשברת פסגה קודמת. זה הסימן היחיד להיפוך אמיתי — חובה."),
        "2_moving_averages": ("ממוצעים נעים 10/20/50",
            "עובר כשהמחיר סוגר מעל MA10 ו-MA20 וה-MA10 מתחיל לעלות (ביטול המבנה היורד)."),
        "3_macd": ("MACD (12,26,9)",
            "עובר כש-MACD חוצה מעל הסיגנל וההיסטוגרמה עולה. היסטוגרמה שעולה לבדה = האטה בלבד, לא אישור."),
        "4_rsi": ("RSI (14)",
            f"עובר כש-RSI מעל {RSI_THRESHOLD:g} או שיש דיברגנס שורי. RSI נמוך (oversold) לבדו אינו אות קנייה."),
        "5_volume": ("נפח / RVOL",
            f"עובר ביום היפוך במחזור גבוה (RVOL מעל {RVOL_THRESHOLD:g}), או כשמחזור העליות גובר על הירידות "
            f"וה-RVOL מעל {RVOL_SOFT_FLOOR:g} (רצפת פעילות מינימלית — שבוע שקט לא מספיק). חובה."),
        "6_volume_profile": ("פרופיל נפח (POC)",
            f"עובר כשהמחיר מחזיק מעל אזור הנפח הכבד, מחושב על {poc_desc} — כלומר יש תמיכה טרייה מתחת לרגליים."),
    }

# Short "what to watch next" hint for the closest-to-passing parameter
def build_closest_hint():
    return {
        "1_price_structure": "המבנה היורד עדיין שולט — צריך שפל גבוה יותר ושבירת פסגה קודמת.",
        "2_moving_averages": "המחיר מתחת לממוצעים — צריך סגירה מעל MA10 ואז MA20.",
        "3_macd": "ההיסטוגרמה מתחילה להאט — האזהרה המוקדמת. עקוב אחר חציית MACD מעל הסיגנל.",
        "4_rsi": f"ה-RSI עוד לא מתאושש — צריך עלייה מעל {RSI_THRESHOLD:g} או דיברגנס שורי.",
        "5_volume": f"הנפח כמעט מספיק — צריך יום עלייה במחזור גבוה (RVOL מעל {RVOL_THRESHOLD:g}).",
        "6_volume_profile": "המחיר מתקרב לאזור הנפח הכבד — צריך סגירה מעליו כדי לקבל תמיכה.",
    }


def render_html(r):
    if "error" in r:
        return f"<h3>{r['ticker']}</h3><p style='color:#b00'>שגיאה: {r['error']}</p>"

    HE = build_he()
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
    blocked_by_regime = (not r.get("market_regime_ok", True)) and r["mandatory_met"] and r["confirmed"] >= MIN_SIGNALS
    if buy:
        strip = "<b>כל הפרמטרים תומכים בהיפוך.</b>"
    elif blocked_by_regime:
        strip = "⚠️ <b>כל הפרמטרים עברו, אך החסימה היא מצב השוק</b> — מדד ה-SPY מתחת לממוצע 200 יום, אז הטריגר נחסם."
    elif r.get("closest"):
        ck = r["closest"]
        pct = int(round(r["progress"][ck] * 100))
        strip = (f"🔎 <b>הכי קרוב לעבור:</b> {HE[ck][0]} "
                 f"(~{pct}%) — {build_closest_hint()[ck]}")
    else:
        strip = "אף פרמטר עדיין לא קרוב — הטרנד היורד חזק."

    tier, rel_detail = reliability_label(r.get("reliability"))
    news_html = ""
    if r.get("headlines"):
        items_html = "".join(
            f"<li style='margin-bottom:4px'>"
            f"<span style='color:#888;font-size:11px'>{h['date']}</span> "
            + (f"<a href='{h['link']}' style='color:#1a4d1a;text-decoration:underline'>{h['title']}</a>"
               if h["link"] else h["title"])
            + f" <span style='color:#888;font-size:11px'>({h['publisher']})</span></li>"
            for h in r["headlines"]
        )
        news_html = f"""
      <div style="background:#f0f9f0;border-bottom:1px solid #dceedc;padding:8px 16px;font-size:12px;color:#1a4d1a">
        📰 <b>חדשות אחרונות (Yahoo Finance, מהחדש לישן):</b>
        <ul style="margin:4px 0 0;padding-right:18px">{items_html}</ul>
      </div>"""

    return f"""
    <div style="border:1px solid #ddd;border-radius:10px;overflow:hidden;margin-bottom:18px">
      <div style="background:#111;color:#fff;padding:14px 16px">
        <span style="font-size:20px;font-weight:700">{r['ticker']}</span>
        <span style="opacity:.8;font-size:13px">&nbsp;·&nbsp;נכון ל-{r['date']}</span>
        <span style="float:left;direction:ltr;font-family:monospace">close {r['close']} | RSI {r['rsi']}</span>
      </div>
      <div style="background:#eef2ff;border-bottom:1px solid #dde3fb;padding:8px 16px;font-size:12px;color:#333">
        📊 <b>אמינות היסטורית של האות במניה זו:</b> {tier}. {rel_detail}
      </div>{news_html}
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
    regime_line = ("נדרש: מדד SPY מעל ממוצע 200 יום שלו (אחרת הטריגר נחסם)"
                    if REQUIRE_MARKET_REGIME else "לא נבדק מצב שוק כללי")
    poc_desc = f"{POC_WINDOW} הימים האחרונים" if POC_WINDOW else "כל ההיסטוריה הזמינה"
    legend = f"""
    <div style="border:1px solid #dde3fb;background:#f7f9ff;border-radius:10px;padding:12px 16px;margin-bottom:16px;font-size:13px;color:#333">
      <b>מקרא ההגדרות של הריצה הזו</b> (לחישוב מדויק ראה detail בכל שורה למטה):
      <ul style="margin:8px 0 0;padding-right:18px;line-height:1.7">
        <li><b>סף כניסה:</b> לפחות {MIN_SIGNALS} מתוך 6 פרמטרים, וחובה שיעברו מבנה מחיר (#1) ונפח (#5).</li>
        <li><b>סף RSI:</b> {RSI_THRESHOLD:g} (ולא 50 — הועלה כדי לצמצם אותות חלשים, ראו backtest).</li>
        <li><b>סף RVOL:</b> {RVOL_THRESHOLD:g} ליום היפוך בנפח גבוה; רצפת פעילות {RVOL_SOFT_FLOOR:g} לענף החלופי.</li>
        <li><b>חלון פרופיל נפח (POC):</b> {poc_desc}.</li>
        <li><b>מצב שוק כללי:</b> {regime_line}.</li>
        <li><b>אמינות היסטורית:</b> מבוססת על backtest.py שרץ בעבר על כל טיקר בנפרד — win rate ותשואה ממוצעת ל-20 יום, מתוקנים לעסקאות בלתי-תלויות. מספר עסקאות קטן (&lt;5) = לא לסמוך.</li>
        <li><b>חדשות אחרונות:</b> מופיע רק למניות עם טריגר היום — עד {MAX_NEWS_ITEMS} כותרות חדשות מ-Yahoo Finance מ-{NEWS_LOOKBACK_DAYS} הימים האחרונים, מהחדש לישן (חינמי, בלי סיכום AI).</li>
      </ul>
    </div>
    """
    return f"""<!DOCTYPE html>
<html dir="rtl" lang="he"><head><meta charset="utf-8"></head>
<body style="font-family:Arial,Helvetica,sans-serif;background:#fafafa;margin:0;padding:18px;direction:rtl;text-align:right">
  <div style="max-width:760px;margin:0 auto">
    <h2 style="margin:0 0 4px">דוח בודק היפוך מגמה</h2>
    <p style="color:#666;margin:0 0 16px;font-size:13px">
      {stamp} · מצב: {mode_he}
    </p>
    {legend}
    {body}
    <p style="color:#999;font-size:11px;margin-top:16px">
      כלי ניתוח אוטומטי, אינו ייעוץ השקעות. ✓=הפרמטר תומך בהיפוך, ✗=עדיין לא.
    </p>
  </div>
</body></html>"""


def main():
    tickers = load_tickers()
    market_ok = fetch_market_regime()
    if REQUIRE_MARKET_REGIME:
        print(f"Market regime (SPY > 200d MA): {market_ok}")
    reliability = load_reliability()
    results = [analyze(t, morning=MORNING_MODE, market_ok=market_ok) for t in tickers]
    for r in results:
        if "error" not in r:
            r["reliability"] = reliability.get(r["ticker"])
    news_calls = 0
    for r in results:
        if r.get("BUY_TRIGGER") and news_calls < 10:
            r["headlines"] = fetch_recent_headlines(r["ticker"])
            news_calls += 1
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
