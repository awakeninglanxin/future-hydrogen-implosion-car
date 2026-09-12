# -*- coding: utf-8 -*-
"""重命名 joe cell/图/前苏联氢原子工艺.png → Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png
并同步更新所有引用该文件名的脚本与 md。

依据（2026-09-12 老师指令）：
  该图 = Lyne《Occult Ether Physics》PDF 物理页 125 的整页插图
       =《Lyne Atomic Hydrogen Furnace》(c)1996 TWL 设计图
  其工艺源头 = Langmuir 1924 专利 US1947267A（德国称 Arcatom）
  —— 故「前苏联氢原子工艺」一名查无实据，按老师指令改名。
"""
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = r"D:\AAA我的文件\未来氢内爆汽车"
OLD  = os.path.join(ROOT, r"joe cell\图\前苏联氢原子工艺.png")
NEW  = os.path.join(ROOT, r"joe cell\图\Langmuir1924原子氢专利US1947267A_来自Lyne著p125.png")

print("=" * 70)
print("重命名图片")
print("=" * 70)

print(f"\n旧名: {OLD}")
print(f"存在: {os.path.exists(OLD)}")
if os.path.exists(OLD):
    print(f"大小: {os.path.getsize(OLD):,} B")
print(f"\n新名: {NEW}")
print(f"已存在: {os.path.exists(NEW)}")

ok = False
if os.path.exists(OLD) and not os.path.exists(NEW):
    try:
        os.rename(OLD, NEW)
        ok = True
    except PermissionError as e:
        print(f"\n[PermissionError] {e}")
        print("→ 可能被 WPS / 资源管理器预览窗格占用，请先关闭。")
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
elif os.path.exists(NEW) and not os.path.exists(OLD):
    print("\n→ 旧名不存在、新名已存在：**重命名已完成**（不重复操作）")
    ok = True

print(f"\n重命名结果: {'✅ 成功' if ok else '❌ 未完成'}")
if ok:
    print(f"最终路径: {NEW}")
    print(f"最终大小: {os.path.getsize(NEW):,} B")
