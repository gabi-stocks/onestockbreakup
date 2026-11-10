# Reversal Checker — 2026-11-10 03:58 UTC [END-OF-DAY]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER, EARLY ALERT or >= 5/6 confirmed, 1/73 tickers)

## CEG  (2026-11-09)  close=276.09  RSI=55.7
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 19.4% מעל השפל של 20 הימים האחרונים (231.3), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 254.43 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי היום: 2026-11-09. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=268.64)
  [PASS] 2. Moving averages
         close>257.61(MA10) & >262.58(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=-4.24 vs Signal=-4.49 (above=True), hist=0.25 rising=True
  [PASS] 4. RSI
         RSI=55.70 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.86, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=276.09 vs POC=259.27 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
