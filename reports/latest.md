# Reversal Checker — 2026-11-11 23:16 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER, EARLY ALERT or >= 5/6 confirmed, 1/73 tickers)

## DKS  (2026-11-10)  close=150.0  RSI=58.1  [today so far: open 149.03 -> 149.46 (+0.29%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 11.4% מעל השפל של 20 הימים האחרונים (134.62), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 148.08 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 13 ימים: 2026-11-24. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=149.33)
  [PASS] 2. Moving averages
         close>142.86(MA10) & >142.95(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=1.45 vs Signal=0.71 (above=True), hist=0.74 rising=True
  [PASS] 4. RSI
         RSI=58.12 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.63, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=150.00 vs POC=124.69 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
