# -*- coding: utf-8 -*-
"""提取 Lyne《OCCULT ETHER PHYSICS》4th Ed. 全文 + 定位 p.125 之后的原子氢内容"""
import sys, os, re, json
import fitz

PDF = r"D:\AAA我的文件\未来氢内爆汽车\OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf"
OUT = r"D:\AAA我的文件\未来氢内爆汽车\_HHO书本提取\Lyne_OccultEtherPhysics_全文.txt"

doc = fitz.open(PDF)
print("页数:", doc.page_count)
meta = doc.metadata
print("元数据:", {k: v for k, v in meta.items() if v})

pages = []
for i in range(doc.page_count):
    t = doc[i].get_text()
    pages.append(t)

full = "\n".join(f"\n=== [PDF p.{i+1}] ===\n{t}" for i, t in enumerate(pages))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(full)
print("已写:", OUT, len(full), "字符")

# 关键词定位
KW = ["atomic hydrogen", "atom", "tungsten", "Welding", "welding", "Langmuir",
      "dissociat", "nascent", "H atom", "hydrogen atom", "Electric arc",
      "arc", "Irving Langmuir", "Russell", "Soviet", "Russia"]
print("\n=== 关键词命中页（页码为 PDF 物理页）===")
hits = {}
for i, t in enumerate(pages):
    low = t.lower()
    for k in ["tungsten", "atomic hydrogen", "langmuir", "nascent"]:
        if k.lower() in low:
            hits.setdefault(k, []).append(i + 1)
for k, v in hits.items():
    print(f"  {k:22s} → {len(v)} 页: {v[:40]}")
