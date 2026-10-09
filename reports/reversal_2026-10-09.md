# Reversal Checker — 2026-10-09 19:44 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 3/72 tickers)

## MRVL  (2026-10-08)  close=274.66  RSI=61.2  [today so far: open 279.26 -> 273.45 (-2.08%) | DELAYED]
  [אמינות היסטורית: אמינות גבוהה יחסית] בבקטסט (5 שנים אחורה): 14 עסקאות בלתי-תלויות, win rate ל-20 יום=64.3%, תשואה ממוצעת ל-20 יום=8.38%.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=267.48)
  [PASS] 2. Moving averages
         close>269.93(MA10) & >256.51(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=13.39 vs Signal=11.63 (above=True), hist=1.76 rising=False
  [PASS] 4. RSI
         RSI=61.23 rising=False, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.49, up>downVol=True
  [----] 6. Volume Profile POC
         close=274.66 vs POC=311.37 (above=False)
  >> 4/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## IGV  (2026-10-08)  close=109.59  RSI=59.4  [today so far: open 110.79 -> 112.40 (+1.45%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=108.44)
  [PASS] 2. Moving averages
         close>108.01(MA10) & >106.90(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=1.67 vs Signal=1.44 (above=True), hist=0.23 rising=False
  [PASS] 4. RSI
         RSI=59.44 rising=False, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.17, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=109.59 vs POC=92.67 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## XLE  (2026-10-08)  close=65.24  RSI=62.7  [today so far: open 64.96 -> 65.06 (+0.15%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=66.17)
  [PASS] 2. Moving averages
         close>62.85(MA10) & >63.31(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=0.24 vs Signal=0.11 (above=True), hist=0.12 rising=True
  [PASS] 4. RSI
         RSI=62.65 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.44, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=65.24 vs POC=56.88 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
