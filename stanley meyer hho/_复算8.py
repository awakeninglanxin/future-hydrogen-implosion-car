# -*- coding: utf-8 -*-
"""复算 ⑨：专利的「电极间距 = 电压波长」主张（权利要求 15-19）"""
print("="*74); print("复算 ⑨  US4798661 权利要求15：「间距 = 电压来回运动的波长」"); print("="*74)
c=2.99792458e8; er=78.54; v_sound=1497.0   # m/s @25C
v_em=c/(er**0.5)
print(f"水介电常数 er={er} -> 水中的电磁波速 v=c/sqrt(er) = {v_em:.4e} m/s")
print(f"水中声速 = {v_sound} m/s")
print()
gaps_in=[0.0625, 0.010]
lens_in=[3.0, 5.0]
print("Meyer 给出的间隙/腔长：")
for g in gaps_in:
    gm=g*0.0254
    print(f"  间隙 {g} in = {gm*1000:.3f} mm")
    print(f"    若按电磁波 λ=间隙 -> f = {v_em/gm:.4e} Hz = {v_em/gm/1e9:.2f} GHz  ❌ 远离 kHz")
    print(f"    若按声波   λ=间隙 -> f = {v_sound/gm:.4e} Hz = {v_sound/gm/1e3:.0f} kHz  ❌ 远离 10 kHz")
print()
print("★ 但若按「腔长」做半波共振：")
for L in lens_in:
    Lm=L*0.0254
    f_half=v_sound/(2*Lm); f_quarter=v_sound/(4*Lm)
    print(f"  腔长 {L} in = {Lm*1000:.1f} mm  → 声学半波 f = {f_half:.0f} Hz = {f_half/1000:.2f} kHz")
    print(f"                          → 声学四分之一波 f = {f_quarter:.0f} Hz")
print()
print("  ★★★ Memo 422DA 给的腔长 = 3 英寸，285/426 给的频率 = 10 kHz")
f=v_sound/(2*3*0.0254); print(f"      复算：3 英寸声学半波共振 = {f:.0f} Hz = {f/1000:.2f} kHz  ← 与 10 kHz 高度接近！")
print(f"      反推：11.33 kHz 对应半波腔长 = {v_sound/(2*11330)*1000:.0f} mm = {v_sound/(2*11330)/0.0254:.1f} 英寸")
print("      （Lawton 自己的管长是 5 英寸 → 与他的 11.33 kHz 不匹配；11.33 kHz 更接近 Meyer 的 3 英寸）")
print()
print("★ 编者判定：")
print("  ① 权利要求 15 的字面主张（间隙 = 波长）在数学上不成立（差 3 个数量级）")
print("  ② 但「腔长 = 声学半波」在 3 英寸/10 kHz 上高度吻合 —— 值得注意的数值巧合")
print("  ③ 声学共振真实存在（声化学/空化），但效应极小，不产生能量增益")
print("  ④ 无论如何：共振只搬运能量，不产生能量 —— 结论不变")
print("="*74)
