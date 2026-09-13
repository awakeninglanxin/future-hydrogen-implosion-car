# -*- coding: utf-8 -*-
"""
打包 OccultChemistry / Anu 相关资料包 → 桌面 zip

范围（B）：只挑 occult chem / anu 相关文件 + 含原典 PDF/DOCX
输出：C:/Users/ThinkPad/Desktop/OccultChemistry_Anu_资料包_20260913.zip
"""
import os
import zipfile
import datetime

SRC = r"D:\AAA我的文件\未来氢内爆汽车"
DST = r"C:\Users\ThinkPad\Desktop\OccultChemistry_Anu_资料包_20260913.zip"

# (源相对路径, zip 内路径)
FILES = [
    # ===== 一、OccultChemistry 精读（12 文件，全部）=====
    ("OccultChemistry精读/00_OccultChemistry书籍系列_总索引与阅读指南.md",
     "01_精读_编者整理/OccultChemistry精读/00_总索引与阅读指南.md"),
    ("OccultChemistry精读/01_神秘化学原典_物质层级与Anu结构.md",
     "01_精读_编者整理/OccultChemistry精读/01_物质层级与Anu结构.md"),
    ("OccultChemistry精读/02_氢族与两种变体_档案原文.md",
     "01_精读_编者整理/OccultChemistry精读/02_氢族与两种变体_档案原文.md"),
    ("OccultChemistry精读/03_元素组别与原子量表.md",
     "01_精读_编者整理/OccultChemistry精读/03_元素组别与原子量表.md"),
    ("OccultChemistry精读/04_1922-1933原始速记记录档案.md",
     "01_精读_编者整理/OccultChemistry精读/04_1922-1933原始速记记录.md"),
    ("OccultChemistry精读/05_Smith再评估_主流科学家的筛查.md",
     "01_精读_编者整理/OccultChemistry精读/05_Smith再评估.md"),
    ("OccultChemistry精读/06_Phillips_omegon模型.md",
     "01_精读_编者整理/OccultChemistry精读/06_Phillips_omegon模型.md"),
    ("OccultChemistry精读/07_Lyne_以太物理学.md",
     "01_精读_编者整理/OccultChemistry精读/07_Lyne_以太物理学.md"),
    ("OccultChemistry精读/08_旧解读勘误表.md",
     "01_精读_编者整理/OccultChemistry精读/08_旧解读勘误表.md"),
    ("OccultChemistry精读/09_Anu结构_逐条核对与提取.md",
     "01_精读_编者整理/OccultChemistry精读/09_Anu结构_逐条核对与提取.md"),
    ("OccultChemistry精读/_复算18_四书关键数字.py",
     "01_精读_编者整理/OccultChemistry精读/_复算18_四书关键数字.py"),
    ("OccultChemistry精读/_复算18_输出.txt",
     "01_精读_编者整理/OccultChemistry精读/_复算18_输出.txt"),

    # ===== 二、Anu 结构图（2 图）=====
    ("Anu结构图归档/leadbeater_E3到E4.jpg",
     "02_Anu结构图/leadbeater_E3到E4.jpg"),
    ("Anu结构图归档/leadbeater_最小物质单元anu1（E1）到E2.jpg",
     "02_Anu结构图/leadbeater_最小物质单元anu1（E1）到E2.jpg"),

    # ===== 三、原典（4 本 + 完整解读）=====
    ("OCCULT CHEMISTRY.pdf",
     "03_原典/OCCULT CHEMISTRY.pdf"),
    ("OCCULT CHEMISTRY RE-EVALUATED cn.pdf",
     "03_原典/OCCULT CHEMISTRY RE-EVALUATED cn.pdf"),
    ("OCCULT CHEMISTRY-神秘化学-翻译.docx",
     "03_原典/OCCULT CHEMISTRY-神秘化学-翻译.docx"),
    ("OCCULT ETHER PHYSICS 4th Revised and Expanded Edition Tesla’s Ideal Flying Machine and the Conspiracy to Conceal It (Lyne, William [Lyne, William]) (z-lib.org).pdf",
     "03_原典/OCCULT ETHER PHYSICS (Lyne 4th ed).pdf"),
    ("Extra-Sensory Perception of Quarks.docx",
     "03_原典/Extra-Sensory Perception of Quarks.docx"),
    ("OCCULT_CHEMISTRY_完整解读.md",
     "03_原典/OCCULT_CHEMISTRY_完整解读.md"),

    # ===== 四、Anu 相关专题（joe cell）=====
    ("joe cell/07_三种氢之辨_单质氢_HHO_氢氧混合气.md",
     "04_Anu相关专题/joe cell/07_三种氢之辨.md"),
    ("joe cell/08_单质氢的两种变体_微灵视MPA档案.md",
     "04_Anu相关专题/joe cell/08_单质氢的两种变体_微灵视MPA档案.md"),
    ("joe cell/09_H2分子的组合方式_两变体如何配对.md",
     "04_Anu相关专题/joe cell/09_H2分子的组合方式_两变体如何配对.md"),
    ("joe cell/10_质子含多少个Anu_碳12的216个Anu.md",
     "04_Anu相关专题/joe cell/10_质子含多少个Anu.md"),
    ("joe cell/11_变体配对假设的检验_ortho与para.md",
     "04_Anu相关专题/joe cell/11_变体配对假设的检验.md"),
    ("joe cell/_复算14_H2组合方式.py",
     "04_Anu相关专题/joe cell/_复算14_H2组合方式.py"),
    ("joe cell/_复算15_质子含多少Anu.py",
     "04_Anu相关专题/joe cell/_复算15_质子含多少Anu.py"),
    ("joe cell/_复算16_变体配对与ortho-para.py",
     "04_Anu相关专题/joe cell/_复算16_变体配对与ortho-para.py"),
    ("joe cell/_复算17_磁荷方向与ortho-para名称归属.py",
     "04_Anu相关专题/joe cell/_复算17_磁荷方向与ortho-para名称归属.py"),

    # ===== 五、Lyne 原子氢技术（anu 相关）=====
    ("Lyne原子氢技术/01_Lyne原作精读_原子氢过程全章.md",
     "05_Lyne原子氢技术/01_Lyne原作精读_原子氢过程全章.md"),
    ("Lyne原子氢技术/04_与既有资料对照_融通与差异.md",
     "05_Lyne原子氢技术/04_与既有资料对照_融通与差异.md"),
    ("Lyne原子氢技术/05_Lyne炉设计图与出处核对.md",
     "05_Lyne原子氢技术/05_Lyne炉设计图与出处核对.md"),
]


def build_readme():
    """生成资料包索引说明（作为包内 00 号文件）"""
    return """# OccultChemistry / Anu 资料包

> 打包日期：2026-09-13
> 来源项目：`未来氢内爆汽车`（D:\\AAA我的文件\\未来氢内爆汽车）
> 文件数：32（另有本说明 1 份）

---

## 这个包里有什么

| 目录 | 内容 | 文件数 |
|---|---|---|
| `01_精读_编者整理/` | **OccultChemistry 系列精读**（编者整理的 10 篇 md + 1 个复算脚本 + 输出） | 12 |
| `02_Anu结构图/` | **Anu 结构原图**（Leadbeater 手绘：E1→E2、E3→E4） | 2 |
| `03_原典/` | **原典 PDF/DOCX**（Occult Chemistry 英/中、Lyne 以太物理、Quarks 超感知） | 6 |
| `04_Anu相关专题/` | **Anu 专题**（joe cell 目录中与 Anu / 单质氢变体相关的 5 篇 + 4 个复算脚本） | 9 |
| `05_Lyne原子氢技术/` | **Lyne 原子氢技术**（与 Anu 相关的 3 篇） | 3 |

---

## 建议阅读顺序

### 路线 A · 想先了解「Anu 是什么」

1. `03_原典/OCCULT CHEMISTRY.pdf`（原典，图谱 + 文本）
2. `01_精读_编者整理/OccultChemistry精读/01_物质层级与Anu结构.md`
3. `01_精读_编者整理/OccultChemistry精读/09_Anu结构_逐条核对与提取.md`（逐条核对，最细）
4. `02_Anu结构图/` 两张图对照看

### 路线 B · 想看「关键数字对不对」

1. `01_精读_编者整理/OccultChemistry精读/03_元素组别与原子量表.md`
2. `_复算18_四书关键数字.py`（可运行，零依赖）→ `_复算18_输出.txt`
3. `01_精读_编者整理/OccultChemistry精读/08_旧解读勘误表.md`（★ 勘误：Anu 正解不是 10×7=70）

### 路线 C · 想看「与氢的关系」

1. `04_Anu相关专题/joe cell/07_三种氢之辨.md`（先分清 H₂ / H· / Anu 三种用法）
2. `04_Anu相关专题/joe cell/08_单质氢的两种变体_微灵视MPA档案.md`
3. `04_Anu相关专题/joe cell/09_H2分子的组合方式_两变体如何配对.md`
4. `04_Anu相关专题/joe cell/10_质子含多少个Anu.md`
5. `04_Anu相关专题/joe cell/11_变体配对假设的检验.md`

---

## ★ 读的时候要留意的几个数（最易错）

| 项 | 正解 | 常见误读 |
|---|---|---|
| **Anu 总价** | **10 线（3 粗 + 7 细）× 1,680 = 16,800** | ❌ 「10 × 7 = 70」 |
| **「7」是什么** | 每线**内部细分阶数**；最低级是 **7 气泡** | ❌ 当成 7 条线 |
| **OC 倍数** | **× 49** | ❌ × 7（也没有 343） |
| **漏斗数 vs 柏拉图立体** | **总价 = 面数 / 2**（4→2、6→3、8→4） | — |
| **两轴不可串** | **轴A** ether E1…E4 **止于 E4**（E5 = 0 次） | ❌ 把 E5 也数上 |
| **轴B** Anu 内部拆解 | `first-order spirillae` 属**轴B** | ❌ 与轴A 混谈 |
| **Anu ÷ 18 ≈ 原子量** | 命中 16/92 = **17.4%** ⇒ **非独立验证** | ❌ 当成「验证通过」 |

> ⚠️ 以上是**编者复算结论**；原典数字均已在 `_复算18` 中逐条核对，
> 表格类内容建议**回原文再核一遍**。

---

## 声明

- 本包为**个人研究归档**，原典 PDF 版权属原作者，仅作研究引用。
- 圈内主张 ↔ 主流实证**分轨并列**，各标证据强度；**不代表编者背书**。
- 相关项目主界面：`未来氢内爆汽车` 项目内的 `AAA_未来氢内爆汽车_主界面.html`。
"""


def main():
    if os.path.exists(DST):
        os.remove(DST)
        print(f"[覆盖] 已删除旧 zip")

    total_src = 0
    total_zip = 0
    missing = []

    with zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        # 0) 索引说明
        zf.writestr("00_资料包说明.md", build_readme())
        print("[加入] 00_资料包说明.md")

        for src_rel, zip_name in FILES:
            src_abs = os.path.join(SRC, src_rel.replace("/", os.sep))
            if not os.path.isfile(src_abs):
                missing.append(src_rel)
                continue
            size = os.path.getsize(src_abs)
            total_src += size
            # 用 UTF-8 标志位写中文名（zipfile 默认会设 0x800 flag）
            zf.write(src_abs, zip_name)
            total_zip += zf.getinfo(zip_name).compress_size

    print(f"输出：{DST}")
    print(f"文件数：{len(FILES) - len(missing)} / {len(FILES)}（另加说明 1 份）")
    print(f"原始总大小：{total_src / 1024 / 1024:.2f} MB")
    print(f"压缩后（不含说明）：{total_zip / 1024 / 1024:.2f} MB")
    print(f"压缩率：{100 * total_zip / total_src:.1f}%")
    if missing:
        print("\n缺失文件：")
        for m in missing:
            print("  ", m)
    else:
        print("\n✅ 全部文件已打包，无缺失")

    # 复验：读回 zip 清单
    print("\n=== zip 清单复验 ===")
    with zipfile.ZipFile(DST, "r") as zf:
        bad = zf.testzip()
        print(f"完整性检查：{'OK' if bad is None else '损坏：' + str(bad)}")
        names = zf.namelist()
        print(f"清单条数：{len(names)}")
        for n in sorted(names):
            print(f"  {zf.getinfo(n).file_size:>10d}  {n}")


if __name__ == "__main__":
    main()
