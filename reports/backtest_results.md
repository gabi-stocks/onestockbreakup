# Backtest results — reversal checklist (BASELINE vs IMPROVED)

Generated 2026-08-02 11:24 UTC. History: 5y, warmup 260d, horizons [5, 10, 20]d.

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

## REGN
BASELINE: 19 independent trades (from 108 raw signal-days) | 5d avg=-2.01% winrate=31.6% | 10d avg=-1.93% winrate=26.3% | 20d avg=0.41% winrate=52.6%
IMPROVED: 10 independent trades (from 37 raw signal-days) | 5d avg=-0.66% winrate=40.0% | 10d avg=-0.28% winrate=50.0% | 20d avg=3.57% winrate=70.0%

## CBRS
SKIPPED — not enough history (54 rows)


## ODD
BASELINE: 7 independent trades (from 32 raw signal-days) | 5d avg=2.71% winrate=42.9% | 10d avg=2.76% winrate=42.9% | 20d avg=7.16% winrate=42.9%
IMPROVED: 3 independent trades (from 7 raw signal-days) | 5d avg=-0.98% winrate=33.3% | 10d avg=2.33% winrate=33.3% | 20d avg=2.87% winrate=66.7%

## RKLB
BASELINE: 19 independent trades (from 106 raw signal-days) | 5d avg=2.76% winrate=63.2% | 10d avg=2.47% winrate=52.6% | 20d avg=11.38% winrate=63.2%
IMPROVED: 14 independent trades (from 55 raw signal-days) | 5d avg=1.91% winrate=50.0% | 10d avg=5.4% winrate=64.3% | 20d avg=13.84% winrate=64.3%

## IBM
BASELINE: 21 independent trades (from 153 raw signal-days) | 5d avg=0.84% winrate=52.4% | 10d avg=0.93% winrate=61.9% | 20d avg=1.75% winrate=61.9%
IMPROVED: 14 independent trades (from 56 raw signal-days) | 5d avg=1.47% winrate=64.3% | 10d avg=1.87% winrate=71.4% | 20d avg=1.15% winrate=64.3%

## MRVL
BASELINE: 16 independent trades (from 82 raw signal-days) | 5d avg=2.3% winrate=68.8% | 10d avg=3.84% winrate=68.8% | 20d avg=8.62% winrate=56.2%
IMPROVED: 14 independent trades (from 36 raw signal-days) | 5d avg=-0.01% winrate=57.1% | 10d avg=2.24% winrate=50.0% | 20d avg=8.38% winrate=64.3%

## QBTS
BASELINE: 14 independent trades (from 105 raw signal-days) | 5d avg=5.24% winrate=50.0% | 10d avg=15.46% winrate=35.7% | 20d avg=28.76% winrate=50.0%
IMPROVED: 13 independent trades (from 79 raw signal-days) | 5d avg=8.37% winrate=53.8% | 10d avg=16.87% winrate=38.5% | 20d avg=31.38% winrate=53.8%

## CHWY
BASELINE: 14 independent trades (from 50 raw signal-days) | 5d avg=-3.43% winrate=21.4% | 10d avg=-3.59% winrate=28.6% | 20d avg=0.38% winrate=42.9%
IMPROVED: 7 independent trades (from 12 raw signal-days) | 5d avg=-1.2% winrate=28.6% | 10d avg=-1.36% winrate=42.9% | 20d avg=1.62% winrate=28.6%

## Aggregate (all tickers' trades pooled together)
BASELINE: 194 total triggers | 5d avg=0.78% median=-0.06% winrate=48.5% | 10d avg=2.46% median=-0.15% winrate=50.0% | 20d avg=6.35% median=1.85% winrate=55.2%
IMPROVED: 134 total triggers | 5d avg=1.33% median=0.43% winrate=50.7% | 10d avg=4.37% median=0.81% winrate=54.5% | 20d avg=7.94% median=2.19% winrate=59.0%

How to read this: n_triggers = independent trades (overlapping signal-days on the same move are collapsed into one, see n_raw_signal_days in the JSON for the raw count). Compare BASELINE vs IMPROVED n_triggers and winrate/avg return at each horizon. More trades with similar or better winrate/avg return = the change helped. Fewer trades with much better winrate can also be a legitimate improvement (higher-quality, rarer signals) — that's a judgment call, not something the numbers alone decide.