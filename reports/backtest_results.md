# Backtest results — reversal checklist (all variants)

Generated 2026-11-26 06:32 UTC. History: 5y, warmup 260d, horizons [5, 10, 20]d.

Signal-only backtest: no position sizing, stops, or costs. Small n_triggers = not statistically meaningful, read literally.


## ORCL
BASELINE: 16 independent trades (from 77 raw signal-days) | 5d avg=1.94% winrate=62.5% | 10d avg=1.95% winrate=56.2% | 20d avg=3.31% winrate=56.2%
IMPROVED: 13 independent trades (from 44 raw signal-days) | 5d avg=1.73% winrate=53.8% | 10d avg=2.52% winrate=61.5% | 20d avg=3.74% winrate=53.8%
VOL_TREND5: 10 independent trades (from 40 raw signal-days) | 5d avg=2.28% winrate=60.0% | 10d avg=6.35% winrate=70.0% | 20d avg=7.56% winrate=60.0%
VOL_LOWFLOOR: 14 independent trades (from 68 raw signal-days) | 5d avg=1.98% winrate=57.1% | 10d avg=2.49% winrate=57.1% | 20d avg=5.21% winrate=64.3%

## HTFL
BASELINE: 1 independent trades (from 7 raw signal-days) | 5d avg=4.01% winrate=100.0% | 10d avg=-2.14% winrate=0.0% | 20d avg=-15.33% winrate=0.0%
IMPROVED: 1 independent trades (from 1 raw signal-days) | 5d avg=4.01% winrate=100.0% | 10d avg=-2.14% winrate=0.0% | 20d avg=-15.33% winrate=0.0%
VOL_TREND5: 1 independent trades (from 1 raw signal-days) | 5d avg=4.01% winrate=100.0% | 10d avg=-2.14% winrate=0.0% | 20d avg=-15.33% winrate=0.0%
VOL_LOWFLOOR: 1 independent trades (from 5 raw signal-days) | 5d avg=4.01% winrate=100.0% | 10d avg=-2.14% winrate=0.0% | 20d avg=-15.33% winrate=0.0%

## QCOM
BASELINE: 15 independent trades (from 57 raw signal-days) | 5d avg=1.61% winrate=46.7% | 10d avg=0.93% winrate=46.7% | 20d avg=1.19% winrate=40.0%
IMPROVED: 10 independent trades (from 29 raw signal-days) | 5d avg=1.68% winrate=40.0% | 10d avg=2.51% winrate=50.0% | 20d avg=2.99% winrate=50.0%
VOL_TREND5: 10 independent trades (from 31 raw signal-days) | 5d avg=2.94% winrate=70.0% | 10d avg=0.88% winrate=30.0% | 20d avg=1.34% winrate=40.0%
VOL_LOWFLOOR: 14 independent trades (from 51 raw signal-days) | 5d avg=2.32% winrate=50.0% | 10d avg=1.36% winrate=50.0% | 20d avg=1.55% winrate=42.9%

## TEM
BASELINE: 5 independent trades (from 13 raw signal-days) | 5d avg=-4.09% winrate=20.0% | 10d avg=-6.96% winrate=20.0% | 20d avg=0.64% winrate=60.0%
IMPROVED: 4 independent trades (from 9 raw signal-days) | 5d avg=-1.39% winrate=25.0% | 10d avg=-7.3% winrate=25.0% | 20d avg=-5.41% winrate=50.0%
VOL_TREND5: 4 independent trades (from 9 raw signal-days) | 5d avg=-1.82% winrate=25.0% | 10d avg=-8.93% winrate=0.0% | 20d avg=-5.76% winrate=50.0%
VOL_LOWFLOOR: 4 independent trades (from 11 raw signal-days) | 5d avg=-1.39% winrate=25.0% | 10d avg=-7.3% winrate=25.0% | 20d avg=-5.41% winrate=50.0%

## GEHC
BASELINE: 11 independent trades (from 40 raw signal-days) | 5d avg=0.34% winrate=45.5% | 10d avg=0.6% winrate=54.5% | 20d avg=1.31% winrate=54.5%
IMPROVED: 10 independent trades (from 18 raw signal-days) | 5d avg=-0.35% winrate=40.0% | 10d avg=-0.86% winrate=50.0% | 20d avg=0.22% winrate=50.0%
VOL_TREND5: 9 independent trades (from 23 raw signal-days) | 5d avg=-0.59% winrate=33.3% | 10d avg=-0.95% winrate=44.4% | 20d avg=0.93% winrate=55.6%
VOL_LOWFLOOR: 11 independent trades (from 32 raw signal-days) | 5d avg=0.44% winrate=45.5% | 10d avg=-0.62% winrate=45.5% | 20d avg=0.05% winrate=45.5%

## AMSC
BASELINE: 17 independent trades (from 103 raw signal-days) | 5d avg=5.16% winrate=70.6% | 10d avg=12.04% winrate=76.5% | 20d avg=20.75% winrate=76.5%
IMPROVED: 16 independent trades (from 63 raw signal-days) | 5d avg=0.42% winrate=50.0% | 10d avg=11.21% winrate=56.2% | 20d avg=12.95% winrate=62.5%
VOL_TREND5: 14 independent trades (from 66 raw signal-days) | 5d avg=2.32% winrate=57.1% | 10d avg=19.02% winrate=71.4% | 20d avg=15.77% winrate=64.3%
VOL_LOWFLOOR: 16 independent trades (from 81 raw signal-days) | 5d avg=3.26% winrate=68.8% | 10d avg=9.81% winrate=68.8% | 20d avg=17.48% winrate=68.8%

## REGN
BASELINE: 15 independent trades (from 63 raw signal-days) | 5d avg=-1.53% winrate=33.3% | 10d avg=-0.83% winrate=46.7% | 20d avg=1.14% winrate=64.3%
IMPROVED: 10 independent trades (from 28 raw signal-days) | 5d avg=-1.03% winrate=30.0% | 10d avg=-0.1% winrate=50.0% | 20d avg=3.62% winrate=66.7%
VOL_TREND5: 9 independent trades (from 32 raw signal-days) | 5d avg=-2.03% winrate=22.2% | 10d avg=0.0% winrate=55.6% | 20d avg=4.12% winrate=50.0%
VOL_LOWFLOOR: 14 independent trades (from 51 raw signal-days) | 5d avg=-1.07% winrate=28.6% | 10d avg=-0.0% winrate=50.0% | 20d avg=2.73% winrate=69.2%

## CBRS
SKIPPED — not enough history (136 rows)


## ODD
BASELINE: 8 independent trades (from 27 raw signal-days) | 5d avg=1.57% winrate=50.0% | 10d avg=2.1% winrate=50.0% | 20d avg=3.44% winrate=50.0%
IMPROVED: 4 independent trades (from 7 raw signal-days) | 5d avg=1.78% winrate=50.0% | 10d avg=3.79% winrate=50.0% | 20d avg=6.18% winrate=75.0%
VOL_TREND5: 5 independent trades (from 11 raw signal-days) | 5d avg=-0.42% winrate=40.0% | 10d avg=1.75% winrate=40.0% | 20d avg=4.35% winrate=60.0%
VOL_LOWFLOOR: 6 independent trades (from 11 raw signal-days) | 5d avg=0.71% winrate=50.0% | 10d avg=1.06% winrate=33.3% | 20d avg=1.66% winrate=50.0%

## RKLB
BASELINE: 19 independent trades (from 79 raw signal-days) | 5d avg=0.49% winrate=47.4% | 10d avg=3.93% winrate=42.1% | 20d avg=15.33% winrate=68.4%
IMPROVED: 17 independent trades (from 53 raw signal-days) | 5d avg=-1.8% winrate=35.3% | 10d avg=2.94% winrate=41.2% | 20d avg=13.67% winrate=70.6%
VOL_TREND5: 15 independent trades (from 62 raw signal-days) | 5d avg=2.53% winrate=46.7% | 10d avg=9.5% winrate=46.7% | 20d avg=12.51% winrate=60.0%
VOL_LOWFLOOR: 17 independent trades (from 64 raw signal-days) | 5d avg=0.03% winrate=41.2% | 10d avg=5.58% winrate=47.1% | 20d avg=15.64% winrate=70.6%

## IBM
BASELINE: 18 independent trades (from 95 raw signal-days) | 5d avg=0.61% winrate=50.0% | 10d avg=-0.35% winrate=55.6% | 20d avg=0.59% winrate=55.6%
IMPROVED: 13 independent trades (from 46 raw signal-days) | 5d avg=1.76% winrate=61.5% | 10d avg=1.91% winrate=69.2% | 20d avg=1.2% winrate=61.5%
VOL_TREND5: 12 independent trades (from 45 raw signal-days) | 5d avg=1.67% winrate=50.0% | 10d avg=0.06% winrate=66.7% | 20d avg=-1.46% winrate=50.0%
VOL_LOWFLOOR: 16 independent trades (from 70 raw signal-days) | 5d avg=0.83% winrate=56.2% | 10d avg=-0.06% winrate=62.5% | 20d avg=0.75% winrate=62.5%

## MRVL
BASELINE: 19 independent trades (from 84 raw signal-days) | 5d avg=0.95% winrate=57.9% | 10d avg=4.54% winrate=63.2% | 20d avg=8.92% winrate=52.6%
IMPROVED: 16 independent trades (from 46 raw signal-days) | 5d avg=-0.04% winrate=56.2% | 10d avg=3.78% winrate=50.0% | 20d avg=5.35% winrate=50.0%
VOL_TREND5: 14 independent trades (from 50 raw signal-days) | 5d avg=3.41% winrate=71.4% | 10d avg=4.93% winrate=57.1% | 20d avg=6.93% winrate=57.1%
VOL_LOWFLOOR: 18 independent trades (from 70 raw signal-days) | 5d avg=1.41% winrate=61.1% | 10d avg=5.24% winrate=61.1% | 20d avg=8.29% winrate=55.6%

## QBTS
BASELINE: 15 independent trades (from 81 raw signal-days) | 5d avg=4.96% winrate=53.3% | 10d avg=14.73% winrate=40.0% | 20d avg=25.91% winrate=46.7%
IMPROVED: 14 independent trades (from 65 raw signal-days) | 5d avg=10.11% winrate=57.1% | 10d avg=15.97% winrate=42.9% | 20d avg=27.87% winrate=50.0%
VOL_TREND5: 12 independent trades (from 66 raw signal-days) | 5d avg=11.35% winrate=58.3% | 10d avg=19.9% winrate=41.7% | 20d avg=31.01% winrate=50.0%
VOL_LOWFLOOR: 14 independent trades (from 73 raw signal-days) | 5d avg=10.04% winrate=57.1% | 10d avg=16.22% winrate=42.9% | 20d avg=28.05% winrate=50.0%

## CHWY
BASELINE: 12 independent trades (from 34 raw signal-days) | 5d avg=-1.43% winrate=41.7% | 10d avg=-4.09% winrate=25.0% | 20d avg=-1.69% winrate=27.3%
IMPROVED: 10 independent trades (from 15 raw signal-days) | 5d avg=-0.96% winrate=30.0% | 10d avg=-2.77% winrate=30.0% | 20d avg=-2.91% winrate=22.2%
VOL_TREND5: 7 independent trades (from 12 raw signal-days) | 5d avg=-2.12% winrate=28.6% | 10d avg=-2.39% winrate=28.6% | 20d avg=-0.77% winrate=28.6%
VOL_LOWFLOOR: 12 independent trades (from 27 raw signal-days) | 5d avg=-1.83% winrate=33.3% | 10d avg=-4.59% winrate=25.0% | 20d avg=-2.5% winrate=27.3%

## NKE
BASELINE: 11 independent trades (from 33 raw signal-days) | 5d avg=-1.37% winrate=36.4% | 10d avg=-2.15% winrate=36.4% | 20d avg=-4.21% winrate=20.0%
IMPROVED: 7 independent trades (from 13 raw signal-days) | 5d avg=-0.67% winrate=42.9% | 10d avg=-3.35% winrate=28.6% | 20d avg=-4.31% winrate=16.7%
VOL_TREND5: 3 independent trades (from 6 raw signal-days) | 5d avg=-2.85% winrate=33.3% | 10d avg=-5.63% winrate=33.3% | 20d avg=-6.38% winrate=33.3%
VOL_LOWFLOOR: 10 independent trades (from 27 raw signal-days) | 5d avg=-0.66% winrate=40.0% | 10d avg=-3.38% winrate=20.0% | 20d avg=-7.63% winrate=11.1%

## BNTX
BASELINE: 15 independent trades (from 44 raw signal-days) | 5d avg=-1.13% winrate=33.3% | 10d avg=-2.77% winrate=33.3% | 20d avg=-4.54% winrate=20.0%
IMPROVED: 8 independent trades (from 20 raw signal-days) | 5d avg=1.9% winrate=37.5% | 10d avg=0.2% winrate=37.5% | 20d avg=-0.22% winrate=37.5%
VOL_TREND5: 9 independent trades (from 20 raw signal-days) | 5d avg=-1.53% winrate=22.2% | 10d avg=-2.71% winrate=22.2% | 20d avg=-3.65% winrate=22.2%
VOL_LOWFLOOR: 12 independent trades (from 30 raw signal-days) | 5d avg=-0.9% winrate=25.0% | 10d avg=-2.37% winrate=33.3% | 20d avg=-3.35% winrate=25.0%

## CEG
BASELINE: 15 independent trades (from 54 raw signal-days) | 5d avg=2.35% winrate=60.0% | 10d avg=1.8% winrate=53.3% | 20d avg=1.89% winrate=60.0%
IMPROVED: 10 independent trades (from 30 raw signal-days) | 5d avg=5.33% winrate=80.0% | 10d avg=5.53% winrate=60.0% | 20d avg=4.17% winrate=60.0%
VOL_TREND5: 9 independent trades (from 33 raw signal-days) | 5d avg=3.92% winrate=88.9% | 10d avg=5.0% winrate=77.8% | 20d avg=5.81% winrate=88.9%
VOL_LOWFLOOR: 13 independent trades (from 44 raw signal-days) | 5d avg=3.76% winrate=69.2% | 10d avg=4.39% winrate=61.5% | 20d avg=2.53% winrate=61.5%

## ASTS
BASELINE: 14 independent trades (from 57 raw signal-days) | 5d avg=-0.19% winrate=42.9% | 10d avg=5.49% winrate=57.1% | 20d avg=19.85% winrate=57.1%
IMPROVED: 12 independent trades (from 35 raw signal-days) | 5d avg=-1.72% winrate=41.7% | 10d avg=4.24% winrate=41.7% | 20d avg=22.49% winrate=58.3%
VOL_TREND5: 12 independent trades (from 45 raw signal-days) | 5d avg=-0.86% winrate=41.7% | 10d avg=-1.25% winrate=50.0% | 20d avg=4.24% winrate=58.3%
VOL_LOWFLOOR: 13 independent trades (from 45 raw signal-days) | 5d avg=-1.7% winrate=38.5% | 10d avg=4.11% winrate=46.2% | 20d avg=21.54% winrate=61.5%

## ROK
BASELINE: 15 independent trades (from 51 raw signal-days) | 5d avg=-0.96% winrate=46.7% | 10d avg=-0.08% winrate=20.0% | 20d avg=1.18% winrate=53.3%
IMPROVED: 9 independent trades (from 15 raw signal-days) | 5d avg=-0.52% winrate=55.6% | 10d avg=-2.27% winrate=11.1% | 20d avg=2.16% winrate=66.7%
VOL_TREND5: 7 independent trades (from 13 raw signal-days) | 5d avg=0.59% winrate=71.4% | 10d avg=0.61% winrate=28.6% | 20d avg=4.55% winrate=85.7%
VOL_LOWFLOOR: 13 independent trades (from 34 raw signal-days) | 5d avg=-1.08% winrate=46.2% | 10d avg=-1.54% winrate=15.4% | 20d avg=-0.09% winrate=53.8%

## DKS
BASELINE: 14 independent trades (from 51 raw signal-days) | 5d avg=-0.09% winrate=53.8% | 10d avg=1.02% winrate=69.2% | 20d avg=3.56% winrate=69.2%
IMPROVED: 11 independent trades (from 24 raw signal-days) | 5d avg=0.61% winrate=72.7% | 10d avg=1.95% winrate=63.6% | 20d avg=0.31% winrate=54.5%
VOL_TREND5: 11 independent trades (from 25 raw signal-days) | 5d avg=0.15% winrate=63.6% | 10d avg=1.17% winrate=54.5% | 20d avg=1.81% winrate=72.7%
VOL_LOWFLOOR: 13 independent trades (from 40 raw signal-days) | 5d avg=-0.31% winrate=53.8% | 10d avg=0.75% winrate=61.5% | 20d avg=3.64% winrate=69.2%

## COPJ
BASELINE: 13 independent trades (from 68 raw signal-days) | 5d avg=2.97% winrate=84.6% | 10d avg=2.86% winrate=61.5% | 20d avg=3.83% winrate=69.2%
IMPROVED: 12 independent trades (from 48 raw signal-days) | 5d avg=3.05% winrate=83.3% | 10d avg=1.91% winrate=66.7% | 20d avg=3.7% winrate=66.7%
VOL_TREND5: 12 independent trades (from 54 raw signal-days) | 5d avg=2.9% winrate=83.3% | 10d avg=2.0% winrate=66.7% | 20d avg=3.45% winrate=66.7%
VOL_LOWFLOOR: 12 independent trades (from 55 raw signal-days) | 5d avg=3.45% winrate=91.7% | 10d avg=2.34% winrate=66.7% | 20d avg=3.79% winrate=66.7%

## ZIM
BASELINE: 17 independent trades (from 71 raw signal-days) | 5d avg=-0.13% winrate=41.2% | 10d avg=3.65% winrate=64.7% | 20d avg=7.8% winrate=58.8%
IMPROVED: 15 independent trades (from 50 raw signal-days) | 5d avg=2.31% winrate=46.7% | 10d avg=3.44% winrate=66.7% | 20d avg=8.61% winrate=60.0%
VOL_TREND5: 13 independent trades (from 53 raw signal-days) | 5d avg=4.55% winrate=46.2% | 10d avg=4.43% winrate=69.2% | 20d avg=10.13% winrate=61.5%
VOL_LOWFLOOR: 15 independent trades (from 57 raw signal-days) | 5d avg=3.01% winrate=46.7% | 10d avg=4.83% winrate=66.7% | 20d avg=9.5% winrate=60.0%

## TEVA
BASELINE: 18 independent trades (from 87 raw signal-days) | 5d avg=2.57% winrate=77.8% | 10d avg=1.57% winrate=61.1% | 20d avg=4.93% winrate=72.2%
IMPROVED: 16 independent trades (from 38 raw signal-days) | 5d avg=0.76% winrate=62.5% | 10d avg=-0.04% winrate=50.0% | 20d avg=1.89% winrate=56.2%
VOL_TREND5: 16 independent trades (from 43 raw signal-days) | 5d avg=0.94% winrate=68.8% | 10d avg=-0.15% winrate=50.0% | 20d avg=2.69% winrate=56.2%
VOL_LOWFLOOR: 17 independent trades (from 59 raw signal-days) | 5d avg=1.11% winrate=64.7% | 10d avg=0.22% winrate=47.1% | 20d avg=2.78% winrate=58.8%

## CRL
BASELINE: 15 independent trades (from 75 raw signal-days) | 5d avg=-0.39% winrate=53.3% | 10d avg=-0.44% winrate=60.0% | 20d avg=-1.41% winrate=40.0%
IMPROVED: 12 independent trades (from 31 raw signal-days) | 5d avg=0.37% winrate=50.0% | 10d avg=-1.73% winrate=50.0% | 20d avg=-2.85% winrate=33.3%
VOL_TREND5: 11 independent trades (from 43 raw signal-days) | 5d avg=0.52% winrate=45.5% | 10d avg=-2.32% winrate=45.5% | 20d avg=-3.78% winrate=27.3%
VOL_LOWFLOOR: 14 independent trades (from 48 raw signal-days) | 5d avg=-0.47% winrate=50.0% | 10d avg=-0.16% winrate=57.1% | 20d avg=-2.29% winrate=35.7%

## MSFT
BASELINE: 19 independent trades (from 109 raw signal-days) | 5d avg=1.06% winrate=78.9% | 10d avg=0.93% winrate=63.2% | 20d avg=3.17% winrate=63.2%
IMPROVED: 17 independent trades (from 31 raw signal-days) | 5d avg=0.53% winrate=64.7% | 10d avg=0.02% winrate=52.9% | 20d avg=0.17% winrate=52.9%
VOL_TREND5: 15 independent trades (from 31 raw signal-days) | 5d avg=0.81% winrate=73.3% | 10d avg=0.41% winrate=60.0% | 20d avg=-0.3% winrate=46.7%
VOL_LOWFLOOR: 18 independent trades (from 78 raw signal-days) | 5d avg=1.4% winrate=83.3% | 10d avg=1.61% winrate=72.2% | 20d avg=1.94% winrate=66.7%

## GOOGL
BASELINE: 17 independent trades (from 68 raw signal-days) | 5d avg=0.5% winrate=52.9% | 10d avg=1.78% winrate=58.8% | 20d avg=2.75% winrate=58.8%
IMPROVED: 12 independent trades (from 31 raw signal-days) | 5d avg=0.4% winrate=58.3% | 10d avg=0.66% winrate=58.3% | 20d avg=1.81% winrate=58.3%
VOL_TREND5: 13 independent trades (from 32 raw signal-days) | 5d avg=-0.63% winrate=46.2% | 10d avg=0.37% winrate=53.8% | 20d avg=0.29% winrate=53.8%
VOL_LOWFLOOR: 16 independent trades (from 54 raw signal-days) | 5d avg=0.21% winrate=50.0% | 10d avg=1.58% winrate=56.2% | 20d avg=2.77% winrate=62.5%

## ETN
BASELINE: 21 independent trades (from 78 raw signal-days) | 5d avg=-0.18% winrate=66.7% | 10d avg=0.81% winrate=61.9% | 20d avg=2.89% winrate=71.4%
IMPROVED: 13 independent trades (from 34 raw signal-days) | 5d avg=-1.05% winrate=46.2% | 10d avg=1.11% winrate=76.9% | 20d avg=1.37% winrate=69.2%
VOL_TREND5: 14 independent trades (from 40 raw signal-days) | 5d avg=-0.69% winrate=57.1% | 10d avg=0.62% winrate=57.1% | 20d avg=1.62% winrate=64.3%
VOL_LOWFLOOR: 17 independent trades (from 55 raw signal-days) | 5d avg=-0.81% winrate=58.8% | 10d avg=1.2% winrate=70.6% | 20d avg=1.75% winrate=64.7%

## VST
BASELINE: 17 independent trades (from 78 raw signal-days) | 5d avg=1.86% winrate=47.1% | 10d avg=5.15% winrate=58.8% | 20d avg=7.7% winrate=64.7%
IMPROVED: 14 independent trades (from 49 raw signal-days) | 5d avg=1.81% winrate=35.7% | 10d avg=4.96% winrate=64.3% | 20d avg=7.25% winrate=71.4%
VOL_TREND5: 13 independent trades (from 51 raw signal-days) | 5d avg=0.33% winrate=38.5% | 10d avg=5.46% winrate=69.2% | 20d avg=7.98% winrate=69.2%
VOL_LOWFLOOR: 16 independent trades (from 65 raw signal-days) | 5d avg=1.55% winrate=43.8% | 10d avg=5.02% winrate=56.2% | 20d avg=7.06% winrate=68.8%

## DTCR
BASELINE: 17 independent trades (from 85 raw signal-days) | 5d avg=0.51% winrate=52.9% | 10d avg=0.53% winrate=47.1% | 20d avg=1.32% winrate=58.8%
IMPROVED: 12 independent trades (from 52 raw signal-days) | 5d avg=0.71% winrate=58.3% | 10d avg=0.85% winrate=58.3% | 20d avg=3.31% winrate=75.0%
VOL_TREND5: 14 independent trades (from 66 raw signal-days) | 5d avg=1.09% winrate=64.3% | 10d avg=0.95% winrate=50.0% | 20d avg=1.9% winrate=64.3%
VOL_LOWFLOOR: 13 independent trades (from 67 raw signal-days) | 5d avg=0.44% winrate=53.8% | 10d avg=0.78% winrate=53.8% | 20d avg=2.93% winrate=69.2%

## CRDO
BASELINE: 17 independent trades (from 78 raw signal-days) | 5d avg=-5.47% winrate=41.2% | 10d avg=-0.68% winrate=41.2% | 20d avg=4.14% winrate=52.9%
IMPROVED: 12 independent trades (from 40 raw signal-days) | 5d avg=-4.06% winrate=50.0% | 10d avg=3.64% winrate=66.7% | 20d avg=3.44% winrate=75.0%
VOL_TREND5: 15 independent trades (from 51 raw signal-days) | 5d avg=-4.47% winrate=46.7% | 10d avg=-1.21% winrate=40.0% | 20d avg=3.58% winrate=53.3%
VOL_LOWFLOOR: 15 independent trades (from 53 raw signal-days) | 5d avg=-4.61% winrate=53.3% | 10d avg=1.02% winrate=53.3% | 20d avg=2.83% winrate=53.3%

## LEU
BASELINE: 15 independent trades (from 74 raw signal-days) | 5d avg=2.83% winrate=53.3% | 10d avg=8.98% winrate=66.7% | 20d avg=15.03% winrate=66.7%
IMPROVED: 12 independent trades (from 48 raw signal-days) | 5d avg=3.92% winrate=58.3% | 10d avg=10.13% winrate=75.0% | 20d avg=15.49% winrate=66.7%
VOL_TREND5: 13 independent trades (from 51 raw signal-days) | 5d avg=1.88% winrate=53.8% | 10d avg=6.96% winrate=53.8% | 20d avg=8.61% winrate=53.8%
VOL_LOWFLOOR: 14 independent trades (from 59 raw signal-days) | 5d avg=1.91% winrate=57.1% | 10d avg=8.31% winrate=64.3% | 20d avg=13.45% winrate=64.3%

## INVZ
BASELINE: 11 independent trades (from 48 raw signal-days) | 5d avg=-1.05% winrate=36.4% | 10d avg=-1.08% winrate=36.4% | 20d avg=12.56% winrate=36.4%
IMPROVED: 9 independent trades (from 36 raw signal-days) | 5d avg=4.2% winrate=55.6% | 10d avg=12.34% winrate=55.6% | 20d avg=8.94% winrate=44.4%
VOL_TREND5: 10 independent trades (from 43 raw signal-days) | 5d avg=2.58% winrate=50.0% | 10d avg=1.91% winrate=50.0% | 20d avg=15.12% winrate=40.0%
VOL_LOWFLOOR: 10 independent trades (from 42 raw signal-days) | 5d avg=2.58% winrate=50.0% | 10d avg=1.91% winrate=50.0% | 20d avg=15.12% winrate=40.0%

## NVDA
BASELINE: 19 independent trades (from 85 raw signal-days) | 5d avg=-0.13% winrate=36.8% | 10d avg=1.29% winrate=47.4% | 20d avg=4.38% winrate=57.9%
IMPROVED: 15 independent trades (from 38 raw signal-days) | 5d avg=-0.72% winrate=46.7% | 10d avg=1.55% winrate=53.3% | 20d avg=3.59% winrate=60.0%
VOL_TREND5: 10 independent trades (from 42 raw signal-days) | 5d avg=2.5% winrate=50.0% | 10d avg=5.31% winrate=60.0% | 20d avg=8.99% winrate=70.0%
VOL_LOWFLOOR: 18 independent trades (from 77 raw signal-days) | 5d avg=-0.03% winrate=38.9% | 10d avg=2.31% winrate=50.0% | 20d avg=4.97% winrate=61.1%

## ARM
BASELINE: 11 independent trades (from 45 raw signal-days) | 5d avg=3.37% winrate=54.5% | 10d avg=5.92% winrate=54.5% | 20d avg=9.77% winrate=54.5%
IMPROVED: 10 independent trades (from 25 raw signal-days) | 5d avg=1.09% winrate=40.0% | 10d avg=1.37% winrate=40.0% | 20d avg=3.84% winrate=50.0%
VOL_TREND5: 10 independent trades (from 28 raw signal-days) | 5d avg=-1.46% winrate=40.0% | 10d avg=-0.18% winrate=30.0% | 20d avg=2.03% winrate=40.0%
VOL_LOWFLOOR: 10 independent trades (from 34 raw signal-days) | 5d avg=5.2% winrate=50.0% | 10d avg=5.88% winrate=50.0% | 20d avg=7.06% winrate=50.0%

## NOW
BASELINE: 17 independent trades (from 72 raw signal-days) | 5d avg=-0.1% winrate=52.9% | 10d avg=1.47% winrate=64.7% | 20d avg=0.45% winrate=41.2%
IMPROVED: 12 independent trades (from 30 raw signal-days) | 5d avg=-0.06% winrate=58.3% | 10d avg=1.76% winrate=50.0% | 20d avg=0.03% winrate=41.7%
VOL_TREND5: 15 independent trades (from 34 raw signal-days) | 5d avg=-0.96% winrate=46.7% | 10d avg=-0.01% winrate=46.7% | 20d avg=-2.18% winrate=33.3%
VOL_LOWFLOOR: 14 independent trades (from 48 raw signal-days) | 5d avg=-0.75% winrate=50.0% | 10d avg=1.1% winrate=57.1% | 20d avg=-0.47% winrate=35.7%

## SPCX
SKIPPED — not enough history (116 rows)


## LUNR
BASELINE: 16 independent trades (from 55 raw signal-days) | 5d avg=-5.21% winrate=50.0% | 10d avg=-3.23% winrate=37.5% | 20d avg=9.23% winrate=50.0%
IMPROVED: 14 independent trades (from 35 raw signal-days) | 5d avg=-7.85% winrate=35.7% | 10d avg=-8.91% winrate=28.6% | 20d avg=3.75% winrate=35.7%
VOL_TREND5: 12 independent trades (from 41 raw signal-days) | 5d avg=-2.15% winrate=50.0% | 10d avg=-2.37% winrate=50.0% | 20d avg=17.17% winrate=50.0%
VOL_LOWFLOOR: 15 independent trades (from 45 raw signal-days) | 5d avg=-2.89% winrate=46.7% | 10d avg=-8.34% winrate=20.0% | 20d avg=5.8% winrate=40.0%

## USO
BASELINE: 16 independent trades (from 68 raw signal-days) | 5d avg=-0.31% winrate=43.8% | 10d avg=0.39% winrate=37.5% | 20d avg=2.76% winrate=56.2%
IMPROVED: 11 independent trades (from 37 raw signal-days) | 5d avg=-0.05% winrate=45.5% | 10d avg=2.25% winrate=54.5% | 20d avg=5.56% winrate=63.6%
VOL_TREND5: 8 independent trades (from 30 raw signal-days) | 5d avg=0.57% winrate=50.0% | 10d avg=2.64% winrate=50.0% | 20d avg=5.86% winrate=62.5%
VOL_LOWFLOOR: 15 independent trades (from 60 raw signal-days) | 5d avg=-0.17% winrate=46.7% | 10d avg=0.75% winrate=40.0% | 20d avg=2.83% winrate=53.3%

## GEV
BASELINE: 9 independent trades (from 37 raw signal-days) | 5d avg=-0.02% winrate=77.8% | 10d avg=2.76% winrate=66.7% | 20d avg=6.45% winrate=66.7%
IMPROVED: 6 independent trades (from 15 raw signal-days) | 5d avg=0.7% winrate=66.7% | 10d avg=2.87% winrate=50.0% | 20d avg=5.34% winrate=50.0%
VOL_TREND5: 4 independent trades (from 11 raw signal-days) | 5d avg=1.46% winrate=75.0% | 10d avg=5.45% winrate=75.0% | 20d avg=5.51% winrate=50.0%
VOL_LOWFLOOR: 7 independent trades (from 24 raw signal-days) | 5d avg=1.29% winrate=85.7% | 10d avg=4.47% winrate=57.1% | 20d avg=4.85% winrate=57.1%

## IREN
BASELINE: 18 independent trades (from 76 raw signal-days) | 5d avg=0.3% winrate=50.0% | 10d avg=6.17% winrate=55.6% | 20d avg=10.32% winrate=50.0%
IMPROVED: 15 independent trades (from 57 raw signal-days) | 5d avg=4.52% winrate=53.3% | 10d avg=11.08% winrate=66.7% | 20d avg=17.3% winrate=53.3%
VOL_TREND5: 16 independent trades (from 71 raw signal-days) | 5d avg=2.66% winrate=56.2% | 10d avg=8.77% winrate=56.2% | 20d avg=11.77% winrate=50.0%
VOL_LOWFLOOR: 18 independent trades (from 73 raw signal-days) | 5d avg=2.37% winrate=50.0% | 10d avg=8.13% winrate=55.6% | 20d avg=10.8% winrate=50.0%

## QTUM
BASELINE: 20 independent trades (from 104 raw signal-days) | 5d avg=0.17% winrate=55.0% | 10d avg=0.55% winrate=60.0% | 20d avg=3.65% winrate=70.0%
IMPROVED: 16 independent trades (from 72 raw signal-days) | 5d avg=0.2% winrate=56.2% | 10d avg=1.08% winrate=62.5% | 20d avg=4.47% winrate=75.0%
VOL_TREND5: 15 independent trades (from 80 raw signal-days) | 5d avg=0.58% winrate=66.7% | 10d avg=0.68% winrate=53.3% | 20d avg=3.97% winrate=66.7%
VOL_LOWFLOOR: 18 independent trades (from 93 raw signal-days) | 5d avg=0.3% winrate=61.1% | 10d avg=0.56% winrate=61.1% | 20d avg=3.85% winrate=72.2%

## CHKP
BASELINE: 20 independent trades (from 62 raw signal-days) | 5d avg=-0.0% winrate=36.8% | 10d avg=0.11% winrate=63.2% | 20d avg=-0.77% winrate=57.9%
IMPROVED: 16 independent trades (from 24 raw signal-days) | 5d avg=0.3% winrate=50.0% | 10d avg=-0.57% winrate=43.8% | 20d avg=-0.6% winrate=56.2%
VOL_TREND5: 14 independent trades (from 33 raw signal-days) | 5d avg=0.37% winrate=42.9% | 10d avg=-0.33% winrate=42.9% | 20d avg=-0.79% winrate=57.1%
VOL_LOWFLOOR: 18 independent trades (from 42 raw signal-days) | 5d avg=-0.07% winrate=44.4% | 10d avg=-0.09% winrate=55.6% | 20d avg=-0.79% winrate=55.6%

## ZBRA
BASELINE: 14 independent trades (from 49 raw signal-days) | 5d avg=0.16% winrate=42.9% | 10d avg=0.91% winrate=42.9% | 20d avg=2.19% winrate=57.1%
IMPROVED: 11 independent trades (from 20 raw signal-days) | 5d avg=-1.54% winrate=27.3% | 10d avg=-0.12% winrate=45.5% | 20d avg=-1.54% winrate=45.5%
VOL_TREND5: 9 independent trades (from 18 raw signal-days) | 5d avg=-2.04% winrate=22.2% | 10d avg=-0.27% winrate=44.4% | 20d avg=0.38% winrate=55.6%
VOL_LOWFLOOR: 12 independent trades (from 33 raw signal-days) | 5d avg=-0.72% winrate=33.3% | 10d avg=-0.62% winrate=33.3% | 20d avg=0.73% winrate=58.3%

## XAR
BASELINE: 17 independent trades (from 79 raw signal-days) | 5d avg=0.16% winrate=58.8% | 10d avg=0.32% winrate=52.9% | 20d avg=1.38% winrate=58.8%
IMPROVED: 13 independent trades (from 45 raw signal-days) | 5d avg=0.58% winrate=61.5% | 10d avg=0.74% winrate=61.5% | 20d avg=2.02% winrate=69.2%
VOL_TREND5: 13 independent trades (from 37 raw signal-days) | 5d avg=1.37% winrate=69.2% | 10d avg=1.11% winrate=61.5% | 20d avg=1.36% winrate=69.2%
VOL_LOWFLOOR: 15 independent trades (from 64 raw signal-days) | 5d avg=0.25% winrate=60.0% | 10d avg=0.52% winrate=53.3% | 20d avg=1.44% winrate=60.0%

## JPM
BASELINE: 18 independent trades (from 102 raw signal-days) | 5d avg=0.45% winrate=50.0% | 10d avg=1.8% winrate=66.7% | 20d avg=3.24% winrate=61.1%
IMPROVED: 11 independent trades (from 32 raw signal-days) | 5d avg=1.01% winrate=63.6% | 10d avg=1.9% winrate=54.5% | 20d avg=2.37% winrate=54.5%
VOL_TREND5: 9 independent trades (from 37 raw signal-days) | 5d avg=2.6% winrate=77.8% | 10d avg=2.67% winrate=66.7% | 20d avg=2.5% winrate=55.6%
VOL_LOWFLOOR: 16 independent trades (from 80 raw signal-days) | 5d avg=0.62% winrate=50.0% | 10d avg=2.08% winrate=75.0% | 20d avg=3.73% winrate=68.8%

## IBIT
BASELINE: 6 independent trades (from 37 raw signal-days) | 5d avg=4.08% winrate=66.7% | 10d avg=3.56% winrate=66.7% | 20d avg=-0.09% winrate=66.7%
IMPROVED: 6 independent trades (from 25 raw signal-days) | 5d avg=3.17% winrate=50.0% | 10d avg=0.61% winrate=50.0% | 20d avg=-1.83% winrate=50.0%
VOL_TREND5: 6 independent trades (from 22 raw signal-days) | 5d avg=1.66% winrate=50.0% | 10d avg=-1.87% winrate=50.0% | 20d avg=-5.62% winrate=50.0%
VOL_LOWFLOOR: 6 independent trades (from 30 raw signal-days) | 5d avg=4.08% winrate=66.7% | 10d avg=1.62% winrate=66.7% | 20d avg=-0.17% winrate=66.7%

## COIN
BASELINE: 16 independent trades (from 56 raw signal-days) | 5d avg=1.06% winrate=50.0% | 10d avg=-0.72% winrate=25.0% | 20d avg=1.17% winrate=50.0%
IMPROVED: 12 independent trades (from 31 raw signal-days) | 5d avg=1.21% winrate=33.3% | 10d avg=2.48% winrate=33.3% | 20d avg=6.25% winrate=41.7%
VOL_TREND5: 13 independent trades (from 40 raw signal-days) | 5d avg=1.06% winrate=46.2% | 10d avg=1.68% winrate=38.5% | 20d avg=-2.26% winrate=38.5%
VOL_LOWFLOOR: 16 independent trades (from 50 raw signal-days) | 5d avg=0.27% winrate=43.8% | 10d avg=-1.52% winrate=18.8% | 20d avg=0.92% winrate=50.0%

## HOOD
BASELINE: 16 independent trades (from 89 raw signal-days) | 5d avg=1.28% winrate=50.0% | 10d avg=4.94% winrate=75.0% | 20d avg=7.38% winrate=68.8%
IMPROVED: 14 independent trades (from 47 raw signal-days) | 5d avg=-0.43% winrate=50.0% | 10d avg=2.44% winrate=64.3% | 20d avg=6.71% winrate=64.3%
VOL_TREND5: 14 independent trades (from 60 raw signal-days) | 5d avg=-0.67% winrate=42.9% | 10d avg=3.17% winrate=71.4% | 20d avg=5.61% winrate=64.3%
VOL_LOWFLOOR: 15 independent trades (from 67 raw signal-days) | 5d avg=1.48% winrate=53.3% | 10d avg=4.56% winrate=73.3% | 20d avg=6.03% winrate=66.7%

## TER
BASELINE: 20 independent trades (from 71 raw signal-days) | 5d avg=1.21% winrate=65.0% | 10d avg=0.58% winrate=60.0% | 20d avg=-0.79% winrate=60.0%
IMPROVED: 13 independent trades (from 26 raw signal-days) | 5d avg=-0.65% winrate=61.5% | 10d avg=-2.01% winrate=53.8% | 20d avg=-0.52% winrate=61.5%
VOL_TREND5: 11 independent trades (from 32 raw signal-days) | 5d avg=1.1% winrate=63.6% | 10d avg=1.28% winrate=81.8% | 20d avg=3.76% winrate=63.6%
VOL_LOWFLOOR: 18 independent trades (from 54 raw signal-days) | 5d avg=-0.24% winrate=61.1% | 10d avg=-0.52% winrate=50.0% | 20d avg=-2.26% winrate=55.6%

## OKLO
BASELINE: 15 independent trades (from 67 raw signal-days) | 5d avg=-3.47% winrate=33.3% | 10d avg=1.79% winrate=40.0% | 20d avg=17.38% winrate=53.3%
IMPROVED: 12 independent trades (from 55 raw signal-days) | 5d avg=-0.35% winrate=58.3% | 10d avg=8.24% winrate=66.7% | 20d avg=27.35% winrate=66.7%
VOL_TREND5: 15 independent trades (from 59 raw signal-days) | 5d avg=-2.25% winrate=40.0% | 10d avg=3.71% winrate=46.7% | 20d avg=19.21% winrate=53.3%
VOL_LOWFLOOR: 14 independent trades (from 63 raw signal-days) | 5d avg=-2.53% winrate=35.7% | 10d avg=3.87% winrate=42.9% | 20d avg=20.62% winrate=57.1%

## NNE
BASELINE: 5 independent trades (from 21 raw signal-days) | 5d avg=-4.81% winrate=40.0% | 10d avg=-8.63% winrate=40.0% | 20d avg=2.97% winrate=60.0%
IMPROVED: 4 independent trades (from 16 raw signal-days) | 5d avg=-2.49% winrate=50.0% | 10d avg=-5.7% winrate=50.0% | 20d avg=11.48% winrate=75.0%
VOL_TREND5: 4 independent trades (from 20 raw signal-days) | 5d avg=-2.49% winrate=50.0% | 10d avg=-5.7% winrate=50.0% | 20d avg=11.48% winrate=75.0%
VOL_LOWFLOOR: 5 independent trades (from 20 raw signal-days) | 5d avg=-4.81% winrate=40.0% | 10d avg=-8.63% winrate=40.0% | 20d avg=2.97% winrate=60.0%

## KRE
BASELINE: 15 independent trades (from 55 raw signal-days) | 5d avg=-0.34% winrate=53.3% | 10d avg=1.44% winrate=60.0% | 20d avg=2.27% winrate=42.9%
IMPROVED: 12 independent trades (from 28 raw signal-days) | 5d avg=0.11% winrate=50.0% | 10d avg=1.58% winrate=58.3% | 20d avg=1.86% winrate=36.4%
VOL_TREND5: 10 independent trades (from 33 raw signal-days) | 5d avg=-0.45% winrate=50.0% | 10d avg=2.02% winrate=70.0% | 20d avg=3.47% winrate=44.4%
VOL_LOWFLOOR: 13 independent trades (from 42 raw signal-days) | 5d avg=0.52% winrate=61.5% | 10d avg=2.06% winrate=61.5% | 20d avg=1.84% winrate=33.3%

## PANW
BASELINE: 19 independent trades (from 78 raw signal-days) | 5d avg=2.55% winrate=63.2% | 10d avg=1.4% winrate=52.6% | 20d avg=3.02% winrate=47.4%
IMPROVED: 13 independent trades (from 38 raw signal-days) | 5d avg=2.27% winrate=61.5% | 10d avg=4.89% winrate=69.2% | 20d avg=4.89% winrate=46.2%
VOL_TREND5: 11 independent trades (from 38 raw signal-days) | 5d avg=1.16% winrate=45.5% | 10d avg=1.81% winrate=45.5% | 20d avg=3.45% winrate=36.4%
VOL_LOWFLOOR: 18 independent trades (from 61 raw signal-days) | 5d avg=2.19% winrate=61.1% | 10d avg=1.78% winrate=55.6% | 20d avg=2.93% winrate=50.0%

## AAPL
BASELINE: 19 independent trades (from 71 raw signal-days) | 5d avg=-0.77% winrate=36.8% | 10d avg=0.2% winrate=52.6% | 20d avg=0.55% winrate=52.6%
IMPROVED: 14 independent trades (from 25 raw signal-days) | 5d avg=0.28% winrate=50.0% | 10d avg=0.78% winrate=57.1% | 20d avg=1.38% winrate=64.3%
VOL_TREND5: 14 independent trades (from 31 raw signal-days) | 5d avg=0.16% winrate=35.7% | 10d avg=-0.14% winrate=42.9% | 20d avg=-0.45% winrate=50.0%
VOL_LOWFLOOR: 18 independent trades (from 62 raw signal-days) | 5d avg=-0.36% winrate=38.9% | 10d avg=0.4% winrate=61.1% | 20d avg=1.25% winrate=61.1%

## TSEM
BASELINE: 18 independent trades (from 91 raw signal-days) | 5d avg=0.64% winrate=61.1% | 10d avg=2.29% winrate=61.1% | 20d avg=4.08% winrate=72.2%
IMPROVED: 16 independent trades (from 48 raw signal-days) | 5d avg=-0.15% winrate=56.2% | 10d avg=0.51% winrate=50.0% | 20d avg=3.32% winrate=68.8%
VOL_TREND5: 13 independent trades (from 54 raw signal-days) | 5d avg=1.36% winrate=61.5% | 10d avg=4.39% winrate=61.5% | 20d avg=6.15% winrate=76.9%
VOL_LOWFLOOR: 16 independent trades (from 70 raw signal-days) | 5d avg=1.04% winrate=62.5% | 10d avg=3.31% winrate=62.5% | 20d avg=4.42% winrate=75.0%

## TLT
BASELINE: 13 independent trades (from 42 raw signal-days) | 5d avg=-0.11% winrate=61.5% | 10d avg=-0.85% winrate=30.8% | 20d avg=-1.53% winrate=25.0%
IMPROVED: 9 independent trades (from 17 raw signal-days) | 5d avg=-0.57% winrate=44.4% | 10d avg=-0.82% winrate=22.2% | 20d avg=-1.41% winrate=37.5%
VOL_TREND5: 8 independent trades (from 19 raw signal-days) | 5d avg=-0.55% winrate=37.5% | 10d avg=-0.47% winrate=25.0% | 20d avg=-0.56% winrate=42.9%
VOL_LOWFLOOR: 11 independent trades (from 30 raw signal-days) | 5d avg=-0.46% winrate=54.5% | 10d avg=-0.87% winrate=27.3% | 20d avg=-1.61% winrate=30.0%

## IEF
BASELINE: 12 independent trades (from 44 raw signal-days) | 5d avg=-0.13% winrate=50.0% | 10d avg=-0.13% winrate=50.0% | 20d avg=-0.09% winrate=41.7%
IMPROVED: 6 independent trades (from 18 raw signal-days) | 5d avg=0.35% winrate=83.3% | 10d avg=0.25% winrate=83.3% | 20d avg=0.66% winrate=50.0%
VOL_TREND5: 7 independent trades (from 22 raw signal-days) | 5d avg=0.08% winrate=57.1% | 10d avg=0.11% winrate=57.1% | 20d avg=-0.1% winrate=42.9%
VOL_LOWFLOOR: 9 independent trades (from 33 raw signal-days) | 5d avg=0.25% winrate=77.8% | 10d avg=0.12% winrate=66.7% | 20d avg=0.4% winrate=55.6%

## VCLT
BASELINE: 16 independent trades (from 52 raw signal-days) | 5d avg=-0.15% winrate=43.8% | 10d avg=-0.25% winrate=56.2% | 20d avg=-0.15% winrate=56.2%
IMPROVED: 11 independent trades (from 25 raw signal-days) | 5d avg=-0.4% winrate=36.4% | 10d avg=-0.15% winrate=45.5% | 20d avg=-0.4% winrate=54.5%
VOL_TREND5: 11 independent trades (from 29 raw signal-days) | 5d avg=-0.3% winrate=36.4% | 10d avg=-0.35% winrate=45.5% | 20d avg=-0.08% winrate=63.6%
VOL_LOWFLOOR: 12 independent trades (from 38 raw signal-days) | 5d avg=-0.3% winrate=41.7% | 10d avg=-0.14% winrate=50.0% | 20d avg=-0.24% winrate=50.0%

## AMZN
BASELINE: 24 independent trades (from 69 raw signal-days) | 5d avg=-0.87% winrate=41.7% | 10d avg=-1.87% winrate=33.3% | 20d avg=0.02% winrate=54.2%
IMPROVED: 16 independent trades (from 34 raw signal-days) | 5d avg=0.39% winrate=56.2% | 10d avg=-0.72% winrate=31.2% | 20d avg=0.39% winrate=56.2%
VOL_TREND5: 14 independent trades (from 34 raw signal-days) | 5d avg=0.44% winrate=50.0% | 10d avg=-0.61% winrate=21.4% | 20d avg=0.1% winrate=42.9%
VOL_LOWFLOOR: 22 independent trades (from 60 raw signal-days) | 5d avg=-0.93% winrate=45.5% | 10d avg=-1.61% winrate=31.8% | 20d avg=-0.62% winrate=45.5%

## ESLT
BASELINE: 14 independent trades (from 55 raw signal-days) | 5d avg=0.16% winrate=42.9% | 10d avg=1.41% winrate=42.9% | 20d avg=4.31% winrate=69.2%
IMPROVED: 8 independent trades (from 24 raw signal-days) | 5d avg=-1.31% winrate=25.0% | 10d avg=-1.33% winrate=37.5% | 20d avg=2.81% winrate=62.5%
VOL_TREND5: 10 independent trades (from 32 raw signal-days) | 5d avg=-2.61% winrate=40.0% | 10d avg=-1.39% winrate=50.0% | 20d avg=2.49% winrate=77.8%
VOL_LOWFLOOR: 10 independent trades (from 35 raw signal-days) | 5d avg=-2.42% winrate=30.0% | 10d avg=-0.85% winrate=30.0% | 20d avg=3.07% winrate=55.6%

## KKR
BASELINE: 18 independent trades (from 83 raw signal-days) | 5d avg=0.24% winrate=55.6% | 10d avg=2.03% winrate=50.0% | 20d avg=3.62% winrate=70.6%
IMPROVED: 16 independent trades (from 39 raw signal-days) | 5d avg=-1.8% winrate=37.5% | 10d avg=-0.63% winrate=31.2% | 20d avg=1.87% winrate=60.0%
VOL_TREND5: 10 independent trades (from 38 raw signal-days) | 5d avg=-1.38% winrate=40.0% | 10d avg=0.3% winrate=40.0% | 20d avg=1.78% winrate=55.6%
VOL_LOWFLOOR: 18 independent trades (from 63 raw signal-days) | 5d avg=-1.09% winrate=44.4% | 10d avg=-0.32% winrate=38.9% | 20d avg=1.72% winrate=58.8%

## REMX
BASELINE: 15 independent trades (from 65 raw signal-days) | 5d avg=-0.53% winrate=46.7% | 10d avg=0.83% winrate=60.0% | 20d avg=0.62% winrate=60.0%
IMPROVED: 14 independent trades (from 49 raw signal-days) | 5d avg=-0.44% winrate=50.0% | 10d avg=1.1% winrate=57.1% | 20d avg=0.8% winrate=57.1%
VOL_TREND5: 12 independent trades (from 49 raw signal-days) | 5d avg=-0.94% winrate=50.0% | 10d avg=-0.3% winrate=50.0% | 20d avg=1.15% winrate=58.3%
VOL_LOWFLOOR: 14 independent trades (from 56 raw signal-days) | 5d avg=-0.28% winrate=50.0% | 10d avg=1.42% winrate=57.1% | 20d avg=1.78% winrate=64.3%

## FCX
BASELINE: 15 independent trades (from 56 raw signal-days) | 5d avg=0.81% winrate=53.3% | 10d avg=2.6% winrate=60.0% | 20d avg=-3.37% winrate=53.3%
IMPROVED: 11 independent trades (from 23 raw signal-days) | 5d avg=-0.05% winrate=45.5% | 10d avg=-0.1% winrate=54.5% | 20d avg=-4.89% winrate=36.4%
VOL_TREND5: 7 independent trades (from 19 raw signal-days) | 5d avg=-1.04% winrate=42.9% | 10d avg=-2.03% winrate=42.9% | 20d avg=-3.87% winrate=42.9%
VOL_LOWFLOOR: 14 independent trades (from 41 raw signal-days) | 5d avg=-0.13% winrate=50.0% | 10d avg=-0.12% winrate=50.0% | 20d avg=-5.77% winrate=35.7%

## MP
BASELINE: 13 independent trades (from 42 raw signal-days) | 5d avg=-3.91% winrate=30.8% | 10d avg=-5.13% winrate=46.2% | 20d avg=2.6% winrate=46.2%
IMPROVED: 13 independent trades (from 32 raw signal-days) | 5d avg=-3.93% winrate=30.8% | 10d avg=-6.36% winrate=38.5% | 20d avg=2.03% winrate=46.2%
VOL_TREND5: 12 independent trades (from 32 raw signal-days) | 5d avg=-2.34% winrate=33.3% | 10d avg=-7.83% winrate=33.3% | 20d avg=1.64% winrate=50.0%
VOL_LOWFLOOR: 13 independent trades (from 37 raw signal-days) | 5d avg=-3.68% winrate=30.8% | 10d avg=-5.59% winrate=46.2% | 20d avg=2.68% winrate=46.2%

## COPX
BASELINE: 24 independent trades (from 105 raw signal-days) | 5d avg=-0.65% winrate=45.8% | 10d avg=0.37% winrate=50.0% | 20d avg=-0.81% winrate=54.2%
IMPROVED: 15 independent trades (from 53 raw signal-days) | 5d avg=0.79% winrate=60.0% | 10d avg=0.97% winrate=60.0% | 20d avg=2.04% winrate=66.7%
VOL_TREND5: 14 independent trades (from 57 raw signal-days) | 5d avg=-0.56% winrate=57.1% | 10d avg=0.99% winrate=64.3% | 20d avg=0.78% winrate=57.1%
VOL_LOWFLOOR: 19 independent trades (from 72 raw signal-days) | 5d avg=-0.66% winrate=47.4% | 10d avg=0.53% winrate=57.9% | 20d avg=0.16% winrate=57.9%

## IGV
BASELINE: 16 independent trades (from 80 raw signal-days) | 5d avg=1.48% winrate=75.0% | 10d avg=2.05% winrate=75.0% | 20d avg=0.93% winrate=50.0%
IMPROVED: 15 independent trades (from 37 raw signal-days) | 5d avg=1.53% winrate=80.0% | 10d avg=1.13% winrate=73.3% | 20d avg=0.8% winrate=53.3%
VOL_TREND5: 13 independent trades (from 44 raw signal-days) | 5d avg=1.46% winrate=69.2% | 10d avg=1.53% winrate=76.9% | 20d avg=0.17% winrate=46.2%
VOL_LOWFLOOR: 16 independent trades (from 53 raw signal-days) | 5d avg=1.3% winrate=75.0% | 10d avg=0.91% winrate=68.8% | 20d avg=0.42% winrate=50.0%

## IFRA
BASELINE: 24 independent trades (from 108 raw signal-days) | 5d avg=0.44% winrate=54.2% | 10d avg=0.37% winrate=54.2% | 20d avg=0.65% winrate=50.0%
IMPROVED: 16 independent trades (from 29 raw signal-days) | 5d avg=0.29% winrate=56.2% | 10d avg=-0.29% winrate=31.2% | 20d avg=-0.45% winrate=37.5%
VOL_TREND5: 17 independent trades (from 48 raw signal-days) | 5d avg=0.54% winrate=58.8% | 10d avg=0.3% winrate=58.8% | 20d avg=-0.18% winrate=47.1%
VOL_LOWFLOOR: 19 independent trades (from 60 raw signal-days) | 5d avg=0.38% winrate=57.9% | 10d avg=0.25% winrate=52.6% | 20d avg=-0.15% winrate=42.1%

## AVGO
BASELINE: 20 independent trades (from 78 raw signal-days) | 5d avg=-0.38% winrate=35.0% | 10d avg=0.9% winrate=65.0% | 20d avg=1.39% winrate=65.0%
IMPROVED: 16 independent trades (from 40 raw signal-days) | 5d avg=0.04% winrate=43.8% | 10d avg=0.02% winrate=62.5% | 20d avg=1.16% winrate=68.8%
VOL_TREND5: 13 independent trades (from 35 raw signal-days) | 5d avg=-1.46% winrate=38.5% | 10d avg=-0.73% winrate=53.8% | 20d avg=-0.66% winrate=69.2%
VOL_LOWFLOOR: 18 independent trades (from 62 raw signal-days) | 5d avg=-0.32% winrate=38.9% | 10d avg=0.32% winrate=66.7% | 20d avg=0.29% winrate=61.1%

## CGNX
BASELINE: 15 independent trades (from 50 raw signal-days) | 5d avg=-1.62% winrate=33.3% | 10d avg=-1.0% winrate=46.7% | 20d avg=-1.72% winrate=53.3%
IMPROVED: 11 independent trades (from 20 raw signal-days) | 5d avg=-0.88% winrate=27.3% | 10d avg=0.56% winrate=54.5% | 20d avg=3.63% winrate=72.7%
VOL_TREND5: 10 independent trades (from 27 raw signal-days) | 5d avg=-2.01% winrate=20.0% | 10d avg=-0.35% winrate=50.0% | 20d avg=2.57% winrate=70.0%
VOL_LOWFLOOR: 13 independent trades (from 40 raw signal-days) | 5d avg=-1.61% winrate=30.8% | 10d avg=-0.73% winrate=53.8% | 20d avg=-2.09% winrate=53.8%

## XLE
BASELINE: 15 independent trades (from 59 raw signal-days) | 5d avg=-1.43% winrate=46.7% | 10d avg=-0.92% winrate=40.0% | 20d avg=-1.55% winrate=40.0%
IMPROVED: 9 independent trades (from 33 raw signal-days) | 5d avg=-0.02% winrate=44.4% | 10d avg=-0.54% winrate=33.3% | 20d avg=2.51% winrate=66.7%
VOL_TREND5: 11 independent trades (from 41 raw signal-days) | 5d avg=-1.0% winrate=36.4% | 10d avg=-0.89% winrate=27.3% | 20d avg=-0.08% winrate=54.5%
VOL_LOWFLOOR: 13 independent trades (from 52 raw signal-days) | 5d avg=-1.5% winrate=46.2% | 10d avg=-0.76% winrate=38.5% | 20d avg=-0.08% winrate=46.2%

## CVX
BASELINE: 12 independent trades (from 59 raw signal-days) | 5d avg=0.18% winrate=58.3% | 10d avg=-0.25% winrate=41.7% | 20d avg=0.1% winrate=50.0%
IMPROVED: 10 independent trades (from 24 raw signal-days) | 5d avg=-0.88% winrate=50.0% | 10d avg=-1.36% winrate=40.0% | 20d avg=-0.93% winrate=50.0%
VOL_TREND5: 7 independent trades (from 25 raw signal-days) | 5d avg=-1.62% winrate=57.1% | 10d avg=-1.43% winrate=28.6% | 20d avg=-0.39% winrate=42.9%
VOL_LOWFLOOR: 11 independent trades (from 45 raw signal-days) | 5d avg=-0.78% winrate=54.5% | 10d avg=-0.74% winrate=45.5% | 20d avg=-1.25% winrate=45.5%

## LEN
BASELINE: 15 independent trades (from 34 raw signal-days) | 5d avg=-1.97% winrate=26.7% | 10d avg=-2.47% winrate=20.0% | 20d avg=-2.82% winrate=42.9%
IMPROVED: 11 independent trades (from 19 raw signal-days) | 5d avg=-2.9% winrate=18.2% | 10d avg=-3.33% winrate=27.3% | 20d avg=-4.82% winrate=30.0%
VOL_TREND5: 8 independent trades (from 13 raw signal-days) | 5d avg=-3.6% winrate=12.5% | 10d avg=-4.99% winrate=12.5% | 20d avg=-5.57% winrate=28.6%
VOL_LOWFLOOR: 14 independent trades (from 26 raw signal-days) | 5d avg=-2.09% winrate=28.6% | 10d avg=-2.63% winrate=21.4% | 20d avg=-3.71% winrate=38.5%

## FLEX
BASELINE: 19 independent trades (from 84 raw signal-days) | 5d avg=0.49% winrate=52.6% | 10d avg=2.27% winrate=63.2% | 20d avg=3.24% winrate=63.2%
IMPROVED: 13 independent trades (from 32 raw signal-days) | 5d avg=1.01% winrate=53.8% | 10d avg=2.46% winrate=53.8% | 20d avg=3.59% winrate=69.2%
VOL_TREND5: 14 independent trades (from 42 raw signal-days) | 5d avg=0.55% winrate=50.0% | 10d avg=1.62% winrate=50.0% | 20d avg=3.73% winrate=78.6%
VOL_LOWFLOOR: 17 independent trades (from 58 raw signal-days) | 5d avg=0.82% winrate=52.9% | 10d avg=2.29% winrate=58.8% | 20d avg=2.44% winrate=64.7%

## Aggregate (all tickers' trades pooled together)
BASELINE: 1096 total triggers | 5d avg=0.16% median=0.08% winrate=50.7% | 10d avg=1.34% median=0.32% winrate=52.1% | 20d avg=3.73% median=1.31% winrate=55.5%
IMPROVED: 837 total triggers | 5d avg=0.33% median=0.07% winrate=50.5% | 10d avg=1.62% median=0.34% winrate=51.6% | 20d avg=4.08% median=1.3% winrate=56.3%
VOL_TREND5: 776 total triggers | 5d avg=0.42% median=0.15% winrate=50.8% | 10d avg=1.66% median=0.25% winrate=50.9% | 20d avg=3.84% median=1.08% winrate=55.2%
VOL_LOWFLOOR: 986 total triggers | 5d avg=0.31% median=0.15% winrate=51.0% | 10d avg=1.31% median=0.25% winrate=51.3% | 20d avg=3.51% median=1.04% winrate=54.9%

How to read this: n_triggers = independent trades (overlapping signal-days on the same move are collapsed into one, see n_raw_signal_days in the JSON for the raw count). Compare BASELINE vs IMPROVED n_triggers and winrate/avg return at each horizon. More trades with similar or better winrate/avg return = the change helped. Fewer trades with much better winrate can also be a legitimate improvement (higher-quality, rarer signals) — that's a judgment call, not something the numbers alone decide.