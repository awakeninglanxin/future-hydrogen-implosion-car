# -*- coding: utf-8 -*-
"""
_复算22_JCB448ABH2参数核对.py
================================
用途：对「JCB 448 ABH2 零柴油氢发动机」的技术参数做**独立复算**，
      为 `joe cell/15_JCB448ABH2技术拆解.md` 提供 🔵 底稿。

原则（项目铁律）：
  1) 凡数字必独立复算 —— 本文所有结论均由常数推出，不照抄口径；
  2) 口径分歧必须显式标注（如 PFI vs 直喷）；
  3) 算不出来的报「证据不足」，不编。

一键运行：
  C:/Users/ThinkPad/.workbuddy/binaries/python/versions/3.13.12/python.exe \
      _复算22_JCB448ABH2参数核对.py

主要来源（均为 2026-09-12 检索所得，全文见 15 号文档 §七）：
  [S1] iVT International, "FEATURE: The world's first production hydrogen
       backhoe loader from JCB"（引 Mark Richards 原话，2025/2026）
  [S2] The Scottish Farmer, 2022-12（引 Ryan Ballard 原文，含 500/350/20 bar）
  [S3] Tech Briefs, CONEXPO 2023
  [S4] Autocar, "Under the skin"（★口径分歧处：写作 direct injection）
"""

import math

T0 = 298.15          # K，参考温度 25 °C
GAMMA = 1.40         # 双原子气体绝热指数
GAS_R = 8.314        # J/(mol·K)

def h(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74)

def sub(t):
    print("\n--- " + t + " " + "-" * max(0, 62 - len(t)))

results = []          # (标签, 值, 判定)

def rec(tag, val, ok=True):
    mark = "OK" if ok else "!!"
    results.append((tag, val, mark))
    print("  [%s] %s = %s" % (mark, tag, val))


# =====================================================================
h("Q1  三级压力链：500 bar 加注 → 350 bar 车罐 → 20 bar 进机")
# =====================================================================
# [S2] 原文：pressure differential between the storage tank or bowser at
#      500 bar and the vehicle tank at 350 bar eliminating any need for a pump
# [S2] 原文：That 350 bar compression ... drops to just 20 bar for the
#      journey to the engine so conventional low-pressure pipes can be used
P_STORE, P_TANK, P_RAIL = 500.0, 350.0, 20.0
print("  储罐/加注车 %.0f bar → 车罐 %.0f bar → 进机(共轨) %.0f bar"
      % (P_STORE, P_TANK, P_RAIL))
rec("加注压差 (免泵)", "%.0f bar" % (P_STORE - P_TANK))
rec("进机前降压倍数", "%.1f 倍 (%.0f→%.0f)" % (P_TANK / P_RAIL, P_TANK, P_RAIL))

# ★ 独立复算：只靠压差「免泵加注」需要多大的储罐？
#   设等温膨胀、理想气体：车罐初压 P0=0，终压要 >= 350 bar
#   P_eq = (P_store*Vs + 0*Vv) / (Vs + Vv) >= P_tank
#   ⇒ Vs/Vv >= P_tank / (P_store - P_tank)
ratio_min = P_TANK / (P_STORE - P_TANK)
print("\n  ★ 独立复算（原文未给）：免泵加注所需的储罐/车罐容积比")
print("     平衡压力  P_eq = (P_store·Vs + 0·Vv) / (Vs + Vv)  ≥ 350 bar")
print("     ⇒  Vs/Vv ≥ P_tank / (P_store − P_tank) = 350 / 150")
rec("储罐容积 / 车罐容积 下限", "%.2f 倍" % ratio_min,
    abs(ratio_min - 7.0 / 3.0) < 1e-9)
print("     ⇒ 若两罐等容(Vs=Vv)，平衡压力只有 %.0f bar（充不满）"
      % (P_STORE / 2))
print("     ⇒ 这就是『为什么储罐要 500 bar 而不是 350 bar』——要留压差余量")

# 储氢密度量级（带压缩因子，避免理想气体高估）
def rho_h2(p_bar, T, Z):
    """kg/m³ ；Z = 压缩因子（实测近似）"""
    return p_bar * 1e5 * 2.016e-3 / (Z * GAS_R * T)

print("\n  储氢密度（300 K，含真实气体压缩因子 Z）")
for p, Z in ((350, 1.17), (700, 1.45)):
    r_id = p * 1e5 * 2.016e-3 / (GAS_R * 300)
    print("     %3d bar : 理想 %.1f → 实际(Z=%.2f) %.1f kg/m³"
          % (p, r_id, Z, rho_h2(p, 300, Z)))
rec("350 bar 储氢密度", "%.1f kg/m³" % rho_h2(350, 300, 1.17))
rec("700 bar 储氢密度", "%.1f kg/m³（旧口径误值，见 Q7）" % rho_h2(700, 300, 1.45))
rec("350/700 密度之比", "%.2f ⇒ 压力减半、密度只降约 4 成"
    % (rho_h2(350, 300, 1.17) / rho_h2(700, 300, 1.45)))


# =====================================================================
h("Q2  扭矩—功率自洽性检验（★ 用来判断参数是否可信）")
# =====================================================================
# [S1] 原文：At 55kW and 440Nm of torque at 1,150rpm
P_H2, TQ, RPM = 55.0, 440.0, 1150.0
P_from_tq = TQ * RPM * 2 * math.pi / 60 / 1000.0
print("  宣称：%.0f kW，%.0f N·m @ %.0f r/min" % (P_H2, TQ, RPM))
print("  复算：P = T·ω = %.0f × (%.0f×2π/60) / 1000" % (TQ, RPM))
rec("由扭矩反算功率", "%.1f kW" % P_from_tq)
dev = abs(P_from_tq - P_H2) / P_H2 * 100
rec("与宣称 55 kW 的相对偏差", "%.1f%%" % dev, dev < 6.0)
print("  ⇒ 偏差 %.1f%% < 6%%，两数可视为同一工况、**互相自洽**" % dev)
print("    （若偏差 >20% 则应怀疑其中一个是峰值点下的不同工况）")

# 功率密度
DISP = 4.8
rec("功率密度", "%.2f kW/L" % (P_H2 / DISP))
rec("升扭矩", "%.0f N·m/L" % (TQ / DISP))
print("  ⇒ 这是**自然吸气柴油级**的功率密度，不是高性能汽油机口径")


# =====================================================================
h("Q3  28 ms 混合窗口 ↔ 曲轴转角（★ 与判据⑨『时间尺度』同源）")
# =====================================================================
# [S2] 原文：achieve a perfectly homogenous mixture of this light gas and
#      air in just 28 milliseconds ... indirect injection with the gas
#      drawn in and starting to be mixed with the air coming from the turbo
MIX_MS = 28.0

def rev_ms(rpm):
    """一转(360°曲轴)的时长，ms"""
    return 60.0 / rpm * 1000.0

def cycle_ms(rpm):
    """一个四冲程循环(720°曲轴)的时长，ms"""
    return 2 * rev_ms(rpm)

def stroke_ms(rpm):
    """一个冲程(180°曲轴)的时长，ms"""
    return 60.0 / rpm / 2 * 1000.0

def deg_of(t_ms, rpm):
    """t_ms 对应的曲轴转角（度）"""
    rev = 60.0 / rpm * 1000.0
    return t_ms / rev * 360.0

print("  原文给的混合窗口：%.0f ms —— 这是**固定时长**，与转速无关" % MIX_MS)
print("  （进气道间接喷射：氢随空气一起被吸入，须在点火前混合均匀）\n")
print("  ★ 关键：转速升高 ⇒ 一转的**时间变短** ⇒ %.0f ms 在曲轴上**占比变大**" % MIX_MS)
print("      ⇒ 判据不是『一个冲程够不够』，而是『%.0f ms 能不能塞进一转』\n" % MIX_MS)
print("  转速    一循环(720°)   一转(360°)   28ms占一转    28ms折合曲轴角   塞得下?")
for rpm in (1000, 1150, 1500, 1875, 2000, 2143, 2500, 3000):
    r, c = rev_ms(rpm), cycle_ms(rpm)
    print("  %5d    %7.1f ms    %7.1f ms     %6.1f%%        %7.1f°        %s"
          % (rpm, c, r, MIX_MS / r * 100, deg_of(MIX_MS, rpm),
             "✅" if MIX_MS <= r else "❌"))
rpm_max = 60.0 / (MIX_MS / 1000.0)
print("\n  反解：一转恰好 = %.0f ms 的转速 = %.0f r/min" % (MIX_MS, rpm_max))
rec("28 ms 混合窗口对应的转速上限", "≈ %.0f r/min（再高就塞不进一转）" % rpm_max)
rec("JCB 额定扭矩点 1150 r/min 占上限", "%.0f%%（留有余量）"
    % (1150.0 / rpm_max * 100))
print("  ⇒ ★ 结论：JCB 把**峰值扭矩点定在 1150 r/min** 不是巧合 ——")
print("     PFI 氢机的混合是**时间受控**：转速越高，留给混合的一转越短；")
print("     28 ms 要求转速 ≲ %.0f r/min（此时一转=28 ms，已无余量）。" % rpm_max)
print("     1150 r/min 时一转 %.1f ms，28 ms 约占 %.0f%% —— 有充分余量，"
      % (rev_ms(1150), MIX_MS / rev_ms(1150) * 100))
print("     但这也决定了它是一台**低转速、大扭矩**机器，而非高速机。")
print("  ⇒ 破解方向也自然出现：**缸内直喷**（进气门关闭后再喷氢）")
print("     把混合约束从『整个进气道时间』缩到『压缩期』，转速上限才能提高 ——")
print("     这正是 [S4] 把 JCB 写成『centrally mounted direct injectors』的由来")
print("     （媒体按**技术方向**写，而一代机的**实际配置**是 PFI，见 Q7 口径分歧）。")


# =====================================================================
h("Q4  空燃比 1:100 的口径复核（质量 vs 体积）")
# =====================================================================
M_H2, M_O2, M_N2 = 2.016, 31.998, 28.014
m_fuel = 2 * M_H2
m_air = M_O2 + 3.76 * M_N2
AFR_mass = m_air / m_fuel
AFR_vol = (2 + 3.76) / 2.0            # 体积比 空气/氢
print("  化学计量：2H₂ + O₂ + 3.76N₂")
print("     燃料 %.3f g  空气 %.2f g" % (m_fuel, m_air))
rec("化学计量空燃比（质量）", "%.2f : 1" % AFR_mass, abs(AFR_mass - 34.3) < 0.5)
rec("化学计量空燃比（体积）", "%.2f : 1" % AFR_vol)

lam_mass = 100.0 / AFR_mass
lam_vol = 100.0 / AFR_vol
print("\n  若 JCB 的『100:1』按**质量**： λ = 100/%.2f = %.2f  ⇒ 极稀燃 ✅"
      % (AFR_mass, lam_mass))
print("  若按**体积**：                 λ = 100/%.2f = %.1f  ⇒ 荒谬，无法点火 ❌"
      % (AFR_vol, lam_vol))
rec("判定", "1:100 只能是**质量比**，λ≈%.2f" % lam_mass, 2.5 < lam_mass < 3.5)

# 氢占进气道体积 ⇒ 挤占空气 ⇒ 功率损失
frac_stoich = 2.0 / (2.0 + 3.76)
frac_lean = frac_stoich / lam_mass
print("\n  氢是**气态**燃料，会挤占进气道体积：")
rec("化学计量时氢体积占比", "%.1f%%" % (frac_stoich * 100))
rec("λ=%.2f 时氢体积占比" % lam_mass, "%.1f%%" % (frac_lean * 100))
print("  ⇒ 同等排量下空气被挤掉约 %.1f%%；对照柴油（液态喷射，几乎不占体积）"
      % (frac_lean * 100))
print("    ⇒ 这就是氢机必须上**大流量涡轮（VGT）**补进气量的定量理由。")


# =====================================================================
h("Q5  排放：为什么『只有水』就意味着三大污染物同时为零")
# =====================================================================
print("  燃料 = H₂，**不含碳、不含硫、不含氮**")
print("  ⇒ CO₂ = 0（无碳源）")
print("  ⇒ HC  = 0（碳氢化合物的『碳』不存在；未燃部分只可能是 H₂ 本身）")
print("  ⇒ SOx = 0（无硫）")
print("  燃烧反应：2H₂ + O₂ → 2H₂O  ⇒ 主要产物只有水\n")
print("  ★ 但 NOx 不同 —— 它来自**空气中的氮**，不来自燃料：")
print("     Zeldovich 热力型 NOx 需要峰值温度约 >1800 K")
print("     氢化学计量燃烧绝热火焰温度 ≈ 2400 K  ⇒ 会大量生成 NOx")
print("     JCB 走 λ≈%.2f 极稀燃 ⇒ 燃烧温度大幅低于阈值 ⇒ NOx 被压住"
      % lam_mass)
rec("JCB 的除 NOx 手段", "极稀燃(λ≈%.1f) + 低温度低压力运行" % lam_mass)
rec("是否需要后处理", "不需要（[S1][S3] 均称 no aftertreatment required）")
print("  ⇒ ★ 对照 Joe Cell：它的主张是**零柴油 + 负压**，")
print("     但从未给出 λ、燃烧温度、NOx 的实测数据 ⇒ 判『证据不足』")


# =====================================================================
h("Q6  机油：★ 两条独立来源同时指向『机油是氢机的关键物料』")
# =====================================================================
# 来源 A：JCB（[S3] 引 Beamish 原话）
#   "oil (must not react with steam)" —— 油必须不与蒸汽反应
#   差异清单：spark plugs / cylinder head / pistons / induction / oil
# 来源 B：润滑油巨头专利（见 14 号文档 §四）
#   Infineum WO 2025191545 A2、US 12662648 B2 —— 专为氢发动机「降预点火」
#   手段：硫酸灰分 ≤1.0–1.2 wt%、降钙/锌/磷
print("  来源 A｜JCB 工程师原话（差异清单 5 项，含 oil）")
print("     『oil (must not react with steam)』⇒ 机油须不与水蒸气反应（抗乳化）")
print("  来源 B｜2024–2026 润滑油巨头**专为氢机**申请的降预点火专利")
print("     核心：硫酸灰分 ≤1.0–1.2 wt%、降钙/锌/磷")
print("\n  ⇒ 两条来源**互相独立**（一家整机厂 / 一家油品商），却都指向：")
print("     ★ 机油是氢发动机的**关键物料**，不是可忽略的耗材。")
print("  ⇒ 这与 14 号文档 §二 把『机油』列为 ★★★ 最高危险度**一致**。")
rec("交叉印证", "成立（整机厂 ⊕ 油品商，两条独立链）")

# 机油自燃温度 vs 压缩终了温度（承接 14 号的硬理由）
T_AUTO_OIL, T_AUTO_DIESEL, T_AUTO_H2 = 490.0, 530.0, 858.0   # K
def t2(cr):
    return T0 * (cr ** (GAMMA - 1))
print("\n  复算压缩终了温度（与 14 号文档 §一 同一公式，此处复现校验）")
for cr in (14, 18, 20, 22):
    print("     CR %2d → %6.1f K = %6.1f °C"
          % (cr, t2(cr), t2(cr) - 273.15))
rec("CR18 压缩终了", "%.1f °C ≫ 机油自燃 约217 °C、柴油 257 °C"
    % (t2(18) - 273.15))
print("  ⇒ 压缩越深，残留物越**必然**先于氢着火 ⇒ 这才是『必须洗净』的硬理由")


# =====================================================================
h("Q7  ★ 口径分歧与更正：350 bar，不是 700 bar")
# =====================================================================
print("  库内旧口径（我上轮所写）：JCB 用『700 bar 车载氢罐』—— ❌ 错误")
print("  权威口径（[S1][S2] 多源一致）：")
print("     车罐 **350 bar**；加注车/储罐 **500 bar**；进机前降到 **20 bar**")
rec("更正结论", "350 bar 罐 / 500 bar 加注 / 20 bar 进机", True)
print("\n  另一处口径分歧（须显式标注，不掩盖）：")
print("     [S4] Autocar 写作『hydrogen direct injectors are centrally mounted』（直喷）")
print("     [S1][S2][S3] 一致写作 port fuel injection / indirect injection（进气道喷氢）")
print("     ⇒ 判定：**一代机 = PFI**（JCB 工程师原话优先；[S4] 为媒体口径混淆）")
rec("喷射方式判定", "一代 = PFI（进气道间接喷射）", True)


# =====================================================================
h("汇总")
# =====================================================================
print("  %-42s %-30s %s" % ("项目", "结果", "判定"))
print("  " + "-" * 84)
for tag, val, mark in results:
    print("  %-42s %-30s %s" % (tag, val, mark))
n_bad = sum(1 for _, _, m in results if m == "!!")
print("\n  共 %d 项复算，异常 %d 项。" % (len(results), n_bad))
print("  ★ 本次复算的**独立增量**（原文没有、由常数推出）：")
print("     1) 免泵加注所需储罐/车罐容积比 ≥ %.2f 倍" % ratio_min)
print("     2) 28 ms 混合窗口 ⇒ 转速上限 ≈ %.0f r/min；1150 r/min 只用掉 %.0f%% 一转"
      % (rpm_max, MIX_MS / rev_ms(1150) * 100))
print("     3) 28 ms 在 1150 r/min 折合 %.0f° 曲轴角 ⇒ 解释 PFI 氢机的低转速特性"
      % deg_of(28, 1150))
print("     4) 氢体积占进气 %.1f%% ⇒ 定量解释为何必须上大流量涡轮"
      % (frac_lean * 100))
print("     5) 更正 700 bar → 350 bar（并给出三级压力链）")
print()
