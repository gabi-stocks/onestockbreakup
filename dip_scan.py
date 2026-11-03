import io, time, datetime as dt
import pandas as pd, numpy as np, requests, yfinance as yf

UA = {'User-Agent': 'Mozilla/5.0 (dip-scan research script)'}

def watchlist():
    out = []
    for line in open('tickers.txt', encoding='utf-8'):
        s = line.strip()
        if s and not s.startswith('#'):
            out.append(s.upper())
    return out

def wiki_table(url, col):
    try:
        html = requests.get(url, headers=UA, timeout=30).text
        for t in pd.read_html(io.StringIO(html)):
            if col in t.columns:
                return [str(x).replace('.', '-').upper() for x in t[col]]
    except Exception as e:
        print('wiki fail', url, e)
    return []

wl = watchlist()
sp = wiki_table('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', 'Symbol')
ndx = wiki_table('https://en.wikipedia.org/wiki/Nasdaq-100', 'Ticker')
universe = sorted(set(wl) | set(sp) | set(ndx) | {'SPY', 'QQQ'})
print('universe', len(universe), 'watch', len(wl), 'sp', len(sp), 'ndx', len(ndx))

data = yf.download(universe, period='1y', interval='1d', auto_adjust=True, group_by='ticker', threads=True, progress=False)

rows = []
for t in universe:
    try:
        df = data[t].dropna(subset=['Close'])
    except Exception:
        continue
    if len(df) < 70:
        continue
    c = df['Close']
    last = c.iloc[-1]
    h52 = c.max(); h3m = c.iloc[-63:].max()
    rows.append(dict(ticker=t, in_watch=t in wl, last_date=str(df.index[-1].date()), close=round(last, 2),
        dd_52w=round((last / h52 - 1) * 100, 1), dd_3m=round((last / h3m - 1) * 100, 1),
        chg_5d=round((last / c.iloc[-6] - 1) * 100, 1), chg_1m=round((last / c.iloc[-22] - 1) * 100, 1),
        chg_3m=round((last / c.iloc[-64] - 1) * 100, 1),
        high_3m_date=str(c.iloc[-63:].idxmax().date())))
prices = pd.DataFrame(rows).set_index('ticker')

cand = prices[(prices.in_watch) | ((prices.dd_3m <= -20) & (prices.chg_1m <= -8))].index.tolist()
print('candidates', len(cand))

def earnings_info(tk, df_close):
    res = {}
    try:
        ed = tk.get_earnings_dates(limit=8)
        if ed is not None and len(ed):
            ed = ed.dropna(subset=['Reported EPS'])
            if len(ed):
                r = ed.iloc[0]; d = ed.index[0]
                res['earn_date'] = str(d.date())
                res['eps_est'] = r.get('EPS Estimate'); res['eps_act'] = r.get('Reported EPS')
                res['eps_surprise_pct'] = r.get('Surprise(%)')
                dn = pd.Timestamp(d.date())
                before = df_close[df_close.index < dn]
                after = df_close[df_close.index > dn]
                if len(before) and len(after) >= 1:
                    # reaction across report: close before report day -> close 1-2 sessions after
                    a = after.iloc[min(1, len(after) - 1)]
                    res['earn_reaction_pct'] = round((a / before.iloc[-1] - 1) * 100, 1)
                    res['since_earn_pct'] = round((df_close.iloc[-1] / before.iloc[-1] - 1) * 100, 1)
    except Exception as e:
        res['earn_err'] = str(e)[:60]
    try:
        n = tk.calendar
        if isinstance(n, dict) and n.get('Earnings Date'):
            res['next_earn'] = str(n['Earnings Date'][0])
    except Exception:
        pass
    return res

keys = ['shortName', 'sector', 'industry', 'marketCap', 'revenueGrowth', 'earningsGrowth', 'trailingPE', 'forwardPE',
        'recommendationMean', 'numberOfAnalystOpinions', 'targetMeanPrice', 'grossMargins', 'operatingMargins', 'freeCashflow', 'debtToEquity']
out = []
for t in cand:
    tk = yf.Ticker(t)
    rec = {'ticker': t}
    try:
        info = tk.info
        for k in keys:
            rec[k] = info.get(k)
    except Exception as e:
        rec['info_err'] = str(e)[:60]
    rec.update(earnings_info(tk, data[t]['Close'].dropna()))
    out.append(rec)
    time.sleep(0.4)

f = pd.DataFrame(out).set_index('ticker')
res = prices.loc[cand].join(f)
res['upside_to_target_pct'] = ((res.targetMeanPrice / res.close - 1) * 100).round(1)
res['good_fund'] = (res.revenueGrowth.fillna(-1) > 0) & (res.earningsGrowth.fillna(-1) > 0) & (res.eps_surprise_pct.fillna(-1) > 0)
res = res.sort_values('dd_3m')
import os
os.makedirs('results', exist_ok=True)
res.to_csv('results/dip_scan.csv')
prices.loc[['SPY', 'QQQ']].to_csv('results/market.csv')
cols = ['in_watch', 'shortName', 'sector', 'close', 'last_date', 'dd_3m', 'dd_52w', 'chg_1m', 'chg_5d', 'revenueGrowth', 'earningsGrowth',
        'earn_date', 'eps_surprise_pct', 'earn_reaction_pct', 'since_earn_pct', 'forwardPE', 'recommendationMean', 'upside_to_target_pct', 'marketCap', 'next_earn', 'good_fund']
res[[c for c in cols if c in res.columns]].to_csv('results/dip_scan_short.csv')
print(res[[c for c in cols if c in res.columns]].head(40).to_string())
