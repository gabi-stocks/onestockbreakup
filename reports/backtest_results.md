# Backtest results — reversal checklist (BASELINE vs IMPROVED)

Generated 2026-08-01 20:02 UTC. History: 5y, warmup 260d, horizons [5, 10, 20]d.

Signal-only backtest: no position sizing, stops, or costs. Small n_triggers = not statistically meaningful, read literally.


## ORCL
BASELINE: 18 independent trades (from 110 raw signal-days) | 5d avg=1.62% winrate=61.1% | 10d avg=2.33% winrate=50.0% | 20d avg=2.91% winrate=50.0%
IMPROVED: 11 independent trades (from 42 raw signal-days) | 5d avg=3.66% winrate=72.7% | 10d avg=6.01% winrate=72.7% | 20d avg=5.13% winrate=54.5%

## HTFL
SKIPPED — not enough history (245 rows)


## QCOM
BASELINE: 17 independent trades (from 84 raw signal-days) | 5d avg=0.51% winrate=41.2% | 10d avg=0.75% winrate=52.9% | 20d avg=1.45% winrate=47.1%
IMPROVED: 11 independent trades (from 43 raw signal-days) | 5d avg=2.05% winrate=54.5% | 10d avg=2.77% winrate=54.5% | 20d avg=3.81% winrate=54.5%

## TEM
BASELINE: 4 independent trades (from 17 raw signal-days) | 5d avg=-2.14% winrate=25.0% | 10d avg=-5.93% winrate=25.0% | 20d avg=-1.04% winrate=50.0%
IMPROVED: 3 independent trades (from 8 raw signal-days) | 5d avg=2.11% winrate=33.3% | 10d avg=-6.03% winrate=33.3% | 20d avg=-9.67% winrate=33.3%

## GEHC
BASELINE: 11 independent trades (from 45 raw signal-days) | 5d avg=-2.17% winrate=18.2% | 10d avg=-0.93% winrate=45.5% | 20d avg=-0.94% winrate=45.5%
IMPROVED: 8 independent trades (from 19 raw signal-days) | 5d avg=-2.57% winrate=37.5% | 10d avg=-1.92% winrate=50.0% | 20d avg=0.16% winrate=62.5%

## ATKR
BASELINE: 16 independent trades (from 89 raw signal-days) | 5d avg=1.8% winrate=62.5% | 10d avg=1.79% winrate=68.8% | 20d avg=4.35% winrate=62.5%
IMPROVED: 10 independent trades (from 30 raw signal-days) | 5d avg=-0.4% winrate=40.0% | 10d avg=-1.12% winrate=50.0% | 20d avg=1.64% winrate=60.0%

## AMSC
BASELINE: 18 independent trades (from 123 raw signal-days) | 5d avg=0.21% winrate=55.6% | 10d avg=8.37% winrate=61.1% | 20d avg=13.49% winrate=72.2%
IMPROVED: 16 independent trades (from 65 raw signal-days) | 5d avg=-0.28% winrate=50.0% | 10d avg=11.64% winrate=56.2% | 20d avg=11.61% winrate=62.5%

## Aggregate (all tickers' trades pooled together)
BASELINE: 84 total triggers | 5d avg=0.45% median=-0.24% winrate=48.8% | 10d avg=2.38% median=0.53% winrate=54.8% | 20d avg=4.46% median=3.29% winrate=56.0%
IMPROVED: 59 total triggers | 5d avg=0.68% median=0.91% winrate=50.8% | 10d avg=4.03% median=0.64% winrate=55.9% | 20d avg=4.62% median=1.85% winrate=57.6%

How to read this: n_triggers = independent trades (overlapping signal-days on the same move are collapsed into one, see n_raw_signal_days in the JSON for the raw count). Compare BASELINE vs IMPROVED n_triggers and winrate/avg return at each horizon. More trades with similar or better winrate/avg return = the change helped. Fewer trades with much better winrate can also be a legitimate improvement (higher-quality, rarer signals) — that's a judgment call, not something the numbers alone decide.