#!/usr/bin/env python3
"""
backtest_params.py
------------------
Which extra technical parameters separate the reversal triggers that work
from the ones that don't?

For every independent trade of two signals (same definitions as
backtest_early.py):
  CURRENT  -- the live trigger (IMPROVED params incl. SPY>200d regime)
  EARLY_D  -- washout + first close above MA10 + MACD histogram up 2 days
this script records the candidate parameters as they stood ON THE ENTRY DAY
(causal, no look-ahead) together with the forward returns, so each parameter
can be judged by comparing the trades where it was true against the trades
where it was false -- on the SAME set of trades, so no parameter gets to
"pick" a different entry day.

Candidate parameters (all computed on data up to the entry day):
  rs20        stock 20d return minus SPY 20d return (relative strength)
  rs_high     relative-strength line (close/SPY) within 2% of its 50d high
  obv_high    On-Balance Volume at a 20-day high (accumulation)
  squeeze     Bollinger band width (20,2) hit the bottom 25% of its last
              120 days somewhere in the last 10 days (volatility contraction)
  clv         close location in the day's range, 0=low .. 1=high
  above200    close above the 200d moving average (long-term uptrend)
  pullback    depth of the preceding drop: 20d low vs 120d high (negative %)
  ext_atr     (close - MA20) / ATR14, how stretched price is
  dryup       volume dried up before the move: lowest 5-day average volume of
              the last 15 days, divided by the 50-day average volume
  from_low    % above the 20-day low (the on-time/late measure)

Writes reports/params_trades.json (one row per trade, all features) and
reports/params_summary.md. Signal study only: no costs, hand-picked tickers.
"""

import os
import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf

from backtest_early import (load_tickers, features, variants, HISTORY_PERIOD,
                            WARMUP, COOLDOWN, HORIZONS, HOLD_DAYS, STOP_BUFFER)


def extra_features(df, spy_close):
    c, h, l, v = df["Close"], df["High"], df["Low"], df["Volume"]
    x = pd.DataFrame(index=df.index)
    spy = spy_close.reindex(df.index).ffill()
    x["rs20"] = 100 * (c.pct_change(20) - spy.pct_change(20))
    rs_line = c / spy
    x["rs_high"] = rs_line >= 0.98 * rs_line.rolling(50).max()
    obv = (np.sign(c.diff()).fillna(0) * v).cumsum()
    x["obv_high"] = obv >= obv.rolling(20).max()
    ma20, sd20 = c.rolling(20).mean(), c.rolling(20).std()
    bw = (4 * sd20) / ma20
    bw_rank = bw.rolling(120).apply(lambda a: (a[:-1] < a[-1]).mean() if len(a) > 1 else np.nan, raw=True)
    x["squeeze"] = bw_rank.rolling(10).min() <= 0.25
    rng = (h - l).replace(0, np.nan)
    x["clv"] = ((c - l) / rng).fillna(0.5)
    x["above200"] = c > c.rolling(200).mean()
    x["pullback"] = 100 * (l.rolling(20).min() / h.rolling(120).max() - 1)
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    x["ext_atr"] = (c - ma20) / atr
    x["dryup"] = v.rolling(5).mean().rolling(15).min() / v.rolling(50).mean()
    return x


def trade_rows(df, f, x, signal, name, ticker):
    close, low, op = (df[k].to_numpy(float) for k in ("Close", "Low", "Open"))
    sig = signal.fillna(False).to_numpy(bool)
    n, out, nxt = len(df), [], WARMUP
    for i in range(WARMUP, n - 1):
        if not sig[i] or i < nxt:
            continue
        nxt = i + COOLDOWN + 1
        row = {"variant": name, "ticker": ticker, "date": str(df.index[i].date()),
               "from_low": 100 * (close[i] / f["low20"].iat[i] - 1)}
        for k in x.columns:
            val = x[k].iat[i]
            row[k] = (bool(val) if isinstance(val, (bool, np.bool_))
                      else (None if pd.isna(val) else round(float(val), 4)))
        for hz in HORIZONS:
            row[f"fwd{hz}"] = 100 * (close[i + hz] / close[i] - 1) if i + hz < n else None
        if i + HOLD_DAYS < n:
            stop = f["low_stop"].iat[i] * (1 - STOP_BUFFER)
            exit_px = close[i + HOLD_DAYS]
            for k in range(1, HOLD_DAYS + 1):
                if low[i + k] <= stop:
                    exit_px = min(op[i + k], stop)
                    break
            row["stop_trade"] = 100 * (exit_px / close[i] - 1)
        else:
            row["stop_trade"] = None
        out.append(row)
    return out


def main():
    tickers = load_tickers()
    spy = yf.Ticker("SPY").history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
    spy.index = spy.index.tz_localize(None).normalize()
    spy_regime = spy["Close"] > spy["Close"].rolling(200).mean()

    rows, skipped = [], []
    for t in tickers:
        try:
            df = yf.Ticker(t).history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
        except Exception as e:
            skipped.append(f"{t} ({e})")
            continue
        if len(df) < WARMUP + 30:
            skipped.append(f"{t} ({len(df)} rows)")
            continue
        df.index = df.index.tz_localize(None).normalize()
        regime = spy_regime.reindex(df.index).ffill().fillna(False).astype(bool)
        f = features(df)
        x = extra_features(df, spy["Close"])
        v = variants(f, regime)
        for name in ("CURRENT", "EARLY_D"):
            rows += trade_rows(df, f, x, v[name], name, t)
        print(f"done {t}", flush=True)

    os.makedirs("reports", exist_ok=True)
    with open("reports/params_trades.json", "w", encoding="utf-8") as fh:
        json.dump({"generated": f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC",
                   "skipped": skipped, "trades": rows}, fh, default=str)

    d = pd.DataFrame(rows)
    L = [f"# Parameter study ({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC)\n",
         f"Trades: {len(d)}. Skipped: {', '.join(skipped) or 'none'}.\n",
         "Full per-trade data in reports/params_trades.json.\n"]
    for name in ("CURRENT", "EARLY_D"):
        s = d[d["variant"] == name].dropna(subset=["fwd20"])
        L.append(f"\n## {name} ({len(s)} trades with 20d outcome)\n")
        L.append("| parameter | n true | 20d win% true | 20d win% false | 20d med true | 20d med false |")
        L.append("|---|---|---|---|---|---|")
        tests = {
            "rs20>0": s["rs20"] > 0, "rs_high": s["rs_high"] == True, "obv_high": s["obv_high"] == True,
            "squeeze": s["squeeze"] == True, "clv>=0.7": s["clv"] >= 0.7, "above200": s["above200"] == True,
            "pullback -35..-10%": s["pullback"].between(-35, -10), "ext_atr<=2": s["ext_atr"] <= 2,
            "dryup<0.8": s["dryup"] < 0.8, "from_low<=10": s["from_low"] <= 10,
        }
        for k, m in tests.items():
            a, b = s[m], s[~m]
            if len(a) == 0 or len(b) == 0:
                continue
            L.append(f"| {k} | {len(a)} | {100*(a['fwd20']>0).mean():.1f} | {100*(b['fwd20']>0).mean():.1f} | "
                     f"{a['fwd20'].median():.2f} | {b['fwd20'].median():.2f} |")
    with open("reports/params_summary.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
