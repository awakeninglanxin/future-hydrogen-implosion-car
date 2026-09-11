# -*- coding: utf-8 -*-
"""复算 ⑥：Memo 426 的「7.4 µL 水/喷射循环」—— Meyer 唯一给出的定量运转指标"""
HHV_H2 = 285.8e3        # J/mol
n_per_L = 1000/18.015   # mol H2O per L
print("="*74); print("复算 ⑥  Memo 426：7.4 µL 水/循环 能否驱动 VW 1600cc 50hp @65mph")
print("="*74)
V = 7.4e-6              # L
n = V*n_per_L           # mol H2O → mol H2
E = n*HHV_H2            # J
print(f"7.4 µL 水 = {V*1e6:.1f} µL = {V*1e3:.3f} g = {V*1e3*1000:.1f} mg  →  {n*1e3:.4f} mmol H2O → {n*1e3:.4f} mmol H2")
print(f"  完全复燃的化学能(HHV) = {E:.1f} J / 循环")

print("\n--- 验算引擎需求（VW 1600cc 4缸 4冲程）---")
for rpm in (2800, 3200, 3600):
    inj_per_min = rpm/2*4
    P_out = E*inj_per_min/60
    water_per_min = 7.4e-6*inj_per_min*1000   # mL/min
    print(f"  @{rpm} rpm → {inj_per_min:.0f} 次喷射/min → 燃料功率 {P_out/1000:.1f} kW = {P_out/745.7:.1f} hp"
          f"  |  水耗 {water_per_min:.1f} mL/min")

print("\n★ 关键：这份燃料是「凭空来的」吗？——不是，必须先电解")
rpm = 3200; inj = rpm/2*4
E_need = E*inj/60            # W
water_per_min = 7.4e-6*inj*1000
print(f"  @3200 rpm 需要 {water_per_min:.1f} mL/min 的 H2+O2")
print(f"  电解这些水的最低电功(100%效率,不可达) = {E_need/1000:.1f} kW")
print(f"  而该引擎的机械输出本身只有 ~{E_need/745.7:.1f} hp")
print(f"  → 引擎必须把 100% 的输出拿去做电解，且效率假设已达 100%（不可能）")
print(f"  → 现实电解效率 ~60-70% → 缺口至少 {E_need/0.65/1000:.1f} kW")

print("\n--- 车用发电机能提供多少？---")
print("  常见车用交流发电机 = 0.6–2 kW  (12V x 50–160A)")
print(f"  → 缺 {(E_need/1000)-1.5:.1f} kW，差 {E_need/1000/1.5:.1f} 倍")

print("\n--- 但有一件事 Meyer 算对了（编者补充）---")
gal = 3785.4  # mL
print(f"  一加仑水 @ {water_per_min:.1f} mL/min → 可跑 {gal/water_per_min:.0f} 分钟")
print(f"  以 65 mph 计 → {gal/water_per_min/60*65:.0f} 英里/加仑(水)")
print(f"  ★ 这个数量级确实是「超高里程」，与 Meyer 宣传吻合 —— 数字自洽")
print(f"  ★ 问题不在「能跑多远」，而在「电从哪来」")

print("\n--- 48.1 µL / 325hp 柴油机 的自洽性 ---")
print(f"  325/50 = {325/50:.2f}   48.1/7.4 = {48.1/7.4:.2f}  → 线性缩放，内部自洽 ✅")

print("\n" + "="*74)
print("✅ 判定：7.4 µL 本身在数量级上自洽（Meyer 算对了「需要多少水」）")
print("❌ 但它要求「免费获得」12.5 kW 电解电力 —— 这是整套体系的天花板")
print("="*74)
