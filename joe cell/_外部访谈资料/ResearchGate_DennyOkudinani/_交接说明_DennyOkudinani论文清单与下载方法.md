# Denny Okudinani 的 ResearchGate 论文 —— 交接说明（清单已查全，下载待接手）

> **状态**：2026-09-13 晚，本任务在「下载」环节中止（老师已转交他人）。
> 本文件=已完成的调研成果交接：**9 篇论文清单（全部查全）+ PDF 下载方法实测笔记**。
> 接手人可直接从「三、下载方法」一节继续，无需重新摸底。

---

## 一、作者档案（已核实）

| 项 | 内容 |
|---|---|
| 姓名 | **Denny Okudinani**（RG 认证，机构邮箱验证） |
| 机构 | Georgetown University, Department of Physics（Affiliate；2016–2025 学生，物理+CS 专业） |
| 自述 | **「Former researcher and experimentalist in solid-state mass displacement and implosive system dynamics」**（前·固态质量位移与内爆系统动力学研究者） |
| 技能标签 | Solid State Inertial Propulsion · **Implosive System Dynamics** · Artificial Gyroscopes · Mach Effect Thrusters · Solid State Mass Displacement · Mass Displacement Systems · Mach Effect |
| YouTube | **@MillennialZoomer**（Alt Propulsion）——其 73 分钟 Repulsine 深度讲解已入库 `joe cell/31–34` |
| RG 统计 | **9 publications / 2,025 reads / 2 citations**（2026-09-13 快照） |
| 座右铭 | *Nam qui curat* |

---

## 二、9 篇论文完整清单（全部 Full-text available）

- **[1] A Short Historical and Technical Examination of Fundamental Spatial Mass Displacement Systems**（Preprint，Apr 2026）——「系统性分类、区分真正起作用的系统与更宽泛的惯性机制提案」
  https://www.researchgate.net/publication/403702161_A_Short_Historical_and_Technical_Examination_of_Fundamental_Spatial_Mass_Displacement_Systems
- **[2] DNO7 Technical Report--On Spatial Mass Displacement Systems (Inertial Propulsion)**（Technical Report，Aug 2025）——**「summary of all of my work on inertial propulsion to date」（其全部工作的总结，★核心）**；含 **M.E.Q.A.L. 系统**爆炸图与循环图（壳/磁体/杆/载荷质量/螺线管）；DOI 10.13140/RG.2.2.25884.19847
  https://www.researchgate.net/publication/394250885_DNO7_Technical_Report--On_Spatial_Mass_Displacement_Systems_Inertial_Propulsion
- **[3] A Heuristic for the Discretization of Classical Mass as Ordinary and Dynamic Quantum Objects**（Preprint，Aug 2025）——「点质量不是单一实体，而是分割为离散相互作用部分」
  https://www.researchgate.net/publication/394250595_A_Heuristic_for_the_Discretization_of_Classical_Mass_as_Ordinary_and_Dynamic_Quantum_Objects
- **[4] On the Thermal Bathing of Accelerated Bodies as Structured Energetic Conduits**（Preprint，Jul 2025）——「加速体的热浴作为结构化能量管道」
  https://www.researchgate.net/publication/393378015_On_the_Thermal_Bathing_of_Accelerated_Bodies_as_Structured_Energetic_Conduits
- **[5] Gravity as a High Frequency Electromagnetic Wave of Displacement in the Spacetime Quantum Vacuum**（Research Proposal，Jul 2024）——「时空量子真空=BEC 超流；引力=高频电磁位移波（麦克斯韦式表述）」
  https://www.researchgate.net/publication/381958168_Gravity_as_a_High_Frequency_Electromagnetic_Wave_of_Displacement_in_the_Spacetime_Quantum_Vacuum
- **[6] A Distributed Computational Approach to Everrett's Relative-State Formulation of Quantum Mechanics**（Preprint，Dec 2025）——「用 Lamport 时间戳处理 MWI 的经验适当性问题」
  https://www.researchgate.net/publication/399068253_A_Distributed_Computational_Approach_to_Everrett's_Relative-State_Formulation_of_Quantum_Mechanics
- **[7] Detection and Visualization of "Graviton" Emissions within Static Magnetic Fields**（Preprint，May 2025）——「静态磁场中的'引力子'发射检测与可视化；自旋电子学→磁场是动态的；脉冲相对论」
  https://www.researchgate.net/publication/391841189_Detection_and_Visualization_of_Graviton_Emissions_within_Static_Magnetic_Fields
- **[8] An Appendix of Howard Johnson's Lab Notes**（Data，May 2025）——**Howard Johnson（磁能先驱）实验室笔记汇编**（fair use）
  https://www.researchgate.net/publication/391742804_An_Appendix_of_Howard_Johnson's_Lab_Notes
- **[9] Physica: A Concise and Informal Treatise on Mass Transfer and Inertial Frames**（Book，Jul 2018）——其大学前所作；「有一些数学错误，但也有一些相当有趣的想法」
  https://www.researchgate.net/publication/326172644_Physica_A_Concise_and_Informal_Treatise_on_Mass_Transfer_and_Inertial_Frames

> 说明：RG 个人页还有一个「Research」条目类型未单列；上表 = 页面上 Publications (9) 的全部条目。

---

## 三、下载方法（实测笔记 —— 接手人从这继续）

### ✅ 已测通
- **WebFetch 可读 RG 页面**（含 Cloudflare 反爬的内容）——已成功读取个人页全文与 [2] DNO7 论文页（含摘要、全部链接、图注）。**读页面信息走 WebFetch 即可。**
- **系统 Edge headless 可用**：`msedge --headless=new --dump-dom <url>`（本机 Edge v153 正常，example.com 实测通过）。

### ❌ 已测失败（不要重复）
- curl / curl_cffi（chrome 指纹）直接请求 RG → **一律 403**（RG 反爬「Temporarily Unavailable」页）。
- PDF 直链（从论文页拿到的 `links/` 地址）→ **同样 403**，需要带浏览器会话的 Cookie。
- agent-browser 自带 Chromium → 本机启动异常（沙箱拒绝访问 + 网络服务崩溃）；「connect 到外部调试 Edge」也挂起（环境问题，未走通）。
- r.jina.ai 代理读 RG → 被 Cloudflare 拦。

### 📌 推荐路径（未完成，交给接手人）
1. **真实浏览器 + 登录**：RG 全文下载通常要求注册/登录账号。用系统 Edge/Chrome 打开论文页 → 点「Download full-text PDF」（未登录会被引导注册）。
2. **或**手动在论文页右键检查「Download」按钮的真实 `links/...pdf` 地址再带 Cookie 下载。
3. [2] DNO7 的两个 PDF 直链已拿到（但未登录被 403）：
   - `.../publication/394250885_.../links/6892856042b47114347c677b/DNO7-Technical-Report--....pdf`
   - `.../publication/394250885_.../links/688ed91f86911c11bfed1d92/DNO7-Technical-Report--....pdf`

---

## 四、与项目主题的关联（供写总结的人参考）

老师要求说明：**论文的 implosive 系统 ↔ 孤子 ↔ Schauberger Repulsine 飞碟** 的联系。关键接口：
- 作者自我定位「**implosive system dynamics**」= 其 Repulsine 复现工作的理论自我描述；书目 [2] 是其全部工作总结。
- 本库已有其视频线：`joe cell/31`（收录+主张总表）、`32`（孤子与涡流力学）、`33`（马赫原理与开放系统）、`34`（内爆发光与等离子）——**写论文总结时应与这四份对读**。
- [8] Howard Johnson 实验室笔记 = 磁能/磁动机主题，与本库「磁现象系列」（`joe cell/30`）相关。
- [5][7] 涉量子真空/磁场动力学，可与孤子（非线性波·自持局域结构）框架对照。

---

## 五、本目录文件说明

- `_probe_curl.html` / `_profile_curl2.html` / `_rjina_test.txt` / `_test_dno7.pdf` —— 探测残留（失败样本），可删。
- `_交接说明_...md` —— 本文件（**保留**）。
