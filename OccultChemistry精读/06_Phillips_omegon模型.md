# 06 · Phillips 的 omegon 模型

> **原书**：Stephen M. Phillips, *Extra-Sensory Perception of Quarks*（神智学出版社，1980）
> **作者身份**：**Stephen M. Phillips, Ph.D.** —— 剑桥大学理论物理 B.A./M.A.、
> 开普敦大学 M.Sc.、加州大学粒子物理博士；1979 年在 *Physics Letters*
> 发表 "Composite Quarks and Hadron-Lepton Unification"
> **本册地位**：★ **OC 与现代物理之间「最精密、最具体」的一次对接尝试**
> **行号对照**：`_book_extract/esp_quarks.txt`（**英文原文完好**，共 2,403 行）
> **编者整理** · 2026-09-12

---

## 〇、这本书要解决的问题（一句话）

**OC 说氢有 18 个 Anu；现代物理说质子有 3 个夸克。**
**3 和 18 之间差 6 倍 —— 这 6 倍怎么补？**

**★ Smith 在本书导论里的原话（第 43 行）：**
> *"The first pointer to a possible reconciliation came when quarks were postulated,
> requiring subdivision of the proton into three bound quarks.
> **But between three and eighteen there still remained a factor of six to be bridged.**
> This feat has been achieved by Dr. Stephen Phillips...
> This theory thus provides for **nine omegons per proton**;
> **the still persisting factor of two was bridged by imperative reinterpretation
> of the E.S.P. data.**"*

**★★ 这一句话是整个「后人建构」线索的核心 —— 它自己承认了两个「桥」：**

| 缺口 | 桥法 | 提供者 |
|------|------|--------|
| 3 → 9（×3） | **理论**：夸克再分成 3 个 omegon（3×3=9） | Phillips 的理论 |
| 9 → 18（×2） | ★ **「imperative reinterpretation of the E.S.P. data」** | **重新解释观测数据** |

**★ 「imperative」在这里的意思是「不得不、强制性的」——
　　 即：理论要求 ×2，所以观测数据**必须**被重新解释成能提供这个 ×2 的样子。**

**⇒ 这句话是 Smith（一位 F.R.S. 级科学家）自己写下的。**
**⇒ 它不是什么外部批评者的恶意解读，而是**共同体内部的公开承认**。**

---

## 一、omegon 模型的核心内容

### 1.1 基本假设（原文第 180–182 行）

> *"It is proposed that **quarks are not discrete, fundamental objects** but, instead,
> are **composite, tightly knit clusters of three particles called 'omegons.'**
> Protons and neutrons, which are each made up of three quarks,
> therefore contain **nine omegons**."*

**★ 组成规则（原文第 182 行，逐字）：**

| 粒子 | 组成 | omegon 数 |
|------|------|-----------|
| omegon **o** | 基本 | — |
| omegon **θ** | 基本 | — |
| **u 夸克** | 2 个 o + 1 个 θ | 3 |
| **d 夸克** | 1 个 o + 2 个 θ | 3 |
| **质子** = uud | (2o+θ) + (2o+θ) + (o+2θ) | **5o + 4θ = 9** ✅ |
| **中子** = udd | (2o+θ) + (o+2θ) + (o+2θ) | **4o + 5θ = 9** ✅ |

**★ 独立复算：**
```python
u = {'o': 2, 'θ': 1}
d = {'o': 1, 'θ': 2}
proton = u+u+d → o: 2+2+1 = 5, θ: 1+1+2 = 4   → 5+4 = 9  ✅
neutron = u+d+d → o: 2+1+1 = 4, θ: 1+2+2 = 5   → 4+5 = 9  ✅
```
**⇒ 复算通过。omegon 数是 9（= 3 夸克 × 3 omegon）。**

### 1.2 omegon 的电荷（原文第 182 行）

> *"o and θ omegons carry electric charges of **+5/9 and −4/9**, respectively
> (in units of the charge of an electron)."*

**★ 独立复算（这是最漂亮的一步）：**
```python
# 质子 = 5o + 4θ
charge_p = 5*(5/9) + 4*(-4/9) = 25/9 - 16/9 = 9/9 = +1  ✅
# 中子 = 4o + 5θ
charge_n = 4*(5/9) + 5*(-4/9) = 20/9 - 20/9 = 0/9 = 0   ✅
# u 夸克 = 2o + 1θ
charge_u = 2*(5/9) + 1*(-4/9) = 10/9 - 4/9 = 6/9 = +2/3  ✅
# d 夸克 = 1o + 2θ
charge_d = 1*(5/9) + 2*(-4/9) = 5/9 - 8/9 = -3/9 = -1/3  ✅
```

**⇒ 四组全部精确命中。这是一个**内部一致**的电荷分配方案。**

**★ 九分之几的分母是「为什么是 9」的关键** —— 
因为一个夸克装 3 个 omegon，一个质子装 9 个 ⇒ 电荷必须能被 9 等分。
**⇒ 用 9 作分母，是模型**自己要求的**，不是硬凑的。**

### 1.3 颜色-影（colour-shade）结构（原文第 182、200–203 行）

> *"Omegons have **nine 'colour-shades'** — dark, medium, and light shades of
> the colours red, blue, and green.
> A quark of a given colour is composed of omegons with dark, medium,
> and light shades of that colour."*

**★ 结构：**
```
3 种颜色（红蓝绿）× 3 种深浅（深中浅） = 9 个 colour-shade 态
```

**★ 规范群链（原文第 194、254 行）：**
> *"SU(10)_c is allowed to be spontaneously broken by the Higgs vacuum
> ... to leave **U(1) × SU(9)_c** as an exact local gauge symmetry."*

| 阶段 | 规范群 | 说明 |
|------|--------|------|
| 初始 | **SU(10)_flavour × SU(10)_colour** | 10 代 |
| 破缺后 | **U(1) × SU(9)_c** | 第 10 个颜色态 = 轻子 |
| 再破缺 | SU(3)_c × SU(3)_cs | 熟悉的 QCD 颜色 + 影 |

**★ 规范场计数（原文第 260 行）：**
> *"The **ninety-nine** vector gauge fields associated with SU(10)_c are made up of
> **nineteen superheavy bosons** ... and the **eighty** vector gauge fields of SU(9)_c"*

**★ 独立复算：**
```python
# SU(9) 的规范场数 = 9² − 1 = 80
# 19 + 80 = 99
# 而 SU(10) 的规范场数 = 10² − 1 = 99  ✅
```
**⇒ 复算精确通过。19 + 80 = 99 = 10² − 1。**

### 1.4 omegon = 磁单极子（原文第 210–212 行）

> *"The condition for topologically distinct Nielsen-Olesen vortices and
> **Dirac monopoles** to exist such that the former cannot be transformed into
> one another by continuous gauge transformations is that the **global gauge group
> should be multiply connected**.
> If this group is **SU(9)/Z₉** ... then **nine distinct vortices exist**...
> One corresponds to the ground state of the vacuum and consists of no vortex;
> the other eight correspond to **non-equivalent magnetic monopoles of
> monopole moment g₀, 2g₀, ..., 8g₀** (g₀ = 1/2e)."*

> *"Thus, **nine and only nine SU(9) monopoles form a magnetically neutral system**
> when embedded in a superconducting Higgs vacuum and bound by Nielsen-Olesen vortices."*

**★★ 这段是本模型的**理论核心**：**

| 步骤 | 内容 |
|------|------|
| 1 | 假设规范群是 SU(9)/Z₉（**多重连通**） |
| 2 | ⇒ 拓扑上存在 9 个不同的涡旋 |
| 3 | 其中 1 个是真空基态，8 个是磁单极 |
| 4 | **只有 9 个一起才是磁中性** |
| 5 | ⇒ 夸克 = 3 个磁单极的束缚态，质子 = 9 个 |

**★ 于是「为什么是 9」有了拓扑学理由**：
不是随便选的，而是「**只有 9 个才能合成磁中性系统**」这个约束逼出来的。

**★ 与 OC 的接口（Smith 的论证）：**
OC 的 U.P.A. 有两种（螺旋顺/逆时针，即**正/负**）——
**Phillips 把它们判为「通量源」与「通量汇」，即磁单极的正负。**

**★★ 但这里有一个**必须写明的时序问题**：**
- OC 的观察：**1895–1933**
- 狄拉克提出磁单极概念：**1931**
- ⇒ **OC 的早期观察（1895–1908）早于磁单极概念 36 年**
- ★ 但 **OC 正文第三版出版于 1951 年**，而 Phillips 的书是 1980 年
- ⇒ 「正/负」的措辞是 1895 年就有，还是 1951 年改写进去的？**本系列无法判定**

**★ 判据九（`05` §5.3）：**「U.P.A. = 磁单极」涉及后设概念，
　　 即使时间差属实，也**只是「早于」，不是「预见」**。
**⇒ 判定：⚠️ 留待核对第三版与第一版的文本差异（记入待办）。**

---

## 二、★★ 两个基本假设（Phillips 如何「接管」OC）

### 2.1 假设内容

| 假设 | 内容 | 原文位置 |
|------|------|----------|
| **假设 I** | **U.P.A. = omegon**（属 SU(10) 基本表示，9 个色-影态） | Phillips 导论 / Smith 第 1285 行 |
| **假设 II** | ★ **观测扰动导致两个原子融合** | Phillips 导论（第 45 行） |

### 2.2 ★★ 假设 II 的关键措辞（英文原文，必须逐字）

**Phillips 导论第 45 行（由 Smith 撰写介绍）：**
> *"Besant and Leadbeater claimed to 'see' the atom **exactly as it was**;
> they could not have known that **the very act of focusing their attention upon it
> and checking its 'wild gyrations' psychokinetically must inevitably cause perturbation.**
> Phillips has carefully analysed the nature of this perturbation and concludes that
> **it would induce the fusion of two atoms of an element into a plasma of free
> omegons and quarks**, which then interact to form stable, quasi-nuclear systems
> of bound particles.
> The new patterns derived by application of the rules of theoretical physics
> **tally perfectly** with the diagrams of Occult Chemistry.
> **With hindsight** it can be seen that there are many pointers to this
> **doubling-up phenomenon** in the text of Occult Chemistry."*

**★★★ 这段话里有四个必须拆开的点：**

| # | 原文措辞 | 含义 | 判定 |
|---|----------|------|------|
| 1 | 「**the fusion of two atoms**」 | **两个原子**融合（不是两个核） | ⚠️ 与 Smith 书的「两个核」表述不同 |
| 2 | 「**tally perfectly**」 | 「完美吻合」 | ⚠️ 主观判断，需核对 |
| 3 | 「**With hindsight**」 | ★ **「事后看来」** | ★★★ **作者自己承认这是事后视角** |
| 4 | 「**doubling-up phenomenon**」 | 「加倍现象」= 那个 ×2 | ★ 这是**为补 6 倍而引入的机制** |

**★ 第 3 点最重要**：「With hindsight」（事后看来）——
**Smith 自己在导论里写明：这是**回头看**才发现的「线索」。**

**★★ 这正是判据七所谓「事后拟合」的教科书级标本：**
- 不是「理论预言了观测」
- 而是「**观测放进去，理论调出来**」
- 而且**理论需要什么，观测就被读成什么**（需要 ×2 ⇒ 读出「加倍现象」）

**★ 更关键的是**：Smith 自己给出了这个 ×2 的来源描述 ——
「**imperative reinterpretation of the E.S.P. data**」（强制重新解释 ESP 数据）。
**⇒ 两个说法合起来就是完整链条：**
```
理论要求 ×2 → 于是「事后看来」观测里有「加倍现象」→ 这个「加倍」是重新解释出来的
```

### 2.3 ★ 与 Smith 书表述的差异（必须并列）

| 出处 | 「加倍」发生在哪一级 |
|------|---------------------|
| **Phillips 导论**（英文原文） | *"the fusion of **two atoms** of an element"* → **两个原子** |
| **Smith 书**（中译本） | 「**两个核**的核子所构成的复合系统」→ **两个核** |

**★ 这是一个值得记录的文本差异。**
**⇒ 两种表述给出的 Anu 数公式不同：**
```python
# 若「两个原子」：N = 2 × (18A) / 2 … 需进一步明确
# 若「两个核」：  N(A₁,A₂) = 9A₁ + 9A₂
#                  N(A)     = 18A       （同核素）
```

**★ 「两个核」的读法给出的 18A 规则，恰好能覆盖全表。**
**⇒ 判定：⚪ 两个表述并存，本系列按「两个核」处理（因为它能对上 `03` §4 的全表数据），
　　 但注明 Phillips 原文写的是「两个原子」。**

---

## 三、★ factor of six 与 factor of two 拆解（本册核心）

### 3.1 完整的倍数链条

```
OC 观测：氢 = 18 个 Anu
现代物理：质子 = 3 个夸克
                    ↓
            18 / 3 = 6  ← 「factor of six」
                    ↓
          Phillips：夸克不是基本的，每个夸克 = 3 个 omegon
                    ↓
            3 × 3 = 9 omegon / 质子
                    ↓
            18 / 9 = 2  ← 「factor of two」
                    ↓
          「强制重新解释 ESP 数据」：观测到的是「两个核/原子的复合体」
                    ↓
            9 × 2 = 18  ✅ 对上 OC
```

### 3.2 ★ 两个「桥」的性质完全不同（这是本册最重要的判定）

| | **第一个桥（×3）** | **第二个桥（×2）** |
|---|---|---|
| 提供者 | **理论** | **对观测数据的重新解释** |
| 性质 | 可独立讨论的物理假设（复合夸克模型） | **事后调整** |
| 可否检验 | ⚠️ 可（高能散射的形状因子） | ❌ **不可**（需回到 1932 年的观测现场） |
| 原文自述 | 「This theory thus provides for nine omegons」 | ★「**imperative reinterpretation of the E.S.P. data**」 |

**★★ 结论：**

**第一个桥（×3）是一个**正经的物理假设** —— 
Phillips 把它写成论文发在 *Physics Letters*（1979），
并且**预言了可测的后果**（原文第 219 行）：
> *"Agreement is better for composite quarks than for point-like quarks.
> **We predict: μ_u = 1.26 μ_N** (0.67 μ_N for point-like quarks),
> μ_d = −1.10 μ_N (−0.33 μ_N) and μ_s = −0.63 μ_N (−0.33 μ_N)."*

**⇒ 这是可检验的预言**（质子/中子磁矩比）。
**★ 原文还说（第 225 行）：**
> *"in agreement with SLAC data"*

**⇒ 但注意：这些预言是**关于夸克复合性的**，与 OC 无关。**
**⇒ 即使复合夸克模型对，也不能推出「OC 看到了 omegon」。**

**★★ 第二个桥（×2）完全不同 —— 它不是一个假设，而是一次**读数调整**。**
**⇒ 它没有任何独立的可检验后果。**
**⇒ 它的唯一功能是**让 9 变成 18**。**

**★ 判定（判据七）：**
- 「3 → 9」：**理论建构**，可独立评估 🟡
- 「9 → 18」：**事后拟合**，该数字**不构成对 OC 的独立支持** ❌

**★★ 一句话总结本册：**
> **OC 与现代物理之间的那个 6 倍缺口，
> 　第一个 3 倍是 Phillips 用理论买的，
> 　第二个 2 倍是 Smith 承认用「重新解释数据」买的。
> 　—— 两次都不是观测本身提供的。**

---

## 四、★ omegon 模型的内部质量（该给的分数也要给）

**★ 本系列不因为它的动机有问题就否定它的技术内容。**
**⇒ 模型内部有不少真功夫，应该如实记下：**

### 4.1 内部一致性检查（复算）

| 项目 | 复算 | 结果 |
|------|------|------|
| 质子电荷：5o + 4θ | 5(5/9) + 4(−4/9) = 9/9 | ✅ +1 |
| 中子电荷：4o + 5θ | 4(5/9) + 5(−4/9) = 0 | ✅ 0 |
| u 夸克：2o + 1θ | 10/9 − 4/9 = 6/9 | ✅ +2/3 |
| d 夸克：1o + 2θ | 5/9 − 8/9 = −3/9 | ✅ −1/3 |
| omegon 数/质子 | 3 夸克 × 3 | ✅ 9 |
| 规范场 19 + 80 | 10² − 1 = 99 | ✅ 99 |
| SU(9) 规范场 | 9² − 1 = 80 | ✅ 80 |
| 磁单极数 | SU(9)/Z₉ 九重连通 ⇒ 9 个（含真空态） | ✅ 自洽 |

**⇒ 八项复算全部通过。模型的算术是干净的。**

### 4.2 ★ 与 OC 的「对撞点」（Smith 自己列出的）

**★ Smith 在导论里列出了「OC 提前说对了」的清单（第 136 行）：**

> *"How could two individuals possessing only a layman's knowledge of physics
> invent descriptions of particle behaviour that vividly portray the
> **Larmor precession of spinning, charged particles in magnetic fields** —
> descriptions that needed a knowledge of the **intrinsic spin** of particles
> but were published prior to the experimental discovery of the spin of the
> electron and the proton?
> For example, **precessional motion of 'Hydrogen Triangles'**
> (identified later in this work as protons) was described during observation
> of the OH group in **1924**, before Uhlenbeck and Goudsmit proposed that
> the electron had an intrinsic angular momentum and before the spin of the
> proton was experimentally detected.
> Also, how could the investigators fabricate an observation of the alignment,
> parallel to an external, static electric field, of the spin axes of various U.P.A.'s?
> It is highly unlikely that they could have known that
> **spinning magnetic charges possess electric dipole moments**
> (the concept of magnetic charges is not explicitly referred to in their published work),
> nor could they have decided to make magnetic monopoles out of U.P.A.'s,
> because their..."*

**★★ 这段是 Phillips 方的**最强论证**，必须完整呈现，也要完整检验。**

**★ 论证结构（拆成可检验的步骤）：**

| 步骤 | 主张 | 时间 | 判定 |
|------|------|------|------|
| 1 | OC 在 **1924** 年描述「氢三角形」的**进动运动** | 1924 | 🟡 需核原文 |
| 2 | 电子自旋（Uhlenbeck & Goudsmit）提出于 **1925** | 1925 | ✅ 史实 |
| 3 | ⇒ OC 早了 1 年 | — | ⚠️ **只有 1 年** |
| 4 | OC 还描述了「自旋轴平行于外静电场排列」 | ? | 🟡 |
| 5 | 「自旋磁荷有电偶极矩」这个概念，OC 不可能知道 | ? | ⚠️ 需核 |

**★ 第 3 步的问题最大**：
**1924 年 vs 1925 年，只差 1 年。**
而 **Larmor 进动本身是 1897 年的经典结论**（Larmor 定理）——
**任何旋转的带电粒子在磁场中都会进动，这是**19 世纪的经典电动力学**，
根本不需要「自旋」概念就能描述。**

**⇒ 判定：⚠️ 「早了 1 年」不足以排除「经典 Larmor 进动」这个更简单的解释。**
**⇒ 判据七第⑤步（冗余性核对）：有一个**更简单、不需要新概念**的解释存在。**
**⇒ 按奥卡姆剃刀，不采纳「提前预见自旋」这一读法。**

**★ 第 5 步是唯一真正有意思的**：
「自旋磁荷有电偶极矩」这个命题 —— 
若 OC 真的描述了「磁单极自旋 ⇒ 电偶极矩」，那确实很特别。
**⇒ 但 Smith 自己加了括号说明**：
> *"the concept of magnetic charges is not explicitly referred to in their published work"*
（他们的出版物里没有明确提到磁荷概念）
**⇒ 即：这是**Phillips 的解读**，不是 OC 的文本。**

**★★ 判定：🟡 待核。**
**⇒ 记入待办：需回 OC 1924 年关于 OH 基的原文，核对「进动」描述的具体措辞。**

---

## 五、★★ 本册对判据体系的贡献

### 5.1 ★ 判据十（本册新增，是对判据七的细化）

> **判据十：把「倍数缺口」拆开 —— 每一个倍数，都要问它是谁提供的。**
>
> | 提供方 | 性质 | 可否作为支持 |
> |--------|------|-------------|
> | **观测本身** | 第一手事实 | ✅ 可以 |
> | **独立理论** | 可检验的假设 | 🟡 部分可以 |
> | **对观测的重新解释** | 事后调整 | ❌ **不可以** |
>
> **★ 判据：若某个倍数需要「重新解释观测数据」才能得到，
> 　　　则整条对应关系**不构成对原观测的独立支持**。**

**★ 应用实例：**

| 对应关系 | 缺口 | 谁提供 | 判定 |
|----------|------|--------|------|
| OC 18 Anu ↔ 9 omegon | ×2 | **重新解释观测** | ❌ 不构成支持 |
| OC 18 Anu ↔ 3 夸克 | ×6 | 理论(×3) + 重新解释(×2) | ❌ 不构成支持 |
| Lyne 1,058 倍 | ×1000 | **单位错读**（kcal 当 cal） | ❌（见 `07`） |
| Smith 18A 规则 | ×18 | **观测 + 除数预先设定** | ⚠️ 需分开评（见 `03` §3.3） |

### 5.2 ★ 判据十一（时序核对，配合判据九使用）

> **判据十一：凡「前人提前说对了」的命题，必须核对：
> 　　　　（a）那个概念**被提出**的年份；
> 　　　　（b）那段文本**被发表**的年份；
> 　　　　（c）若文本经过**再版修订**，则该文本不能作为「提前」的证据。**

**★ 本项目立即适用的一例：**

| 命题 | 观察年份 | 概念提出 | 文本发表 | 问题 |
|------|----------|----------|----------|------|
| U.P.A. = 磁单极子 | 1895 | 1931（狄拉克） | **1951（第三版）** | ⚠️ **修订版可能回填** |
| 氢三角形进动 = 自旋 | 1924 | 1925 | **1951（第三版）** | ⚠️ 同上 |

**★★ 这一条极重要** —— OC 的「正文」是 **1951 年第三版**，
比观察（1895–1933）晚了 **18 年以上**。
**⇒ 在这 18 年里，原作者完全可能把后来的科学概念写进描述里。**
**⇒ 要证明「提前」，必须核对**第一版（1908）/ 第二版（1919）**的原始措辞。**

**★ 记入待办：需获取 OC 第一版 / 第二版与第三版的文本对照。**

### 5.3 ★ 一条对 Phillips 有利的诚实记录

**Phillips 的书里有不少「limitations」类声明**（原文第 136 行段落末尾被截断处、
以及第 2003 行附近）。**Smith 的导论也写了：**
> *"It stretches credulity to concede that omegons, conceived by Phillips in the
> mid-1970s, and the physicist's quarks had been 'seen' extra-sensorily
> some eighty years previously."*
> （**要在 80 年前就被「看到」，这已经是在考验人的信任了。**）

**★ 作者自己说「这有点难以相信」** —— 这是学术诚实的一面。**
**⇒ 本系列记下这一点。**
**⇒ 但这也意味着：**连作者都知道这个对应是勉强的**。**

---

## 六、小结

### 6.1 可直接引用的（🟡 原文属实）

1. **倍数的两段拆解**：3 → 9（理论 ×3）；9 → 18（**重新解释观测** ×2）
2. ★ **Smith 原话**：*"the still persisting factor of two was bridged by
   **imperative reinterpretation of the E.S.P. data**"*
3. ★ **Phillips 原文**：*"**With hindsight** it can be seen that there are many pointers
   to this **doubling-up phenomenon**"*
4. **omegon 组成**：u = 2o+θ，d = o+2θ；质子 = 5o+4θ，中子 = 4o+5θ
5. **电荷**：o = +5/9，θ = −4/9（四组电荷复算全部通过）
6. **规范群链**：SU(10) → U(1)×SU(9)_c → SU(3)_c×SU(3)_cs；99 = 19 + 80
7. **磁单极**：SU(9)/Z₉ 九重连通 ⇒ 只有 9 个才磁中性
8. **doubling 的机制**：观测扰动 ⇒ 原子融合 ⇒ 看到的是复合体

### 6.2 必须加限定的

- ⚠️ ★ **「With hindsight」（事后看来）** —— 作者自己承认是事后视角
- ⚠️ ★ **×2 靠「重新解释数据」** —— 不是观测提供、不是理论预言
- ⚠️ **「两个原子」vs「两个核」** —— Phillips 导论与 Smith 书表述不同
- ⚠️ **假设 II 修改了观察对象**（一个原子 → 两个原子/核的复合体）
- ⚠️ **「提前说对了」只有 1 年差距**（1924 vs 1925），且 Larmor 进动是 1897 年经典结论
- ⚠️ **OC 正文是 1951 年第三版**，比观察晚 18 年 ⇒ **可能回填**（判据十一）
- ⚠️ ★ **连作者自己都说**「It stretches credulity」（这已经是在考验信任）

### 6.3 ★ 本册对本项目主线的直接贡献

| 项目文件 | 本册提供的 |
|----------|-----------|
| `joe cell/08`「正/负 Anu」 | 🟡 Phillips 把正/负判为**磁单极的通量源/汇**（三种用法中的①） |
| `joe cell/09`「H₂ = 变体1+变体2」 | ★ **假设 II 的「两个原子融合」在形式上最接近** —— 但它改对象了 |
| `joe cell/11`「配对假设检验」 | ★★ `05` 的「观测扰动」在本册有完整的理论机制（原子融合） |
| 本项目判据体系 | ★ 新增**判据十**（倍数拆解）与**判据十一**（时序核对） |

### 6.4 ★★ 一句话总结

> **Phillips 的模型在技术上相当扎实（八项复算全通过），
> 　但它与 OC 的连接处是靠两次「买入」完成的：
> 　第一次买的是理论（×3），第二次买的是**对数据的重新解释**（×2）。
> 　而 Smith 把这件事写进了导论，用的是自己的话。
> 　—— 这份坦白，比模型本身更有价值。**

---

> 下一册：`07_Lyne_以太物理学.md` —— Lyne 的原子氢炉与 1,058 倍。
