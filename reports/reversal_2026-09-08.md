# Reversal Checker — 2026-09-08 19:42 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 2/21 tickers)

## ORCL  (2026-09-04)  close=158.78  RSI=60.9  [today so far: open 167.60 -> 162.03 (-3.32%) | DELAYED]
  [אמינות היסטורית: אמינות בינונית] בבקטסט (5 שנים אחורה): 11 עסקאות בלתי-תלויות, win rate ל-20 יום=54.5%, תשואה ממוצעת ל-20 יום=5.13%.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=153.99)
  [PASS] 2. Moving averages
         close>148.79(MA10) & >148.31(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=2.51 vs Signal=1.59 (above=True), hist=0.92 rising=True
  [PASS] 4. RSI
         RSI=60.94 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=False, RVOL=1.16, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=158.78 vs POC=142.95 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## CEG  (2026-09-04)  close=298.96  RSI=66.7  [today so far: open 303.40 -> 299.30 (-1.35%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [חדשות אחרונות, מהחדש לישן]
         - 2026-09-08 15:25 UTC Google’s revived nuclear power plant gets $1.9B loan from US government (TechCrunch)
         - 2026-09-07 15:01 UTC These 2 AI Power Stocks Jumped While the S&P 500 Fell (Insider Monkey)
         - 2026-09-07 14:22 UTC XLU’s AI Power Story Crumbles as Texas Freezes Data-Center Demand (24/7 Wall St.)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=285.26)
  [PASS] 2. Moving averages
         close>281.97(MA10) & >278.66(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=5.62 vs Signal=4.11 (above=True), hist=1.51 rising=True
  [PASS] 4. RSI
         RSI=66.71 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.18, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=298.96 vs POC=273.60 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed
