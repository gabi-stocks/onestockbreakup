# Backtest results — reversal checklist (BASELINE vs IMPROVED)

Generated 2026-08-01 19:48 UTC. History: 5y, warmup 260d, horizons [5, 10, 20]d.

Signal-only backtest: no position sizing, stops, or costs. Small n_triggers = not statistically meaningful, read literally.


## ORCL
BASELINE: 110 triggers | 5d avg=1.62% winrate=60.9% | 10d avg=3.15% winrate=60.9% | 20d avg=7.16% winrate=64.5%
IMPROVED: 42 triggers | 5d avg=2.42% winrate=66.7% | 10d avg=5.16% winrate=76.2% | 20d avg=9.03% winrate=69.0%

## HTFL
SKIPPED — not enough history (245 rows)


## QCOM
BASELINE: 84 triggers | 5d avg=-0.17% winrate=41.7% | 10d avg=0.24% winrate=46.4% | 20d avg=0.81% winrate=42.9%
IMPROVED: 43 triggers | 5d avg=1.19% winrate=44.2% | 10d avg=1.99% winrate=53.5% | 20d avg=3.93% winrate=48.8%

## TEM
BASELINE: 17 triggers | 5d avg=-3.16% winrate=23.5% | 10d avg=-6.64% winrate=17.6% | 20d avg=-13.28% winrate=25.0%
IMPROVED: 8 triggers | 5d avg=-1.11% winrate=25.0% | 10d avg=-6.06% winrate=25.0% | 20d avg=-17.35% winrate=12.5%

## GEHC
BASELINE: 45 triggers | 5d avg=-0.76% winrate=42.2% | 10d avg=0.77% winrate=55.6% | 20d avg=0.32% winrate=57.8%
IMPROVED: 19 triggers | 5d avg=-1.29% winrate=36.8% | 10d avg=-0.04% winrate=57.9% | 20d avg=0.41% winrate=63.2%

## ATKR
BASELINE: 89 triggers | 5d avg=1.52% winrate=56.2% | 10d avg=2.29% winrate=53.9% | 20d avg=4.94% winrate=65.2%
IMPROVED: 30 triggers | 5d avg=-0.36% winrate=40.0% | 10d avg=1.0% winrate=56.7% | 20d avg=3.95% winrate=73.3%

## AMSC
BASELINE: 123 triggers | 5d avg=3.35% winrate=61.8% | 10d avg=11.15% winrate=65.9% | 20d avg=14.46% winrate=69.9%
IMPROVED: 65 triggers | 5d avg=1.89% winrate=53.8% | 10d avg=11.09% winrate=61.5% | 20d avg=14.05% winrate=67.7%

## Aggregate (all tickers' trades pooled together)
BASELINE: 468 total triggers | 5d avg=1.33% median=0.49% winrate=53.6% | 10d avg=3.98% median=1.41% winrate=56.2% | 20d avg=6.16% median=3.95% winrate=60.2%
IMPROVED: 207 total triggers | 5d avg=1.12% median=0.0% winrate=49.8% | 10d avg=4.85% median=2.37% winrate=60.4% | 20d avg=7.0% median=4.52% winrate=62.3%

How to read this: compare BASELINE vs IMPROVED n_triggers and winrate/avg return at each horizon. More triggers with similar or better winrate/avg return = the change helped. Fewer triggers with much better winrate can also be a legitimate improvement (higher-quality, rarer signals) — that's a judgment call, not something the numbers alone decide.