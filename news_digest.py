#!/usr/bin/env python3
"""
Daily material-news digest for every symbol in tickers.txt, emailed in Hebrew.

Runs on GitHub Actions (news_digest.yml), sends through the same Gmail SMTP
secrets as reversal_checker.py. Free sources only, no API keys:
  - Yahoo Finance headlines via yfinance (publisher + exact publish time)
  - Google News RSS (English, per company; Hebrew Israeli business press for
    Israeli companies; sector / macro queries)
  - SEC EDGAR filings feed (8-K with item codes, offerings, 13D)
  - Yahoo earnings calendar (reused from reversal_checker.py)
  - reports/latest.md from the reversal scanner (trigger / early-alert flags)

Every item shows its exact publish date, its sources, whether a second
independent source corroborates it, and a flag when it contains a
forward-looking element whose status may still change. No AI: materiality is
keyword based and the possible-impact label is a keyword heuristic.
Analysis tooling, not investment advice.
"""

import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo

import yfinance as yf

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from reversal_checker import fetch_next_earnings, load_tickers

IL = ZoneInfo("Asia/Jerusalem")
NY = ZoneInfo("America/New_York")
UA_BROWSER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
# SEC asks automated clients to identify themselves with a contact address.
SEC_UA = os.environ.get("SEC_USER_AGENT") or f"onestockbreakup news digest {os.environ.get('GMAIL_USER', '')}".strip()
TRANSLATE = os.environ.get("TRANSLATE", "true").lower() == "true"
MAX_ITEMS_PER_TICKER = int(os.environ.get("MAX_ITEMS_PER_TICKER", "4"))
EARNINGS_AHEAD_DAYS = 7
SCANNER_REPORT = os.path.join("reports", "latest.md")

# Israeli / Israel-linked companies -> Hebrew name for the Israeli press search.
ISRAELI = {"TEVA": "טבע", "CHKP": "צ'ק פוינט", "ESLT": "אלביט מערכות",
           "TSEM": "טאואר", "INVZ": "אינוויז", "ZIM": "צים", "NNDM": "ננו דיימנשן",
           "CYBR": "סייברארק", "WIX": "וויקס", "NICE": "נייס", "MBLY": "מובילאיי"}
IL_SITES = "(site:globes.co.il OR site:calcalist.co.il OR site:themarker.com OR site:bizportal.co.il)"

# ---------------- Materiality rules ----------------
# (key, Hebrew label, priority, English regex, Hebrew regex)
CATEGORIES = [
    ("earnings", "דוח כספי ותחזית", 10,
     r"\b(earnings|quarterly results|(first|second|third|fourth)[- ]quarter|q[1-4] (results|revenue|earnings|sales)|"
     r"revenue|eps|guidance|outlook|forecast|preliminary results|beats?|miss(es|ed)?|profit warning)\b",
     r"(דוח|רבעון|תחזית|הכנסות|רווח)"),
    ("mna", "מיזוג ורכישה", 9,
     r"\b(acquir\w*|acquisition|merger|merge|takeover|buyout|to buy|divest\w*|spin-?off|tender offer|bid for)\b",
     r"(רכישה|רוכשת|מיזוג|השתלטות|מכירת פעילות)"),
    ("regulation", "רגולציה", 9,
     r"\b(fda|approv\w*|clearance|ema|chmp|phase (3|iii|2|ii)|topline|trial (results|data)|antitrust|ftc|doj|"
     r"export (controls?|ban|curbs?|restrictions?)|sanction\w*|tariff\w*|regulator\w*|probe|investigation)\b",
     r"(אישור|רגולטור|רשות|חקירה|מכס|סנקציות|מגבלות יצוא)"),
    ("contracts", "חוזה ושותפות", 8,
     r"\b(contract|award(ed|s)?|partner(ship)?|agreement|collaborat\w*|selected by|order(s)? (for|from|worth)|"
     r"supply deal|deal with|wins?|signs?)\b",
     r"(חוזה|הסכם|עסקה|הזמנה|זכתה|שיתוף פעולה)"),
    ("capital", "הון ודילול", 8,
     r"\b(offering|priced|convertible|senior notes|private placement|dilut\w*|buyback|repurchase|dividend|"
     r"stock split|lock-?up|credit rating|moody'?s|s&p 500|index inclusion|added to the|join(s|ing)? the s&p|atm program)\b",
     r"(הנפקה|דילול|רכישה עצמית|דיבידנד|דירוג אשראי|מדד)"),
    ("management", "הנהלה", 7,
     r"\b(ceo|cfo|chairman|chief executive|chief financial|steps? down|resign\w*|appoint\w*|names? new|retire\w*|successor)\b",
     r"(מנכ\"ל|מנכ''ל|סמנכ\"ל|יו\"ר|מינוי|מתפטר|פורש)"),
    ("legal", "משפט וחקירות", 7,
     r"\b(lawsuit|sues?|sued|settle\w*|class action|short (report|seller)|fraud|subpoena|indict\w*|verdict|court)\b",
     r"(תביעה|ייצוגית|הסדר|כתב אישום|בית משפט|שורט)"),
    ("analyst", "המלצת אנליסטים", 5,
     r"\b(upgrade\w*|downgrade\w*|price target|initiat\w* (coverage|at)|outperform|overweight|underweight|"
     r"underperform|raises? (pt|target)|cuts? (pt|target))\b",
     r"(המלצה|מחיר יעד|שדרוג|הורדת דירוג)"),
]
NOISE = re.compile(
    r"\b(stocks? to (buy|watch|sell|own)|best \w+ stocks?|top \d+|\d+ (stocks|reasons)|should you (buy|sell)|"
     r"buy (now|today|before)|is it (too late|time)|millionaire|better buy|vs\.? |forever|retire rich|"
     r"magnificent seven stocks|motley|zacks rank|options? (activity|volume)|unusual options|"
     r"(stock|shares) (is|are) (up|down|soaring|sinking|jumping|falling|sliding|rising|climbing|tumbling)( today)?$)",
    re.I)
FORWARD = re.compile(
    r"\b(will|to (acquire|buy|report|present|vote|host|announce|launch|close)|plans?|expect(s|ed)?|scheduled|set to|"
    r"pending|proposed|upcoming|agrees? to|could|may|nears?|in talks|consider\w*|weighs?|eyes|seeks?|aims?|"
    r"guidance|outlook|forecast|to (step down|retire|leave|resign|depart|take effect)|effective (on|as of)|at year-end|"
    r"next (week|month|quarter|year)|by (year-end|the end of))\b|(צפוי|צפויה|תדווח|מתכננת|בוחנת|עשויה|במגעים)", re.I)
POSITIVE = re.compile(
    r"\b(beats?|tops?|raises?|raised|record|approv\w*|upgrade\w*|wins?|won|awarded|surges?|soars?|jumps?|"
    r"buyback|repurchase|dividend increase|strong|exceeds?|outperform|overweight|clearance|partnership)\b"
    r"|(עקפה|שיא|אישור|שדרוג|זכתה|זינוק)", re.I)
NEGATIVE = re.compile(
    r"\b(miss(es|ed)?|cuts?|lowers?|downgrade\w*|lawsuit|sued|probe|investigation|offering|dilut\w*|resign\w*|"
    r"steps? down|plunges?|sinks?|tumbles?|falls?|warns?|recall|halt\w*|delay\w*|reject\w*|crl|fraud|"
    r"underperform|underweight|layoffs?|short (report|seller)|ban)\b"
    r"|(החמיצה|הורדת|תביעה|חקירה|הנפקה|דילול|צניחה|קריסה|אזהרה|פיטורים)", re.I)
STOP = set("a an the of to in on for and or with at by from is are be as its it this that after over amid into new "
           "inc corp co ltd plc shares stock stocks company says said report reports".split())

# SEC forms worth reporting, and 8-K items -> Hebrew.
SEC_FORMS = re.compile(r"^(8-K|8-K/A|6-K|S-1|S-1/A|S-3|S-3ASR|F-1|F-3|424B\d|SC 13D|SC 13D/A|SCHEDULE 13D)")
SEC_FORM_HE = {"S-1": "תשקיף הנפקה", "S-3": "תשקיף מדף להנפקה", "S-3ASR": "תשקיף מדף להנפקה",
               "F-1": "תשקיף הנפקה", "F-3": "תשקיף מדף להנפקה", "424B": "תשקיף סופי להנפקה (תמחור)",
               "SC 13D": "דיווח על החזקה מהותית של משקיע פעיל", "SCHEDULE 13D": "דיווח על החזקה מהותית של משקיע פעיל",
               "6-K": "דיווח שוטף של חברה זרה"}
ITEMS_8K = {"1.01": ("הסכם מהותי חדש", "contracts"), "1.02": ("סיום הסכם מהותי", "contracts"),
            "1.05": ("אירוע סייבר מהותי", "legal"), "2.01": ("השלמת רכישה או מכירה של נכסים", "mna"),
            "2.02": ("תוצאות כספיות", "earnings"), "2.03": ("התחייבות כספית מהותית", "capital"),
            "2.05": ("פעולות התייעלות ופיטורים", "management"), "2.06": ("ירידת ערך מהותית", "earnings"),
            "3.01": ("הודעה על אי-עמידה בכללי הבורסה", "legal"), "3.02": ("מכירת מניות שלא במסגרת הנפקה רשומה", "capital"),
            "4.02": ("אי-הסתמכות על דוחות קודמים", "legal"), "5.01": ("שינוי שליטה", "mna"),
            "5.02": ("חילופי נושאי משרה", "management"), "5.07": ("תוצאות הצבעה באסיפת בעלי המניות", "management"),
            "7.01": ("גילוי לציבור (מצגת או הודעה)", None), "8.01": ("אירוע אחר", None)}
# Items that alone are not worth a line (exhibits / generic) unless combined.
ITEMS_8K_MINOR = {"9.01", "7.01", "8.01", "5.07"}

# Sector / macro scans: (Hebrew label, Google News query, required regex, symbols it may affect)
SECTORS = [
    ("ריבית, אינפלציה ואג\"ח", "Federal Reserve OR CPI OR inflation OR \"Treasury yields\"",
     r"\b(fed|federal reserve|powell|rate (cut|hike)|cpi|inflation|treasury yields?|jobs report|payrolls)\b",
     ["TLT", "IEF", "VCLT", "KRE", "JPM", "KKR", "HOOD"]),
    ("נפט ואנרגיה", "oil prices OPEC", r"\b(oil|opec|crude|brent|wti)\b", ["USO", "XLE", "CVX", "ZIM"]),
    ("נחושת ומתכות נדירות", "copper prices OR \"rare earths\"", r"\b(copper|rare earths?|lithium|critical minerals)\b",
     ["FCX", "COPX", "COPJ", "REMX", "MP"]),
    ("שבבים ומגבלות יצוא", "semiconductor export controls OR chip stocks Nvidia",
     r"\b(chips?|semiconductors?|export controls?|nvidia|tsmc|ai chips?)\b",
     ["NVDA", "ARM", "AVGO", "MRVL", "QCOM", "TSEM", "CRDO", "TER", "QBTS", "QTUM"]),
    ("חשמל, גרעין ואורניום", "nuclear power OR uranium OR \"data center power\"",
     r"\b(nuclear|uranium|reactor|smr|power demand|data cent(er|re)s? power|grid)\b",
     ["CEG", "VST", "OKLO", "NNE", "LEU", "GEV", "ETN", "IFRA", "AMSC"]),
    ("קריפטו", "bitcoin price OR crypto regulation", r"\b(bitcoin|crypto\w*|stablecoin|sec)\b",
     ["IBIT", "COIN", "HOOD", "IREN"]),
    ("חלל", "space stocks OR satellite launch OR NASA contract", r"\b(space|satellite|launch|nasa|rocket)\b",
     ["RKLB", "ASTS", "LUNR", "SPCX"]),
    ("ביטחון", "defense spending OR Pentagon budget", r"\b(defen[cs]e|pentagon|nato|military)\b",
     ["XAR", "ESLT"]),
    ("תוכנה וסייבר", "cybersecurity stocks OR software stocks AI", r"\b(cyber\w*|software|saas|breach)\b",
     ["PANW", "CHKP", "NOW", "IGV", "MSFT", "ORCL", "IBM"]),
    ("ביוטק ופארמה", "FDA drug pricing OR biotech stocks", r"\b(fda|drug pricing|biotech|pharma\w*|medicare)\b",
     ["REGN", "BNTX", "CRL", "TEVA", "TEM", "GEHC"]),
]

FAILURES = {}  # source name -> count of failed fetches


def send_email(subject, text_body, html_body):
    """Like reversal_checker.send_email, but raises on failure so the GitHub run
    turns red and GitHub notifies you, instead of failing silently."""
    user, pw = os.environ.get("GMAIL_USER"), os.environ.get("GMAIL_APP_PASSWORD")
    to = os.environ.get("MAIL_TO") or user
    if not (user and pw):
        raise SystemExit("GMAIL_USER / GMAIL_APP_PASSWORD secrets are missing -- email not sent.")
    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    msg["Subject"], msg["From"], msg["To"] = subject, user, to
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as s:
        s.login(user, pw)
        s.sendmail(user, [a.strip() for a in to.split(",")], msg.as_string())
    print(f"Email sent to {to}")


def note_fail(src, err):
    FAILURES[src] = FAILURES.get(src, 0) + 1
    print(f"WARNING {src}: {err}")


# ---------------- Helpers ----------------
def http_get(url, ua=UA_BROWSER, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Language": "en-US,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fmt_il(dt):
    d = dt.astimezone(IL)
    return f"{d.day}.{d.month}.{d.year} {d:%H:%M}"


def fmt_day(d):
    return f"{d.day}.{d.month}.{d.year}"


def window_start(now_il):
    """24h back to ~09:00 yesterday; on Sunday and Monday, since Friday's US close."""
    if now_il.weekday() in (6, 0):  # Sunday, Monday
        days_back = 2 if now_il.weekday() == 6 else 3
        fri = (now_il - timedelta(days=days_back)).astimezone(NY)
        return fri.replace(hour=16, minute=0, second=0, microsecond=0).astimezone(timezone.utc)
    y = (now_il - timedelta(days=1)).replace(hour=9, minute=0, second=0, microsecond=0)
    return y.astimezone(timezone.utc)


def clean_company_name(name):
    if not name:
        return ""
    n = re.sub(r"[,.]", " ", name)
    n = re.sub(r"\b(inc|corp|corporation|co|company|ltd|limited|plc|holdings?|group|n ?v|s ?a|ag|se|class [a-c]|"
               r"common stock|ordinary shares|the)\b", " ", n, flags=re.I)
    return re.sub(r"\s+", " ", n).strip()


def tokens(title):
    words = re.findall(r"[a-z0-9֐-׿$%.]+", title.lower())
    return {w.strip(".") for w in words if w.strip(".") and w not in STOP and len(w) > 2}


def publisher_key(p):
    p = (p or "").lower()
    p = re.sub(r"^(www\.)|\.(com|co\.il|net|org)$", "", p)
    return re.sub(r"[^a-z0-9֐-׿]", "", p)


# ---------------- Sources ----------------
def yahoo_news(ticker, since):
    out = []
    try:
        raw = yf.Ticker(ticker).news or []
    except Exception as e:
        note_fail("יאהו פייננס", e)
        return out
    for entry in raw:
        node = entry.get("content", entry) if isinstance(entry, dict) else {}
        title = node.get("title") or entry.get("title")
        if not title:
            continue
        pub = ((node.get("provider") or {}).get("displayName") or node.get("publisher") or entry.get("publisher") or "")
        link = ((node.get("canonicalUrl") or {}).get("url") or (node.get("clickThroughUrl") or {}).get("url")
                or entry.get("link") or "")
        ts = entry.get("providerPublishTime")
        dt = None
        if isinstance(ts, (int, float)):
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        else:
            s = node.get("pubDate") or node.get("displayTime")
            if isinstance(s, str):
                try:
                    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
                except ValueError:
                    dt = None
        if dt is None or dt < since:
            continue  # no verifiable date -> not reported
        summary = node.get("summary") or node.get("description") or ""
        out.append({"title": title.strip(), "summary": re.sub("<[^>]+>", " ", summary or "")[:400],
                    "publisher": pub.strip() or "Yahoo Finance", "link": link, "dt": dt, "via": "יאהו פייננס"})
    return out


def google_news(query, since, lang="en"):
    if lang == "he":
        params = {"q": query, "hl": "iw", "gl": "IL", "ceid": "IL:iw"}
    else:
        params = {"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"}
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(params)
    out = []
    try:
        root = ET.fromstring(http_get(url))
    except Exception as e:
        note_fail("גוגל חדשות", e)
        return out
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        src_el = it.find("source")
        pub = (src_el.text or "").strip() if src_el is not None else ""
        # Google appends " - Publisher" to the title.
        if pub and title.endswith(" - " + pub):
            title = title[: -len(pub) - 3].strip()
        try:
            dt = parsedate_to_datetime(it.findtext("pubDate"))
        except Exception:
            continue
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        if dt < since or not title:
            continue
        out.append({"title": title, "summary": "", "publisher": pub or "Google News",
                    "link": (it.findtext("link") or "").strip(), "dt": dt, "via": "גוגל חדשות"})
    return out


def sec_filings(ticker, since):
    url = ("https://www.sec.gov/cgi-bin/browse-edgar?" + urllib.parse.urlencode(
        {"action": "getcompany", "CIK": ticker, "type": "", "dateb": "", "owner": "include",
         "count": "40", "output": "atom"}))
    out = []
    try:
        raw = http_get(url, ua=SEC_UA)
        time.sleep(0.15)  # SEC fair-access limit
        root = ET.fromstring(raw)
    except Exception as e:
        note_fail("רשות ניירות הערך האמריקאית", e)
        return out
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for e in root.findall("a:entry", ns):
        cat = e.find("a:category", ns)
        form = (cat.get("term") if cat is not None else "") or ""
        if not SEC_FORMS.match(form):
            continue
        upd = e.findtext("a:updated", default="", namespaces=ns)
        try:
            dt = datetime.fromisoformat(upd)
        except ValueError:
            continue
        if dt < since:
            continue
        summary = re.sub("<[^>]+>", " ", e.findtext("a:summary", default="", namespaces=ns))
        link_el = e.find("a:link", ns)
        link = link_el.get("href") if link_el is not None else ""
        items = re.findall(r"Item (\d\.\d\d)", summary)
        if form.startswith("8-K"):
            major = [i for i in items if i not in ITEMS_8K_MINOR]
            if not major and "7.01" not in items and "8.01" not in items:
                continue
            labels = [ITEMS_8K[i][0] for i in items if i in ITEMS_8K and i != "9.01"]
            cats = [ITEMS_8K[i][1] for i in items if i in ITEMS_8K and ITEMS_8K[i][1]]
            text = f"דיווח מיידי (טופס {form}): " + ("; ".join(labels) if labels else "אירוע מהותי")
            cat_key = cats[0] if cats else "other"
        else:
            base = next((k for k in SEC_FORM_HE if form.startswith(k)), form)
            text = f"{SEC_FORM_HE.get(base, 'דיווח')} (טופס {form})"
            cat_key = "mna" if "13D" in form else "capital"
        out.append({"title_he": text, "title": "", "summary": "", "publisher": "SEC EDGAR", "link": link,
                    "dt": dt, "via": "רשות ניירות הערך האמריקאית", "cat": cat_key, "official": True,
                    "items": items})
    return out


# ---------------- Classification ----------------
def classify(text, hebrew=False):
    if NOISE.search(text):
        return None
    for key, _he, _prio, en_re, he_re in CATEGORIES:
        if re.search(he_re if hebrew else en_re, text, re.I):
            return key
    return None


CAT = {c[0]: c for c in CATEGORIES}
CAT["other"] = ("other", "דיווח רשמי", 6, "", "")


def impact(text):
    pos, neg = bool(POSITIVE.search(text)), bool(NEGATIVE.search(text))
    if pos and not neg:
        return "חיובית"
    if neg and not pos:
        return "שלילית"
    return "לא ברורה"


def cluster(items):
    """Group items that report the same story (title-token overlap)."""
    clusters = []
    for it in sorted(items, key=lambda x: x["dt"]):
        tk = tokens(it.get("title") or it.get("title_he", ""))
        best, best_sim = None, 0.0
        for c in clusters:
            if c["official"] or it.get("official"):
                continue
            inter = len(tk & c["tokens"])
            sim = inter / max(1, min(len(tk), len(c["tokens"])))
            if sim > best_sim:
                best, best_sim = c, sim
        if best is not None and best_sim >= 0.5:
            best["items"].append(it)
            best["tokens"] |= tk
        else:
            clusters.append({"items": [it], "tokens": set(tk), "official": bool(it.get("official"))})
    for c in clusters:
        c["publishers"] = {publisher_key(i["publisher"]): i for i in c["items"]}
        c["first"] = min(c["items"], key=lambda x: x["dt"])
        c["cat"] = c["first"].get("cat")
    return clusters


def corroborate_with_sec(clusters):
    """A news cluster in the same category as a same-day SEC filing counts as corroborated."""
    sec = [c for c in clusters if c["official"]]
    for c in clusters:
        if c["official"]:
            continue
        for s in sec:
            if s["cat"] == c["cat"] and abs((s["first"]["dt"] - c["first"]["dt"]).total_seconds()) < 2 * 86400:
                c["sec_link"] = s["first"]["link"]


# ---------------- Translation (free, best effort) ----------------
_TR_CACHE = {}


def to_hebrew(text):
    if not TRANSLATE or not text:
        return None
    if text in _TR_CACHE:
        return _TR_CACHE[text]
    url = "https://translate.googleapis.com/translate_a/single?" + urllib.parse.urlencode(
        {"client": "gtx", "sl": "en", "tl": "iw", "dt": "t", "q": text})
    try:
        data = json.loads(http_get(url, timeout=10).decode("utf-8"))
        he = "".join(seg[0] for seg in data[0] if seg and seg[0]).strip()
        time.sleep(0.2)
    except Exception as e:
        note_fail("תרגום אוטומטי", e)
        he = None
    _TR_CACHE[text] = he
    return he


# ---------------- Scanner flags ----------------
def scanner_flags():
    flags = {}
    try:
        txt = open(SCANNER_REPORT, encoding="utf-8").read()
    except OSError:
        return flags, None
    m = re.search(r"Reversal Checker — (\d{4}-\d{2}-\d{2})", txt)
    rep_date = m.group(1) if m else None
    for block in re.split(r"\n(?=## )", txt):
        h = re.match(r"## (\S+)", block)
        if not h:
            continue
        t = h.group(1).upper()
        if "BUY TRIGGER" in block:
            flags[t] = "טריגר קנייה בסורק"
        elif "EARLY ALERT" in block:
            flags[t] = "התראה מוקדמת בסורק"
    return flags, rep_date


# ---------------- Main ----------------
def should_run_now():
    """Two UTC crons cover Israel summer/winter time; run only the one that lands ~09:10 Israel."""
    if os.environ.get("GITHUB_EVENT_NAME") != "schedule":
        return True
    sched = os.environ.get("SCHEDULE", "")
    offset_h = int(datetime.now(IL).utcoffset().total_seconds() // 3600)
    expected = "10 6 * * *" if offset_h == 3 else "10 7 * * *"
    if sched != expected:
        print(f"Skipping: schedule '{sched}' is not the Israel-09:10 slot today (offset +{offset_h}).")
        return False
    return True


def collect_ticker(t, info, since):
    name = clean_company_name(info.get("shortName") or info.get("longName") or "")
    raw = yahoo_news(t, since)
    q = f'"{name}" ({t} OR stock OR shares) when:2d' if name else f"{t} stock when:2d"
    raw += google_news(q, since)
    if t in ISRAELI:
        raw += google_news(f'"{ISRAELI[t]}" {IL_SITES} when:2d', since, lang="he")
    picked = []
    for it in raw:
        hebrew = bool(re.search(r"[֐-׿]", it["title"]))
        text = f'{it["title"]} {it.get("summary", "")}'
        if not hebrew and name and t not in it["title"].upper() and \
                not re.search(re.escape(name.split()[0]), text, re.I):
            continue  # story is not about this company
        cat = classify(text, hebrew=hebrew)
        if cat:
            it["cat"], it["hebrew"] = cat, hebrew
            picked.append(it)
    picked += sec_filings(t, since)
    clusters = cluster(picked)
    corroborate_with_sec(clusters)
    for c in clusters:
        c["prio"] = CAT[c["cat"]][2] + (2 if len(c["publishers"]) > 1 or c.get("sec_link") else 0) \
            + (2 if c["official"] else 0)
    clusters.sort(key=lambda c: (c["prio"], c["first"]["dt"]), reverse=True)
    return name, clusters[:MAX_ITEMS_PER_TICKER]


def render_cluster(c, show_impact=True):
    f = c["first"]
    if c["official"]:
        he_title, orig = f["title_he"], ""
        verify = "מקור רשמי: דיווח לרשות ניירות הערך האמריקאית"
        verify_color = "#1a7f37"
    else:
        best = next((i for i in c["items"] if i.get("hebrew")), f)
        if best.get("hebrew"):
            he_title, orig = best["title"], ""
        else:
            he_title = to_hebrew(best["title"]) or best["title"]
            orig = best["title"] if he_title != best["title"] else ""
        n = len(c["publishers"])
        if c.get("sec_link"):
            verify, verify_color = "אומת מול דיווח רשמי לרשות ניירות הערך", "#1a7f37"
        elif n > 1:
            verify, verify_color = f"אומת: {n} מקורות בלתי תלויים", "#1a7f37"
        else:
            verify, verify_color = "מקור יחיד – לא אומת", "#b54708"
    all_text = " ".join((i.get("title") or i.get("title_he", "")) + " " + i.get("summary", "") for i in c["items"])
    imp = impact(all_text) if not c["official"] else impact(f["title_he"])
    fwd = bool(FORWARD.search(all_text))
    srcs = []
    for i in list(c["publishers"].values())[:4]:
        label = html.escape(i["publisher"] if i["publisher"] != "SEC EDGAR" else "רשות ניירות הערך")
        srcs.append(f'<a href="{html.escape(i["link"])}" style="color:#1a56db">{label}</a>' if i["link"] else label)
    if c.get("sec_link"):
        srcs.append(f'<a href="{html.escape(c["sec_link"])}" style="color:#1a56db">דיווח רשמי</a>')
    imp_color = {"חיובית": "#1a7f37", "שלילית": "#c62828"}.get(imp, "#555")
    parts = [
        f'<div style="margin:8px 0;padding:8px 10px;border-right:3px solid #c9d3f5;background:#fff">',
        f'<span style="font-size:11px;background:#eef2ff;border-radius:4px;padding:1px 6px">{CAT[c["cat"]][1]}</span> ',
        f'<b>{html.escape(he_title)}</b>',
    ]
    if orig:
        parts.append(f'<div dir="ltr" style="text-align:left;color:#888;font-size:11px;margin-top:2px">{html.escape(orig)}</div>')
    parts.append(
        f'<div style="font-size:12px;color:#444;margin-top:4px;line-height:1.6">'
        f'📅 תאריך פרסום: {fmt_il(f["dt"])} (שעון ישראל) · '
        + (f'השפעה אפשרית: <b style="color:{imp_color}">{imp}</b> · ' if show_impact else "") +
        f'<span style="color:{verify_color}">{verify}</span><br>'
        f'מקורות: {" · ".join(srcs)}</div>')
    if fwd:
        parts.append('<div style="font-size:12px;color:#b54708;margin-top:2px">⏳ יש בידיעה רכיב צופה פני עתיד; '
                     'הסטטוס עשוי להשתנות.</div>')
    parts.append("</div>")
    return "".join(parts), he_title, verify


def main():
    if not should_run_now():
        return
    now_il = datetime.now(IL)
    since = window_start(now_il)
    tickers = load_tickers()
    flags, rep_date = scanner_flags()
    print(f"{len(tickers)} tickers, window since {since.isoformat()}")

    funds, companies, infos = [], [], {}
    for t in tickers:
        try:
            info = yf.Ticker(t).info or {}
        except Exception as e:
            note_fail("יאהו פייננס", e)
            info = {}
        infos[t] = info
        (funds if info.get("quoteType") in ("ETF", "MUTUALFUND") else companies).append(t)

    with_news, quiet, earnings = [], [], []
    for t in companies:
        name, clusters = collect_ticker(t, infos[t], since)
        if clusters:
            with_news.append((t, name or t, clusters))
        else:
            quiet.append(t)
        try:
            e = fetch_next_earnings(t)
            if e and 0 <= e["days"] <= EARNINGS_AHEAD_DAYS:
                earnings.append((t, e))
        except Exception as ex:
            note_fail("לוח דוחות", ex)

    # Sector / macro: only corroborated stories (>= 2 publishers), max 2 per sector.
    present = set(tickers)
    sector_html = []
    for label, q, req, syms in SECTORS:
        affected = [s for s in syms if s in present]
        if not affected:
            continue
        items = [i for i in google_news(q + " when:1d", since)
                 if re.search(req, i["title"], re.I) and not NOISE.search(i["title"])]
        for i in items:
            i["cat"] = "other"
        cl = [c for c in cluster(items) if len(c["publishers"]) >= 2]
        cl.sort(key=lambda c: len(c["publishers"]), reverse=True)
        for c in cl[:2]:
            block, _, _ = render_cluster(c, show_impact=False)
            block = block.replace(f'>{CAT["other"][1]}<', f">{html.escape(label)}<", 1)
            sector_html.append(block + f'<div style="font-size:12px;color:#333;margin:-4px 0 10px">'
                                       f'עשוי להשפיע על: {", ".join(affected)}</div>')

    # Rank tickers: scanner flag first, then strongest item.
    with_news.sort(key=lambda x: (x[0] in flags, max(c["prio"] for c in x[2])), reverse=True)
    cards, top_lines, text_lines = [], [], []
    for t, name, clusters in with_news:
        badge = (f' <span style="background:#e6f4ea;color:#1a7f37;border-radius:4px;padding:1px 6px;font-size:12px">'
                 f'🔔 {flags[t]}</span>') if t in flags else ""
        blocks = []
        for c in clusters:
            b, he_title, verify = render_cluster(c)
            blocks.append(b)
            text_lines.append(f"{t}: {he_title} ({fmt_il(c['first']['dt'])}, {verify})")
            if len(top_lines) < 3:
                top_lines.append(f"<b>{t}</b>: {html.escape(he_title)}")
        cards.append(f'<div style="border:1px solid #e3e6ee;border-radius:10px;padding:10px 14px;margin:10px 0;'
                     f'background:#fafbff"><div style="font-size:16px"><b>{t}</b> · {html.escape(name)}{badge}</div>'
                     + "".join(blocks) + "</div>")

    date_he = fmt_day(now_il)
    subject = f"תקציר חדשות מהותיות – {date_he}"
    if earnings:
        earnings.sort(key=lambda x: x[1]["date"])
        e_rows = "".join(
            f"<li><b>{t}</b> – {fmt_day(datetime.fromisoformat(e['date']))}"
            f"{' (משוער)' if e['estimated'] else ' (מאושר)'}</li>" for t, e in earnings)
        earnings_html = f'<ul style="margin:4px 0;padding-right:18px">{e_rows}</ul>'
    else:
        earnings_html = '<p style="margin:4px 0">לא נמצאו דוחות מתוכננים ב-7 הימים הקרובים.</p>'
    fail_html = ""
    if FAILURES:
        fail_html = ('<p style="color:#b54708;font-size:12px">⚠️ מקורות שנכשלו חלקית בריצה הזו (ייתכן שחסרות ידיעות): '
                     + ", ".join(f"{k} ({v} פעמים)" for k, v in FAILURES.items()) + "</p>")
    scan_note = (f"דוח הסורק שנבדק: {rep_date}" if rep_date else "דוח הסורק לא נמצא")
    if with_news:
        opening = (f"<p><b>{len(with_news)}</b> מניות עם חדשות מהותיות. העיקר:</p>"
                   f'<ul style="margin:4px 0;padding-right:18px">' + "".join(f"<li>{l}</li>" for l in top_lines) + "</ul>")
    else:
        opening = "<p><b>לא נמצאו היום חדשות מהותיות</b> על המניות ברשימת המעקב.</p>"

    def section(title, body):
        return f'<h3 style="margin:18px 0 6px;border-bottom:1px solid #e3e6ee;padding-bottom:4px">{title}</h3>{body}'

    body_html = f"""<!DOCTYPE html>
<html dir="rtl" lang="he"><head><meta charset="utf-8"></head>
<body style="font-family:Arial,Helvetica,sans-serif;background:#f5f6fa;margin:0;padding:16px;direction:rtl;text-align:right">
<div style="max-width:760px;margin:0 auto;background:#fff;border-radius:12px;padding:16px 18px">
<h2 style="margin:0 0 4px">{subject}</h2>
<p style="color:#666;font-size:12px;margin:0 0 12px">חלון הבדיקה: מ-{fmt_il(since)} עד {fmt_il(now_il)} (שעון ישראל) ·
{len(companies)} חברות ו-{len(funds)} קרנות · {scan_note}</p>
{fail_html}
{opening}
{section("חדשות לפי מניה", "".join(cards) or "<p>אין.</p>")}
{section("סקטור ומאקרו", "".join(sector_html) or "<p>לא נמצאו ידיעות סקטור שאומתו בשני מקורות לפחות.</p>")}
{section("דוחות בשבוע הקרוב", earnings_html)}
{section("ללא חדשות מהותיות", f'<p style="font-size:13px">{", ".join(quiet) or "אין"}</p>')}
{section("קרנות סל (מכוסות רק דרך סקטור ומאקרו)", f'<p style="font-size:13px">{", ".join(funds) or "אין"}</p>')}
<p style="color:#999;font-size:11px;margin-top:18px;line-height:1.6">
מקורות: יאהו פייננס, גוגל חדשות (כולל גלובס, כלכליסט, דה מרקר וביזפורטל לחברות ישראליות), דיווחים לרשות ניירות הערך האמריקאית.
הסינון והערכת ההשפעה אוטומטיים לפי מילות מפתח, בלי בינה מלאכותית; הכותרות מתורגמות אוטומטית והמקור באנגלית מוצג מתחתן.
"אומת" = אותה ידיעה נמצאה אצל לפחות שני מפרסמים שונים או בדיווח רשמי.</p>
</div></body></html>"""

    text_body = subject + "\n\n" + ("\n".join(text_lines) or "לא נמצאו חדשות מהותיות.")
    os.makedirs("reports", exist_ok=True)
    with open(os.path.join("reports", "news_latest.html"), "w", encoding="utf-8") as fh:
        fh.write(body_html)
    send_email(subject, text_body, body_html)
    print(f"Done: {len(with_news)} tickers with news, {len(quiet)} quiet, {len(funds)} funds, failures={FAILURES}")


if __name__ == "__main__":
    sys.exit(main())
