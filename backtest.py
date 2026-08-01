#!/usr/bin/env python3
"""
backtest.py
-----------
Walk-forward backtest of the reversal_checker.py signal logic.

For each ticker and each historical trading day, recomputes the 6-parameter
checklist using ONLY data available up to that day (no lookahead / no
future data leakage), and whenever BUY_TRIGGER fires, records the forward
return over several holding periods.

Runs two parameter sets side by side so you can compare them on the same
data:

  BASELINE  -- exact thresholds currently in reversal_checker.py
  IMPROVED  -- a proposed alternative meant to address weaknesses found in
               a design review of the baseline:
                 * market-regime filter: only trust signals when SPY is
                   above its 200d moving average (skip bear-market chop)
                 * tighter RSI pass condition (>55 instead of >50, since 50
                   is barely above "neutral" and passes very easily)
                 * volume-profile POC computed on a rolling recent window
                   (120 trading days) instead of the full lookback period,
                   so it reflects where money has traded recently rather
                   than a stale level from a year ago
                 * a floor on the "up-volume > down-volume" branch of the
                   volume check, so it can't pass on a quiet, low-activity
                   week

This script does NOT assume IMPROVED is actually better -- that is exactly
what its output tells you. Read both columns in reports/backtest_results.md
before changing reversal_checker.py's thresholds.

Important caveats baked into the results, read before trusting them:
  - Overlapping trades are de-duplicated: after a trade triggers, there's a
    cooldown (default = longest horizon, 20 trading days) before another
    trade can be recorded, so no two trades share a forward-return window.
    n_triggers is therefore a count of INDEPENDENT trades; n_raw_signal_days
    (reported alongside) shows how many raw signal-days that was collapsed
    from, so you can see how much a ticker's signal tends to "stay on".
  - Sample sizes can still be small even after de-duplication. Winrates on
    <10 independent trades are not statistically meaningful -- look at
    n_triggers before trusting a winrate.
  - This backtests the SIGNAL only, not a trading strategy: no position
    sizing, no stop-loss, no transaction costs/slippage. A positive average
    forward return does not mean a strategy built on this signal would be
    profitable after costs.
  - Survivorship / selection bias: tickers in tickers.txt were picked by
    hand (partly because they already look interesting), not sampled
    neutrally, so results here may not generalize to other stocks.
  - Prices are unadjusted (auto_adjust=False, matching reversal_checker.py)
    so large splits/dividends could distort forward returns around their
    ex-dates for a given ticker.

Usage: python backtest.py
Writes: reports/backtest_results.md, reports/backtest_results.json
"""

import os
import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf

from reversal_checker import rsi, macd, pivots  # reuse the exact same indicator math

TICKERS_FILE = "tickers.txt"
HISTORY_PERIOD = "5y"           # need several years for a meaningful sample
HORIZONS = [5, 10, 20]          # forward-return windows, in trading days
PIVOT_L, PIVOT_R = 3, 3
WARMUP = 260                    # skip first ~1y so all indicators are valid


def load_tickers():
    if os.path.exists(TICKERS_FILE):
        syms = []
        for line in open(TICKERS_FILE, encoding="utf-8"):
            line = line.split("#")[0].strip().upper()
            if line:
                syms.append(line)
        if syms:
            return syms
    return ["ORCL"]


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


def evaluate_day(sub, params):
    """Replicates the reversal checklist using ONLY sub (data up to and
    including 'today'). Returns True/False for BUY_TRIGGER."""
    if len(sub) < 60:
        return False

    close, high, low, vol, op = sub["Close"], sub["High"], sub["Low"], sub["Volume"], sub["Open"]
    last_close = float(close.iloc[-1])

    ma10, ma20 = close.rolling(10).mean(), close.rolling(20).mean()
    rsi_s = rsi(close)
    macd_line, sig_line, hist = macd(close)
    rvol = vol / vol.rolling(20).mean()

    plows = pivots(low.values, PIVOT_L, PIVOT_R, "low")
    phighs = pivots(high.values, PIVOT_L, PIVOT_R, "high")

    checks = {}

    # 1) Price structure (mandatory)
    higher_low = broke_high = False
    if len(plows) >= 2:
        higher_low = low.iloc[plows[-1]] > low.iloc[plows[-2]]
    if phighs:
        last_swing_high = float(high.iloc[phighs[-1]])
        broke_high = last_close > last_swing_high
    checks["1_price_structure"] = bool(higher_low and broke_high)

    # 2) Moving averages
    above_short = last_close > ma10.iloc[-1] and last_close > ma20.iloc[-1]
    ma10_rising = len(ma10) >= 3 and ma10.iloc[-1] > ma10.iloc[-3]
    checks["2_moving_averages"] = bool(above_short and ma10_rising)

    # 3) MACD
    hist_rising = len(hist) >= 3 and hist.iloc[-1] > hist.iloc[-2] > hist.iloc[-3]
    macd_above = macd_line.iloc[-1] > sig_line.iloc[-1]
    checks["3_macd"] = bool(macd_above and hist_rising)

    # 4) RSI (+ bullish divergence), threshold is tunable per variant
    bull_div = False
    if len(plows) >= 2:
        p1, p2 = plows[-2], plows[-1]
        bull_div = (low.iloc[p2] < low.iloc[p1]) and (rsi_s.iloc[p2] > rsi_s.iloc[p1])
    rsi_now = float(rsi_s.iloc[-1])
    rsi_rising = len(rsi_s) >= 2 and rsi_s.iloc[-1] > rsi_s.iloc[-2]
    checks["4_rsi"] = bool(rsi_now > params["rsi_threshold"] or (bull_div and rsi_rising))

    # 5) Volume / RVOL (mandatory), soft-floor is tunable per variant
    rvol_today = float(rvol.iloc[-1]) if not np.isnan(rvol.iloc[-1]) else 0.0
    latest_up = last_close > float(op.iloc[-1])
    recent = sub.tail(10)
    up_vol = recent.loc[recent["Close"] >= recent["Open"], "Volume"].mean()
    down_vol = recent.loc[recent["Close"] < recent["Open"], "Volume"].mean()
    up_gt_down = np.nan_to_num(up_vol) > np.nan_to_num(down_vol)
    checks["5_volume"] = bool(
        (latest_up and rvol_today > params["rvol_threshold"])
        or (up_gt_down and rvol_today > params["rvol_soft_floor"])
    )

    # 6) Volume Profile POC, window is tunable per variant (None = full sub)
    window = params["poc_window"]
    poc_close = close.tail(window) if window else close
    poc_vol = vol.tail(window) if window else vol
    poc = volume_profile_poc(poc_close, poc_vol)
    checks["6_volume_profile"] = bool(last_close > poc)

    n_conf = sum(checks.values())
    mandatory = checks["1_price_structure"] and checks["5_volume"]
    return n_conf >= params["min_signals"] and mandatory


def forward_return(close_series, i, horizon):
    if i + horizon >= len(close_series):
        return None
    p0 = float(close_series.iloc[i])
    p1 = float(close_series.iloc[i + horizon])
    return (p1 / p0 - 1) * 100


def run_variant(df, regime_by_date, params, cooldown_days=None):
    """Walk forward and record BUY_TRIGGER days.

    IMPORTANT: a signal that stays True for several consecutive days (very
    common -- the same reversal move keeps re-qualifying) is NOT several
    independent trades. Counting each day separately inflates n_triggers
    and biases winrate/avg-return toward whatever regime happened to be
    trending at the time. To get an honest, independence-respecting count:
    after a trigger fires, we go into a cooldown of `cooldown_days` (default:
    the longest forward-return horizon) during which new triggers are not
    recorded, so no two recorded trades have overlapping forward-return
    windows. `n_raw_signal_days` is kept alongside for transparency, showing
    how much de-duplication happened.
    """
    if cooldown_days is None:
        cooldown_days = max(HORIZONS)
    triggers = []
    raw_signal_days = 0
    close_series = df["Close"]
    next_eligible_i = WARMUP
    for i in range(WARMUP, len(df) - 1):
        if params.get("require_market_regime"):
            date = df.index[i]
            if not bool(regime_by_date.get(date, True)):
                continue
        sub = df.iloc[:i + 1]
        if evaluate_day(sub, params):
            raw_signal_days += 1
            if i < next_eligible_i:
                continue  # still in cooldown from a previous independent trade
            row = {"date": str(df.index[i].date()), "close": float(close_series.iloc[i])}
            for h in HORIZONS:
                row[f"fwd_{h}d_%"] = forward_return(close_series, i, h)
            triggers.append(row)
            next_eligible_i = i + cooldown_days + 1
    return triggers, raw_signal_days


BASELINE_PARAMS = {
    "min_signals": 4,
    "rsi_threshold": 50,
    "rvol_threshold": 1.5,
    "rvol_soft_floor": 0.0,   # original had no floor on the up>down-volume OR branch
    "poc_window": None,       # None = full available history (original behavior)
    "require_market_regime": False,
}

IMPROVED_PARAMS = {
    "min_signals": 4,
    "rsi_threshold": 55,
    "rvol_threshold": 1.5,
    "rvol_soft_floor": 1.1,   # up>down volume only counts with some above-average activity
    "poc_window": 120,        # recent volume profile, not a stale full-history level
    "require_market_regime": True,
}


def pooled_stats(triggers):
    if not triggers:
        return {"n_triggers": 0}
    out = {"n_triggers": len(triggers)}
    for h in HORIZONS:
        vals = [t[f"fwd_{h}d_%"] for t in triggers if t[f"fwd_{h}d_%"] is not None]
        if vals:
            out[f"avg_fwd_{h}d_%"] = round(float(np.mean(vals)), 2)
            out[f"median_fwd_{h}d_%"] = round(float(np.median(vals)), 2)
            out[f"winrate_{h}d_%"] = round(100 * float(np.mean([v > 0 for v in vals])), 1)
        else:
            out[f"avg_fwd_{h}d_%"] = out[f"median_fwd_{h}d_%"] = out[f"winrate_{h}d_%"] = None
    return out


def main():
    tickers = load_tickers()

    try:
        spy = yf.Ticker("SPY").history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
        spy_regime_series = (spy["Close"] > spy["Close"].rolling(200).mean())
    except Exception as e:
        print(f"WARNING: could not fetch SPY for market-regime filter ({e}); "
              f"IMPROVED variant will treat regime as always-on.")
        spy_regime_series = pd.Series(dtype=bool)

    detail_lines = ["# Backtest results \u2014 reversal checklist (BASELINE vs IMPROVED)\n"]
    detail_lines.append(
        f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. "
        f"History: {HISTORY_PERIOD}, warmup {WARMUP}d, horizons {HORIZONS}d.\n"
    )
    detail_lines.append(
        "Signal-only backtest: no position sizing, stops, or costs. "
        "Small n_triggers = not statistically meaningful, read literally.\n"
    )

    pooled_by_variant = {"BASELINE": [], "IMPROVED": []}
    per_ticker_json = []

    for ticker in tickers:
        try:
            df = yf.Ticker(ticker).history(period=HISTORY_PERIOD, auto_adjust=False).dropna()
        except Exception as e:
            detail_lines.append(f"\n## {ticker}\nSKIPPED \u2014 data fetch failed: {e}\n")
            continue
        if len(df) < WARMUP + 30:
            detail_lines.append(f"\n## {ticker}\nSKIPPED \u2014 not enough history ({len(df)} rows)\n")
            continue

        regime_by_date = spy_regime_series.reindex(df.index).ffill().fillna(False) \
            if len(spy_regime_series) else pd.Series(True, index=df.index)

        detail_lines.append(f"\n## {ticker}")
        for label, params in (("BASELINE", BASELINE_PARAMS), ("IMPROVED", IMPROVED_PARAMS)):
            triggers, raw_days = run_variant(df, regime_by_date, params)
            pooled_by_variant[label] += triggers
            stats = pooled_stats(triggers)
            stats["n_raw_signal_days"] = raw_days
            per_ticker_json.append({"ticker": ticker, "variant": label, **stats})
            if stats["n_triggers"] == 0:
                detail_lines.append(f"  {label}: 0 independent trades ({raw_days} raw signal-days) in sample period")
                continue
            parts = [f"{label}: {stats['n_triggers']} independent trades (from {raw_days} raw signal-days)"]
            for h in HORIZONS:
                parts.append(f"{h}d avg={stats[f'avg_fwd_{h}d_%']}% winrate={stats[f'winrate_{h}d_%']}%")
            detail_lines.append(" | ".join(parts))

    detail_lines.append("\n## Aggregate (all tickers' trades pooled together)")
    aggregate_json = {}
    for label in ("BASELINE", "IMPROVED"):
        stats = pooled_stats(pooled_by_variant[label])
        aggregate_json[label] = stats
        if stats["n_triggers"] == 0:
            detail_lines.append(f"{label}: 0 triggers total")
            continue
        parts = [f"{label}: {stats['n_triggers']} total triggers"]
        for h in HORIZONS:
            parts.append(f"{h}d avg={stats[f'avg_fwd_{h}d_%']}% median={stats[f'median_fwd_{h}d_%']}% "
                         f"winrate={stats[f'winrate_{h}d_%']}%")
        detail_lines.append(" | ".join(parts))

    detail_lines.append(
        "\nHow to read this: n_triggers = independent trades (overlapping signal-days on the "
        "same move are collapsed into one, see n_raw_signal_days in the JSON for the raw count). "
        "Compare BASELINE vs IMPROVED n_triggers and winrate/avg return at each horizon. More "
        "trades with similar or better winrate/avg return = the change helped. Fewer trades with "
        "much better winrate can also be a legitimate improvement (higher-quality, rarer signals) "
        "\u2014 that's a judgment call, not something the numbers alone decide."
    )

    os.makedirs("reports", exist_ok=True)
    text = "\n".join(detail_lines)
    with open("reports/backtest_results.md", "w", encoding="utf-8") as f:
        f.write(text)
    with open("reports/backtest_results.json", "w", encoding="utf-8") as f:
        json.dump({"per_ticker": per_ticker_json, "aggregate": aggregate_json,
                    "baseline_params": BASELINE_PARAMS, "improved_params": IMPROVED_PARAMS},
                   f, indent=2, default=str)
    print(text)


if __name__ == "__main__":
    main()
