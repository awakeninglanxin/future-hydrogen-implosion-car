#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核对 joe cell/图/Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png 是否来自 Lyne PDF 第 125 页。

老师说明：该 PNG = 书中第 125 页截图。
本脚本：
  1) 取 PDF 第 125 页（物理页）的嵌入图像对象 → 存出 + 记录尺寸/哈希
  2) 读 PNG → 尺寸/哈希/EXIF
  3) 与相邻页（120–130）一起做「图像指纹」比对，看 PNG 最像哪一页
"""
import os, sys, hashlib, io

PDF = r"D:\AAA我的文件\未来氢内爆汽车\OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf"
PNG = r"D:\AAA我的文件\未来氢内爆汽车\joe cell\图\Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png"
OUT = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_p125核对"
os.makedirs(OUT, exist_ok=True)

import fitz  # pymupdf

def h(b):
    return hashlib.sha256(b).hexdigest()[:16]

print("=" * 70)
print("一、PNG 本体")
print("=" * 70)
png_bytes = open(PNG, "rb").read()
print(f"文件大小 : {len(png_bytes):,} B")
print(f"sha256   : {h(png_bytes)}")
try:
    from PIL import Image
    im = Image.open(PNG)
    print(f"尺寸     : {im.size[0]} x {im.size[1]} px")
    print(f"模式     : {im.mode}")
    print(f"格式     : {im.format}")
    ex = im.getexif()
    if ex:
        print("EXIF:")
        for k, v in ex.items():
            print(f"   {k}: {v}")
    else:
        print("EXIF     : 无")
except ImportError:
    print("(PIL 不可用，跳过尺寸/EXIF)")

print()
print("=" * 70)
print("二、PDF 第 125 页（物理页）")
print("=" * 70)
doc = fitz.open(PDF)
print(f"总页数   : {doc.page_count}")

def page_info(i0):
    """i0 = 0-based 页索引"""
    pg = doc[i0]
    txt = pg.get_text().strip()
    imgs = pg.get_images(full=True)
    return pg, txt, imgs

pg, txt, imgs = page_info(124)   # 物理页 125 = 索引 124
print(f"索引 124（物理页 125）")
print(f"  页面尺寸   : {pg.rect.width:.1f} x {pg.rect.height:.1f} pt")
print(f"  文本字符数 : {len(txt)}")
print(f"  嵌入图像数 : {len(imgs)}")
if txt:
    print("  文本前 400 字:")
    print("   " + txt[:400].replace("\n", "\n   "))
else:
    print("  ★ 无文本 → 整页为图像（与『125 页是整页插图』一致）")

# 导出该页所有图像
for j, im in enumerate(imgs):
    xref = im[0]
    d = doc.extract_image(xref)
    ext = d["ext"]
    fp = os.path.join(OUT, f"p125_img{j+1}_xref{xref}.{ext}")
    open(fp, "wb").write(d["image"])
    print(f"    [图{j+1}] xref={xref} {d['width']}x{d['height']} {ext} "
          f"{len(d['image']):,} B sha={h(d['image'])} -> {os.path.basename(fp)}")

# 同时把整页渲染成 PNG（用于人工比对）
pix = pg.get_pixmap(dpi=150)
rp = os.path.join(OUT, "p125_render150.png")
pix.save(rp)
print(f"  整页渲染 -> {os.path.basename(rp)} ({pix.width}x{pix.height}) "
      f"{os.path.getsize(rp):,} B")

print()
print("=" * 70)
print("三、邻居页扫描（物理页 118–132），看哪几页是整页插图")
print("=" * 70)
print(f"{'物理页':>6} | {'字符数':>7} | {'图数':>4} | 首行文字")
print("-" * 70)
for i0 in range(117, 132):        # 索引 117..131 = 物理页 118..132
    p = doc[i0]
    t = p.get_text().strip()
    first = t.split("\n")[0][:46] if t else "(无文字)"
    n = len(p.get_images(full=True))
    mark = "  ★整页图" if len(t) < 40 and n else ""
    print(f"{i0+1:>6} | {len(t):>7} | {n:>4} | {first}{mark}")

doc.close()
print()
print(f"产出目录: {OUT}")
