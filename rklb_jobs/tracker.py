"""
מעקב שבועי אחרי משרות פתוחות ב-Rocket Lab (RKLB).

מקור הנתונים: לוח המשרות הרשמי של החברה ב-Greenhouse (ממשק ציבורי, ללא מפתח).
כל ריצה:
  1. מושכת את כל המשרות + שיוך למחלקות.
  2. שומרת תמונת מצב ב-rklb_jobs/data/snapshots/YYYY-MM-DD.json
  3. משווה לתמונת המצב הקודמת ומוסיפה שורה ל-rklb_jobs/data/history.csv
  4. שולחת מייל בעברית עם שורת סיכום: לטובה / לרעה / ללא שינוי מהותי.

הרצה מקומית בלי שליחת מייל:  python rklb_jobs/tracker.py --dry-run
"""
import csv
import json
import os
import smtplib
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

BOARD = "rocketlab"
API = f"https://boards-api.greenhouse.io/v1/boards/{BOARD}"
UA = "rklb-jobs-tracker/1.0"          # בלי כתובת מייל – בכוונה
BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
SNAP_DIR = DATA / "snapshots"
HISTORY = DATA / "history.csv"
REPORT = BASE / "latest_report.html"

# ספים לשורת הסיכום
NET_MILD, NET_STRONG = 3.0, 8.0        # שינוי נטו באחוזים במספר המשרות
NEW_HIGH, NEW_LOW = 1.25, 0.75         # משרות חדשות השבוע מול ממוצע 4 השבועות הקודמים
OLD_DAYS = 90                          # משרה פתוחה מעל 90 יום = "ישנה"

HISTORY_FIELDS = ["date", "total", "added", "removed", "net", "net_pct",
                  "new_7d", "old_share_pct", "verdict"]


# ---------- משיכת נתונים ----------
def fetch(path):
    req = urllib.request.Request(f"{API}/{path}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def collect():
    jobs = fetch("jobs").get("jobs", [])
    dept_of = {}
    try:
        for d in fetch("departments").get("departments", []):
            for j in d.get("jobs", []):
                dept_of[j["id"]] = d.get("name") or "ללא מחלקה"
    except Exception as e:                       # המחלקות הן תוספת – לא קריטי
        print("departments fetch failed:", e)
    out = {}
    for j in jobs:
        jid = str(j["id"])
        out[jid] = {
            "title": j.get("title", ""),
            "location": (j.get("location") or {}).get("name", "") or "לא צוין",
            "dept": dept_of.get(j["id"], "ללא מחלקה"),
            "first_published": j.get("first_published") or "",
            "updated_at": j.get("updated_at") or "",
        }
    return out


# ---------- שמירה וטעינה ----------
def previous_snapshot(today):
    if not SNAP_DIR.exists():
        return None, None
    files = sorted(p for p in SNAP_DIR.glob("*.json") if p.stem < today)
    if not files:
        return None, None
    p = files[-1]
    return p.stem, json.loads(p.read_text(encoding="utf-8"))


def load_history():
    if not HISTORY.exists():
        return []
    with HISTORY.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(today, jobs, row):
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    (SNAP_DIR / f"{today}.json").write_text(
        json.dumps(jobs, ensure_ascii=False, indent=0), encoding="utf-8")
    rows = [r for r in load_history() if r["date"] != today] + [row]
    with HISTORY.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_FIELDS)
        w.writeheader()
        w.writerows(rows)


# ---------- ניתוח ----------
def analyse(today, jobs, prev_date, prev, history):
    now = datetime.now(timezone.utc)
    total = len(jobs)
    pub = [parse_dt(j["first_published"]) for j in jobs.values()]
    new_7d = sum(1 for d in pub if d and now - d <= timedelta(days=7))
    known = [d for d in pub if d]
    old_share = (100 * sum(1 for d in known if now - d > timedelta(days=OLD_DAYS))
                 / len(known)) if known else 0.0

    res = {"date": today, "total": total, "new_7d": new_7d,
           "old_share": old_share, "prev_date": prev_date,
           "loc": Counter(j["location"] for j in jobs.values()),
           "dept": Counter(j["dept"] for j in jobs.values()),
           "baseline": prev is None, "reasons": [], "warnings": []}

    if prev is None:
        res.update(added=[], removed=[], net=0, net_pct=0.0, score=0,
                   verdict="מדידה ראשונה – בסיס להשוואה")
        return res

    added = sorted(set(jobs) - set(prev))
    removed = sorted(set(prev) - set(jobs))
    net = total - len(prev)
    net_pct = 100 * net / len(prev) if prev else 0.0
    prev_loc = Counter(j["location"] for j in prev.values())
    prev_dept = Counter(j["dept"] for j in prev.values())
    res.update(added=added, removed=removed, net=net, net_pct=net_pct,
               prev_total=len(prev), prev_loc=prev_loc, prev_dept=prev_dept)

    score = 0
    if net_pct >= NET_STRONG:
        score += 2; res["reasons"].append(f"מספר המשרות עלה ב-{net_pct:.1f}% – עלייה חדה")
    elif net_pct >= NET_MILD:
        score += 1; res["reasons"].append(f"מספר המשרות עלה ב-{net_pct:.1f}%")
    elif net_pct <= -NET_STRONG:
        score -= 2; res["reasons"].append(f"מספר המשרות ירד ב-{abs(net_pct):.1f}% – ירידה חדה")
    elif net_pct <= -NET_MILD:
        score -= 1; res["reasons"].append(f"מספר המשרות ירד ב-{abs(net_pct):.1f}%")
    else:
        res["reasons"].append(f"מספר המשרות כמעט לא השתנה ({net_pct:+.1f}%)")

    past_new = [int(r["new_7d"]) for r in history[-4:] if r.get("new_7d", "").isdigit()]
    if past_new and sum(past_new) > 0:
        avg = sum(past_new) / len(past_new)
        ratio = new_7d / avg
        if ratio >= NEW_HIGH:
            score += 1; res["reasons"].append(
                f"קצב פרסום משרות חדשות גבוה מהרגיל ({new_7d} מול ממוצע {avg:.0f})")
        elif ratio <= NEW_LOW:
            score -= 1; res["reasons"].append(
                f"קצב פרסום משרות חדשות נמוך מהרגיל ({new_7d} מול ממוצע {avg:.0f})")
        else:
            res["reasons"].append(f"קצב פרסום משרות חדשות רגיל ({new_7d} מול ממוצע {avg:.0f})")

    if net_pct <= -10:
        res["warnings"].append("ירידה של יותר מ-10% בשבוע אחד – כדאי לבדוק אם יש הקפאת גיוס או פיטורים.")
    if prev and len(removed) > 0.25 * len(prev):
        res["warnings"].append("יותר מרבע מהמשרות של השבוע שעבר נסגרו – שינוי חריג.")

    res["score"] = score
    res["verdict"] = "לטובה" if score >= 1 else "לרעה" if score <= -1 else "ללא שינוי מהותי"
    return res


# ---------- דוח ----------
COLOR = {"לטובה": "#1a7f37", "לרעה": "#cf222e"}


def table(rows, head):
    th = "".join(f"<th style='padding:4px 6px;border-bottom:1px solid #ccc'>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td style='padding:4px 6px'>{c}</td>" for c in r) + "</tr>"
                 for r in rows)
    return f"<table style='border-collapse:collapse;width:100%;font-size:14px'><tr>{th}</tr>{tr}</table>"


def breakdown(cur, prev, n=8):
    rows = []
    for name, c in cur.most_common(n):
        if prev is None:
            rows.append([f"<span dir='ltr'>{name}</span>", c])
        else:
            d = c - prev.get(name, 0)
            rows.append([f"<span dir='ltr'>{name}</span>", c, f"{d:+d}" if d else "0"])
    return rows


def build_html(res, jobs, prev):
    v = res["verdict"]
    color = COLOR.get(v, "#57606a")
    parts = [f"<div dir='rtl' style='font-family:Arial,sans-serif;max-width:600px;margin:auto;"
             f"text-align:right;line-height:1.5;font-size:15px'>",
             f"<h2 style='margin:0 0 4px'>מעקב משרות – Rocket Lab</h2>",
             f"<div style='color:#57606a'>תאריך מדידה: {res['date']}"
             + (f" | השוואה ל-{res['prev_date']}" if res['prev_date'] else "") + "</div>",
             f"<div style='margin:12px 0;padding:10px;border-radius:8px;background:{color};"
             f"color:#fff;font-size:18px;font-weight:bold'>סיכום: {v}</div>"]

    if res["reasons"]:
        parts.append("<ul style='padding-right:18px;margin:0'>" +
                     "".join(f"<li>{r}</li>" for r in res["reasons"]) + "</ul>")
    for w in res["warnings"]:
        parts.append(f"<div style='margin-top:8px;padding:8px;background:#fff8c5;border-radius:6px'>⚠️ {w}</div>")

    nums = [["משרות פתוחות", res["total"]]]
    if not res["baseline"]:
        nums += [["בשבוע שעבר", res["prev_total"]],
                 ["שינוי נטו", f"{res['net']:+d} ({res['net_pct']:+.1f}%)"],
                 ["משרות שנפתחו", len(res["added"])],
                 ["משרות שנסגרו", len(res["removed"])]]
    nums += [["פורסמו לראשונה ב-7 הימים האחרונים", res["new_7d"]],
             [f"פתוחות יותר מ-{OLD_DAYS} יום", f"{res['old_share']:.0f}%"]]
    parts.append("<h3 style='margin:16px 0 4px'>המספרים</h3>" + table(nums, ["מדד", "ערך"]))

    head = ["מיקום", "משרות"] + ([] if res["baseline"] else ["שינוי"])
    parts.append("<h3 style='margin:16px 0 4px'>לפי מיקום</h3>" +
                 table(breakdown(res["loc"], res.get("prev_loc")), head))
    head = ["מחלקה", "משרות"] + ([] if res["baseline"] else ["שינוי"])
    parts.append("<h3 style='margin:16px 0 4px'>לפי מחלקה</h3>" +
                 table(breakdown(res["dept"], res.get("prev_dept")), head))

    if res["added"]:
        items = "".join(f"<li><span dir='ltr'>{jobs[i]['title']} – {jobs[i]['location']}</span></li>"
                        for i in res["added"][:10])
        more = f"<div>ועוד {len(res['added']) - 10}</div>" if len(res["added"]) > 10 else ""
        parts.append(f"<h3 style='margin:16px 0 4px'>דוגמאות למשרות חדשות</h3><ul>{items}</ul>{more}")
    if res["removed"]:
        items = "".join(f"<li><span dir='ltr'>{prev[i]['title']} – {prev[i]['location']}</span></li>"
                        for i in res["removed"][:10])
        more = f"<div>ועוד {len(res['removed']) - 10}</div>" if len(res["removed"]) > 10 else ""
        parts.append(f"<h3 style='margin:16px 0 4px'>דוגמאות למשרות שנסגרו</h3><ul>{items}</ul>{more}")

    parts.append("<p style='color:#57606a;font-size:13px;margin-top:16px'>"
                 "משרה שנסגרה יכולה להיות משרה שאוישה או משרה שבוטלה – אי אפשר להבדיל ביניהן. "
                 "לכן המגמה לאורך כמה שבועות חשובה יותר משבוע בודד. "
                 "מקור: לוח המשרות הרשמי של החברה.</p></div>")
    return "".join(parts)


def send_mail(subject, html):
    user, pwd, to = (os.environ.get(k) for k in ("GMAIL_USER", "GMAIL_APP_PASSWORD", "MAIL_TO"))
    if not (user and pwd and to):
        print("mail secrets missing – skipping email")
        return
    msg = MIMEMultipart("alternative")
    msg["Subject"], msg["From"], msg["To"] = subject, user, to
    msg.attach(MIMEText(html, "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(user, pwd)
        s.sendmail(user, [a.strip() for a in to.split(",")], msg.as_string())
    print("email sent")


def main():
    dry = "--dry-run" in sys.argv
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    jobs = collect()
    if not jobs:
        raise SystemExit("לא התקבלו משרות – כנראה תקלה בממשק. לא שומר כלום.")
    prev_date, prev = previous_snapshot(today)
    history = [r for r in load_history() if r["date"] != today]
    res = analyse(today, jobs, prev_date, prev, history)

    html = build_html(res, jobs, prev)
    REPORT.write_text(html, encoding="utf-8")
    save(today, jobs, {
        "date": today, "total": res["total"], "added": len(res["added"]),
        "removed": len(res["removed"]), "net": res["net"],
        "net_pct": f"{res['net_pct']:.2f}", "new_7d": res["new_7d"],
        "old_share_pct": f"{res['old_share']:.1f}", "verdict": res["verdict"]})

    subject = f"[מניית RKLB] מעקב משרות שבועי – {res['verdict']} ({res['total']} משרות)"
    print(subject)
    if not dry:
        send_mail(subject, html)


if __name__ == "__main__":
    main()
