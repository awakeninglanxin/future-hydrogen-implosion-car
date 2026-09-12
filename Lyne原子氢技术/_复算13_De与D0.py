#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""★ 复算13：Lyne「1,058 倍」的真正机制 —— De 与 D0 是同一个量的两种定义。

【原文链条（全部来自 Lyne 自己引用）】
  Partington 1953 p.170      : "about 100 kcal per gram-molecule"          → 100 kcal/mol
  Van Nostrand 1976 p.1311   : "heat of dissociation about 103 cal/gram mole" → 应读作 103 kcal/mol
  Moelwyn-Hughes 1965 p.417  : "In kilocalories per mole, De is 109."       → De = 109 kcal/mol
  Langmuir (older text)      : "100,000 cal/gram mole liberated on recombination"

【假设】109 与 103 之差 = H2 的零点能（ZPE），即 De（电子解离能）vs D0（基态解离能）。
本脚本用 H2 光谱常数独立验证这一假设。
"""
import math

# ── H2 光谱常数（文献值）──────────────────────────────
OMEGA_E   = 4401.21   # cm^-1  谐振频率
OMEGA_E_XE= 121.336   # cm^-1  非谐性常数
D0_CM     = 36118.069 # cm^-1  基态解离能（从 v=0, J=0 起算）

# 换算因子：1 cm^-1 -> J/mol
H  = 6.62607015e-34
C  = 299792458.0
NA = 6.02214076e23
CM1_TO_J_MOL = H * C * 100 * NA          # = 11.96266 J/mol
J_TO_CAL     = 1.0 / 4.184
KCAL_PER_MOL = 1000 * J_TO_CAL           # 1 kcal/mol = 4.184 kJ/mol

def cm1_to_kcal(x):
    return x * CM1_TO_J_MOL * J_TO_CAL / 1000.0

print("=" * 76)
print("一、由 H2 光谱常数独立计算 De 与 D0（不引用 Lyne 的任何数字）")
print("=" * 76)

# 零点能 G(0) = omega_e/2 - omega_e*xe/4
zpe_cm = OMEGA_E/2 - OMEGA_E_XE/4
zpe_kcal = cm1_to_kcal(zpe_cm)

d0_kcal = cm1_to_kcal(D0_CM)

# 电子解离能 De = D0 + G(0)
de_cm = D0_CM + zpe_cm
de_kcal = cm1_to_kcal(de_cm)

print(f"H2 谐振频率      omega_e   = {OMEGA_E:>10.2f} cm^-1")
print(f"   非谐性常数    omega_e*xe= {OMEGA_E_XE:>10.3f} cm^-1")
print(f"   零点能        G(0)      = {zpe_cm:>10.2f} cm^-1 = {zpe_kcal:>7.2f} kcal/mol")
print()
print(f"   基态解离能    D0        = {D0_CM:>10.3f} cm^-1 = {d0_kcal:>7.2f} kcal/mol")
print(f"   电子解离能    De        = {de_cm:>10.3f} cm^-1 = {de_kcal:>7.2f} kcal/mol")
print()
print(f"★ De - D0 = {de_kcal - d0_kcal:>6.2f} kcal/mol  （= 零点能 {zpe_kcal:.2f}，吻合）")

print()
print("=" * 76)
print("二、与 Lyne 引用的两个数字对照")
print("=" * 76)
LYNE_D0_BOOK = 103.0   # kcal/mol（Van Nostrand 写作 "103 cal"，实为 103 kcal）
LYNE_DE_BOOK = 109.0   # kcal/mol（Moelwyn-Hughes "De is 109"）

print(f"{'量':<12}{'Lyne 引用':>12}{'独立计算':>12}{'偏差':>10}")
print("-" * 76)
print(f"{'D0':<12}{LYNE_D0_BOOK:>10.0f} kcal{d0_kcal:>10.2f} kcal{(LYNE_D0_BOOK-d0_kcal)/d0_kcal*100:>9.2f}%")
print(f"{'De':<12}{LYNE_DE_BOOK:>10.0f} kcal{de_kcal:>10.2f} kcal{(LYNE_DE_BOOK-de_kcal)/de_kcal*100:>9.2f}%")
print(f"{'De - D0':<12}{LYNE_DE_BOOK-LYNE_D0_BOOK:>10.0f} kcal{zpe_kcal:>10.2f} kcal{(6.0-zpe_kcal)/zpe_kcal*100:>9.2f}%")
print()
print("★ 两本书给的是【同一个键能的两种定义】，不是【输入】与【输出】。")
print("  Van Nostrand 的 103 = D0（基态解离能），单位漏了 k（实为 103 kcal/mol）")
print("  Moelwyn-Hughes 的 109 = De（电子解离能），单位写全（kcal/mol）")
print("  两者之差 = 零点能，是基态固有能量，不可提取。")

print()
print("=" * 76)
print("三、逐层放大：错误是怎么滚成 1,058 倍的")
print("=" * 76)

steps = [
    ("① 真实物理差",   de_kcal - d0_kcal, "kcal/mol", "De 与 D0 之差 = 零点能"),
    ("② Lyne 读作能量", 109.0 - 103.0,     "kcal/mol", "把同一定义的差当成『净输出』"),
    ("③ 单位漏 k 放大", 109000.0 - 103.0,  "cal/mol",  "分子按 cal，分母按 cal 读 103（少 1000 倍）"),
]
for name, v, unit, note in steps:
    print(f"  {name:<16} = {v:>12,.1f} {unit:<9} │ {note}")

print()
print(f"  Lyne 的算式 : 109,000 ÷ 103      = {109000/103:>8.1f} 倍")
print(f"  修正分母后  : 109,000 ÷ 103,000  = {109000/103000:>8.4f} 倍")
print(f"  真实物理比  : De ÷ D0            = {de_kcal/d0_kcal:>8.4f} 倍")
print()
print("  ★ 1,058 倍 = 【单位错配(×1000)】 × 【把 De-D0 当净输出】的复合产物。")
print("  ★ 修正单位后剩 1.058 倍 ≈ 1 —— 即热化学可逆，毫无奇迹。")

print()
print("=" * 76)
print("四、Lyne 自己是否察觉？—— 原文对照")
print("=" * 76)
quotes = [
    ("p.115", "I believe the true dissociation energy must be somewhere between the 103 calories and the 109 kcals./gram mole."),
    ("p.115", "the process was theoretically capable of producing 1,058 times the input energy. This is probably too high but it is definitely higher than all previous calculations."),
    ("p.121", "the '103 cal/gram mole' dissociation energy did not appear to be a typographical error or misprint, and should have been corrected by that time if discovered."),
    ("p.122", "since there appears to be no way the naked atoms could 'store' the 109,000 cal/gram mole. Where, exactly would this energy 'reside'?"),
]
for p, q in quotes:
    print(f"  [{p}] \"{q}\"")
print()
print("  ★ Lyne 在 p.115 明说『这大概太高了』，在 p.122 追问『这能量到底存在哪里？』")
print("    —— 他察觉了异常，却选择把它当作自己的论据。这是『选择性采信』。")

print()
print("=" * 76)
print("五、结论")
print("=" * 76)
print("""  Lyne 的错误可以精确表述为：
    · 他从 A 书取「输入」(Van Nostrand 的 103)，
      从 B 书取「输出」(Moelwyn-Hughes 的 109)，
    · 而这两个数其实是【同一个键能的两种理论定义】D0 与 De，
      相差的只是 H2 的零点能（本算独立算得 %.2f kcal/mol）,
    · 再加上 A 书的单位漏了 k，把差放大 1000 倍。

  → 错误源头在【Van Nostrand 百科编辑部】（1976 年版 p.1311 印的就是 "103 cal"），
    Lyne 是忠实引用；他自己的失误在于【跨来源拼接时未检查单位与定义的一致性】。""" % zpe_kcal)
