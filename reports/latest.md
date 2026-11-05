# Reversal Checker — 2026-11-05 22:29 UTC [MORNING (through last completed close)]
(needs >= 4/6 + mandatory structure & volume; showing only BUY_TRIGGER, EARLY ALERT or >= 5/6 confirmed, 8/73 tickers)

## JPM  (2026-11-04)  close=352.11  RSI=63.2  [today so far: open 358.64 -> 337.35 (-5.94%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: בזמן ✅] המחיר רק 8.1% מעל השפל של 20 הימים האחרונים (325.63). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: 2027-01-14, בעוד 70 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 22:06 UTC OpenAI Could Go Public In 2027 As Greg Brockman Signals IPO Readiness (Benzinga Private Markets)
         - 2026-11-05 21:55 UTC Financial Services Roundup: Market Talk (The Wall Street Journal)
         - 2026-11-05 20:09 UTC Bank Earnings Have Entered the Upside-Down (Motley Fool)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=345.75)
  [PASS] 2. Moving averages
         close>338.85(MA10) & >336.66(MA20)=True, MA10 rising=True, MA10>MA50=False
  [----] 3. MACD
         MACD=0.79 vs Signal=-1.04 (above=True), hist=1.84 rising=False
  [PASS] 4. RSI
         RSI=63.25 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.45, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=352.11 vs POC=331.13 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## KRE  (2026-11-04)  close=74.13  RSI=62.0  [today so far: open 74.97 -> 72.32 (-3.53%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: בזמן ✅] המחיר רק 9.4% מעל השפל של 20 הימים האחרונים (67.79). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: לא נמצא תאריך (למשל בקרן סל, או שהתאריך עוד לא פורסם). כדאי לבדוק ידנית לפני קנייה.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-03 10:20 UTC Is State Street SPDR S&P Regional Banking ETF (KRE) a Strong ETF Right Now? (Zacks)
         - 2026-10-23 13:37 UTC Composition vs. Returns: Breaking Down the Structural Drift Between KBE and KRE (Motley Fool)
         - 2026-10-22 09:20 UTC Should You Invest in the State Street SPDR S&P Regional Banking ETF (KRE)? (Zacks)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=71.36)
  [PASS] 2. Moving averages
         close>72.79(MA10) & >71.19(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=0.58 vs Signal=0.17 (above=True), hist=0.41 rising=False
  [PASS] 4. RSI
         RSI=61.97 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.18, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=74.13 vs POC=69.49 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## IBIT  (2026-11-04)  close=45.33  RSI=48.6  [today so far: open 44.96 -> 43.03 (-4.28%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [התראה מוקדמת 🔵] תחילת היפוך, לפני שהטבלה מאשרת. המניה ירדה בתיקון בריא (-12.9% מהשיא של חצי השנה), נרגעה (התנודתיות התכווצה), והיום סגרה לראשונה מעל ממוצע 10 עם מומנטום מקד שמתחיל לעלות. בגלל שזה מוקדם, רוב הפרמטרים בטבלה עדיין ייכשלו, וזה צפוי. עצירה מוצעת: 42.59 (1% מתחת לשפל של 10 הימים, סיכון של 6.4%). בבדיקה על 5 שנים: 62% הצלחה אחרי 20 יום, תשואה חציונית של ‎+3.3%, אבל העצירה נפגעה בכמחצית מהעסקאות, ולכן מתאים לפוזיציה קטנה מהרגיל.
  [תזמון כניסה: בזמן ✅] המחיר רק 5.4% מעל השפל של 20 הימים האחרונים (43.02). ההיפוך התחיל והמניה עוד לא ברחה, ולכן פקודת העצירה קרובה. בבדיקה על 5 שנים, אותות כאלה הצליחו ב-61% מהמקרים אחרי 20 יום.
  [דוח כספי] דוח כספי הבא: לא נמצא תאריך (למשל בקרן סל, או שהתאריך עוד לא פורסם). כדאי לבדוק ידנית לפני קנייה.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 19:43 UTC Bitcoin’s $378 Million Short Squeeze Faded Under $80,000. Is It Already Over? (24/7 Wall St.)
         - 2026-11-05 17:53 UTC Trump Media Just Lost a Quarter of Its Value in a Day (24/7 Wall St.)
         - 2026-11-05 17:23 UTC Trump Media Just Moved 4,259 Bitcoin. Is It About to Sell? (24/7 Wall St.)
  [----] 1. Price structure (HL+HH)
         HigherLow=False, brokeSwingHigh=False (last swing high=46.37)
  [----] 2. Moving averages
         close>45.09(MA10) & >45.88(MA20)=False, MA10 rising=False, MA10>MA50=False
  [----] 3. MACD
         MACD=-0.40 vs Signal=-0.09 (above=False), hist=-0.31 rising=True
  [----] 4. RSI
         RSI=48.59 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.51, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=45.33 vs POC=36.28 (above=True)
  >> 2/6 confirmed | mandatory(structure+volume)=False
  >> EARLY ALERT - reversal starting, not yet confirmed

## GEHC  (2026-11-04)  close=85.81  RSI=85.2  [today so far: open 86.25 -> 83.77 (-2.88%) | DELAYED]
  [אמינות היסטורית: אמינות בינונית] בבקטסט (5 שנים אחורה): 8 עסקאות בלתי-תלויות, win rate ל-20 יום=62.5%, תשואה ממוצעת ל-20 יום=0.16%.
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 35.5% מעל השפל של 20 הימים האחרונים (63.31), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 69.65 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2027-02-03, בעוד 90 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 16:27 UTC GE HealthCare Unveils Allia Celeo to Advance Interventional Imaging (Zacks)
         - 2026-11-05 13:15 UTC Haemonetics Corporation (HAE) Hits Fresh High: Is There Still Room to Run? (Zacks)
         - 2026-11-05 12:55 UTC STE Stock Up on Q2 Earnings & Revenue Beat, '27 EPS View Up (Zacks)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=71.32)
  [PASS] 2. Moving averages
         close>76.08(MA10) & >72.23(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=3.67 vs Signal=2.25 (above=True), hist=1.42 rising=True
  [PASS] 4. RSI
         RSI=85.25 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=2.24, up>downVol=False
  [PASS] 6. Volume Profile POC
         close=85.81 vs POC=64.87 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## CHWY  (2026-11-04)  close=23.4  RSI=66.8  [today so far: open 23.48 -> 23.02 (-1.94%) | DELAYED]
  [אמינות היסטורית: אמינות נמוכה] בבקטסט (5 שנים אחורה): 7 עסקאות בלתי-תלויות, win rate ל-20 יום=28.6%, תשואה ממוצעת ל-20 יום=1.62%.
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 30.2% מעל השפל של 20 הימים האחרונים (17.98), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 19.77 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2026-12-09, בעוד 34 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 16:55 UTC Chewy vs. GameStop: Which Consumer Stock Is a Better Buy for 2027? (Motley Fool)
         - 2026-11-05 09:13 UTC Chewy Stock Gets A Pet Supplements Boost With Spirited Paw Launch (Simply Wall St.)
         - 2026-11-03 18:20 UTC Chewy vs. Five Below: Stable Growth vs. Seasonal Revenue Spikes in Retail (Motley Fool)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=22.38)
  [PASS] 2. Moving averages
         close>21.82(MA10) & >21.09(MA20)=True, MA10 rising=True, MA10>MA50=True
  [PASS] 3. MACD
         MACD=0.57 vs Signal=0.36 (above=True), hist=0.22 rising=True
  [PASS] 4. RSI
         RSI=66.79 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.15, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=23.40 vs POC=21.32 (above=True)
  >> 6/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## REGN  (2026-11-04)  close=930.67  RSI=69.8  [today so far: open 939.91 -> 902.26 (-4.01%) | DELAYED]
  [אמינות היסטורית: אמינות גבוהה יחסית] בבקטסט (5 שנים אחורה): 10 עסקאות בלתי-תלויות, win rate ל-20 יום=70.0%, תשואה ממוצעת ל-20 יום=3.57%.
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 28.6% מעל השפל של 20 הימים האחרונים (723.65), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 796.02 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2027-01-28, בעוד 84 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 10:36 UTC Is Regeneron Stock Riskier Than It Looks? (Trefis)
         - 2026-11-04 22:22 UTC Is Regeneron Stock Increasing Your Market Risk? (Trefis)
         - 2026-11-04 20:59 UTC Was There Any Sign Regeneron Stock Would Run? (Trefis)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=825.52)
  [PASS] 2. Moving averages
         close>867.31(MA10) & >821.79(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=41.34 vs Signal=23.28 (above=True), hist=18.06 rising=False
  [PASS] 4. RSI
         RSI=69.81 rising=False, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=False, RVOL=1.62, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=930.67 vs POC=611.84 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## NKE  (2026-11-04)  close=40.49  RSI=67.8  [today so far: open 40.38 -> 39.56 (-2.02%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 19.7% מעל השפל של 20 הימים האחרונים (33.83), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 37.21 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2026-12-17, בעוד 42 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 21:31 UTC Nike recovery may lag valuation expectations, UBS warns (Proactive)
         - 2026-11-05 18:29 UTC Is Now a Good Time to Buy Nike Stock? (Motley Fool)
         - 2026-11-05 17:10 UTC Nike (NKE) Put Vietnam’s First Fully Electric Container Barge Into Service (Simply Wall St.)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=36.67)
  [PASS] 2. Moving averages
         close>38.34(MA10) & >37.29(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=0.74 vs Signal=0.41 (above=True), hist=0.34 rising=False
  [PASS] 4. RSI
         RSI=67.85 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.33, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=40.49 vs POC=34.00 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed

## LEN  (2026-11-04)  close=92.19  RSI=65.0  [today so far: open 93.53 -> 91.59 (-2.07%) | DELAYED]
  [אמינות היסטורית: אין נתוני בקטסט] לא נמצאה עבור המניה הזו היסטוריית בקטסט (תריץ את workflow ה-Backtest כדי לקבל נתונים).
  [תזמון כניסה: מאוחרת ⚠️] המחיר כבר 28.4% מעל השפל של 20 הימים האחרונים (71.78), כלומר רוב העלייה כבר קרתה ופקודת העצירה תהיה רחוקה. לא לרדוף: לחכות לתיקון אל 78.96 ומטה (עד 10% מעל השפל), או לוותר.
  [דוח כספי] דוח כספי הבא: 2026-12-15, בעוד 40 ימים. מחוץ לחלון העסקה של כ-20 ימי מסחר.
  [חדשות אחרונות, מהחדש לישן]
         - 2026-11-05 13:12 UTC Who Swung The Midterms: Women Or Men? (Trefis)
         - 2026-11-04 21:17 UTC Home Depot Soars 7% as Housing Stocks Rally on Midterm Election Results (TIKR)
         - 2026-11-04 21:16 UTC What Do Lennar (LEN) New Georgia And New Jersey Projects Mean For Growth? (Simply Wall St.)
  [PASS] 1. Price structure (HL+HH)
         HigherLow=True, brokeSwingHigh=True (last swing high=86.15)
  [PASS] 2. Moving averages
         close>86.31(MA10) & >81.37(MA20)=True, MA10 rising=True, MA10>MA50=True
  [----] 3. MACD
         MACD=2.53 vs Signal=1.26 (above=True), hist=1.27 rising=False
  [PASS] 4. RSI
         RSI=64.96 rising=True, bullishDivergence=False
  [PASS] 5. Volume / RVOL
         day up=True, RVOL=1.70, up>downVol=True
  [PASS] 6. Volume Profile POC
         close=92.19 vs POC=82.31 (above=True)
  >> 5/6 confirmed | mandatory(structure+volume)=True
  >> BUY TRIGGER - reversal confirmed
