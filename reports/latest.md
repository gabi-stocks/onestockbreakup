# Reversal Checker — 2026-10-12 23:26 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 2/72 tickers)

## ODD  (2026-10-09)  close=21.11  RSI=69.0  [today so far: open 20.90 -> 21.57 (+3.18%) | DELAYED]
  [אמינות היסטורית: מדגם קטן מדי (3 עסקאות)] רק 3 טריגרים היסטוריים נמצאו בבקטסט — מעט מדי כדי לשפוט אמינות. התייחס לטריגר בזהירות כפולה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=20.67)
  [PASS] 2. Moving averages
         close>19.06(MA10) & >18.73(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=1.09 vs Signal=1.01 (above=True), hist=0.08 rising=True
  [PASS] 4. RSI
         RSI=68.99 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.71, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=21.11 vs POC=16.48 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## TEVA  (2026-10-09)  close=41.1  RSI=65.3  [today so far: open 41.34 -> 41.14 (-0.48%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=40.28)
  [PASS] 2. Moving averages
         close>39.55(MA10) & >39.41(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=0.70 vs Signal=0.74 (above=False), hist=-0.03 rising=False
  [PASS] 4. RSI
         RSI=65.32 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=2.53, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=41.10 vs POC=34.64 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed
