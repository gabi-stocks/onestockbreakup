# Reversal Checker — 2026-09-04 19:16 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 1/21 tickers)

## CEG  (2026-09-03)  close=285.05  RSI=58.7  [today so far: open 284.04 -> 297.25 (+4.65%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=False (last swing high=285.26)
  [PASS] 2. Moving averages
         close>279.36(MA10) & >277.21(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=4.40 vs Signal=3.73 (above=True), hist=0.67 rising=True
  [PASS] 4. RSI
         RSI=58.73 rising=False, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.29, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=285.05 vs POC=273.60 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
