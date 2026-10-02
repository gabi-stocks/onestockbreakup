# Reversal Checker — 2026-10-02 21:08 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER or >= 5/6 confirmed, 1/22 tickers)

## ROK  (2026-10-01)  close=442.45  RSI=59.9  [today so far: open 447.74 -> 454.46 (+1.50%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=436.00)
  [PASS] 2. Moving averages
         close>430.82(MA10) & >426.80(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=0.23 vs Signal=-2.70 (above=True), hist=2.92 rising=True
  [PASS] 4. RSI
         RSI=59.90 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.25, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=442.45 vs POC=435.50 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
