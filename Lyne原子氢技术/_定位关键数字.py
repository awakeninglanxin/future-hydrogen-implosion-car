#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 Lyne PDF 中逐页搜索关键数字，精确定位物理页号。
文本层可能因 OCR/排版失真，故同时输出每处的完整上下文行。
"""
import fitz, re

PDF = r"D:\AAA我的文件\未来氢内爆汽车\OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf"

PATTERNS = [
    ("103 cal",        r"103\s*cal"),
    ("103 kcal",       r"103\s*k\.?cal"),
    ("109,000",        r"109\s*,\s*000"),
    ("109 kcal/1.9",   r"109\s*k\.?cal|1\.9\s*k\.?cal"),
    ("De is 109",      r"De\s+is\s+109"),
    ("100 kcal",       r"100\s*k\.?cal"),
    ("gram mole",      r"gram[- ]?mole"),
]

doc = fitz.open(PDF)
hits = {name: [] for name, _ in PATTERNS}

for i0 in range(doc.page_count):
    pg = doc[i0]
    txt = pg.get_text()
    # 规整空白便于匹配
    flat = re.sub(r"\s+", " ", txt)
    for name, pat in PATTERNS:
        for m in re.finditer(pat, flat, re.I):
            s = max(0, m.start()-90)
            e = min(len(flat), m.end()+110)
            hits[name].append((i0+1, flat[s:e]))

for name, _ in PATTERNS:
    hs = hits[name]
    pages = sorted(set(p for p, _ in hs))
    print("=" * 78)
    print(f"【{name}】 命中 {len(hs)} 处，分布物理页: {pages}")
    print("=" * 78)
    for p, ctx in hs:
        print(f"  p.{p:>3} │ …{ctx.strip()}…")
    print()

doc.close()
