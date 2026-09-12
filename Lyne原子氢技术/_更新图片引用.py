# -*- coding: utf-8 -*-
"""批量更新引用：前苏联氢原子工艺.png → Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png
覆盖 3 个脚本 + 3 个 md。逐文件读→替换→写→复验。
"""
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = r"D:\AAA我的文件\未来氢内爆汽车"
OLD_NAME = "前苏联氢原子工艺.png"
NEW_NAME = "Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png"

TARGETS = [
    r"Lyne原子氢技术\_核对_像素比对.py",
    r"Lyne原子氢技术\_核对_全本扫描.py",
    r"Lyne原子氢技术\_核对_第125页来源.py",
    r"joe cell\00_总索引_阅读指南.md",
    r"joe cell\06_编者校核与后续清单.md",
    r"Lyne原子氢技术\04_与既有资料对照_融通与差异.md",
]

print("=" * 72)
print("批量替换文件名引用")
print("=" * 72)

for rel in TARGETS:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print(f"\n[跳过] 不存在: {rel}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    n = txt.count(OLD_NAME)
    if n == 0:
        print(f"\n[无命中] {rel}")
        continue
    txt2 = txt.replace(OLD_NAME, NEW_NAME)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(txt2)
    # 复验
    with open(p, "r", encoding="utf-8") as f:
        back = f.read()
    print(f"\n[已改] {rel}")
    print(f"       替换 {n} 处 | 复验 旧名残留={back.count(OLD_NAME)} 新名={back.count(NEW_NAME)}")

print("\n" + "=" * 72)
print("全库残留扫描")
print("=" * 72)
hits = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in filenames:
        if not fn.lower().endswith((".py", ".md", ".txt")):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                c = f.read()
        except Exception:
            continue
        if OLD_NAME in c:
            hits += 1
            print(f"  ⚠️ {os.path.relpath(fp, ROOT)}")
if hits == 0:
    print("  ✅ 全库已无旧文件名残留（脚本/md/txt）")
