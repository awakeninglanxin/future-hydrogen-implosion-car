# -*- coding: utf-8 -*-
"""从 tesla3.com 抓取的 HTML 中提取 Memo 英文全文，落盘为 txt。"""
import re, html, os, glob

MAP = {
    'tesla3/p2364.html': ('section1', 'Memo WFC 420 · Hydrogen Fracturing Process', 'WATER FUEL CELL'),
    'tesla3/p2367.html': ('section2', 'Memo WFC 421 · Quenching Circuit Technology', 'WATER FUEL CELL'),
    'tesla3/p2368.html': ('section3', 'Memo WFC 422DA · WFC Hydrogen Gas Management System', 'WATER FUEL CELL'),
    'tesla3/p2369.html': ('section4', 'Memo WFC 423DA · Water Fuel Injection System', 'WATER FUEL CELL'),
    'tesla3/stanley-meyer-memo-6.html': ('section6', 'Memo WFC 425 · Water Fuel Injector: Taper Resonant Cavity', 'WATER FUEL CELL'),
    'tesla3/p2372.html': ('section7', 'Memo WFC 426 · VIC Matrix Circuit', 'WATER FUEL CELL'),
    'tesla3/p2373.html': ('section8', 'Memo WFC 427 · Voltage Wave-Guide Propagating', 'Voltage Wave-Guide Propagating'),
}

OUT = 'tesla3_extract'
os.makedirs(OUT, exist_ok=True)

# 页面尾部要砍掉的导航/评论噪声标志
CUT_MARKERS = [
    'Laisser un commentaire', 'Commentaires', 'Navigation des articles',
    'Articles similaires', 'À propos', 'Propulsé par WordPress',
    'Ce site utilise des cookies', 'Votre adresse',
]

def clean_text(h):
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
    h = re.sub(r'<!--.*?-->', ' ', h, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', h))
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t.strip()

for path, (name, title, anchor) in MAP.items():
    if not os.path.exists(path):
        print('MISSING', path); continue
    raw = open(path, encoding='utf-8', errors='ignore').read()
    t = clean_text(raw)
    i = t.find(anchor)
    if i < 0:
        print('ANCHOR-NOT-FOUND', path, name); continue
    body = t[i:]
    # 砍尾部
    for m in CUT_MARKERS:
        j = body.find(m)
        if j > 500:
            body = body[:j]
    body = body.strip()
    dst = os.path.join(OUT, f'{name}_{title.split("·")[0].strip().replace(" ","_")}.txt')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n# 来源：tesla3.com（原文为 users.skynet.be 的 sectionN.pdf，HTML 转录版）\n\n')
        f.write(body)
    print(f'OK {name:10s} {len(body):7d} chars -> {os.path.basename(dst)}')
