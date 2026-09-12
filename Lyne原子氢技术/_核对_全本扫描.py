#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全本 137 页扫描：找出 PNG 最像哪一页（含旋转/裁剪容差）。

对每一页：
  ① 取出该页所有嵌入图像，逐个与 PNG 比 NCC（多尺度）
  ② 该页整页渲染（150dpi）与 PNG 比 NCC
对嵌入图像另做 0/90/180/270 旋转、以及「贴边裁剪」容差。
输出 Top-10 相似项。
"""
import os, numpy as np, fitz
from PIL import Image

PDF  = r"D:\AAA我的文件\未来氢内爆汽车\OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf"
PNG  = r"D:\AAA我的文件\未来氢内爆汽车\joe cell\图\Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png"
OUT  = r"D:\AAA我的文件\未来氢内爆汽车\Lyne原子氢技术\_p125核对"
os.makedirs(OUT, exist_ok=True)

TARGET = (426, 552)   # 统一到 PNG 尺寸

def gray_arr(im):
    return np.asarray(im.convert("L").resize(TARGET, Image.LANCZOS), dtype=np.float64)

def ncc(a, b):
    a = a - a.mean(); b = b - b.mean()
    d = np.sqrt((a*a).sum()) * np.sqrt((b*b).sum())
    return float((a*b).sum()/d) if d else float("nan")

def best_ncc_over_rotations(ref, cand_im):
    """cand_im 原图 + 4 个旋转，取最大 NCC"""
    best = (-2, None)
    for ang in (0, 90, 180, 270):
        im = cand_im.rotate(ang, expand=True) if ang else cand_im
        try:
            v = ncc(ref, gray_arr(im))
        except Exception:
            continue
        if v > best[0]:
            best = (v, ang)
    return best

def crop_tolerant(ref, cand_im):
    """容忍截图裁掉页边：对候选图做多组贴边裁剪后比 NCC"""
    W, H = cand_im.size
    best = (-2, None)
    for fx in (0.0, 0.03, 0.06):
        for fy in (0.0, 0.03, 0.06):
            box = (int(W*fx), int(H*fy), int(W*(1-fx)), int(H*(1-fy)))
            c = cand_im.crop(box)
            v = ncc(ref, gray_arr(c))
            if v > best[0]:
                best = (v, (fx, fy))
    return best

png = Image.open(PNG)
ref = gray_arr(png)
print(f"PNG: {png.size}  sha=39a7c12a6b83ed2e")
print(f"统一比对尺寸: {TARGET}")
print()

doc = fitz.open(PDF)
results = []

for i0 in range(doc.page_count):
    pnum = i0 + 1
    pg = doc[i0]

    # ① 整页渲染
    pix = pg.get_pixmap(dpi=150)
    render = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    v = ncc(ref, gray_arr(render))
    results.append((v, f"整页渲染", pnum, ""))

    # ② 每张嵌入图像
    for j, info in enumerate(pg.get_images(full=True)):
        xref = info[0]
        try:
            d = doc.extract_image(xref)
        except Exception:
            continue
        try:
            im = Image.open(__import__("io").BytesIO(d["image"]))
        except Exception:
            continue
        v2, ang = best_ncc_over_rotations(ref, im)
        results.append((v2, f"嵌入图{j+1} xref={xref} {d['width']}x{d['height']} rot={ang}", pnum,
                        f"{len(d['image'])}B"))
        # 裁剪容差（仅当旋转后仍不高时，才做更贵的裁剪比对）
        if v2 < 0.9:
            v3, box = crop_tolerant(ref, im)
            if v3 > v2:
                results.append((v3, f"嵌入图{j+1} xref={xref} 裁剪{box}", pnum, ""))

doc.close()

results.sort(key=lambda x: -x[0])
print("=" * 84)
print("Top 15 相似项（NCC 降序）")
print("=" * 84)
print(f"{'NCC':>8} | {'页':>4} | 类型")
print("-" * 84)
for v, typ, pnum, extra in results[:15]:
    flag = ""
    if v > 0.98: flag = "  ★★ 几乎同图"
    elif v > 0.90: flag = "  ★ 高度相似"
    elif v > 0.70: flag = "  ~ 有关联"
    print(f"{v:8.4f} | {pnum:>4} | {typ}  {extra}{flag}")

print()
print("=" * 84)
mx, mtyp, mp, _ = results[0]
print(f"最高 NCC = {mx:.4f}  出现在 物理页 {mp}  ({mtyp})")
if mx > 0.90:
    print("→ ✅ 找到来源页")
elif mx > 0.70:
    print("→ 🟡 相关但非同一画面（可能不同版次/不同截图区域）")
else:
    print("→ ❌ 全本 137 页均无匹配：该 PNG 不是 Lyne 这一版 PDF 第125页的截图")

# 落盘完整表
with open(os.path.join(OUT, "_全本扫描.csv"), "w", encoding="utf-8-sig") as f:
    f.write("ncc,页,类型,备注\n")
    for v, typ, pnum, extra in results:
        f.write(f"{v:.6f},{pnum},{typ},{extra}\n")
print(f"\n完整 {len(results)} 行已存: _全本扫描.csv")
