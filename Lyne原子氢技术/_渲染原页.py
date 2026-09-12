#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染 Lyne PDF 中与「103 / 109」有关的原页，供人眼核对。"""
import os, fitz

PDF = r"D:\AAA我的文件\未来氢内爆汽车\OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf"
OUT = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_原页核对"
os.makedirs(OUT, exist_ok=True)

# 物理页 -> 关注的文字
PAGES = {
    110: "首次出现 103 cal/gram mole（工艺段落）",
    111: "103 与 109 并列讨论 + Lyne 自疑原话",
    112: "Partington 引文（100 kcal）",
    113: "Partington 续 + 关键句",
    114: "103「骗局」说法",
    121: "Norton Encyclopedia 引用 + 各类热值",
    122: "Moelwyn-Hughes「De is 109 kcal」+ p.418 引文",
}

doc = fitz.open(PDF)
print(f"总页数: {doc.page_count}\n")
for pnum, note in sorted(PAGES.items()):
    i0 = pnum - 1
    if i0 >= doc.page_count:
        print(f"物理页 {pnum}: 超范围")
        continue
    pg = doc[i0]
    pix = pg.get_pixmap(dpi=200)
    fp = os.path.join(OUT, f"p{pnum:03d}.png")
    pix.save(fp)
    txt = pg.get_text().strip()
    print(f"物理页 {pnum:>3} | {pix.width}x{pix.height} | "
          f"{os.path.getsize(fp):,} B | {note}")
    print(f"          {txt[:150].replace(chr(10),' / ')}")
    print()
doc.close()
print(f"产出: {OUT}")
