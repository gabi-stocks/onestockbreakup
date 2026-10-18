# Parameter study (2026-10-18 11:51 UTC)

Trades: 2012. Skipped: CBRS (108 rows), SPCX (88 rows).

Full per-trade data in reports/params_trades.json.


## CURRENT (806 trades with 20d outcome)

| parameter | n true | 20d win% true | 20d win% false | 20d med true | 20d med false |
|---|---|---|---|---|---|
| rs20>0 | 694 | 55.0 | 60.7 | 1.05 | 1.24 |
| rs_high | 463 | 56.4 | 55.1 | 1.30 | 0.57 |
| obv_high | 527 | 56.9 | 53.8 | 1.36 | 0.47 |
| squeeze | 435 | 56.3 | 55.3 | 0.85 | 1.30 |
| clv>=0.7 | 544 | 54.0 | 59.5 | 0.50 | 2.03 |
| above200 | 650 | 56.3 | 53.8 | 1.18 | 0.50 |
| pullback -35..-10% | 503 | 55.3 | 56.8 | 1.05 | 1.04 |
| ext_atr<=2 | 277 | 55.6 | 56.0 | 0.96 | 1.16 |
| dryup<0.8 | 637 | 56.7 | 52.7 | 1.16 | 1.04 |
| from_low<=10 | 213 | 61.0 | 54.0 | 1.16 | 1.05 |

## EARLY_D (1175 trades with 20d outcome)

| parameter | n true | 20d win% true | 20d win% false | 20d med true | 20d med false |
|---|---|---|---|---|---|
| rs20>0 | 183 | 51.4 | 54.1 | 0.85 | 0.82 |
| rs_high | 36 | 63.9 | 53.4 | 6.06 | 0.67 |
| obv_high | 65 | 47.7 | 54.1 | -0.21 | 0.99 |
| squeeze | 478 | 59.2 | 49.9 | 2.42 | 0.00 |
| clv>=0.7 | 750 | 54.8 | 51.8 | 1.24 | 0.29 |
| above200 | 588 | 54.8 | 52.6 | 0.91 | 0.77 |
| pullback -35..-10% | 730 | 56.7 | 48.8 | 1.37 | -0.25 |
| ext_atr<=2 | 1171 | 53.6 | 75.0 | 0.81 | 13.92 |
| dryup<0.8 | 873 | 53.7 | 53.6 | 1.05 | 0.36 |
| from_low<=10 | 783 | 55.0 | 51.0 | 1.01 | 0.30 |