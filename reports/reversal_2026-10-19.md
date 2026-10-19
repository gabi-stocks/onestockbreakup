# Reversal Checker — 2026-10-19 21:19 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER, EARLY ALERT or >= 5/6 confirmed, 6/72 tickers)

## ATKR  (2026-10-16)  close=94.96  RSI=72.5
  [אמינות היסטורית: אמינות גבוהה יחסית] בבקטסט (5 שנים אחורה): 10 עסקאות בלתי-תלויות, win rate ל-20 יום=60.0%, תשואה ממוצעת ל-20 יום=1.64%.
  [תזמון כניסה: בזמן ✅] המחיר רק 0.6% מעל השפל של 20 הימים האחרונים (94.35). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: 2026-11-19, בעוד 31 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=94.90)
  [PASS] 2. Moving averages
         close>94.86(MA10) & >94.73(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=0.51 vs Signal=0.66 (above=False), hist=-0.15 rising=True
  [PASS] 4. RSI
         RSI=72.50 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.73, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=94.96 vs POC=93.66 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## DKS  (2026-10-16)  close=144.35  RSI=57.5  [today so far: open 144.35 -> 143.82 (-0.37%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 20.1% מעל השפל של 20 הימים האחרונים (120.15), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 132.17 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2026-11-24, בעוד 36 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=137.75)
  [PASS] 2. Moving averages
         close>137.15(MA10) & >135.16(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=-1.27 vs Signal=-3.64 (above=True), hist=2.37 rising=True
  [PASS] 4. RSI
         RSI=57.53 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.97, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=144.35 vs POC=124.69 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## GEHC  (2026-10-16)  close=69.57  RSI=61.0  [today so far: open 69.29 -> 69.76 (+0.68%) | DELAYED]
  [אמינות היסטורית: אמינות בינונית] בבקטסט (5 שנים אחורה): 8 עסקאות בלתי-תלויות, win rate ל-20 יום=62.5%, תשואה ממוצעת ל-20 יום=0.16%.
  [תזמון כניסה: בזמן ✅] המחיר רק 9.9% מעל השפל של 20 הימים האחרונים (63.31). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [⚠️ דוח כספי] דוח כספי בעוד 9 ימים: 2026-10-28. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=66.55)
  [PASS] 2. Moving averages
         close>67.01(MA10) & >66.36(MA20)=True, MA10 rising=True, MA10>MA50=False
  [PASS] 3. MACD
         MACD=0.44 vs Signal=-0.25 (above=True), hist=0.70 rising=True
  [PASS] 4. RSI
         RSI=61.00 rising=False, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=False, RVOL=0.84, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=69.57 vs POC=64.24 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## USO  (2026-10-16)  close=161.76  RSI=66.9  [today so far: open 159.00 -> 160.89 (+1.19%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 14.1% מעל השפל של 20 הימים האחרונים (141.76), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 155.94 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: לא נמצא תאריך (למשל בקרן סל, או שהתאריך עוד לא פורסם). כדאי לבדוק ידנית לפני קנייה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=155.60)
  [PASS] 2. Moving averages
         close>150.53(MA10) & >149.21(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=3.31 vs Signal=2.44 (above=True), hist=0.87 rising=True
  [PASS] 4. RSI
         RSI=66.88 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.23, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=161.76 vs POC=143.70 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## CHKP  (2026-10-16)  close=137.87  RSI=56.9  [today so far: open 138.40 -> 138.94 (+0.39%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: בזמן ✅] המחיר רק 9.7% מעל השפל של 20 הימים האחרונים (125.72). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [⚠️ דוח כספי] דוח כספי בעוד 14 ימים: 2026-11-02. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=141.66)
  [PASS] 2. Moving averages
         close>134.32(MA10) & >133.44(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=0.83 vs Signal=0.18 (above=True), hist=0.66 rising=True
  [PASS] 4. RSI
         RSI=56.90 rising=False, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.70, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=137.87 vs POC=130.54 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## CVX  (2026-10-16)  close=224.99  RSI=70.8  [today so far: open 223.88 -> 224.43 (+0.25%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 12.1% מעל השפל של 20 הימים האחרונים (200.78), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 220.86 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 11 ימים: 2026-10-30. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=208.25)
  [PASS] 2. Moving averages
         close>214.18(MA10) & >209.61(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=3.97 vs Signal=2.35 (above=True), hist=1.62 rising=True
  [PASS] 4. RSI
         RSI=70.77 rising=True, bullishDivergence=True
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.16, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=224.99 vs POC=191.19 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
