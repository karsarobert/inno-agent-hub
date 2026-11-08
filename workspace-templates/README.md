# Workspace Templates

按场景整理的**工作区模板**(预设)。每个模板是一个目录,把一个学习/创作场景所需的 **Agent 人格 + 专项技能**打包在一起,让你开箱即用。

Inno Agent 的「简单模式」会直接把这些模板渲染成欢迎页的**预设卡片**,点一下就进入一个配好的工作区开始对话。你也可以手动把模板内容上传到任意工作区(见下文)。

---

## 目录结构

每个模板目录包含:

```
<模板 id>/
├── preset.json        # 元数据:id / name / description / icon(App 预设卡片读它)
├── agent.md           # 工作区上下文:每次对话注入到 Agent 系统提示
└── .skills/           # 可选,工作区私有技能
    └── <技能名>/
        └── SKILL.md   # 技能定义(name 与目录名一致)
```

### `preset.json` 字段

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | ✅ | 唯一标识,**必须与目录名完全一致**(防路径穿越)。只用字母/数字/`._-`。 |
| `name` | ✅ | 显示名,出现在预设卡片标题。 |
| `description` | | 一句话说明这个模板帮用户做什么,显示在卡片副标题。 |
| `category` | ✅ | 分类标签,客户端按此分组与筛选。当前可用: `教学` / `演示` / `verymath`。**缺失会落到「未分类」组**,详见仓库根目录 [README.md 的「分类标签 (必填)」](../README.md#分类标签-必填)。 |
| `icon` | | [lucide](https://lucide.dev/icons/) 图标名,如 `presentation` / `book-open` / `lightbulb`。 |

---

## VeryMath AI4Math 系列

本目录收录了来自 [**VeryMath**](https://github.com/VeryMath) 的 7 个 AI4Math 工作区模板（分类标签：`verymath`）。

[VeryMath](https://github.com/VeryMath) 是一个专注于 **AI 辅助数学研究** 的开源社区，目标是让 AI Agent 成为数学家的协作伙伴。其仓库覆盖从论文阅读、形式化证明到自动科研的完整研究链路，每个仓库提供对应场景的 Skill 定义与工作流指导。

| 模板 | 上游仓库 | 场景 |
|---|---|---|
| `ai4math-lean-agents` | [AI4Math-Lean-Agents](https://github.com/VeryMath/AI4Math-Lean-Agents) | Lean 4 定理形式化、证明修复、sorry 补全 |
| `ai4math-paper-reading` | [AI4Math-Paper-Reading](https://github.com/VeryMath/AI4Math-Paper-Reading) | 数学论文结构化阅读、论文转 Skill |
| `ai4math-paper-writing` | [AI4Math-Paper-Writing](https://github.com/VeryMath/AI4Math-Paper-Writing) | 数学论文起草、修订与审稿回复 |
| `ai4math-computational-mathematics` | [AI4Math-Computational-Mathematics](https://github.com/VeryMath/AI4Math-Computational-Mathematics) | 有限元、不变量计算、科研代码复现 |
| `ai4math-optimization` | [AI4Math-Optimization](https://github.com/VeryMath/AI4Math-Optimization) | LP / MIP / SOCP / CDOpt 流形优化 |
| `ai4math-auto-research` | [AI4Math-Auto-Research](https://github.com/VeryMath/AI4Math-Auto-Research) | 问题发现、猜想生成、证明蓝图审查 |
| `ai4math-evolving` | [AI4Math-Evolving](https://github.com/VeryMath/AI4Math-Evolving) | OpenEvolve 进化实验与迭代改进 |

> 如需了解 VeryMath 的整体愿景与更多子项目（如 [co-mathematician](https://github.com/VeryMath/co-mathematician)、[AI4Math-Sagemath-skill](https://github.com/VeryMath/AI4Math-Sagemath-skill)），请访问 https://github.com/VeryMath 。

---

## 模板列表

| 目录 | 场景 | 包含 Skill | 状态 |
|---|---|---|---|
| [ielts-prep/](./ielts-prep/) | 雅思英语备考 | card-maker(词汇卡片生成器)| ✅ 可用 |
| [ielts-coach/](./ielts-coach/) | 雅思备考(英文闭环版) | card-maker / essay-grader / reading-trainer / weekly-review | ✅ 可用 |
| [ppt-creation/](./ppt-creation/) | PPT / 演示文稿制作 | ppt-builder(结构化幻灯片生成)| ✅ 可用 |
| [teaching-webpage-en/](./teaching-webpage-en/) | 课堂互动网页(英文版) | webpage-builder / claude-design / visual-explainer | ✅ 可用 |
| [math-interactive-en/](./math-interactive-en/) | 数学交互解题(英文版) | edu-analytic-geometry / edu-solid-geometry | ✅ 可用 |
| [cpp-lesson-01/](./cpp-lesson-01/) | C++ 基础第 1 课(初学者):理论回顾 + 实操实验 + 自测 | cpp-course-tutor | ✅ 可用 |
| [deeplearning-gyakorlat-1/](./deeplearning-gyakorlat-1/) | Deep Learning 1. 练习课 — TensorFlow 基础 · MNIST 分类器(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-2/](./deeplearning-gyakorlat-2/) | Deep Learning 2. 练习课 — 从单个权重到可训练网络:权重/损失/梯度步、NumPy 与 Keras 小网络、酒数据预处理、回归与分类、学习曲线(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-3/](./deeplearning-gyakorlat-3/) | Deep Learning 3. 练习课 — 梯度法、神经元与螺旋分类:单个权重/bias 的梯度步、三层螺旋数据的基线 / 16 神经元 / 50–50 网络,必修学习率实验 0.01 → 0.001,按验证损失选模型并自己写理由,收尾 10 道代码理解选择题,RUN 按钮或终端,本地运行无需 Colab/GPU、无作业(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-4/](./deeplearning-gyakorlat-4/) | Deep Learning 4. 练习课 — 学习率、动量、激活函数与正则化:单权重向最小值的靠近 (G04_01)、两种更新规则的路径对比 (G04_02)、激活函数与局部导数 (G04_03)、小网络中神经元数与训练时长的影响 (G04_04)、L2 权重惩罚与 loss/MAE (G04_05)、dropout 随机掩码与两种模式 (G04_06),每次运行在 nezet 下生成带时间戳的结果文件夹,收尾 10 道代码理解选择题,并附 oktatoi/ 教师材料(准备、解答、测试答案、实测结果),RUN 按钮或终端、纯 CPU 本地运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-5/](./deeplearning-gyakorlat-5/) | Deep Learning 5. 练习课 — 自编码器与基于 EKG 的异常检测:环境检查(本地数据/CPU/图片保存)、正常与异常心电波形 (G05_01)、真实自编码器训练与重构 (G05_02)、逐样本 MAE 与误差分布 (G05_03)、决策阈值对报警与误判的影响及 precision/recall (G05_04);G05_03 与 G05_04 始终使用随附的 30 轮、瓶颈为 8 的参考重构,每次运行在 nezet 下生成短序号结果文件夹,收尾 10 道固定讲解题,并附 oktatoi/ 教师材料(准备、答案、实测运行、示例图),Run 按钮或终端、纯 CPU 本地运行无需 GPU/联网,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-7/](./deeplearning-gyakorlat-7/) | Deep Learning 7. 练习课 — Colab 中由 Inno 引导的三个任务:房价回归(真实目标)、MNIST 数字识别(one-hot 目标)、自编码器 input=target 重构的异常检测;学生逐格编辑运行 PTE_DL7_FELADATOK.ipynb(E01、R01–R10、M01–M10、A01–A10、Z01),已备好的格子重在理解与解读,15 个指定格子(R04–R06、R10、M03–M06、M09、A03–A05、A07–A09)需自写短代码;关键检查点 R03 划分 303/101/102、M09 测试集、A08 在测试前固定 97% 校准分位阈值;收尾三个口头问题,需要联网与个人 Colab 会话,GPU 可选,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-8/](./deeplearning-gyakorlat-8/) | Deep Learning 8. 练习课 — Colab 中的迁移学习:用预训练 MobileNetV2 识别五种花卉类别,全部代码预先给出,学生逐格运行 PTE_DL8_VIRAGOK_FELADATOK.ipynb 并回传所要求的简短输出(E01–E02、E03 对话点、D01–D05、F01–F05、T01–T05、V00–V04、Z01–Z02),每类 100/40/40 划分(共 500/200/200)、冻结基座与自带 preprocess_input、五类 softmax 头与 sparse categorical 交叉熵、对 block_16_ 与 Conv_1 定向微调(新 Adam 1e-3 → 1e-5)、按最小 val_loss 选模、在未触碰的测试集上评估 accuracy 与 5×5 混淆矩阵;关键检查点 E01 GPU 列表、D04 batch 形状/类型、F02 头部、T02 可训练性规则、T05 选择、V02 矩阵;收尾三个口头问题,需要联网与个人 Colab 会话,GPU 建议(GPU 列表为空时在 E01 停下),无作业(匈牙利语/英语) | — | ✅ 可用 |
| [deeplearning-gyakorlat-9/](./deeplearning-gyakorlat-9/) | Deep Learning 9. 练习课 — Colab 中的 batch normalization、CNN 构建单元与残差连接:两份未改动的交互式 HTML 讲解(forrasok/ 下的 Batch Normalization 与 Skip Connection),学生按 CELLA_TERKEP.json 的固定顺序逐格运行自建 Colab/Jupyter 中的 PTE_DL9_CNN_LAB.ipynb,共 28 个点(E01 环境与 GPU 关口、B01–B06 从样本–特征面板到 gamma–beta、真实 Keras 权重与滑动统计、冻结 BN 与第 8 课关联,P01–P02 局部/全局池化与 Flatten、GAP 头部参数量,C01 1×1 卷积,R00 跳跃连接讲解中的观察,R01–R03 真实残差块、投影捷径与梯度探针,G01–G02 dropout 与 L2 正则,D01–D03 CIFAR-10 图像、固定的 8000/2000/2000 划分(每类 800/200/200)与共享 batch,M01–M05 同一构建函数产出的两个小 CNN(5370 与 5562 参数,相同层序与 batch,各 6 轮、独立 Adam 1e-3)、按最佳 val_loss 回载 checkpoint 并据此决策,V01 决策之后才在固定 2000 张上做最终测试,V02 逐步估计与 10×10 混淆矩阵,Z01–Z02 三个反思与收尾总结),其中 B01、R00、Z01 仅对话,其余 25 个为代码单元格;需要联网下载约 170 MB 的 CIFAR-10 与个人 Colab 会话,GPU 为 E01 的硬性关口(GPU: [] 时 E01 阻断,本地 Jupyter 的 CPU 情形例外);不要求提交笔记本或保存产物,无作业且无额外练习(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-1-gyakorlat/](./cpp-1-gyakorlat/) | C++ 1. 练习课 — C++ 基础:预处理宏 / 条件编译 / I/O(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-2-gyakorlat/](./cpp-2-gyakorlat/) | C++ 2. 练习课 — 类型与数值表示:类型尺寸/初始化/位模式/除法/范围/浮点精度/输出格式/容差比较/收尾修错(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-3-gyakorlat/](./cpp-3-gyakorlat/) | C++ 3. 练习课 — 控制结构:if / if–else / else if / switch / while / do–while / for,两个综合任务(偶数计数、3 的倍数求和),收尾选择测验 T1 + 输出预测测验 T2,RUN 按钮或终端编译运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-4-gyakorlat/](./cpp-4-gyakorlat/) | C++ 4. 练习课 — 数组与指针:索引与元素访问、数组修改与遍历、求和/平均/条件计数、值–地址–指针–解引用、nullptr 检查、数组与指针的关系及指针遍历修改,收尾选择测验 T1 + 输出预测测验 T2,仅在 90 分钟内完成必修部分时才提供可选综合加练,RUN 按钮或终端编译运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-5-gyakorlat/](./cpp-5-gyakorlat/) | C++ 5. 练习课 — 函数与过程:自定义函数(返回值 / 参数 / void / 原型)、测量数据剖析项目 P1–P7(输出、求和、平均、最大值、阈值以上的计数、通过指针提高阈值、以 <cmath> sqrt 求距离),收尾 T1 选择题 10 道 + T2 代码理解 10 道(输出预测与排错),RUN 按钮或终端编译运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-7-gyakorlat/](./cpp-7-gyakorlat/) | C++ 7. 练习课 — 结构体、联合与作用域:自定义结构体与独立副本、按值传递结构体 / 返回 / 指针访问、带标志的联合体、内层块与名字隐藏、循环变量作用域,有效性测量数据分析项目 P1–P6(嵌套日期输出、完整序列、有效计数、有效平均、严格高于阈值计数、通过指针修改原记录),收尾 T1 选择题 10 道 + T2 代码理解 10 道(输出预测与排错),HALADAS.json 跟踪进度,RUN 按钮或终端编译运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-8-gyakorlat/](./cpp-8-gyakorlat/) | C++ 8. 练习课 — 类、const 成员函数与 private 数据成员:带成员函数与持久状态的时长、const 查询与独立副本的矩形、private 亮度与对象复制的灯、赋值前拒绝的储罐,库借阅项目 P1–P6(图书类型与库存、计算的可借数量与 const 快照、借出与归还可借/已借检查、六个图书类型数组与聚合自由函数、在副本与原对象上试借、为何可借数量不作存储成员),收尾 T1 选择题 10 道 + T2 代码理解 10 道(输出预测与排错),HALADAS.json 跟踪进度,RUN 按钮或终端编译运行,无作业(匈牙利语/英语) | — | ✅ 可用 |
| [cpp-9-gyakorlat/](./cpp-9-gyakorlat/) | C++ 9. 练习课 — 构造函数、有效初始状态、协作类与组合:三种创建方式的竞赛者、条件表达式设定亮度与默认状态、包裹与独立计费类协作、对象数组与组合的结果单,剧院售票项目 P1–P6(带有效初始状态的票、空售票处与添加一张、拒绝重复预订、退票并以左移补齐空位、列表与当前收入、通过协作库类以文本返回汇总),收尾 20 道固定题(T1 选择题 10 道 + T2 输出预测 5 道与排错 5 道),HALADAS.json 跟踪进度,RUN 按钮或终端编译运行,无作业且无单独加练(匈牙利语/英语) | — | ✅ 可用 |
| [python-alapok-01-gyakorlat/](./python-alapok-01-gyakorlat/) | Python 基础 01. 练习课 — 第一个程序的编写/保存/运行(双编辑器+双终端,预测-运行法)(匈牙利语) | — | ✅ 可用 |
| [python-alapok-01-gyakorlat-v1/](./python-alapok-01-gyakorlat-v1/) | Elemi programozás 1. gyakorlat (EP_01) V1 — 修订版材料:E0 环境检查、E1 首次输出、B1–B5 咖啡店系列、Z1–Z3 独立收尾、可选加练、进度表、详细 HTML 讲义(匈牙利语) | — | ✅ 可用 |
| [elemi-programozas-2-gyakorlat/](./elemi-programozas-2-gyakorlat/) | Elemi programozás 2. gyakorlat (EP_02) — 函数与条件分支、咖啡馆程序组装:def / 参数 / 返回值、if–elif–else、学生自己写代码并运行、检查用例、详细 HTML 讲义(匈牙利语) | — | ✅ 可用 |
| [elemi-programozas-3-gyakorlat/](./elemi-programozas-3-gyakorlat/) | Elemi programozás 3. gyakorlat (EP_03) — 循环与购物篮咖啡店程序组装:while 与状态更新、for–range、重复输入校验、break 与累加求和、列表遍历、continue、学生自己写代码并运行、检查用例、详细 HTML 讲义(匈牙利语) | — | ✅ 可用 |
| [elemi-programozas-4-gyakorlat/](./elemi-programozas-4-gyakorlat/) | Elemi programozás 4. gyakorlat (EP_04) — 字符串与购物篮咖啡店程序组装:文本统一(大小写、首尾空白)、索引与切片、逐字符遍历、列表方法、split/join 与过滤、运行中构建购物篮并接入结账、学生自己写代码并运行、检查用例、详细 HTML 讲义(匈牙利语) | — | ✅ 可用 |
| [elemi-programozas-5-gyakorlat/](./elemi-programozas-5-gyakorlat/) | Elemi programozás 5. gyakorlat (EP_05) — 字典与咖啡馆扩展程序组装:字典连接商品名与价格、统一名称查价、已有价格的受控更新、可负担商品筛选、购物篮求和与合并咖啡块函数、独立代码改造、10+10 题理论与代码知识结课测验、学生自己写代码并运行、检查用例、详细 HTML 讲义(匈牙利语) | — | ✅ 可用 |
| [diszkret-matematika-1/](./diszkret-matematika-1/) | Diszkrét matematika 1. 1. 练习课 — 命题逻辑:导师引导、课堂练习(出口卡)、作业、典型误解指南(匈牙利语) | math-tutor | ✅ 可用 |
| [lesson-plan/](./lesson-plan/) | 结构化教案生成 | — | 🚧 骨架(工作流待细化)|
| [scenario-explain/](./scenario-explain/) | 情景化讲题 | — | 🚧 骨架(工作流待细化)|
| [ai4math-paper-reading/](./ai4math-paper-reading/) | 数学论文阅读：PDF 摄入、论文转 Skill | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-computational-mathematics/](./ai4math-computational-mathematics/) | 计算数学：有限元、不变量、最小二乘、代码复现 | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-optimization/](./ai4math-optimization/) | 数学优化：LP / MIP / SOCP / CDOpt / COPT | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-lean-agents/](./ai4math-lean-agents/) | Lean 4 形式化、证明修复、sorry 补全 | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-auto-research/](./ai4math-auto-research/) | 自动数学科研：问题发现、证明蓝图生成与审查 | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-evolving/](./ai4math-evolving/) | 进化 Agent：OpenEvolve 实验配置与迭代改进 | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [ai4math-paper-writing/](./ai4math-paper-writing/) | 数学论文写作：起草、修订、结构化与审稿回复 | — | ✅ 可用（[VeryMath](https://github.com/VeryMath)）|
| [_template/](./_template/) | **新模板起点** | example-skill(示例)| 📋 模板 |

---

## 怎么用

### 方式一:简单模式预设卡片(推荐)

Inno Agent 默认从本仓库的 `workspace-templates/` 拉取模板。打开「简单模式」,欢迎页会列出上面这些预设,点卡片即创建并绑定一个配好的工作区。

> 拉取源可在 App 设置 →「内容源」中切换(公共仓库 / 私有 GitHub 仓库 / 自托管服务)。

### 方式二:手动上传到工作区

1. 在 Inno Agent 新建一个工作区。
2. 把模板的 `agent.md` 放到工作区根目录(让 Agent 创建,或拖拽到文件树空白区域)。
3. 把模板 `.skills/` 下每个技能的 `SKILL.md`(或自行打包的 `.zip`)通过文件树工具栏 **✦ 按钮**上传,落到工作区的 `.skills/<名称>/SKILL.md`。
4. 新建会话绑定该工作区即可。

> 详细操作步骤参见 [`how-to/skill-tutorial.md`](../how-to/skill-tutorial.md)。

---

## 贡献一个新模板

1. 复制 [`_template/`](./_template/),重命名为你的模板 id(如 `my-template`)。
2. 编辑 `preset.json`:把 `id` 改成新目录名,填好 `name` / `description` / **`category`**(必填,见下) / `icon`。
3. 编辑 `agent.md`:定义这个工作区的 Agent 人格与工作流程。
4. 按需在 `.skills/` 下增删技能(每个技能一个目录,内含 `SKILL.md`)。
5. 在上面的「模板列表」表格里加一行。
6. 提交 PR。

> **`category` 必填** —— 客户端按 `category` 分组显示预设卡片,缺失会落到「未分类」组。当前可用: `教学` / `演示` / `verymath`(从这三个里挑,不要新造)。新增分类请先提 issue。详见仓库根目录 [README.md 的「分类标签 (必填)」](../README.md#分类标签-必填)。

> 命名约定:`id` 用小写连字符(`kebab-case`);以 `_` 或 `.` 开头的目录(如 `_template`)不会被当作可用预设拉取,适合放骨架/草稿。
