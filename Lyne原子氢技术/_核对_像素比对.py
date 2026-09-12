#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""像素级比对：PNG vs PDF 第125页（内嵌原图 / 整页渲染）。

PNG:            426 x 552   (比例 0.7717)
PDF 内嵌图:     797 x 1051  (比例 0.7583)
PDF 整页渲染:  1275 x 1650  (比例 0.7727)  ← 页面 612x792pt 比例 0.7727

→ 先看比例，PNG 与「整页渲染」几乎一致 (0.7717 vs 0.7727)，
  与「内嵌图」差得多 (0.7717 vs 0.7583)。
本脚本用归一化互相关(NCC)与平均绝对误差(MAE)量化验证。
"""
import os, numpy as np
from PIL import Image, ImageOps

PNG   = r"D:\AAA我的文件\未来氢内爆汽车\joe cell\图\Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png"
EMB   = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_p125核对\p125_img1_xref286.jpeg"
REND  = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_p125核对\p125_render150.png"

def load_gray(p):
    im = Image.open(p).convert("L")
    return im

def compare(a_path, b_path, label, target=(426, 552)):
    a = load_gray(a_path)
    b = load_gray(b_path)
    # 统一到 target 尺寸
    a2 = np.asarray(a.resize(target, Image.LANCZOS), dtype=np.float64)
    b2 = np.asarray(b.resize(target, Image.LANCZOS), dtype=np.float64)
    # MAE
    mae = np.abs(a2 - b2).mean()
    # NCC
    a3 = a2 - a2.mean(); b3 = b2 - b2.mean()
    denom = (np.sqrt((a3**2).sum()) * np.sqrt((b3**2).sum()))
    ncc = float((a3*b3).sum()/denom) if denom else float('nan')
    print(f"{label}")
    print(f"   原始尺寸     : {a.size} vs {b.size}")
    print(f"   长宽比       : {a.size[0]/a.size[1]:.4f} vs {b.size[0]/b.size[1]:.4f}")
    print(f"   MAE (0-255)  : {mae:8.3f}   （越小越像；<25 视为同一画面）")
    print(f"   NCC (0-1)    : {ncc:8.4f}   （>0.90 高度相似；>0.98 几乎同图）")
    print()
    return mae, ncc

print("=" * 74)
print("PNG  尺寸:", Image.open(PNG).size)
print("内嵌图    :", Image.open(EMB).size, " 比例 %.4f" % (797/1051))
print("整页渲染  :", Image.open(REND).size, " 比例 %.4f" % (1275/1650))
print("=" * 74)
print()

r1 = compare(PNG, EMB,  "【比对 A】PNG  vs  PDF 内嵌原图(797x1051)")
r2 = compare(PNG, REND, "【比对 B】PNG  vs  PDF 整页渲染(1275x1650)")

print("=" * 74)
print("结论")
print("=" * 74)
if r2[1] > r1[1]:
    print("★ 整页渲染 NCC 更高 → PNG 是【整页截图】，含页面白边与页码")
else:
    print("★ 内嵌原图 NCC 更高 → PNG 是【图像对象提取】，无页面白边")
print(f"   A(内嵌) NCC={r1[1]:.4f} MAE={r1[0]:.2f}")
print(f"   B(整页) NCC={r2[1]:.4f} MAE={r2[0]:.2f}")

# 额外：把 PNG 与渲染页做「差异图」存档，便于人眼确认
a = np.asarray(load_gray(PNG).resize((426,552), Image.LANCZOS), dtype=np.float64)
b = np.asarray(load_gray(REND).resize((426,552), Image.LANCZOS), dtype=np.float64)
diff = np.abs(a-b)
dimg = Image.fromarray(diff.astype(np.uint8))
OUT = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_p125核对"
dimg.save(os.path.join(OUT, "_diff_png_vs_render.png"))
print(f"\n差异图已存: _diff_png_vs_render.png（越黑越一致，均值 {diff.mean():.2f}）")
