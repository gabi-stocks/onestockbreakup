# Reversal Checker — 2026-10-07 21:45 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 2/22 tickers)

## MRVL  (2026-10-06)  close=287.01  RSI=69.9  [today so far: open 280.99 -> 284.73 (+1.33%) | DELAYED]
  [אמינות היסטורית: אמינות גבוהה יחסית] בבקטסט (5 שנים אחורה): 14 עסקאות בלתי-תלויות, win rate ל-20 יום=64.3%, תשואה ממוצעת ל-20 יום=8.38%.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=267.48)
  [PASS] 2. Moving averages
         close>265.98(MA10) & >251.64(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=13.12 vs Signal=10.54 (above=True), hist=2.59 rising=False
  [PASS] 4. RSI
         RSI=69.88 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=2.73, up>downVol=True
  [----] 6. Volume Profile POC
         close=287.01 vs POC=310.94 (above=False)
  >> 4/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## CEG  (2026-10-06)  close=300.4  RSI=67.1  [today so far: open 290.42 -> 299.44 (+3.10%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=305.80)
  [PASS] 2. Moving averages
         close>265.22(MA10) & >267.20(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=-0.60 vs Signal=-3.08 (above=True), hist=2.48 rising=True
  [PASS] 4. RSI
         RSI=67.13 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=3.77, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=300.40 vs POC=264.97 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
