# Reversal Checker — 2026-10-16 18:20 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 2/72 tickers)

## GEHC  (2026-10-15)  close=70.35  RSI=65.1  [today so far: open 71.10 -> 69.70 (-1.97%) | DELAYED]
  [אמינות היסטורית: אמינות בינונית] בבקטסט (5 שנים אחורה): 8 עסקאות בלתי-תלויות, win rate ל-20 יום=62.5%, תשואה ממוצעת ל-20 יום=0.16%.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=66.55)
  [PASS] 2. Moving averages
         close>66.48(MA10) & >66.08(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=0.26 vs Signal=-0.43 (above=True), hist=0.69 rising=True
  [PASS] 4. RSI
         RSI=65.06 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.95, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=70.35 vs POC=64.24 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## NOW  (2026-10-15)  close=148.57  RSI=65.4  [today so far: open 151.92 -> 140.74 (-7.36%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=140.80)
  [PASS] 2. Moving averages
         close>139.44(MA10) & >137.59(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=2.47 vs Signal=1.89 (above=True), hist=0.58 rising=True
  [PASS] 4. RSI
         RSI=65.37 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.61, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=148.57 vs POC=103.66 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
