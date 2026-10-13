# Reversal Checker — 2026-10-13 20:21 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 5/72 tickers)

## ODD  (2026-10-12)  close=21.58  RSI=70.7  [today so far: open 21.50 -> 22.12 (+2.88%) | DELAYED]
  [אמינות היסטורית: מדגם קטן מדי (3 עסקאות)] רק 3 טריגרים היסטוריים נמצאו בבקטסט — מעט מדי כדי לשפוט אמינות. התייחס לטריגר בזהירות כפולה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=20.67)
  [PASS] 2. Moving averages
         close>19.46(MA10) & >18.86(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=1.21 vs Signal=1.05 (above=True), hist=0.16 rising=True
  [PASS] 4. RSI
         RSI=70.66 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.79, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=21.58 vs POC=16.52 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## ZIM  (2026-10-12)  close=30.9  RSI=62.4  [today so far: open 30.94 -> 30.43 (-1.65%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=False (last swing high=30.96)
  [PASS] 2. Moving averages
         close>29.67(MA10) & >29.70(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=0.46 vs Signal=0.43 (above=True), hist=0.03 rising=True
  [PASS] 4. RSI
         RSI=62.45 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.12, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=30.90 vs POC=25.19 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## TEVA  (2026-10-12)  close=41.17  RSI=65.6  [today so far: open 41.23 -> 41.24 (+0.02%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=40.28)
  [PASS] 2. Moving averages
         close>39.77(MA10) & >39.53(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=0.78 vs Signal=0.75 (above=True), hist=0.04 rising=True
  [PASS] 4. RSI
         RSI=65.64 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.26, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=41.17 vs POC=35.33 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## MSFT  (2026-10-12)  close=541.15  RSI=69.9  [today so far: open 544.62 -> 543.66 (-0.18%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=509.95)
  [PASS] 2. Moving averages
         close>523.53(MA10) & >511.89(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=11.57 vs Signal=9.62 (above=True), hist=1.95 rising=True
  [PASS] 4. RSI
         RSI=69.86 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.83, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=541.15 vs POC=373.55 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## AMZN  (2026-10-12)  close=259.53  RSI=55.6  [today so far: open 260.39 -> 258.62 (-0.68%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=259.49)
  [PASS] 2. Moving averages
         close>253.92(MA10) & >252.32(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=0.76 vs Signal=-0.70 (above=True), hist=1.45 rising=True
  [PASS] 4. RSI
         RSI=55.58 rising=False, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=False, RVOL=0.72, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=259.53 vs POC=232.96 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
