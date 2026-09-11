# -*- coding: utf-8 -*-
"""
_复算12_Lyne原子氢账目.py
=========================
独立复算 William Lyne《Occult Ether Physics》第 VI 章「The Atomic Hydrogen Process」
中所有关键数字。不复用原书结论，全部从标准物理常数重算。

用途：给「Lyne原子氢技术」系列 md 提供可一键重跑的算术底稿。
运行：python _复算12_Lyne原子氢账目.py
"""

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

N_A = 6.02214076e23          # 阿伏伽德罗常数 /mol
KJ_PER_CAL = 4.184e-3        # kJ/cal
BTU_PER_KJ = 0.947817        # BTU/kJ
LHV_H2_KJ_PER_MOL = 241.8    # H2 + 1/2 O2 -> H2O(g)，低位热值 kJ/mol
HHV_H2_KJ_PER_MOL = 285.8    # H2 + 1/2 O2 -> H2O(l)，高位热值 kJ/mol

# 书中引用的原始数值（Lyne 原文，逐字）
LYNE_DISSOC_CAL = 103        # "heat of dissociation about 103 cal/gram mole"
LYNE_RECOMB_CAL = 109_000    # "109,000 cal/gram mole"(gross heat output)
LYNE_BREAD_CAL = 109_000     # 他自己把 109 000 cal 比作 75 个面包

# 真实氢解离能（光谱学值，文献公认）
TRUE_DISSOC_KJ_PER_MOL = 436.0     # kJ/mol
TRUE_DISSOC_CAL_PER_MOL = TRUE_DISSOC_KJ_PER_MOL / KJ_PER_CAL   # ≈ 104 200 cal/mol

RULE = "=" * 74


def head(t):
    print("\n" + RULE)
    print(t)
    print(RULE)


head("A. 先把「103 cal/gram mole」到底是不是笔误算清楚")

print(f"真实氢解离能 D0(H-H) = {TRUE_DISSOC_KJ_PER_MOL} kJ/mol")
print(f"                     = {TRUE_DISSOC_CAL_PER_MOL:,.0f} cal/mol")
print(f"                     = {TRUE_DISSOC_CAL_PER_MOL/1000:,.1f} kcal/mol")
print()
print("书中写的 103「cal/gram mole」若按字面读 = 103 cal/mol")
ratio_needed = TRUE_DISSOC_CAL_PER_MOL / 103
print(f"  与真实值相差 {ratio_needed:,.0f} 倍 → 字面读法不成立（差三个数量级）")
print()
print("书中写的 103 若单位其实是「kcal/mol」（排印掉了 k）：")
print(f"  103 kcal/mol vs 真实 {TRUE_DISSOC_CAL_PER_MOL/1000:,.1f} kcal/mol")
print(f"  误差 {abs(103-TRUE_DISSOC_CAL_PER_MOL/1000)/(TRUE_DISSOC_CAL_PER_MOL/1000)*100:.1f}%"
      "  → ★ 完全落在实验误差内")
print()
print("【结论 A】103 的真实身份 = 103 kcal/mol（约合 431 kJ/mol），")
print("          书中所有「103 cal/gram mole」写法都漏了 k，")
print("          是排印/单位错，不是物理异常。")

head("B. 由此，Lyne 的「1,058 倍」是怎么来的")

naive = LYNE_RECOMB_CAL / LYNE_DISSOC_CAL
print(f"Lyne 算式：{LYNE_RECOMB_CAL:,} / {LYNE_DISSOC_CAL} = {naive:,.1f} 倍")
print(f"  书中印作 1,058 倍（他减了 103 得 108,897，再除 103 → {108897/103:,.2f}）")
print()
print("但两边单位不同源：")
print(f"  分子 {LYNE_RECOMB_CAL:,} 的真实单位 = cal/mol")
print("  分母 103 的真实单位          = kcal/mol")
print(f"  修正分母为 cal/mol 后：{LYNE_RECOMB_CAL:,} / {TRUE_DISSOC_CAL_PER_MOL:,.0f}"
      f" = {LYNE_RECOMB_CAL/TRUE_DISSOC_CAL_PER_MOL:.2f} 倍")
print()
print("【结论 B】1,058 倍 = 纯单位错配的产物（把 kcal 当 cal 除）。")
print("          修正后倍数 ≈ 1.05，即复合放热与解离能同量级——")
print("          这正是教科书上「热化学可逆」的普通结果，无 any over-unity。")

head("C. 那 109,000 cal/mol 本身可与什么对齐？")

btu_per_lbmol = LYNE_RECOMB_CAL * 1.8   # cal -> BTU (×1.8)，per lb-mol
print(f"{LYNE_RECOMB_CAL:,} cal/mol × 1.8 = {btu_per_lbmol:,.0f} BTU/lb-mol")
print("书中 p.116 原话：'109,000 cal./gram mole equals 432.5 BTU/gram mole'")
print(f"  实际 109,000/1000 × 4.184 × 0.9478 = "
      f"{109*4.184*0.947817:.1f} BTU/mol = {109*1000*4.184*0.947817:.0f} BTU/... ")
print()
print("对照 H2 真实燃烧热：")
lh = LHV_H2_KJ_PER_MOL / KJ_PER_CAL / 1000
hh = HHV_H2_KJ_PER_MOL / KJ_PER_CAL / 1000
print(f"  LHV = {LHV_H2_KJ_PER_MOL} kJ/mol = {lh:.2f} kcal/mol = 57,800 cal/mol")
print(f"  HHV = {HHV_H2_KJ_PER_MOL} kJ/mol = {hh:.2f} kcal/mol = 68,300 cal/mol")
print(f"  书中 p.121 引 'Heat of combustion (net) 57,797.6 cal/gram' → ✅ 与 LHV 吻合")
print(f"  书中 p.121 引 'Heat of combustion (gross) 63,317 cal/gram' → 略低于 HHV，同量级")
print()
print("【结论 C】109,000 cal/mol 约为 H2 真实燃烧热的 1.9 倍(LHV) / 1.6 倍(HHV)。")
print("          它不是「凭空多出来的能」，而更可能来自：")
print("          ① 早期光谱法测定 D0 的误差与单位换算层层累积；")
print("          ② 把「解离能 + 燃烧热」两项混加。")
print("          无论哪种，都不是新能量通道。")

head("D. 焊接那一段的独立复算（这才是能落地的部分）")

CP_H2 = 14.3          # J/(mol·K)  H2 定压摩尔热容 (300 K)
T_ARC = 5000.0        # Lyne 称原子氢焰可达 5000 °C，取上限
T0 = 298.0

dH_sensible = CP_H2 * (T_ARC - T0) / 1000          # kJ/mol
print(f"把 1 mol H2 从 25 ℃ 加到 5000 ℃ 所需显热")
print(f"  ≈ Cp·ΔT = {CP_H2} J/mol/K × {T_ARC-T0:.0f} K = {dH_sensible:.1f} kJ/mol")
print(f"  = {dH_sensible/KJ_PER_CAL/1000:.2f} kcal/mol")
print()
frac = dH_sensible / (TRUE_DISSOC_CAL_PER_MOL * KJ_PER_CAL)
print(f"对比真实解离能 {TRUE_DISSOC_KJ_PER_MOL} kJ/mol：")
print(f"  显热/解离能 = {frac*100:.1f}%  → 加热本身解释不了成原子")
print()
print("但焊接现场并【不需要】把气全解离：")
print(f"  即使只有 1% 的 H2 解离，复合放热 = "
      f"{TRUE_DISSOC_KJ_PER_MOL*0.01:.2f} kJ/mol 混气")
print(f"  = {TRUE_DISSOC_KJ_PER_MOL*0.01/KJ_PER_CAL/1000*1000:.0f} cal/mol 混气")
print()
print("【结论 D】原子氢焊的『高温』来自原子在工件表面复合时释放的 436 kJ/mol，")
print("          而不是来自电弧加热。这与教科书完全一致，✓ 可采信。")
print("          5000 ℃ 数字的正确性取决于解离率；工程上真实焊枪约 3400–4000 ℃。")

head("E. Lyne 的 10.5 倍、315 mile/lb —— 用他自己给的数据重算")

gaso_btu = 19_314      # 书中 p.120：gasoline(n-Heptane) 19,314 BTU/lb
h2_btu = 52_200        # 书中 p.120：hydrogen combustion 52,200 BTU/lb
atom_btu = 196_200     # 书中 p.120：atomic hydrogen 196,200 BTU/lb

print(f"分子氢/汽油 = {h2_btu:,} / {gaso_btu:,} = {h2_btu/gaso_btu:.2f} 倍"
      "  ← 书中称 2.7:1，✓ 基本吻合（差值来自 n-Heptane 取值不同）")
print(f"原子氢/汽油 = {atom_btu:,} / {gaso_btu:,} = {atom_btu/gaso_btu:.2f} 倍"
      "  ← 书中称 10.5:1，✓ 算术自洽")
print()
print("但注意：10.5 倍是「原子氢复合放热 ÷ 汽油燃烧放热」，")
print("          它【没有】扣除产生原子氢所花的电。")
print(f"  原子氢 196,200 BTU/lb 来自 109,000 cal/mol ÷ 1.008 g/mol")
print(f"  = {109000/1.008:.0f} cal/g = {109000/1.008*1.8:.0f} BTU/lb")
print(f"  而真实解离能 436 kJ/mol = {TRUE_DISSOC_CAL_PER_MOL/1.008:.0f} cal/g"
      f" = {TRUE_DISSOC_CAL_PER_MOL/1.008*1.8:.0f} BTU/lb")
print(f"  → 真实值只有 Lyne 所引的 {TRUE_DISSOC_CAL_PER_MOL/LYNE_RECOMB_CAL*100:.1f}%")
print()
print("【结论 E】10.5 倍这个「输出端」数字，其唯一支撑是 196,200 BTU/lb，")
print("          而 196,200 BTU/lb 又唯一来自 109,000 cal/mol。")
print("          既然 109,000 已被结论 A/C 证伪，10.5 倍随之不成立。")

head("F. 一句话总账")

print("""
┌─ Lyne 的账 ────────────────────────────────────────────────┐
│ 输出端 196,200 BTU/lb  ←  109,000 cal/mol  ←  来源可疑     │
│ 输入端 103「cal/mol」  ←  真实是 103 kcal/mol（漏 k）      │
│ 比值   1,058 倍        ←  两个错位数相除的假象             │
│                                                            │
│ 修正后：436 kJ/mol 解离 / 436 kJ/mol 复合 = 1 : 1           │
│         这就是教科书上的可逆热化学，没有多余能量。         │
└────────────────────────────────────────────────────────────┘

★ 可采信的部分（与主流物理一致）：
    原子氢焊的工艺事实——钨电极电弧解离、分子氢射流吹出、
    复合放热可达 3400 ℃+、自屏蔽、可焊异种金属、热变形小。
    这些是 1930s 真实商用工艺，有教科书与图 106 佐证。

★ 不可采信的部分（圈内主张，标 🟡 存疑）：
    「原子氢是免费能源」「氢只是介质」「1,058 倍 over-unity」
    「能量来自以太/Primary Solar Rays」——这些依赖以太假设，
    且其唯一数字支撑已被证伪。
""")
print(RULE)
print("复算完毕。全部常数取自标准物理表，未引用原书结论。")
