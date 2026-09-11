# 03 · section2.pdf — Memo WFC 421《Quenching Circuit Technology》

> **原文件**：`section2.pdf`
> **原文标题**：WATER FUEL CELL — Quenching Circuit Technology；Rendering Hydrogen Safer Than Natural Gas
> **版本**：Memo WFC 421
> **全文来源**：`tesla3.com`（HTML 转录版）
> **本 md 依据**：`_原文提取/section2_Memo_WFC_421.txt`（8,907 B，完整全文）

---

## ⭐ 先说结论：这是整套 10 份文件里**最扎实的一份**

Memo 421 **不吹能量**。它讲的是：**「怎么让氢气烧得跟天然气一样安全」**。

而编者独立复算后确认：**它的所有关键数字，量级全部与文献吻合。**

> 一个自称「水变燃料」的人，这一册却在认真地做**燃烧安全工程**，
> 而且做对了。这是本批最值得注意的反差。

---

## 1. 原文要点（照录）

### 1.1 主题句（原文）

> 「The Quenching Circuit Technology is a combination and integration of several Gas-Processes
> that uses **noncombustible gases** to render **hydrogen safer than Natural Gas**.」
>
> 「The "Non-Burnable" gases are used to adjust hydrogen **"Burn-Rate"** to Fuel-Gas burning levels …
> **recycled** to stabilize Gas-Flame temperatures … **intermixed** to sustain and maintain an hydrogen Gas-Flame …
> and used to **prevent Spark-Ignition of supply gases**.」

**三件事**（Meyer 自己列的）：
1. 调整氢的**燃速**，使其匹配其他燃料气
2. 回收惰性气**稳定火焰温度**
3. **防止供气管路被火花点燃**

### 1.2 各组件（原文）

| 组件 | 尺寸/参数（原文） | 功能 |
|---|---|---|
| **Spark-Ignition Tube (B)** | 管径 **1/8 inch** | 测量燃速的试验管：点火后测「1 秒内火焰前进长度」 |
| **燃速定义** | cm/sec | 「The Gas-Ignition Process … establishes the "Burn-Rate" of a Burnable Gas-Mixture in **centimetres per second (cm/sec.)**」 |
| **Gas Injection Process** | — | 把**非可燃气体 (D)** 混入可燃气 (B)，**降低**混合气燃速；加入量越多，燃速越低 |
| **Gas Mixing Regulator** | — | 「the Water Fuel Cell allows the "Burn-Rate" of Hydrogen to be "Changed" or "adjusted" **from 325 cm/sec. to 42 cm/sec.** (Co-equalling Natural Gas Burning levels)」 |
| **惰性气来源** | — | 「**Non-Combustible Gases (such as Nitrogen, Argon, and other non-burnable gases) derived from Ambient Air dissolved in natural water**」 |
| **火焰温度** | — | 「sustaining and maintaining an **Open-Air Flame beyond 5000-degrees F**」 |
| **Quenching Circuit** | 通道 **至少 1/8 inch 长**、**0.015 inch 直径** | 狭窄通道阻止燃烧原子「Re-Grouping」→ 防回火 |
| **Quenching Circuit 关键性质** | — | 「"Anti-Spark technique" is **"independent" of both Gas-Velocity and Gas-Pressure**」 |
| **Quenching Nozzle** | 碟形多孔配置 | 补偿气体流速增加；「overlapping Flame-Pattern re-ignites the expelling hydrogen gas-mixture should Flame-Out occur」 |
| **Quenching Disc 材料** | **陶瓷（Ceramic）** | 「to prevent hole-size enlargement due to gas-oxidation」 |
| **Quenching Tube** | 柔性管 | 长距离安全输送燃气 |
| **Catalytic Block** | 倒置半球腔 | 回收「escaped or unused burnable gases」→ 完全燃烧，防氧化物生成 |
| **Gas Grid System** | — | 「Ambient Air is the **prime source of Non-Combustible Gases**」；处理过的空气混氢后可**经现有燃气管网输送** |

### 1.3 火焰温度调节（原文）

> 「By capturing and recycling the expelled non-combustible gas (D) … back into the sustained hydrogen gas-flame
> or Fuel-Cell causes the gas flame temperature to be "changed" or "altered" by way of the Gas Retarding Process」
>
> 「Continual feedback of non-combustible gases (D) is, hereinafter, called **"The Gas Combustion Stabilization Process"**」
>
> 「The "newly" formed and established gas flame-temperature **remains constant regardless of the gas flow-rate** of the Fuel-Cell」

### 1.4 内燃机应用（原文）

> 「The Gas Combustion Stabilization Process (recycling non-combustible gases) is also applicable to operating an
> Internal Combustion Engine **without changing Engine-Parts** since the Gas Retarding Process allows the hydrogen
> "Burn-Rate" to "equal" the "Burn-Rate" of Gasoline or Diesel-Fuel」
>
> 「The engine **provides its own non-combustible gases** derived from Ambient Air undergoing the gas-combustion process.
> **Engine temperature remains the same** since The Gas Stabilization Process is used.」

---

## 2. 独立复算 / 核实（★ 本份的重点）

复算脚本 `_复算.py` 第 ③ 段输出：

```
Meyer 称 H2 burn-rate 325 cm/s  → 文献 H2/空气层流火焰速度 ~270 cm/s  🟡 量级吻合
Meyer 称 天然气 burn-rate 42 cm/s → 文献 CH4 ~36 cm/s              ✅ 吻合
Meyer 称 火焰 >5000°F → 换算 5000°F = 2760°C
   文献 H2/O2 绝热火焰温度 ~3080°C，H2/空气 ~2250°C → 5000°F(2760°C) 在 O2 环境可达 ✅
Meyer 称淬火通道 0.015 in 直径 = 0.38 mm
   文献 H2/空气最小淬火直径 ~0.6–0.8 mm → 0.38 mm 理论上足以阻火 ✅ 工程合理
```

### 2.1 逐条对照表

| 项目 | Meyer 给的数 | 文献值 | 判定 |
|---|---|---|---|
| **H₂ 燃速** | 325 cm/s | H₂/空气层流火焰速度 **~270 cm/s**（H₂ 是最快的燃料气之一，高氢混合比下可到 300+） | 🟡 **量级吻合**。325 略偏高但在他描述的条件（可能富氧）下不离谱 |
| **天然气燃速** | 42 cm/s | 甲烷/空气 **~36 cm/s** | ✅ **吻合**（42 vs 36，同一数量级） |
| **火焰温度** | >5000 °F = **2760 °C** | H₂/O₂ 绝热焰温 **~3080 °C**；H₂/空气 **~2250 °C** | ✅ **在纯氧环境可达**；公开空气中略高于理论值但仍合理 |
| **淬火通道直径** | 0.015 in = **0.38 mm** | H₂/空气最小淬火直径（MESG）**~0.6–0.8 mm** | ✅ **0.38 mm < MESG → 理论上足以阻火** |
| **淬火通道长度** | ≥ 1/8 in = **3.2 mm** | 标准阻火器要求 L/D ≥ 一定值；3.2 mm / 0.38 mm ≈ **L/D = 8.3** | ✅ **L/D 比例合理**（工业阻火器常用 L/D 在 5–20 之间） |
| **陶瓷做淬火碟** | 为了抗氧化扩孔 | 工业阻火器正是用烧结金属/陶瓷 | ✅ **工程正确** |
| **燃速与流速/压力无关** | Meyer 明确声明 | 淬火（阻火）**确实是几何决定的**，与流速/压力基本无关（这正是阻火器的原理） | ✅ **Meyer 抓到了要害** |

> **★ 编者评价**：`"Anti-Spark technique" is "independent" of both Gas-Velocity and Gas-Pressure`
> 这句话，是**整批 10 份文件中技术含量最高的一句**。
> 它精确地描述了**阻火器（flame arrestor）的工作原理** ——
> 靠的是「**冷壁淬灭**」（火焰通过窄通道时热量被壁面带走，自由基链式反应中止），
> 因此**与流速和压力无关，只与通道尺寸有关**。
> Meyer 不但说对了，还给出了正确的尺寸量级。

### 2.2 惰性气体调燃速：有物理基础

| 主张 | 核实 |
|---|---|
| 混入 N₂/Ar 可**降低**氢的燃速 | ✅ **正确** —— 稀释效应 + 惰性气的高热容吸收热量，降低火焰温度和层流火焰速度。这是**燃烧学的标准结论** |
| 从**空气溶解气**中获取惰性气 | 🟡 **部分成立** —— 水中确实溶有 N₂/O₂/Ar（天然水中溶解空气），电解时会一起析出。**但量极小**（25°C 下水中溶解空气约 1.5% 体积比），**不足以把 270 cm/s 降到 40 cm/s** |
| 「引擎自产惰性气」 | ✅ **真实** —— 内燃机**废气再循环（EGR）**正是这个原理，是现代发动机的标准技术。Meyer 的「Gas Combustion Stabilization Process」= **EGR 的另一种说法** |
| 「引擎温度不变」 | 🟡 **方向正确** —— EGR 确实降低燃烧峰值温度（这是它抑制 NOx 的原因）。但「不变」过于绝对 |

### 2.3 「燃气可经现有管网输送」：这一条的含金量

Meyer 声称：把处理过的空气混入氢，氢就可以**经现有天然气管网安全输送**。

- **物理方向正确**：混入惰性气 = 抑制回火 = 提高输送安全性
- **但**：燃气管网对**氢脆（hydrogen embrittlement）**、**泄漏率**、**热值计量**有完全不同的要求
- 现实中「掺氢天然气（H₂ blending）」正是当前能源行业的活跃课题 —— **掺氢比例目前普遍在 5–20% 体积比**，远低于 Meyer 暗示的「纯氢 + 惰性气」

> **判定**：🟡 方向对、量级不成立。**但这个思路本身在 1990 年代提出是相当超前的** —— 掺氢管网今天是真实产业方向。

---

## 3. 燃烧安全清单（可直接借鉴的工程内容）

Memo 421 给出的这套东西，**本质上是一份「氢气安全使用工程指南」**，逐项都有真实对应：

| Meyer 的器件 | 现代对应物 | 是否真实 |
|---|---|---|
| **Spark-Ignition Tube**（1/8" 管测燃速） | **层流火焰速度测定管**（Burner method / tube method） | ✅ 标准实验方法 |
| **Quenching Circuit**（0.38 mm × 3.2 mm 窄通道） | **阻火器（Flame Arrestor）** 的阻火芯元件 | ✅ |
| **Quenching Disc**（陶瓷多孔碟） | **烧结金属/陶瓷阻火芯** | ✅ |
| **Quenching Tube**（柔性阻火输送管） | **阻火呼吸阀 / 阻火器管路** | ✅ |
| **Catalytic Block**（倒置半球回收未燃气） | **催化氧化器 / 后燃器** | ✅ |
| **Gas Mixing Regulator**（水槽溶解气自动调燃速） | **燃料气调质（fuel gas conditioning）** | 🟡 原理对、量级不足 |
| **Gas Combustion Stabilization Process**（废气回流稳焰） | **EGR（废气再循环）** | ✅ |
| **Gas Grid System**（处理空气 + 氢入管网） | **掺氢天然气管网（H₂ blending）** | 🟡 方向对、比例不同 |

> **7 项中 5 项完全真实** —— 这个比例远高于 Memo 420 或 427。

---

## 4. 判定

| 维度 | 判定 | 说明 |
|---|---|---|
| **命名层** | 🟡 | 「Quenching Circuit」「Gas Combustion Stabilization Process」是**自造名，但所指物真实存在**（阻火器 / EGR） |
| **物质层** | ✅ | 气体就是 H₂/O₂/N₂/Ar，没有神秘物质 |
| **能量层** | **本份不涉及** | ⭐ **这是它扎实的根本原因** —— Memo 421 完全不谈「能量倍增」，只谈「怎么烧得安全」 |
| **工程层** | ✅✅ **最高分** | 燃速数据量级正确；淬火尺寸符合阻火器设计原理；陶瓷抗氧化扩孔正确；「阻火与流速压力无关」判断精确 |
| **本文定位** | **整套体系的「安全外壳」** | Meyer 用这一册来回答「氢气太危险怎么办」—— 而这个回答**基本是对的** |

### 一句话

> **Memo 421 是 Meyer 体系里唯一一份「把话说对了」的文件。**
> 它不谈 250 万桶，不造新词，只老老实实讲**氢气燃烧安全工程**。
> 编者对它的评价是：**如果 Meyer 只发表这一份，他会被当成一位认真的（虽然方向小众的）安全工程师。**

### 但同时要注意（编者提醒）

Memo 421 的扎实，**不等于 Memo 420 的核心主张成立**。
它的正确性**恰恰建立在「氢气就是普通氢气」这个前提上** ——
而 Memo 420 主张的是「被激光加能、缺电子的亚临界气原子」。
**两者不兼容**：

- 若气体真是「缺电子的亚临界态」（Memo 420），就**必须重新测燃速**，325/42 那组数字就不适用
- Memo 421 用的是**普通氢气的文献量级数字**来论证 —— 这本身说明 Meyer 在这一册里**默认了常规氢化学**

> 详见 `11_汇总` §5.1「内部矛盾」与 §5.4「D14 否证 Memo 421 的安全主张」。

---

*编者整理 · 2026-09-11 · 原文全文见 `_原文提取/section2_Memo_WFC_421.txt`*
