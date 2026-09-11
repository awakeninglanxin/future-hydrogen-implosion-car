# 08 · section8.pdf — Memo WFC 427《Voltage Wave-Guide Propagating》

> **原文件**：`section8.pdf`
> **原文标题**：Voltage Wave-Guide Propagating；"Resonant Action" By Voltage Tickling of State Space
> **版本**：Memo WFC 427
> **全文来源**：`tesla3.com`（HTML 转录版）
> **本 md 依据**：`_原文提取/section8_Memo_WFC_427.txt`（25,852 B，完整全文）
> **相册预览 OCR**：`_ima知识库_stanley_meyer/OCR/01_0197af92f8307a28.win.txt`
> **⚠️ 说明**：本份原文在 3 处被截断（原文标注 `[truncated]`），
> 涉及 `Traveling Voltage Wave-Guides`、`VIC Voltage Sync-Pulse Circuit` 两节的尾部。
> 本 md 对截断处**如实标注**，不作推测补写。

---

## 1. 这一份是什么

**Memo 427 是 Meyer 体系的「理论层」** —— 也是**最抽象、最玄、最难核实**的一份。

它引入了两个核心概念：

1. **State Space（状态空间）** —— 借自**控制论/动力系统**的真术语
2. **Voltage Tickling（电压轻挠）** —— Meyer 自造的比喻

并提出了 **Energy Vectoring（能量矢量分配）**：
**通过改变腔体几何 + 脉冲波形，把能量在「火焰推力」与「火焰温度」之间分配**。

> **★ 编者判断（先给结论）**：
> Memo 427 是整套体系里**「术语密度最高、可验证内容最低」**的一份。
> 它把**真实的电路细节**（Amp Inhibitor Circuit、Balance Phasing、三种脉冲串）
> 与**完全虚化的理论**（State Space、Voltage Tickling、Energy Vectoring）**混在一起**。
>
> **读法建议**：**只看电路段落，跳过理论段落。** 前者有货，后者是包装。

---

## 2. 原文要点（照录）

### 2.1 核心概念：State Space（状态空间）

**原文定义（照录）**：

> 「The established "State Space" is governed by either one of two variables being of either
> "**Static**" or "**Dynamic**" state of condition.
> **Dynamic State** condition is a variable of condition that is changing all the time;
> whereas, **Static** variable of condition is set at some point but then never changes.
> A point in "State Space" represents the state of the flame-system at a given time」
>
> 「**Static variables condition** is established when the resultant gas pressure is held constant
> with the never changing static electrical stress of opposite polarity of Voltage Pulse-Wave」
>
> 「**Dynamic variable conditions** exists when both the applied electrical stress of opposite polarity
> and dynamic gas pressure are continually changing in a preset time frame」
>
> 「**Combinatorial variables conditions** … subjecting constant static gas pressure to an ever changing
> electrical stress of opposite polarity」
>
> 「**Differential dynamic variables condition** … whenever changing dynamic electrical stress of opposite polarity
> encounters a **negative (decrease/drop-in) dynamic gas pressure**」

**四种状态空间（编者归纳）**：

| 类型 | 电应力 | 气压 | 
|---|---|---|
| **Static（静态）** | 恒定 | 恒定 |
| **Dynamic（动态）** | 变化 | 变化 |
| **Combinatorial（组合）** | 变化 | 恒定 |
| **Differential Dynamic（微分动态）** | 变化 | **下降** |

**Meyer 的命名**：
> 「Voltage Tickling of State Space under "Resonant Electrical Stress" **without amp influxing**
> while "Tuning-In" to the dielectric properties of water is herein referred to in this WFC Tech-manual
> as **"Resonant Action."**」

### 2.2 ★ 编者的术语溯源（重要）

**「State Space（状态空间）」不是 Meyer 发明的** —— 它是**控制论与动力系统的标准术语**：

| 概念 | 学术界定义 |
|---|---|
| **State Space** | 一个系统所有可能状态构成的集合。系统状态由一组**状态变量**（如位置、速度）唯一确定 |
| **State Space Representation（状态空间表示）** | 用一阶微分方程组描述系统：`ẋ = Ax + Bu`，`y = Cx + Du` |
| **State Vector（状态向量）** | 时刻 t 的状态 `x(t)` 在状态空间中的一个**点** |
| **Trajectory（轨迹）** | 状态点随时间移动的路径 |

> **★ 关键发现**：Meyer **借用了正确的术语，并给出了基本正确的「静态 vs 动态」区分**
> （静态 = 参数不随时间变；动态 = 参数随时间变）。
> 这在**术语层面是对的**。
>
> **但他的问题是**：
> - 他从未定义**状态变量是什么**（是电压？是压力？还是「火焰系统」的什么？）
> - 他从未写出**任何一个方程**（没有 `ẋ = Ax + Bu`）
> - 他把「**状态空间**」当成「**工况**」的同义词在用（这在中文里等于把「相空间」说成「工作档位」）
>
> **判定**：🟡 **术语借用正确，概念使用错误。**
> 这属于 `HHO书本精读/03` 所说的**「命名层伪装」的学术版** ——
> 用真术语制造专业性，但抽掉了术语的数学内容。

### 2.3 ★ 电路干货一：Traveling Voltage Wave-Guide（行波电压波导）

**原文（含截断标记）**：

> 「The formation of tubular Traveling Voltage Wave-guide (570a) … is physically formed
> when **positive electrical voltage surface (661/E9)** and **negative electrical voltage surface (671/E10)**
> are placed in **parallel space relationship** to form voltage surfaces (E9/E10) about a
> **cylindrical axis of rotation** having **space-gap (35)** there between」
>
> 「stainless steel material (s/s) (**T304**) forming Voltage surfaces (E9/E10) electrically conducts and transfers
> (**skin effect**) Voltage Pulse-Frequency Potential (583) along the **inside surface area** of the
> **chemically inert and non-oxidizing stainless steel tubular material** …
> which physically dictates the shape and configuration of voltage waves …
> forming tubular voltage wave-guide(s) (570) that, now, becomes
> **the same physical configuration of Water Gap (616)**」

**★ 关键的新信息（本份首次出现）**：

> 「The surface tension of water (584) adjacent to both voltage surfaces (E9/E10) further aids the transmission
> of voltage potential (66/67) since **Electrical Charging Effect (585) does not change or alter
> the dielectric value of water (Re)**」
>
> 「**Electrical transmission zone (587) is almost free of electron leakage** …
> since Water Bath (85) is a **dielectric-liquid (typically 78.54) that does not like to transfer
> nor exchange electrons** … thereby, maintaining voltage amplitude potential …
> **without experiencing amp arc-over across Water-Gap (616) in any appreciable amount**」

**★ 编者判读**：

| Meyer 的主张 | 物理核实 |
|---|---|
| 不锈钢管内表面「skin effect」传播电压 | 🟡 **部分成立但机制错**。**趋肤效应（skin effect）** 是高**频**交流电流集中于导体表面的现象。Meyer 用它来解释「电压沿表面传播」——**概念混用**：趋肤效应描述的是**电流分布**，不是「电压沿导体表面传播」 |
| 水是介电液体，「不愿交换电子」 | ✅ **方向对** —— 纯水的电导率确实极低（18.2 MΩ·cm 超纯水）。**但**：「不愿交换电子」是**拟人化表述**；真实原因是**缺乏载流子（离子）** |
| 「无电弧跃过水隙」 | 🟡 **在击穿电压以下成立** —— 这正是「电容」的定义。**但一旦到击穿电压，必然放电** |
| 「水的介电常数不改变」 | ❌ **不成立** —— 水的介电常数**强依赖于频率和温度**（25°C 静电场下是 78.54；但在 GHz 频段降到约 4–5，因为**水分子偶极子来不及转向**）。**Meyer 全程只用 78.54 这一个值，忽略了频率依赖** |

### 2.4 ★★ 电路干货二：三种脉冲串（本份最实用的内容）

**原文**：

> 「(780A) **Unipolar Pulse-Train**（单极性脉冲串）
> (780B) **Crossover Unipolar Pulse-Train**（交叉单极性脉冲串）
> (780C) **Clipped Unipolar Pulse Train**（削顶单极性脉冲串）」

**三种波形的用法（原文）**：

| 波形 | 用途（原文） |
|---|---|
| **Unipolar (780A)** | 基础型；「Progressive Voltage Sync-Wave」→ 鼓励 **Dynamic Voltage Stimulation (Dvs)** |
| **Crossover (780B)** | 「is used when particle oscillation of the water molecule atom(s) is/are to be **continually electrical stressed** under changing conditions of **higher magnitude** (Compressing Voltage Pulse Wave-form)」 |
| **Clipped (780C)** | 「is used to encourage further increase in **atomic dwell-time** capable of **raising Atomic Energy Level (AEL)** of the Water Atoms to even a higher energy-state before **Snapping-Action** occurs」 |

**★ 这三种波形在真实电路里的身份（编者）**：

| Meyer 的名字 | 真实对应 |
|---|---|
| **Unipolar Pulse Train** | 标准**单极性脉冲**（普通 PWM / 脉冲） |
| **Crossover Unipolar Pulse Train** | **DCM（断续导通模式）** —— 电流在周期内回零，下一个脉冲在**非零电压点**起始（原文：`Convergent Point "Q"` 不落到地，位于 `1/3 高度`）→ 即**连续三角波电流模式（CCM）与 DCM 的临界** |
| **Clipped Unipolar Pulse Train** | **削顶脉冲（chopped pulse）** —— 即用**限幅电路**把峰值削平，延长高电平时间 → **增加有效占空比** |

**Meyer 给出的「1/3 高度」细节（原文）**：
> 「each VIC Pickup Coils (52A-52B-52C) are **axially spaced 120° apart** to cause **Convergent Point "Q"
> to be located 1/3 the height of Voltage Amplitude Peak Level (Vpp)**」

✅ **这是一个真实的开关电源设计细节** —— 三相 120° 交错（interleaved）控制 + 谷底检测。
**这属于「准谐振 LLC / 三相交错 PFC」的技术范畴**，是**真实的现代电源技术**。

### 2.5 ★★ 电路干货三：Amp Inhibitor Circuit（抑流电路，本份最重要的一段）

**原文**：

> 「are zero reference to electrical ground state (0V) by placing **Amp Inhibitor Circuit (860)**
> (**Amp Inhibiting Coil 617, Blocking Diode 618, and Magnetic Induction Core 619**) between
> **electrical ground (0V)** and **Center Tap of Dual Bifilar Secondary Pickup Coils (616A/B)**
> of VIC Matrix Circuit (690)」
>
> 「By doing so, **Balance Phasing** of opposite voltage intensity (+Vpp / −Vpp) is accomplished
> without experiencing current influxing caused by differential variances where
> Negative Voltage Peak Potential (−Vpp) is less than Positive Voltage Peak Potential (+Vpp) or vice versa」
>
> 「allowing Inductor Resonant Choke Coils Electromagnetic Fields Intensity (+Z2 / −Z3) to be, in turn,
> free of Electromagnetic variances of intensity (Z2 − Z3).
> This **non-voltage shift** (Balance Phasing of opposite Voltage Potential) helps **prevents atom displacement
> during "Snapping-Action"** by which "Resonant Electrical Stress" of opposite electrical polarity
> is applied **equally** across Water Molecule(s)」

**参数（原文，本份再次确认）**：
> 「Amp Inhibiting Coil-Assembly (617) is made up of **magnetic inductance Stainless Steel 430F/FR wire material**
> wrapped around a **closed-loop Induction Magnetic Core (619)** which is a **separate coil-unit (860)**
> apart from VIC Coil Assembly (580)」
>
> 「both Resonant Charging Chokes (56/Z2 – 62/Z3) resistive values are the same (**Typically 11.6 k each**)」

**★ 编者判读**：

| Meyer 的表述 | 真实对应 | 判定 |
|---|---|---|
| 「Dual Bifilar Secondary Pickup Coils (616A/B) + 中心抽头」 | **双线并绕、中心抽头次级** → 产生**对称的正负双极性输出** | ✅ 真实拓扑 |
| 「把抑流网络接到中心抽头与地之间」 | 相当于**在中心抽头引入阻抗，平衡两臂** | ✅ 真实的平衡技术 |
| 「Balance Phasing（相位平衡）」 | 确保 `+Vpp = −Vpp`（对称双极性） | ✅ 真实且重要（不对称会导致**净直流偏置**，伤害电极） |
| 「避免 atom displacement」 | 🟡 Meyer 的解说（防原子位移），但**真实的工程意义是防直流偏置/防电极极化** | 🟡 结论对，机制错 |
| **430F/FR + 闭环磁芯的独立线圈单元** | **共模扼流圈（common-mode choke）** | ✅ 真实元件 |

> **★ 编者评价：`Amp Inhibitor Circuit (860)` 是 Memo 427 里唯一「货真」的部分。**
> 它描述的是一个**「中心抽头 + 共模扼流 + 阻断二极管」的对称双极性输出网络** ——
> 这在现代**半桥/全桥开关电源**里是**标准做法**（用于抑制共模电流、平衡两臂）。
>
> **Meyer 用「防原子位移」来解释它，但把它拿掉「gtnt」叙事，这个电路本身是合理的。**

### 2.6 谐振腔几何与应用对应（原文，本份给出完整对照表）

**原文**：

> 「(A) **Linear Cylindrical Resonant Cavity**;
> (B) **Taper Cylindrical Resonant Cavity**; and
> (C) **Non-Linear Cylindrical Resonant Cavity**」

**对应的「状态空间」（原文）**：

| 腔型 | 状态空间 | 火焰锋 | 说明 |
|---|---|---|---|
| **(730A) Linear** | Static Variable Condition (Svc) | **VS1** | 「Flame-Front is of **equal magnitude** when thermal explosive energy-yield (gtnt) is compared with thermal heat-energy (Teh)」 |
| **(730B) Taper** | Dynamic Variable | **VS3** | 「Dynamic Electrical Stress and Dynamic Gas Pressure are **both increasing**」→ **"Progressional State Space"** |
| **(730C) Non-Linear** | Differential Dynamic Variables | **VS4** | 「Dynamic Electrical Stress is **increased** while the resultant gas pressure is **allow to drop**」→ **"Expanding State Space"** |

**应用对应（原文，★ 本份最实用的结论表）**：

| 腔型 | 推荐应用（原文） |
|---|---|
| **Taper (730B)** | 「**ideally suited for internal combustion I.C. engines as well as Rocket Engines** where **high thrust-yield of explosive power** is required」 |
| **Non-Linear / Expanding (730C)** | 「**best suited for Furnace Applications**」 |
| **Linear (730A)** | 「**for Cutting-Torch applications**」 |

**激光注入（原文）**：
> 「**Laser Energy (588)** being injected into Resonant Pulse Waves (16) by way of
> **Laser Inject Tube-Port (589)** helps **maintain Plasma-temperatures at extremely elevated temperatures**
> over the prior art」

> **★ 编者评价**：这张「腔型 → 应用」对照表，是**本份最有价值的一段**。
> 它把 Memo 425/426 的抽象几何，落实到了**三个具体工况**上：
> **推进（锥形收缩）/ 加热（非线性扩张）/ 切割（线性恒定）**。
> **这个分类逻辑本身是清晰的、可理解的，而且工程上说得通** ——
> 不同的火焰形态需求，确实对应不同的腔体几何。
> （**唯一的保留**是：它假设了「能量可以矢量分配」这个错误前提。）

### 2.7 「Snapping-Action（弹跳动作）」概念

**原文**：
> 「Clipped Unipolar Pulse Train (780C) is used to encourage further increase in **atomic dwell-time**
> capable of **raising Atomic Energy Level (AEL)** of the Water Atoms to even a higher energy-state
> before **Snapping-Action** occurs when Unipolar Pulse Wave (Upw) **returns to ground state (Vo)**
> after voltage propagation (Vpa/Vpb)」
>
> 「the repetition-rate of "**Atomic Snapping-Action**" (Asa) (the number of Voltage Pulse Fields Vpf
> occurring per unit of space-time) directly determines the resultant energy level of
> Static Electrical Charging Effect (585) since **"Particle Oscillation" is being used as a "Energy Generator" (EGpo)**」

**★ 编者判读**：
- 「Snapping-Action」描述的是**脉冲结束后电压急速回落到地**的过程
- 这在真实电路里叫 **关断沿（falling edge / turn-off transient）**
- Meyer 把它解读为「原子被弹回、释放能量」→ ❌ **无物理对应**
- 「把粒子振荡当作发电机」→ ❌ **这是整套体系里最核心的错误主张**
  （振荡是**消耗**能量的，不是产生能量的。参 LC 振荡必须由电源补充损耗）

---

## 3. 独立复算 / 核实

### 3.1 「Snapping-Action 作为能量发生器」的判定

**Meyer 的主张**：粒子在电场中来回振荡 → 作为「Energy Generator」→ 能量增加。

**编者核实**：

| 检验 | 结果 |
|---|---|
| 带电粒子在交变电场中会振荡吗？ | ✅ **会** —— 这是**介电损耗**的本质（水分子偶极子随电场转向） |
| 振荡会产生净能量吗？ | ❌ **不会** —— 振荡消耗能量（转化为**热**）。这正是**微波炉加热水**的原理 |
| 介电损耗的热效应有多大？ | 水的介电损耗在 kHz 频段**很小**（因为偶极子完全跟得上电场），但**不为零** |
| 所以 Meyer 的 20 kV @ 10 kHz 输入，有多少变成热？ | 需要具体水质与几何才能算，但**方向是：损耗总是正的，即总是消耗** |
| 「能量效率 126%（复算②）」与此矛盾吗？ | ✅ **不矛盾** —— 那 126% 是**测量误差**（见 3.2），不是「粒子振荡发电」的产物 |

> **★ 判定**：❌ **「Particle Oscillation as Energy Generator」的核心主张错误。**
> 振荡是**耗能**过程（介电加热），不是产能过程。Meyer 把「介电损耗产生的热」误认为「新获得的能量」。
> **这是一个概念级的错误，无法通过任何测量修正。**

### 3.2 ★ 与复算 ② 的对接

Memo 427 提供了**测量条件**，这正好帮助解释 Lawton 的「3 倍」：

| Memo 427 所述条件 | 与 Lawton 数据的对应 |
|---|---|
| 脉冲频率「10 kHz or above」 | Lawton 实测 **11.33 kHz** ✅ 吻合 |
| 「restricting amp leakage in the milliamperes range」 | Lawton 实测 **187.5 mA** ✅ 吻合 |
| 复杂多相波形（Unipolar / Crossover / Clipped） | Lawton 实测 **方波，占空比 78%/22%** 🟡 简化版 |
| 高压（20 kV 级） | Lawton 实测 **仅 3.9 V**（未做谐振升压） |

**★ 关键推论**：

> Lawton 的复现件**没有实现 Meyer 的高压谐振升压**（他只有 3.9 V，而不是 20 kV）。
> 也就是说：**Lawton 测到的「3 倍」，是在一个「简化到只剩脉冲调制」的版本上测到的。**
>
> 那么，如果连「只有脉冲调制、没有高压谐振」的版本都能测出「3 倍」，
> **这个「3 倍」就更不可能是某种精妙的高压量子效应，而只能是**
> **① 测量误差（11.33 kHz 超仪表带宽，见下）或 ② 脉冲电解的真实小幅增益。**

**★ 测量误差的复核（本批核心方法论，再次确认）**：

```
波形 = 11.33 kHz 方波、占空比 78%/22%
普通万用表 AC 电流档带宽通常 1–3 kHz
11.33 kHz 远超带宽 → 电流被显著低估
若真实电流被低估 3.3 倍 (即 0.624 A)
→ 法拉第预测恰好等于实测量
→ 「超法拉第」完全消失，效率回落至 32.1% (LHV) = 普通电解槽水平
```

> **★ 补充一个旁证**：Memo 427 特意强调系统「restricting amp leakage in the **milliamperes** range」，
> 说明 Meyer **自己也认为电流很小**。
> 如果 Meyer 和他的复现者**都先验地相信「电流应该很小」**，
> 那么他们对仪表读数的**偏低**，就**不会有任何怀疑**。
> **这是确认偏误（confirmation bias）与仪表带宽限制的叠加。**

### 3.3 「水的介电常数 78.54」的频率依赖（Memo 427 的盲点）

Meyer 在 420 / 422DA / 425 / 426 / 427 **五份文件里一致使用 `78.54 @ 25°C`**。

**编者的核实**：

| 频率 | 水的相对介电常数 εr（25°C，近似） |
|---|---|
| 静态 / DC | **78.5** |
| 1 MHz | ~78 |
| 1 GHz | ~55（已有明显下降） |
| **10 GHz** | **~20** |
| 100 GHz | ~5 |
| 光频 | ~1.8（折射率平方） |

- **德拜弛豫（Debye relaxation）** 特征频率在 25°C 约 **17 GHz**
- 在 Meyer 用的 **1–10 kHz** 范围内，**用 78.54 是合理的** ✅

> **判定**：✅ **Meyer 在这个频段用 78.54，是正确的。**
> **但**：这也意味着**「介电常数 = 78.54」这个看似巨大的数字，并不能给他带来什么优势** ——
> 因为它只是一个**电容乘数**，让同样的电极面积得到更大的电容。
> 大电容在 LC 谐振里意味着**更低的谐振频率**，仅此而已。
>
> **Meyer 反复强调 78.54，给人一种「水有神奇介电性」的印象 ——
> 但 78.54 只是说「水是一种很好的电容介质」，这没错，也不神奇。**

### 3.4 「Laser Inject Tube-Port 维持等离子温度」

**原文**：激光注入帮助「maintain Plasma-temperatures at extremely elevated temperatures over the prior art」

✅ **真实** —— 这是**激光维持等离子体（Laser-Sustained Plasma, LSP）**的原理，
用于**等离子体炬、激光焊接、EUV 光源**。
🟡 但「维持高温」≠「增加总能量」—— 激光本身要耗电，且总能量账仍是负的。

---

## 4. 判定

| 维度 | 判定 | 说明 |
|---|---|---|
| **命名层** | ❌ **最严重** | 「State Space」「Voltage Tickling」「Energy Vectoring」「Snapping-Action」「Energy Generator」—— 术语密度最高，但要么借用学术词后抽空内容（State Space），要么纯自造 |
| **物质层** | 🟡 | 水的介电常数用对了（78.54，在 kHz 频段合理），但忽略了频率依赖 |
| **能量层** | ❌ | **核心错误**：「Particle Oscillation as Energy Generator」——振荡是耗能（介电加热），不是产能 |
| **工程层** | ✅ **有真货** | Amp Inhibitor Circuit（中心抽头 + 共模扼流 + 阻断二极管）、Balance Phasing、三相 120° 交错、三种脉冲串、三种腔型→应用对应表 |
| **本文定位** | **「理论包装 + 电路细节」的混合体** | 理论部分最抽象，电路部分仍有价值 |

### 一句话

> **Memo 427 用「状态空间」这个真学术词，包装了一个假主张（振荡发电）；
> 但在包装的夹缝里，藏着一套真实的对称双极性输出电路。**

---

## 5. 可借鉴清单（工程层萃取）

| # | 技术点 | 真实对应 | 可借鉴度 |
|---|---|---|---|
| 1 | **中心抽头 + 双线并绕次级的对称双极性输出** | 半桥/全桥开关电源 | ⭐⭐⭐ |
| 2 | **Amp Inhibitor Circuit（共模扼流 + 阻断二极管接中心抽头）** | 共模电流抑制 + 两臂平衡 | ⭐⭐⭐ |
| 3 | **Balance Phasing（确保 +Vpp = −Vpp）** | 防直流偏置/防电极极化 | ⭐⭐⭐ |
| 4 | **三相 120° 交错控制（Convergent Point 位于 1/3 高度）** | 交错式 PFC / LLC 谷底检测 | ⭐⭐⭐ |
| 5 | **Clipped Pulse（削顶脉冲延长高电平）** | 削顶脉冲调制（chopped pulse） | ⭐⭐ |
| 6 | **Crossover Pulse（谷底不完全回零）** | CCM/DCM 临界模式 | ⭐⭐ |
| 7 | **腔型 → 应用对应**（锥形=推进 / 非线性=加热 / 线性=切割） | 电场集中度与火焰形态匹配 | ⭐⭐⭐ |
| 8 | **激光注入维持等离子体** | Laser-Sustained Plasma (LSP) | ⭐⭐ |

> **★ 第 1–3 条是本份最有价值的**：
> 「**中心抽头 + 共模扼流 + 阻断二极管**」这套组合，
> 是**现代高频开关电源处理「双极性对称输出 + 共模抑制」的标准手段**。
> **Meyer 用「防止原子位移」来解释它，但他的电路设计是对的。**

---

## 6. 本份的三处原文截断（如实标注）

| 位置 | 截断内容 |
|---|---|
| `Traveling Voltage Wave-Guides` 节末 | 「as illustrated in (720) of Figure (… **truncated**」 |
| 同节 | 「Secondary Voltage pickup coil (52) of Figure (7-8) d… **truncated**」 |
| `VIC Voltage Sync-Pulse Circuit` 节末 | 「Blocking Diode … **truncated**」 |

> **编者声明**：以上三处截断来自 `tesla3.com` 的 HTML 转录版本本身（非我方抓取失误）。
> 如需补全，需找到 `section8.pdf` 原件。
> **本 md 不对截断处作任何推测性补写** —— 符合本项目「不妄语」约定。

---

*编者整理 · 2026-09-11 · 原文全文见 `_原文提取/section8_Memo_WFC_427.txt`（含 3 处原文截断）*
