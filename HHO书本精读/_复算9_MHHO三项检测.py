# -*- coding: utf-8 -*-
"""
_复算9 · MHHO 三项检测的关键数字独立复算
=========================================================================
对应文档：HHO书本精读/05_三项检测的第三方文献检索_要不要先送检.md
           §2.3（2.5倍液氢的算术矛盾）
           §4.2（液化点 -178 ℃ 与"混合气"身份的冲突）

原则：凡数字必独立复算。本脚本不依赖任何外部库。
物理常数取教科书值，来源写在每项后面。
=========================================================================
"""
import math

LINE = "=" * 74
SUB = "-" * 74

print(LINE)
print("  _复算9 · MHHO 三项检测关键数字独立复算")
print(LINE)

# -------------------------------------------------------------------------
# 数据（教科书值，1 atm）
# -------------------------------------------------------------------------
T_O2_BOIL_C = -183.0     # O2 正常沸点（1 atm）    ℃
T_H2_BOIL_C = -253.0     # H2 正常沸点（1 atm）    ℃
DHVAP_O2 = 6820.0        # O2 汽化热              J/mol
R = 8.314                # 气体常数               J/(mol·K)

RHO_LIQ_H2 = 70.8        # 液氢密度（20.4 K）      kg/m3
M_H2O = 18.0             # 水摩尔质量             g/mol
M_H2 = 2.016
M_O2 = 32.00
VM = 22.414              # 标准摩尔体积（0 ℃,1 atm） L/mol

T_MHHO_CLAIM_C = -178.0  # MHHO/Ohmasa 气主张的液化点 ℃

print("\n【输入数据】")
print(f"  O2 沸点（1 atm）      = {T_O2_BOIL_C:.1f} ℃  = {T_O2_BOIL_C+273.15:.2f} K")
print(f"  H2 沸点（1 atm）      = {T_H2_BOIL_C:.1f} ℃  = {T_H2_BOIL_C+273.15:.2f} K")
print(f"  O2 汽化热             = {DHVAP_O2:.0f} J/mol")
print(f"  液氢密度              = {RHO_LIQ_H2:.1f} kg/m3")
print(f"  MHHO 主张液化点       = {T_MHHO_CLAIM_C:.1f} ℃  = {T_MHHO_CLAIM_C+273.15:.2f} K")


# =========================================================================
print("\n" + LINE)
print("  复算 A · 液化点：H2:O2=2:1 混合气在常压下根本不会比纯 O2 先液化")
print(LINE)
print("""
  原理：混合理想气体不"共同液化"，而是**分馏**——
        先凝沸点高的组分（O2），此时 O2 的分压只有总压的 1/3，
        所以它的冷凝温度**比纯 O2 更低**，不是更高。
""")

T_O2_K = T_O2_BOIL_C + 273.15
# Clausius-Clapeyron: ln(P2/P1) = -(dHvap/R)(1/T2 - 1/T1)
# 求 O2 在分压 P2 下的沸点 T2
for frac, label in [(1.0, "纯 O2（分压 1 atm）"),
                    (1.0 / 3.0, "2:1 混合气中的 O2（分压 1/3 atm）")]:
    lnP = math.log(frac)
    inv_T2 = 1.0 / T_O2_K + lnP / (-DHVAP_O2 / R)
    T2 = 1.0 / inv_T2
    print(f"  {label}")
    print(f"    → 冷凝温度 = {T2:.2f} K = {T2-273.15:.1f} ℃")

# 混合气中 O2 的分馏点
lnP = math.log(1.0 / 3.0)
inv_T2 = 1.0 / T_O2_K + lnP / (-DHVAP_O2 / R)
T_frac_K = 1.0 / inv_T2
T_frac_C = T_frac_K - 273.15

print(f"\n  ★ 混合气开始液化温度 ≈ {T_frac_C:.1f} ℃")
print(f"  ★ MHHO 主张          = {T_MHHO_CLAIM_C:.1f} ℃")
print(f"  → 主张值比混合气分馏点 **高 {T_MHHO_CLAIM_C - T_frac_C:.1f} ℃**")
print(f"  → 主张值比纯 O2 沸点    **高 {T_MHHO_CLAIM_C - T_O2_BOIL_C:.1f} ℃**")
print("""
  🔴 判定：
     要在常压下"更早液化"，只可能是**总压更高**，或**存在第三种物质**。
     一个 H2+O2 混合气，不可能在 1 atm 下比纯 O2 更早凝。
""")

# =========================================================================
print("\n" + LINE)
print("  复算 B · 反推：-178 ℃ 若要成立，需要多大压力？")
print(LINE)

T_claim_K = T_MHHO_CLAIM_C + 273.15
# 反解 O2 需要的分压
lnP_need = -DHVAP_O2 / R * (1.0 / T_claim_K - 1.0 / T_O2_K)
P_need_atm = math.exp(lnP_need)
P_total_atm = P_need_atm * 3.0   # O2 占 1/3

print(f"  要让 O2 在 {T_MHHO_CLAIM_C:.1f} ℃ 冷凝，所需 O2 分压 = {P_need_atm:.3f} atm")
print(f"  O2 占混合气 1/3 → 所需总压 = {P_need_atm:.3f} × 3 = **{P_total_atm:.2f} atm**")
print(f"  换算成 MPa：{P_total_atm * 0.101325:.2f} MPa")
print("""
  ★ 这条给出了一个**精确且可证伪**的判据：
     - 若 Omasa 的测试在 **≈1 atm** 下做 → -178 ℃ **不成立**（与混合气身份冲突）
     - 若在 **≈4.8 atm（0.49 MPa）** 下做 → -178 ℃ 可以是**分压效应**，
       **不需要任何新物种**，问题自动关闭
     - 若他报的压力**两者都不是** → 需要解释第三种物质

  🔴 注意：0.49 MPa 恰好落在**工业常见的中低压范围**内（气瓶、车载储气都在几 MPa 量级），
     所以"加压导致读数变化"是**最容易发生的平凡解释**，必须先排除。
""")

# =========================================================================
print("\n" + LINE)
print("  复算 C · 「1 m3 液 MOH 含 2.5 倍于液氢的 H2 质量」")
print(LINE)

target = 2.5 * RHO_LIQ_H2
max_frac = M_H2 / M_H2O          # H2 质量分数上限（全水都是 H2 时的极限）

print(f"  液氢密度                      = {RHO_LIQ_H2:.1f} kg/m3")
print(f"  2.5 倍 → 需含 H2              = {target:.1f} kg-H2/m3")
print(f"\n  若 MOH 真是 HHO 混合物，其 H2 质量分数上限：")
print(f"     H2/H2O = {M_H2:.3f}/{M_H2O:.1f} = {max_frac*100:.2f}%   ← 即使按纯水的极限算")
print(f"  所需密度 = {target:.1f} / {max_frac:.4f} = **{target/max_frac:.0f} kg/m3**")
print(f"\n  ★ 对照 MHHO 材料里出现过的三个密度值：")
for v, note in [(517.2, "Omasa 材料（03 判定复算应 ≈425）"),
                (1503.0, "同材料另一处"),
                (target / max_frac, "★ 本复算：要满足'2.5 倍液氢'所需值")]:
    print(f"     {v:>8.1f} kg/m3   ← {note}")
print(f"  → 所需值与材料自报的 517.2 相差 **{(target/max_frac)/517.2:.2f} 倍**")
print("""
  🔴 判定：
     "2.5 倍于液氢的 H2 质量" 与 "密度 517.2" 不能同时成立。
     而材料**从未算过"H2 质量分数上限 11.11%"这一步** ——
     这正是 11 汇总 判据三说的："不要看它算错了什么，要看它没算什么"。
""")

# =========================================================================
print("\n" + LINE)
print("  复算 D · 「1 L 液 MOH = 1868 L 气」—— 这个数字的真正来源")
print(LINE)

# 2:1 H2:O2 混合气的平均分子量与密度
M_mix = (2 * M_H2 + 1 * M_O2) / 3
rho_mix = M_mix / VM                      # g/L
print(f"  H2:O2 = 2:1 混合气平均分子量 = (2×{M_H2} + {M_O2})/3 = {M_mix:.3f} g/mol")
print(f"  0 ℃,1 atm 密度            = {M_mix:.3f} / {VM} = {rho_mix:.4f} g/L")
print(f"  ★ 对照 Nature 2026 论文实测 HHO 密度 0.536 g/L → 吻合度 {abs(rho_mix-0.536)/0.536*100:.1f}% 偏差 ✅")

vol_per_L = 1868.0
rho_implied_gL = vol_per_L * rho_mix          # g/L
rho_implied = rho_implied_gL                   # 1 g/L = 1 kg/m3
print(f"\n  「1 L 液 = {vol_per_L:.0f} L 气」隐含的液相密度：")
print(f"     = {vol_per_L:.0f} L × {rho_mix:.4f} g/L = {rho_implied_gL:.1f} g/L = **{rho_implied:.0f} kg/m3**")

# 反过来：1 kg 水完全电解得多少气？
n_h2o = 1000.0 / M_H2O
n_gas = n_h2o + n_h2o / 2.0      # H2O → H2 + 0.5 O2
V_gas = n_gas * VM
print(f"\n  ★ 反向验证：1 kg(=1 L) 水完全电解")
print(f"     1000/{M_H2O:.1f} = {n_h2o:.2f} mol H2O")
print(f"     → {n_h2o:.2f} mol H2 + {n_h2o/2:.2f} mol O2 = {n_gas:.2f} mol 气")
print(f"     → {n_gas:.2f} × {VM} = **{V_gas:.0f} L**  (0 ℃,1 atm)")
print(f"  ★ 与 MHHO 材料写的 1868 L 相差仅 {abs(V_gas-1868)/1868*100:.1f}% → **实质相等**")
print("""
  🔴 判定（这是本次复算最重要的发现）：
     "1868" 不是"MOH 的物性" —— 它是**化学计量数**，
     即"1 L（约1 kg）水完全电解所得的气体体积"。

     两条推论：
       ① 若材料的意思是"1 L 液态 MOH 汽化得 1868 L 气"，
          则隐含密度 = 1000 kg/m3，**恰好是水的密度**，
          而非它自报的 517.2 / 1503；
       ② 若材料只是把"水电解的气量"搬来当 MOH 的数据，
          则这个数字**与 MOH 无关**，是张冠李戴。

     无论哪种，都指向同一件事：
     ★ 这些"物性数字"更像是**水的数据**（或从水推出来的数），
       而不是某个"新物种"的独立测量结果。
""")

# =========================================================================
print("\n" + LINE)
print("  复算总表")
print(LINE)
rows = [
    ("A", "混合气常压分馏点",            f"{T_frac_C:.1f} ℃",        "低于纯 O2 的 -183 ℃ → 更晚液化"),
    ("A", "主张值 -178 ℃ 高出分馏点",     f"{T_MHHO_CLAIM_C-T_frac_C:.1f} ℃", "❌ 常压下不可能"),
    ("B", "-178 ℃ 成立所需总压",          f"{P_total_atm:.2f} atm",   "≈0.49 MPa，必须先问压力"),
    ("C", "2.5 倍液氢所需密度",           f"{target/max_frac:.0f} kg/m3", "❌ 与自报 517.2 差 3.1 倍"),
    ("D", "1868 L 气/L 隐含密度",         f"{rho_implied:.0f} kg/m3",  "★ 恰为水的密度"),
    ("D", "1 kg 水电解产气",              f"{V_gas:.0f} L",           "★ 与 1868 实质相等"),
]
print(f"  {'项':<3}{'复算内容':<26}{'结果':<20}{'判定'}")
print("  " + SUB[:70])
for a, b, c, d in rows:
    print(f"  {a:<3}{b:<26}{c:<20}{d}")
print(LINE)
print("  结论：三项检测中，'密度/2.5倍液氢' 是纯算术题（本脚本即可否）；")
print("        '液化点'的先决条件是'测试压力'（免费可问）；")
print("        真正必须花钱的只有 '液化后成分' 与 '拉曼新谱线' 两项。")
print(LINE)
