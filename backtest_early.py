#!/usr/bin/env python3
"""
backtest_early.py
-----------------
Question being tested: the reversal checklist in reversal_checker.py tends to
fire only after a stock has already bounced hard off its low. Is there an
EARLIER signal that catches the turn sooner, with an equal or better outcome?

Compares, on the same 5y history and the same tickers.txt:

  CURRENT        -- the live trigger (IMPROVED params, incl. SPY>200d regime)
  CURRENT_NOCHASE-- CURRENT, but skipped when price is already >10% above
                    its 20-day low ("don't chase")
  EARLY_D        -- washout + FIRST close back above MA10 + MACD histogram
                    rising 2 days in a row
  EARLY_D_REGIME -- EARLY_D, only when SPY is above its 200d MA
  EARLY_C        -- washout + MACD histogram rising 2 days while MACD is
                    still BELOW its signal + RSI rising + (higher low OR
                    bullish RSI divergence)
  ALL_DAYS       -- every day, no signal at all: the base rate. A signal is
                    only useful if it beats this.

"washout" = in the last 10 days RSI(14) dipped below 40, OR the close was
            more than 5% below MA20.

Everything is computed causally: each day only uses data up to that day.
Swing pivots (3 bars each side) count only once they are confirmed, i.e.
3 bars after the pivot, exactly like reversal_checker.py does when it runs
on a series that ends "today".

Per independent trade (20-day cooldown, same as backtest.py) it records:
  - forward return at 5/10/20 trading days
  - how far price already was above its 20-day low at entry ("lateness")
  - a simple stop-loss trade: stop 1% under the lowest low of the last
    10 days, held up to 20 days; exit at the stop (or the open, if it gaps
    below the stop) otherwise at the day-20 close.

Signal study only: no costs/slippage, hand-picked tickers, unadjusted prices.

Usage: python backtest_early.py
Writes: reports/early_backtest_results.md, reports/early_backtest_results.json
"""

import os
import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf

from reversal_checker import rsi, macd

TICKERS_FILE = "tickers.txt"
HISTORY_PERIOD = "5y"
HORIZONS = [5, 10, 20]
PIVOT_L, PIVOT_R = 3, 3
WARMUP = 260
COOLDOWN = 20
STOP_LOOKBACK = 10
STOP_BUFFER = 0.01
HOLD_DAYS = 20

# live IMPROVED parameters from reversal_checker.py
RSI_THRESHOLD = 55
RVOL_THRESHOLD = 1.5
RVOL_SOFT_FLOOR = 1.1
POC_WINDOW = 120
MIN_SIGNALS = 4


def load_tickers():
    syms = []
    if os.path.exists(TICKERS_FILE):
        for line in open(TICKERS_FILE, encoding="utf-8"):
            line = line.split("#")[0].strip().upper()
            if line:
                syms.append(line)
    return syms or ["ORCL"]


def pivot_flags(values, left, right, kind):
    """Boolean array: True at index p if p is a swing pivot (same rule as
    reversal_checker.pivots). A pivot at p is only KNOWN at day p+right."""
    n = len(values)
    out = np.zeros(n, dtype=bool)
    for i in range(left, n - right):
        seg = values[i - left:i + right + 1]
        if kind == "low" and values[i] == seg.min():
            out[i] = True
        if kind == "high" and values[i] == seg.max():
            out[i] = True
    return out


def poc_of(close, volume, bins=50):
    lo, hi = float(close.min()), float(close.max())
    if hi <= lo:
        return float(close[-1])
    edges = np.linspace(lo, hi, bins + 1)
    idx = np.clip(np.digitize(close, edges) - 1, 0, bins - 1)
    vol_bin = np.bincount(idx, weights=volume, minlength=bins)
    p = int(vol_bin.argmax())
    return float((edges[p] + edges[p + 1]) / 2)


def features(df):
    """Per-day, causal features. Returns a DataFrame aligned to df.index."""
    close, high, low, vol, op = (df[c].to_numpy(float) for c in ("Close", "High", "Low", "Volume", "Open"))
    s_close = df["Close"]
    n = len(df)
    f = pd.DataFrame(index=df.index)
    f["close"] = close
    f["ma10"] = s_close.rolling(10).mean()
    f["ma20"] = s_close.rolling(20).mean()
    f["rsi"] = rsi(s_close)
    m_line, m_sig, m_hist = macd(s_close)
    f["macd"], f["sig"], f["hist"] = m_line, m_sig, m_hist
    rvol = df["Volume"] / df["Volume"].rolling(20).mean()
    f["rvol"] = rvol.fillna(0.0)

    # up-volume vs down-volume over the last 10 days (NaN mean -> 0, like the checker)
    upv = df["Volume"].where(df["Close"] >= df["Open"])
    dnv = df["Volume"].where(df["Close"] < df["Open"])
    f["up_gt_down"] = upv.rolling(10, min_periods=1).mean().fillna(0) > dnv.rolling(10, min_periods=1).mean().fillna(0)
    f["day_up"] = close > op

    # causal pivots
    pl = pivot_flags(low, PIVOT_L, PIVOT_R, "low")
    ph = pivot_flags(high, PIVOT_L, PIVOT_R, "high")
    higher_low = np.zeros(n, bool)
    bull_div = np.zeros(n, bool)
    broke_high = np.zeros(n, bool)
    last_lows, last_high = [], None
    rsi_arr = f["rsi"].to_numpy()
    for i in range(n):
        p = i - PIVOT_R                 # pivot that becomes confirmed today
        if p >= PIVOT_L:
            if pl[p]:
                last_lows.append(p)
            if ph[p]:
                last_high = p
        if len(last_lows) >= 2:
            p1, p2 = last_lows[-2], last_lows[-1]
            higher_low[i] = low[p2] > low[p1]
            bull_div[i] = (low[p2] < low[p1]) and (rsi_arr[p2] > rsi_arr[p1])
        if last_high is not None:
            broke_high[i] = close[i] > high[last_high]
    f["higher_low"], f["bull_div"], f["broke_high"] = higher_low, bull_div, broke_high

    # rolling-window POC
    poc = np.full(n, np.nan)
    for i in range(n):
        a = max(0, i + 1 - POC_WINDOW)
        poc[i] = poc_of(close[a:i + 1], vol[a:i + 1])
    f["poc"] = poc

    f["hist_up2"] = (f["hist"] > f["hist"].shift(1)) & (f["hist"].shift(1) > f["hist"].shift(2))
    f["rsi_rising"] = f["rsi"] > f["rsi"].shift(1)
    f["ma10_rising"] = f["ma10"] > f["ma10"].shift(2)
    above10 = f["close"] > f["ma10"]
    f["first_above10"] = above10 & ~above10.shift(1, fill_value=True)
    f["washout"] = (f["rsi"].rolling(10).min() < 40) | ((f["close"] / f["ma20"] - 1).rolling(10).min() < -0.05)
    f["low20"] = df["Low"].rolling(20).min()
    f["low_stop"] = df["Low"].rolling(STOP_LOOKBACK).min()
    return f


def current_trigger(f, regime):
    c1 = f["higher_low"] & f["broke_high"]
    c2 = (f["close"] > f["ma10"]) & (f["close"] > f["ma20"]) & f["ma10_rising"]
    c3 = (f["macd"] > f["sig"]) & f["hist_up2"]
    c4 = (f["rsi"] > RSI_THRESHOLD) | (f["bull_div"] & f["rsi_rising"])
    c5 = (f["day_up"] & (f["rvol"] > RVOL_THRESHOLD)) | (f["up_gt_down"] & (f["rvol"] > RVOL_SOFT_FLOOR))
    c6 = f["close"] > f["poc"]
    n_conf = sum(x.astype(int) for x in (c1, c2, c3, c4, c5, c6))
    return (n_conf >= MIN_SIGNALS) & c1 & c5 & regime


def variants(f, regime):
    cur = current_trigger(f, regime)
    early_d = f["washout"] & f["first_above10"] & f["hist_up2"]
    early_c = (f["washout"] & f["hist_up2"] & (f["macd"] < f["sig"]) & f["rsi_rising"]
               & (f["higher_low"] | f["bull_div"]))
    return {
        "CURRENT": cur,
        "CURRENT_NOCHASE": cur & (f["close"] <= 1.10 * f["low20"]),
        "EARLY_D": early_d,
        "EARLY_D_REGIME": early_d & regime,
        "EARLY_C": early_c,
        "ALL_DAYS": pd.Series(True, index=f.index),
    }


def trades_for(df, f, signal, cooldown=COOLDOWN):
    close = df["Close"].to_numpy(float)
    low = df["Low"].to_numpy(float)
    op = df["Open"].to_numpy(float)
    sig = signal.fillna(False).to_numpy(bool)
    n = len(df)
    out, raw, nxt = [], 0, WARMUP
    for i in range(WARMUP, n - 1):
        if not sig[i]:
            continue
        raw += 1
        if i < nxt:
            continue
        row = {"date": str(df.index[i].date()), "close": close[i],
               "from_low20_%": 100 * (close[i] / f["low20"].iat[i] - 1)}
        for h in HORIZONS:
            row[f"fwd_{h}d_%"] = 100 * (close[i + h] / close[i] - 1) if i + h < n else None
        # stop-loss trade
        if i + HOLD_DAYS < n:
            stop = f["low_stop"].iat[i] * (1 - STOP_BUFFER)
            row["risk_%"] = 100 * (close[i] / stop - 1)
            exit_px = close[i + HOLD_DAYS]
            stopped = False
            for k in range(1, HOLD_DAYS + 1):
                if low[i + k] <= stop:
                    exit_px = min(op[i + k], stop)
                    stopped = True
                    break
            row["stop_trade_%"] = 100 * (exit_px / close[i] - 1)
            row["stopped"] = stopped
        else:
            row["risk_%"] = row["stop_trade_%"] = row["stopped"] = None
        out.append(row)
        nxt = i + cooldown + 1
    return out, raw


def stats(trades):
    s = {"n": len(trades)}
    if not trades:
        return s
    def col(k):
        return np.array([t[k] for t in trades if t.get(k) is not None], float)
    for h in HORIZONS:
        v = col(f"fwd_{h}d_%")
        if len(v):
            s[f"fwd{h}_avg"] = round(float(v.mean()), 2)
            s[f"fwd{h}_med"] = round(float(np.median(v)), 2)
            s[f"fwd{h}_win"] = round(100 * float((v > 0).mean()), 1)
    v = col("from_low20_%")
    s["from_low_med"] = round(float(np.median(v)), 2)
    v = col("stop_trade_%")
    if len(v):
        s["stop_avg"] = round(float(v.mean()), 2)
        s["stop_med"] = round(float(np.median(v)), 2)
        s["stop_win"] = round(100 * float((v > 0).mean()), 1)
        s["risk_med"] = round(float(np.median(col("risk_%"))), 2)
        st = [t["stopped"] for t in trades if t.get("stopped") is not None]
        s["stopped_%"] = round(100 * float(np.mean(st)), 1)
    return s


def main():
    tickers = load_tickers()
    spy = yf.Ticker("SPY").history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
    spy_regime = spy["Close"] > spy["Close"].rolling(200).mean()
    spy_regime.index = spy_regime.index.tz_localize(None).normalize()

    names = ["CURRENT", "CURRENT_NOCHASE", "EARLY_D", "EARLY_D_REGIME", "EARLY_C", "ALL_DAYS"]
    pooled = {k: [] for k in names}
    per_ticker, skipped = [], []

    for t in tickers:
        try:
            df = yf.Ticker(t).history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
        except Exception as e:
            skipped.append(f"{t} (fetch failed: {e})")
            continue
        if len(df) < WARMUP + 30:
            skipped.append(f"{t} ({len(df)} rows)")
            continue
        df.index = df.index.tz_localize(None).normalize()
        regime = spy_regime.reindex(df.index).ffill().fillna(False).astype(bool)
        f = features(df)
        for name, sig in variants(f, regime).items():
            cd = 0 if name == "ALL_DAYS" else COOLDOWN
            tr, raw = trades_for(df, f, sig, cooldown=cd)
            for x in tr:
                x["ticker"] = t
            pooled[name] += tr
            per_ticker.append({"ticker": t, "variant": name, "raw_signal_days": raw, **stats(tr)})
        print(f"done {t}", flush=True)

    agg = {k: stats(v) for k, v in pooled.items()}

    L = ["# Early-entry backtest — does an earlier signal beat the current trigger?\n",
         f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. History {HISTORY_PERIOD}, "
         f"warmup {WARMUP}d, cooldown {COOLDOWN}d, {len(tickers) - len(skipped)} tickers used.\n",
         "Signal study only: no costs/slippage, hand-picked tickers, unadjusted prices.\n",
         "## Aggregate (all tickers pooled)\n",
         "| variant | trades | from 20d low (med) | 5d med | 10d med | 10d win% | 20d avg | 20d med | 20d win% | stop-trade avg | stop-trade win% | stopped% | risk to stop (med) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for k in names:
        s = agg[k]
        if not s.get("n"):
            L.append(f"| {k} | 0 |" + " |" * 11)
            continue
        L.append(f"| {k} | {s['n']} | {s['from_low_med']}% | {s.get('fwd5_med')}% | {s.get('fwd10_med')}% | "
                 f"{s.get('fwd10_win')}% | {s.get('fwd20_avg')}% | {s.get('fwd20_med')}% | {s.get('fwd20_win')}% | "
                 f"{s.get('stop_avg')}% | {s.get('stop_win')}% | {s.get('stopped_%')}% | {s.get('risk_med')}% |")

    # yearly split of the two main variants, to see if a result is one regime only
    L.append("\n## By year (20d median / win%, trades)\n")
    L.append("| year | " + " | ".join(names[:-1]) + " |")
    L.append("|---|" + "---|" * (len(names) - 1))
    years = sorted({x["date"][:4] for v in pooled.values() for x in v})
    for y in years:
        cells = []
        for k in names[:-1]:
            v = np.array([x["fwd_20d_%"] for x in pooled[k] if x["date"][:4] == y and x["fwd_20d_%"] is not None])
            cells.append(f"{np.median(v):.1f}% / {100*(v>0).mean():.0f}% ({len(v)})" if len(v) else "-")
        L.append(f"| {y} | " + " | ".join(cells) + " |")

    if skipped:
        L.append("\nSkipped: " + ", ".join(skipped))

    os.makedirs("reports", exist_ok=True)
    with open("reports/early_backtest_results.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    with open("reports/early_backtest_results.json", "w", encoding="utf-8") as fh:
        json.dump({"aggregate": agg, "per_ticker": per_ticker,
                   "trades": {k: v for k, v in pooled.items() if k != "ALL_DAYS"}},
                  fh, indent=1, default=str)
    print("\n".join(L))


if __name__ == "__main__":
    main()
