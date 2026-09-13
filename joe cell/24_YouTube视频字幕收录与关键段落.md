# 24 · YouTube 视频字幕收录与关键段落核对（reddpill 五集 + 1996 访谈 + 关联频道）

> **来源**：老师 2026-09-13 提供两批 YouTube 链接
> **收录方式**：★ **只取字幕，不下载视频**（老师指示）——字幕经 `yt_subtitle_extractor.py` / `yt-dlp` 提取为 SRT → 纯文本
> **归档**：`joe cell/_外部访谈资料/reddpill_5集视频/` ＋ `joe cell/_外部访谈资料/youtube视频字幕/`

---

## 〇、本批档案

### 0.1 A 批：reddpill 五集（**Joe 本人演示**）—— 老师提供的 5 个链接

| # | 标题 | 时长 | 上传 | 链接 |
|---|---|---|---|---|
| 1 | **Part 1 - Joe Cell. The basics** | 13.7 分 | 2015-04-11 | `v=dK7TI4JmPGU` |
| 2 | **Part 2 - Joe Cell. Early prototypes** | 14.4 分 | 2015-04-11 | `v=do0S7J3BEIA` |
| 3 | **Part 3 - Joe Cell. Experimentation** | 13.5 分 | 2015-04-11 | `v=aOr4dcpvaDA` |
| 4 | **Part 4 - Joe Cell. The Car** | 14.9 分 | 2015-04-12 | `v=pH2E2PZ-7yI` |
| 5 | **Part 5 - Joe Cell. Observations** | 15.1 分 | 2015-04-13 | `v=9av-P1DdASo` |

- 上传者：**reddpill**；全部有**英语自动字幕**（已提取）
- 总时长约 **71.5 分钟**；转录文本合计 **48,477 字符**
- 内容性质：★★ **Joe 本人（或其团队）向外来访者演示水电池装车运行** —— 含**水怎么处理**与**现场观察到的异常现象**
- ★ 视频本体：老师指示**不下载**（只为内容）；Part 1 的 mp4 曾试下载已留存本地（128 MB，**不入库**），其余 4 集未下载

### 0.2 B 批：老师新给的 3 链接 + 关联频道

| # | 标题 | 时长 | 频道 | 上传 | 字幕 |
|---|---|---|---|---|---|
| 1 | **Joe Cell Energy Power Test Cell**（★ stage3/heartbeat 那条） | 95 秒 | joecellenergy | 2009-03-16 | ❌ **无字幕**（见 §六） |
| 2 | **joe cell talks 7** | 9.5 分 | Daemon Nice | 2013-04-10 | ✅ en 自动 |
| 3 | ★★ **Joe's Energy Cell (interview 1996)** | **58.3 分** | EMERSON5 | 2023-03-28 | ✅ en 自动（**104 KB 字幕**） |
| 4-12 | @**HydrogenTechnology** 频道 **9 条**（见 §五） | 1–4 分 | HydrogenTechnology | — | ✅ en 自动 |

> 老师对 2A2LHkqnNEQ 的介绍（原文）：
> 「This is the power cell, tuned and charged to align perfectly and deliver its "heartbeat"，
> **这是 Joe Cell stage 3 的证明**」——该句即视频**描述栏原文**（见 §六）。
>
> 老师补充介绍（抄录）：「Joe is self educated backyard inventor who has an intuitive feel
> for what he does. Wanting to produce hydrogen to run his car he figured out something that
> is quite different and claims that through his process he can **tune the harmonics of his
> cell to maximize the extraction of the hydrogen**.」

### 0.3 归档清单

| 目录 | 内容 |
|---|---|
| `reddpill_5集视频/` | 5 个 `.srt` + 5 个 `.txt`（纯文本）+ **`reddpill_5集_全文.txt`**（合并 48,477 字符）＋（Part1 mp4 本地留存，⚠️ 不入库） |
| `youtube视频字幕/` | 11 个 `.srt` + 11 个 `.txt` + `_小视频合集.txt`（12,310 字符）+ `_urls.txt` |
| 工具 | `D:\AAA我的文件\youtube视频+字幕下载工具\yt_subtitle_extractor.py`（★ 纯字幕提取，老师所提示；`--batch`/`--text` 均可用） |

> ⚠️ **字幕质量说明**：自动字幕对 1990 年代录像 + Joe 口音识别**错误较多**
> （如 `Mt George`→"M George"、`cell`→"sell/thece"、`twice`→"ice"）。
> 本库引用时**以语义可确认为准**，凡不确定处标注 [原文如此]。

---

## 一、★★★ A 批核心 1：reddpill 五集的「真空/负压」一手演示

### 1.1 五集概要（按内容脉络）

| 集 | 概要 |
|---|---|
| **Part 1 · basics** | 展示单元实物：「**我开着它下来的，一滴汽油没用，从这儿到 Mt George 大约用了 1~1.5 杯水**」；介绍 plate system 与 Ron Davis 教授的往事 |
| **Part 2 · prototypes** | 原型尺寸/间隙对比；★ **pressure vs vacuum 两型对比**（见 1.2） |
| **Part 3 · experimentation** | 极板接法实验：负-正跨接 →「产气量剧增」；电流减半/产气翻倍的观察 |
| **Part 4 · The Car** | 第三方摄制组现场拍摄装车（「a place in Australia which we will remain nameless」）；单元结构描述 |
| **Part 5 · Observations** | ★★ **异常现象集**：深充、真空表读数、3 点钟自深充、蓝焰内爆打砖实验 |

### 1.2 ★★★ 「拔机油尺就熄火」——负压现象的一手描述（Part 2）

> 「…**instead of pressurizing fume out** from your positions around your pollution positions,
> **it then has a vacuum**… if you pull the **dipstick** out, **the motor will stall**;
> if you loosen off the **filler cap** (oil filler cap), **the motor will stall**.
> That's with this **solid unit**… **solid unit has a vacuum, pull inwards.**
> You can put your **finger over the little tiny hole in the tapper cover** …
> and **the motor runs smooth**; take your finger off, **she'll start shaking like anything,
> can stall out — she has a suction on your finger**…」

中文：

> 「……它**不是往外压**，而是**变成真空**……**拔出机油尺，发动机会熄火**；
> **拧松机油加注盖，发动机会熄火**。这是**实心（不锈钢）单元**的表现——
> **实心单元是真空、向内吸**。你把**手指堵在气门室盖的小孔**上，**发动机运转平顺**；
> 手指一拿开，**她就开始剧烈抖动、可能熄火——她吸住你的手指**。」

### 1.3 两型单元对比（Part 2，★ 关键的现场对照）

| 单元类型 | 现象 | 其他表述 |
|---|---|---|
| **poly（塑料/可膨胀型）** | **pressure out**（往外压） | 「it can expand…under vacuum will expand instead of contracting」 |
| **solid（实心不锈钢型）** | **vacuum pull inwards**（向内吸） | 「**with a stainless one you can increase your performance three times over**」（宣称） |

- 另描述：实心单元让「**manifold vacuum**（进气歧管真空）」明显 ⇒ 松油门/踩刹车时感受不同（"it sort of works the opposite way"）
- 「任何压力都没有、事实上是真空对着发动机，**no oil usage**（不耗机油）」

### 1.4 ★★ 温度异常（Part 2）

> 「your motor should run somewhere around about **90**（温度表）… this is a solid unit…
> **when you hooked up the solid unit to it she went to instant cold — the motor just run
> dead cold, and it wanted to perform better on dead cold. You couldn't get it hot.**
> And you take it off and put it back on the (petrol), she would come straight back up to
> your medium or normal running… **she would even override your thermostat**…」

中文：

> 「发动机正常应该在 **90 度**左右……**接上实心单元后，她瞬间变冷——发动机跑得冰冷，
> 在冷态下反而表现更好，你根本热不起来**。把它拿掉换回（汽油），温度**立刻回到正常**——
> **她甚至能盖过节温器（override your thermostat）**。」

★ 这段是老师主张「**排气口冰冷 / 发动机冷**」的视频一手语境（对照实验完整：装上=冷、取下=恢复）。

### 1.5 ★★ 「深充单元」与电压数据（Part 5 + Part 1）

**深充描述**（Part 5 开头）：

> 「**very very deep charge unit which will run all day** — you can turn it off and leave it
> for hours… and you can come back, **no power on**, turn ignition on, hit the key, **instantly
> the vacuum goes onto that unit — it is a charge unit, it runs, it starts.**
> You leave it overnight and somewhere between… about **3:00 in the morning the unit seems to
> go deep by itself**… you can run it up to 12:00 at night and the vehicle will still start.」

**电压/电流数据**（多段现场读数）：

| 场景 | 读数 |
|---|---|
| 充电后静置 | 「stabilizing about **170 milliamps**…dropped down to below 1 volt…voltmeter is reading **700 m volts**」 |
| 断电衰减（另一段） | 「**13 volts approximately**…Now disconnecting. It's dropping down to…**1.3**…Now you got **1.2 volts**. **There's still bubbles being formed in the chamber**…**1.14 volt. Still gas coming**」 |
| 单元启动（Part 1） | 「down to **1.01 volts**…」 |

⇒ ★ **「断电后留下 1~1.3 V 且仍产气」** —— 与库内 `03`「活细胞约 1V」（断电静置 24h）**同量级**、
与老师说的「**正负管材料本身产生自然电位差 1.5V**」**同量级**。★ 三处独立记录相互印证（数字量级一致）。

### 1.6 ★ 水的处理（配方与操作，Part 2/4/5）

| 项 | 原话 | 备注 |
|---|---|---|
| **配方（真空表演示段）** | 「an outer mesh **filled with water, a teaspoon of caustic in about 4 L**… so this is about **1/4 teaspoon to 2 L**」 | ★「caustic」= 氢氧化钠（与后来 Richard 的 NaOH 配方同类） |
| **水的用量（行车）** | 「about **a cup to a cup and a half** of water to go from here down to Mt George」 | 行车消耗的宣称 |
| **水的状态变化** | 「all the water in the container **turned milk white**… when you take the battery off… **goes back to clear water**」（Tape 1 已录，本批复现） | 「奶白 ↔ 清澈」可逆 |

> ⚠️ 按判据⑬核对：本条「water + caustic」与库内 `03` 的「（另一处）雨水+柠檬汁」配方是**两种不同配方**
> —— 两处**并列保存**，不做合并。

### 1.7 ★ 蓝焰「内爆」打砖实验（Part 5）

> 「the tip had a **very fine little imploding blue flame, very very short imploding —
> it was not exploding** — and we applied that down onto the brick and what happened was
> the brick started to swirl and gurgle up and **she blew a clean hole**…
> the same gas blew straight through and out there as **the implosion** seems to be that
> while it was inflating and we pushed it down through the brick, **she seems to pull up the
> melted ceramic brick upwards and twirl around the top, not out the bottom**…」

⇒ 现场演示：**内爆火焰在砖上打洞，且熔融物被"往上拉"而非往下吹**
（当事人描述；属**现象记录**，非受控实验——标「待独立验证」）。

### 1.8 ★ 另外两个细节（附录）

- **铜管污染只在正极侧**（Tape 1 已录）：「your copper tube which was polluted — dark green crystallized — further up the tube was **clear and clean** because it was not there near where the **positive charge stuff** is」
- **一杯水行车**（Part 1）：见上表

---

## 二、★★★ B 批核心 1：1996 访谈（58 分钟）——「特斯拉线圈 90° 尖峰」

> ★★ **这是老师点题「特斯拉线圈 90° 相位差点火」的原话所在**（`Joe's Energy Cell (interview 1996)`，
> 由 **Naomi** 采访拍摄、对话中另有一位提问者 Peter）。

### 2.1 完整引文（按对话顺序）

**【A】火花从哪来（@7845）**：

> 「…bringing it back to the — where's his spark come from — **the coil, which is called the
> Tesla coil**. Coil in the cars and everything else… **it's got a primary and a secondary
> winding**, and what happens is… your **negative coming off your block goes through your
> points, your condenser**, and then up into your coil…」

**【B】90 度尖峰（@8542）**：

> 「…it comes out negative. Now you don't use any of them — none of them are used up to
> actually make the **AC Spike** that comes out the **center of the coil**. It is a
> **90 degree Spike**… **check that out — it's a 90 degree Spike.** So — and on Commodore
> it's just giving for you roughly… **Commodore has used something called waste spark
> management**, Ford used it for a while, wouldn't pay (holder)…」

**【C】正负不是被"用掉"的，是建场的（@12834）**：

> 「…**your spark coming out of your coil is a 90 degree Spike. You're not using the positive
> or the negative for your coil — you're using them there to SET UP THE FIELD, and when you
> COLLAPSE ONE SIDE OF THE FIELD, you get that going across**…」

**【D】线圈中心 = 90 度（@28683 / @29196）**：

> 「what is a coil? … it's called the **Tesla coil**, it's got a primary and a secondary…
> **what's in the middle of those windings? — Nothing.** … you drive these two fields to it,
> and you **collapse one side of the fields** — you get **not a DC, you get an AC Spike**
> coming out… the DC might have a positive or negative charge… but **that one out the center
> at 90 degrees — what has it got? You just check that out yourself.**」

**【E】同现象类比（@44376）**：

> 「…see, that's what a coil does — car coil **goes out through the center**… **not in and
> out — it goes out a different direction, 90 degree Spike**. Same thing happens on the
> **starter motors when you wind them up too far — they end up with a new energy, a new
> frequency, and a new spark… a new kind (of) the spark, because there's no spark and it's
> not being cut, it's not being pulsing…**」

### 2.2 ★ 结构还原（Joe 的链条）

```
点/电容 → 初级线圈 → 次级线圈 → 「中心的输出」不是正、不是负
        → 而是「90 度尖峰（90 degree Spike）」/ AC 尖峰
        ⇐ 前提：正负两路只是「建立磁场」；一侧磁场「塌缩（collapse）」时产生此尖峰
```

★ 关联对照：**同一「90 度」主题**在 `23` 号文档（JOE TALKS）里也出现过（Tape 1：
「somewhere around eight to twelve degrees before the top of the stroke…」是**另一处**正时主题；
而 "eighteen to twenty"、"fifty degrees" 等同属「正时数字谱」）。
⇒ **两者应分开记**：**「90° 尖峰」= 点火线圈输出特征**（本节）；**「8–12°/18–20°…」= 分电器正时**（`23 §一`）。

### 2.3 ★★ 与老师提示的对应

| 老师提示 | 1996 访谈中的对应 |
|---|---|
| 「**特斯拉线圈**」 | ✅ 原话：「the coil, which is called the **Tesla coil**」 |
| 「**90° 相位差**」 | ✅ 原话：「it is a **90 degree Spike**」「out the center **at 90 degrees**」 |
| 「**点火**」的机制位置 | ✅ 原话：「you're not using the positive or the negative… you're using them to **set up the field**, and when you **collapse one side of the field**, you get that going across」⇒ 即**「场塌缩 → 尖峰 → 点火」** |

---

## 三、★★ B 批核心 2：1996 访谈的「整个系统极性反转」（Suzuki 车）

> 观众来信（Joe 当场读出来）：

> 「…to answer your question you posed in the **Suzuki video** — I just wanted to tell you
> firsthand that **I figured out what you did in the Suzuki truck: you have REVERSED THE
> POLARITY OF THE ENTIRE SYSTEM**…」

Joe 的回应（片段）：

> 「(that's not a question) **I told you — we were dipper（颠倒的）**…」

⇒ ★★ 1996 年访谈确认：**Suzuki 卡车上 Joe 做的是「整个系统的极性反转」**。
这与库内主题簇（`18 §三` 正负极、反接电池、`talks 7` 的「polarity 讨论」）**同源**。

> ⚠️ 安全判据不变（`18 §三`）：**接反 = 筒体蚀刻 + 短路 + 爆炸风险**（理由是电化学与电气，不是"磁化"）。
> 本节的记录属「Joe 做过什么」的史料，**不构成操作建议**。

### 3.1 附带：正时与「六度」

- 「on the Commodores they're far at **six degrees before top (dead) Centre**… they fire」（waste spark 系统）
- 「the **positive is fired then into the exhaust at six degrees before top**…」
- 「say **six degrees before top dead center** because there's top dead center…」
- 「when you turn the key off — where is your actual spark or frequency going? …」

⇒ ★ 「六度」是该访谈中反复出现的正时数字（Commodore/waste-spark 语境）；
与 `23 §一`「正时数字谱」**合并记谱**（该谱新增 6° 一项，并注明机型语境 = Commodore waste spark）。

---

## 四、★ B 批核心 3：`joe cell talks 7` —— Joe 现场「验收」他人复刻品

> 内容：Joe 在现场检查一个叫 **Peter** 的人做的 cell（"this is a p-cell… peter melbourne"）。
> ★ 性质：**失败诊断清单**（Joe 逐条指出为什么这个复刻品不行）。

### 4.1 Joe 的失败原因清单（现场指认）

| # | Joe 指出的问题 | 原话要点 |
|---|---|---|
| 1 | **不锈钢种类混用** | 「you've got **three different kinds of stainless** in there」 |
| 2 | **用磷酸作电解液 → 吃掉铬、粉化** | 「I was using **phosphoric acid** — that's turned around and it's **eating all the chromium** out of there… that's powdering up」 |
| 3 | **绝缘子被击穿 / 极板底部短路** | 「the insulators… **they're dead shorting underneath the plates**… so it's not neutral plates in there — you've got active plates all the way」 |
| 4 | **焊缝（seams）与电弧** | 「you've got to **line it up. Look at all the seams. Seal them. Look at all the arcing**」 |
| 5 | **材料来源不明（蒸汽机残件）** | 「that's a (rum) off a steamer… there was copper rolled around it」 |

### 4.2 ★ 「中性板（neutral plates）」的正确定义（Joe 原话）

> 「they're called **neutral plates — neutral is not positive but not negative — which means
> **it will NOT break down**, and it will not cause anything to go to it; and if you had
> anything on a plate, **it would actually polish it up, it would clean it**…」

⇒ 「中性」= **不参与电解消耗、且能"清洁/抛光"极板**的第三种状态。
（★ 待与主流电化学对照——档案记录，不预判。）

### 4.3 ★ 「铝桌磁化」事件（1994/95，Joe 口述）

> 「…we can do aluminium and **magnetize it** — we've done that way back to '95…
> we had a whole table, **aluminium table — the whole damn thing is violently magnetic**…
> but **it's very easily discharged. People's bodies can discharge it very easily**…
> this guy walked in there and… **she's gone**（磁化消失）…」

⇒ ★ 这段是「**磁化**」主题的一手语境（与此前老师提到的"磁化"话题衔接）：
Joe 主张①铝可被（某种方式）磁化到「强烈磁性」；②**人体在场即可放电消磁**。
⚠️ 本库此前判据（铝顺磁体、电流磁场仅 ~20 μT）不变——**此段存为"主张的原话出处"**，标「待验证」。

### 4.4 其他：白泡 + 内爆 + 耳朵响（复现）

> 「when I added some electrolyte… you got the **white bubbles** and they really **cracked**…
> I like the **implosion**… did your **ears ring**? — oh yeah…」

⇒ 与 `23 §三`（内爆耳朵机制）★ **一致复现**（跨年份、跨拍摄者）。

---

## 五、★ B 批核心 4：@HydrogenTechnology 频道（9 条，别人做的实验）

| # | 标题 | 时长 | 要点 |
|---|---|---|---|
| 1-3 | HT7 氢氧分离演示 ×3 | 1–2.5 分 | 「hydrogen only」电解单元：**氧从侧边、氢从顶部**输出；点火演示 |
| 4 | **HHO Fuel Cell 17 plate** | 2.5 分 | ★ 参数：**17 极板**（+中性-中性+ 交替）；16 oz 水 + **<1/4 茶匙 NaOH**；12V、**~20 A**、**~2 L/min** |
| 5 | **Hydrogen Generator installed in 2003 Ford F150** | 3 分 | 装车（氢助燃）；★ **安全建议原话**：**「never install… directly wired to the battery」＋「always use at least a bubbler（防回火）」** |
| 6-7 | **电解液测试 Tap water vs NaOH（1/2）** | 3–4 分 | ★ 数据：**纯自来水 = ~5 A / 5–6 盎司每分钟**；**加 1/8 茶匙 NaOH = ~10 A / ~1 L/min** |
| 8 | ★★ **Joe Cell powering an LED after it's powered down!!** | 2.3 分 | **断电后 LED 仍亮**（两次重复演示）：「the joe cell is off, battery charger's off — **the LED is still on**」 |
| 9 | ★ **Joe Cell Pulsing Water in the center** | 1.8 分 | 中心水出现**脉冲现象**（观察者自述「never seen that before… don't really know what that pulsing was about」） |

★ **第 8 条**（断电后 LED 仍亮）为**独立第三方**的现场演示 —— 与库内「活细胞残留电位」主题（1–1.5 V 量级）
可对照；⚠️ 但「点亮 LED」与「残留 ~1 V」在电压上**尚未核对**（LED 需 1.8–3 V —— ⏳ **待查看视频/复现验证**）。
★ **第 9 条**（中心水脉冲）与 Richard 自己也无法解释 ⇒ 记为**未解释现象**（N=1）。

---

## 六、★ B 批核心 5：`Joe Cell Energy Power Test Cell`（2A2LHkqnNEQ）——无字幕

| 项 | 内容 |
|---|---|
| 标题 | **Joe Cell Energy Power Test Cell** |
| 频道 | **joecellenergy**（2009-03-16 上传，95 秒，观看 20,977+） |
| 字幕 | ❌ **无**（无手动、无自动——已核对） |
| 描述 | ★ **「This is the power cell, tuned and charged to align perfectly and deliver its "heartbeat"」**（老师引用句即此）＋ `www.joecellenergy.com` |
| 标签 | `joe cell` / `water fuel` / `water car` / `car runs on water` / `hho` |

⇒ ★ 老师称其「**Joe Cell stage 3 的证明**」——本库记录：**该视频存在、无字幕可取**，
其内容（"heartbeat" 演示）待以**视频画面/其他渠道**补充（⏳ 待办见 §八）。

---

## 七、仍未出现的（保持「本库未收录」，不降级不拔高）

| # | 主题 | 本批检索结果 |
|---|---|---|
| 1 | **「悬浮/飞行」** | ❌ 本批**全部 16 个字幕（含 58 分钟访谈）均未出现** levitation/floating 主题（`float` 命中均为 "floating unit" 等无关词）⇒ 「悬浮」仍只有转录稿层面的 **F-100** 提及（`23 §四`） |
| 2 | **「低温超导」** | ❌ 本批 0 命中（与 `23 §六` 一致） |
| 3 | **「最低怠速 60 rpm」** | ❌ 未命中（reddpill 有「16,000 revs」等，已录） |

> ★ 按判据⑰：**未命中 ≠ 不存在**。老师所指的「悬浮」视频若另有出处，继续待收录。

---

## 八、来源与待办

### 来源

| # | 内容 |
|---|---|
| S1 | ★ **老师 5 个 reddpill 链接**（`dK7TI4JmPGU` 等）→ 字幕已收录（`reddpill_5集视频/`） |
| S2 | ★ **老师 3 个新链接**（`2A2LHkqnNEQ` / `GFj0w1Cw5_4` / `Zcm85LBIICs`）→ 2 条字幕已收录；1 条无字幕 |
| S3 | ★ **@HydrogenTechnology 频道**（9 条）→ 字幕已收录 |
| S4 | 工具：**`yt_subtitle_extractor.py`**（老师提示位置 `D:\AAA我的文件\youtube视频+字幕下载工具\`）——已验证可用（**批量 11 条**） |

### 待办

1. ⏳ **「悬浮」视频**：若老师确认另有出处（YouTube 或其他），补收录。
2. ⏳ **2A2LHkqnNEQ 的「heartbeat」**：无字幕 ⇒ 如需内容，建议老师转述或提供其他版本链接。
3. ⏳ 「断电 LED 仍亮」：需核对 **LED 工作电压 vs 残留电位量级**（见 §五第 8 条注释）。
4. ⏳ 「铝磁化」：如做实验设计（对照：未处理铝 vs "处理"铝；测剩磁/吸引），另立文档。
5. ⏳ 1996 访谈还有约 40+ 分钟内容未逐段精读（本次为**主题式提取**）——如需可做全篇通读笔记。

---

> **编者按**：本批最值得标注的两件事——
> **①** 「**特斯拉线圈 90° 尖峰**」找到了原话（老师提示的机制话题，在 1996 访谈里）；
> **②** 「**拔机油尺就熄火**」的负压现场描述（reddpill Part 2），是「发动机吸成负压」这一主题
> **最具体的一次操作性描述**（机油尺/机油盖/手指三个"探针"效应）。
> 两者都属**逐字史料**；其物理判定仍按各行既有复算与判据**分层处理**（运行层 vs 机制层），
> **不作跨层互证**。
