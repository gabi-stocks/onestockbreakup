"""Run the daily news digest exactly as before (same email), and also save the
items as reports/news_latest.json for the stock dashboard.

It wraps news_digest.py instead of changing it: it records each ticker's news
clusters and the Hebrew title / verification line the email shows, then writes
them out after the digest finishes.
"""
import json
import os
import sys

import news_digest as nd

_found = []      # (ticker, company name, clusters) for tickers with news
_shown = {}      # id(cluster) -> (hebrew title, verification line) as rendered in the email

_orig_collect = nd.collect_ticker
_orig_render = nd.render_cluster


def _collect(t, info, since):
    name, clusters = _orig_collect(t, info, since)
    if clusters:
        _found.append((t, name or t, clusters))
    return name, clusters


def _render(c, show_impact=True):
    block, he_title, verify = _orig_render(c, show_impact)
    _shown[id(c)] = (he_title, verify)
    return block, he_title, verify


nd.collect_ticker = _collect
nd.render_cluster = _render


def _item(t, name, c):
    he_title, verify = _shown.get(id(c), (c["first"].get("title_he") or c["first"].get("title", ""), ""))
    text = " ".join((i.get("title") or i.get("title_he", "")) + " " + i.get("summary", "") for i in c["items"])
    link = next((i["link"] for i in c["publishers"].values() if i.get("link")), c.get("sec_link") or "")
    dt = c["first"]["dt"]
    return {
        "ticker": t, "name": name,
        "category": nd.CAT[c["cat"]][1],
        "title": he_title,
        "verify": verify,
        "verified": verify.startswith("אומת") or verify.startswith("מקור רשמי"),
        "impact": nd.impact(c["first"].get("title_he", "") if c.get("official") else text),
        "forward": bool(nd.FORWARD.search(text)),
        "date": dt.astimezone(nd.IL).isoformat(),
        "date_il": nd.fmt_il(dt),
        "link": link,
    }


def main():
    run_today = nd.should_run_now()
    rc = nd.main()
    if not run_today:
        return rc
    now = nd.datetime.now(nd.IL)
    out = {
        "generated": now.isoformat(),
        "generated_il": nd.fmt_il(now),
        "window_start": nd.window_start(now).isoformat(),
        "items": [_item(t, name, c) for t, name, clusters in _found for c in clusters],
    }
    os.makedirs("reports", exist_ok=True)
    with open(os.path.join("reports", "news_latest.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"news_latest.json: {len(out['items'])} items")
    return rc


if __name__ == "__main__":
    sys.exit(main())
