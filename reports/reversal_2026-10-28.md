# Reversal Checker — 2026-10-28 19:52 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER, EARLY ALERT or >= 5/6 confirmed, 9/71 tickers)

## IFRA  (2026-10-27)  close=57.65  RSI=56.3  [today so far: open 57.84 -> 57.61 (-0.40%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: בזמן ✅] המחיר רק 5.7% מעל השפל של 20 הימים האחרונים (54.55). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: לא נמצא תאריך (למשל בקרן סל, או שהתאריך עוד לא פורסם). כדאי לבדוק ידנית לפני קנייה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=57.26)
  [PASS] 2. Moving averages
         close>56.84(MA10) & >56.69(MA20)=True, MA10 rising=True, MA10>MA50=False
  [----] 3. MACD
         MACD=-0.07 vs Signal=-0.23 (above=True), hist=0.16 rising=False
  [PASS] 4. RSI
         RSI=56.26 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=2.22, up>downVol=True
  [----] 6. Volume Profile POC
         close=57.65 vs POC=62.17 (above=False)
  >> 4/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## MRVL  (2026-10-27)  close=243.57  RSI=48.7  [today so far: open 247.45 -> 251.07 (+1.46%) | DELAYED]
  [אמינות היסטורית: אמינות גבוהה יחסית] בבקטסט (5 שנים אחורה): 14 עסקאות בלתי-תלויות, win rate ל-20 יום=64.3%, תשואה ממוצעת ל-20 יום=8.38%.
  [התראה מוקדמת 🔵] תחילת היפוך, לפני שהטבלה מאשרת. המניה ירדה בתיקון בריא (-33.2% מהשיא של חצי השנה), נרגעה (התנודתיות התכווצה), והיום סגרה לראשונה מעל ממוצע 10 עם מומנטום מקד שמתחיל לעלות. בגלל שזה מוקדם, רוב הפרמטרים בטבלה עדיין ייכשלו, וזה צפוי. עצירה מוצעת: 218.01 (1% מתחת לשפל של 10 הימים, סיכון של 11.7%). בבדיקה על 5 שנים: 62% הצלחה אחרי 20 יום, תשואה חציונית של ‎+3.3%, אבל העצירה נפגעה בכמחצית מהעסקאות, ולכן מתאים לפוזיציה קטנה מהרגיל.
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 10.6% מעל השפל של 20 הימים האחרונים (220.21), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 242.23 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2026-12-01, בעוד 34 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=250.12)
  [----] 2. Moving averages
         close>236.59(MA10) & >254.90(MA20)=False, MA10 rising=False, MA10>MA50=False
  [----] 3. MACD
         MACD=-4.07 vs Signal=-0.62 (above=False), hist=-3.45 rising=True
  [PASS] 4. RSI
         RSI=48.71 rising=True, bullishDivergence=True
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.76, up>downVol=False
  [----] 6. Volume Profile POC
         close=243.57 vs POC=311.74 (above=False)
  >> 1/6 confirmed | mandatory(structure+volume)=False
  >> EARLY ALERT - reversal starting, not yet confirmed

## NVDA  (2026-10-27)  close=217.94  RSI=46.3  [today so far: open 219.37 -> 215.11 (-1.94%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [התראה מוקדמת 🔵] תחילת היפוך, לפני שהטבלה מאשרת. המניה ירדה בתיקון בריא (-13.6% מהשיא של חצי השנה), נרגעה (התנודתיות התכווצה), והיום סגרה לראשונה מעל ממוצע 10 עם מומנטום מקד שמתחיל לעלות. בגלל שזה מוקדם, רוב הפרמטרים בטבלה עדיין ייכשלו, וזה צפוי. עצירה מוצעת: 208.08 (1% מתחת לשפל של 10 הימים, סיכון של 4.7%). בבדיקה על 5 שנים: 62% הצלחה אחרי 20 יום, תשואה חציונית של ‎+3.3%, אבל העצירה נפגעה בכמחצית מהעסקאות, ולכן מתאים לפוזיציה קטנה מהרגיל.
  [תזמון כניסה: בזמן ✅] המחיר רק 3.7% מעל השפל של 20 הימים האחרונים (210.18). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [⚠️ דוח כספי] דוח כספי בעוד 20 ימים: 2026-11-17. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=False (last swing high=222.19)
  [----] 2. Moving averages
         close>216.53(MA10) & >224.44(MA20)=False, MA10 rising=False, MA10>MA50=False
  [----] 3. MACD
         MACD=-2.60 vs Signal=-1.27 (above=False), hist=-1.32 rising=True
  [----] 4. RSI
         RSI=46.29 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=False, RVOL=0.83, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=217.94 vs POC=211.18 (above=True)
  >> 1/6 confirmed | mandatory(structure+volume)=False
  >> EARLY ALERT - reversal starting, not yet confirmed

## GEV  (2026-10-27)  close=895.08  RSI=45.1  [today so far: open 876.38 -> 876.36 (-0.00%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [התראה מוקדמת 🔵] תחילת היפוך, לפני שהטבלה מאשרת. המניה ירדה בתיקון בריא (-33.4% מהשיא של חצי השנה), נרגעה (התנודתיות התכווצה), והיום סגרה לראשונה מעל ממוצע 10 עם מומנטום מקד שמתחיל לעלות. בגלל שזה מוקדם, רוב הפרמטרים בטבלה עדיין ייכשלו, וזה צפוי. עצירה מוצעת: 788.45 (1% מתחת לשפל של 10 הימים, סיכון של 13.5%). בבדיקה על 5 שנים: 62% הצלחה אחרי 20 יום, תשואה חציונית של ‎+3.3%, אבל העצירה נפגעה בכמחצית מהעסקאות, ולכן מתאים לפוזיציה קטנה מהרגיל.
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 12.4% מעל השפל של 20 הימים האחרונים (796.41), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 876.06 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי היום: 2026-10-28. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=1052.78)
  [----] 2. Moving averages
         close>890.67(MA10) & >942.73(MA20)=False, MA10 rising=False, MA10>MA50=False
  [----] 3. MACD
         MACD=-27.12 vs Signal=-15.88 (above=False), hist=-11.24 rising=True
  [----] 4. RSI
         RSI=45.08 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=1.28, up>downVol=False
  [----] 6. Volume Profile POC
         close=895.08 vs POC=940.95 (above=False)
  >> 0/6 confirmed | mandatory(structure+volume)=False
  >> EARLY ALERT - reversal starting, not yet confirmed

## QTUM  (2026-10-27)  close=142.07  RSI=45.5  [today so far: open 142.98 -> 143.59 (+0.42%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [התראה מוקדמת 🔵] תחילת היפוך, לפני שהטבלה מאשרת. המניה ירדה בתיקון בריא (-21.1% מהשיא של חצי השנה), נרגעה (התנודתיות התכווצה), והיום סגרה לראשונה מעל ממוצע 10 עם מומנטום מקד שמתחיל לעלות. בגלל שזה מוקדם, רוב הפרמטרים בטבלה עדיין ייכשלו, וזה צפוי. עצירה מוצעת: 132.79 (1% מתחת לשפל של 10 הימים, סיכון של 7.0%). בבדיקה על 5 שנים: 62% הצלחה אחרי 20 יום, תשואה חציונית של ‎+3.3%, אבל העצירה נפגעה בכמחצית מהעסקאות, ולכן מתאים לפוזיציה קטנה מהרגיל.
  [תזמון כניסה: בזמן ✅] המחיר רק 5.9% מעל השפל של 20 הימים האחרונים (134.13). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: לא נמצא תאריך (למשל בקרן סל, או שהתאריך עוד לא פורסם). כדאי לבדוק ידנית לפני קנייה.
  [----] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=False (last swing high=142.15)
  [----] 2. Moving averages
         close>139.26(MA10) & >146.04(MA20)=False, MA10 rising=False, MA10>MA50=False
  [----] 3. MACD
         MACD=-3.21 vs Signal=-2.51 (above=False), hist=-0.70 rising=True
  [----] 4. RSI
         RSI=45.50 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=0.82, up>downVol=False
  [----] 6. Volume Profile POC
         close=142.07 vs POC=147.94 (above=False)
  >> 0/6 confirmed | mandatory(structure+volume)=False
  >> EARLY ALERT - reversal starting, not yet confirmed

## CHKP  (2026-10-27)  close=159.84  RSI=77.8  [today so far: open 158.96 -> 155.41 (-2.23%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 26.8% מעל השפל של 20 הימים האחרונים (126.01), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 138.61 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 5 ימים: 2026-11-02. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=141.66)
  [PASS] 2. Moving averages
         close>146.37(MA10) & >139.31(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=6.11 vs Signal=3.28 (above=True), hist=2.83 rising=True
  [PASS] 4. RSI
         RSI=77.83 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.14, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=159.84 vs POC=136.94 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## HTFL  (2026-10-27)  close=57.82  RSI=68.7  [today so far: open 58.06 -> 59.29 (+2.12%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 24.3% מעל השפל של 20 הימים האחרונים (46.5), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 51.15 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 15 ימים: 2026-11-12. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=54.32)
  [PASS] 2. Moving averages
         close>53.80(MA10) & >51.83(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=2.39 vs Signal=1.79 (above=True), hist=0.60 rising=True
  [PASS] 4. RSI
         RSI=68.71 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=1.09, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=57.82 vs POC=50.07 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## CRL  (2026-10-27)  close=358.84  RSI=76.8  [today so far: open 360.01 -> 373.14 (+3.65%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 26.1% מעל השפל של 20 הימים האחרונים (284.61), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 313.07 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 7 ימים: 2026-11-04. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=310.53)
  [PASS] 2. Moving averages
         close>326.99(MA10) & >312.93(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=16.54 vs Signal=11.12 (above=True), hist=5.42 rising=True
  [PASS] 4. RSI
         RSI=76.79 rising=True, bullishDivergence=False
  [----] 5. Volume / RVOL
         day up=True, RVOL=1.03, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=358.84 vs POC=294.08 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation

## ESLT  (2026-10-27)  close=790.0  RSI=67.5  [today so far: open 774.96 -> 777.07 (+0.27%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 21.4% מעל השפל של 20 הימים האחרונים (650.68), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 715.75 ומטה (עד 10% מעל השפל), או לוותר.
  [⚠️ דוח כספי] דוח כספי בעוד 20 ימים: 2026-11-17. זה בתוך חלון העסקה של כ-20 ימי מסחר. דוח יכול להזיז את המניה יותר מכל אות טכני, לשני הכיוונים, והבדיקה ההיסטורית לא הפרידה מקרים כאלה. שקול לחכות לאחרי הדוח, או להקטין את המנה.
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=True (last swing high=766.46)
  [PASS] 2. Moving averages
         close>749.15(MA10) & >713.87(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=13.06 vs Signal=2.84 (above=True), hist=10.22 rising=True
  [PASS] 4. RSI
         RSI=67.45 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.60, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=790.00 vs POC=780.93 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=False
  >> NO ENTRY - wait for confirmation
