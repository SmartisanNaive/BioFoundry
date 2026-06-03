# 合成生物大设施对接需求文档

> RhlA Biofoundry Agent CLI — 设备集成、证据链、体系兼容

## 1. 背景与目标

本项目（RhlA Biofoundry Agent CLI）构建了一套 LLM 驱动的自动化实验体系，覆盖从酶工程实验设计到数据反馈的全链路。核心叙事为：

```
LLM 自主调研已有 SOP → 自动设计引物/文库 → 生成自动化指令
→ 驱动设备执行（移液、培养、检测）→ 数据回传 → LLM 分析 → 下一轮迭代
```

为实现这一闭环，需要合成生物大设施提供以下三类支持：

1. **设备集成接口** — CLI 通过 API/文件方式驱动各设备
2. **证据链材料** — 证明实验确实由自动化系统执行，非人工操作
3. **体系兼容保障** — 设施提供的数据/接口与本项目的技能栈可对接

---

## 2. 项目现有能力基线

本 CLI 项目已具备以下与设施对接相关的能力：

| 模块 | 位置 | 能力 |
|------|------|------|
| Momentum API Client | `Knowledge/biofoundry-skills/momentum-automation/scripts/momentum_ws.py` | 完整的 Momentum Web Services REST API 封装（认证、设备查询、进程管理、工作队列、模拟模式） |
| Momentum CLI | `Knowledge/biofoundry-skills/momentum-automation/scripts/control_momentum.py` | 命令行工具 + Mock 模式（`MOMENTUM_MOCK=1`） |
| Momentum Skill | `Knowledge/biofoundry-skills/skills/momentum-automation/` | LLM 可调用的三个工具：`get_momentum_status`、`control_momentum`、`run_momentum_process` |
| Sequence Space Parser | `Knowledge/biofoundry-skills/sequence-space-parser/` | Golden Gate 组装路径计算 + Opentrons 脚本生成 |
| Phenotype Tensor Processor | `Knowledge/biofoundry-skills/phenotype-tensor-processor/` | MS 数据查询 + Python 分析沙盒 |
| Momentum Workflow (stub) | `Knowledge/biofoundry-skills/skills/momentum-workflow/` | 工作流编排（尚未实现，仅 SKILL.md 定义） |

**当前缺口：** Tecan Fluent 原生接口、RF-MS 控制、培养箱集成、工作流编排实现、证据链自动采集。

---

## 3. 设备集成需求

### 3.1 Tecan Fluent（液体操作平台）

负责：PCR 体系配置、Gibson Assembly 组装、转化涂板等移液操作。

| 需求项 | 说明 | 期望交付形式 |
|--------|------|-------------|
| FluentControl 版本 | 确认 API 能力范围 | 版本号截图 |
| Worklist 示例文件 | CLI 生成 `.gwl` 文本指令的基础 | `.gwl` 文件（至少包含：移液、分液、板间转移操作） |
| Labware definition | 板型、tip、reservoir 定义 | `.ldf` / `.ddf` 文件 |
| Deck layout 配置 | 载台物理布局映射 | 配置截图 + 导出文件 |
| 液面校准参数 | 小体积精确移液（PCR ≤ 5 µL） | 校准报告 |
| FluentControl run report 样例 | 验证 CLI 生成的 worklist 是否可被设备接受 | 历史实验的 run report |

**集成路径：**

```
CLI (Python) → 生成 .gwl worklist 文件
             → 通过共享目录 / API 传输到 FluentControl 所在主机
             → FluentControl 加载并执行
             → 执行完成后回传 run report
```

**备选路径（若 Momentum 已管理 Tecan）：**

```
CLI → Momentum API → Momentum 调度 Tecan 任务
```

### 3.2 Momentum（自动化调度引擎）

负责：多设备工作流编排、样本路由、异常处理。

| 需求项 | 说明 | 期望交付形式 |
|--------|------|-------------|
| Momentum 版本 + License | 确认 REST API 可用性 | 版本号 + License 类型 |
| Web Services URL + 认证凭据 | CLI 已有 API client（`momentum_ws.py`），需接入地址 | URL + API Token / Basic Auth 凭据 |
| 设备注册表 | 已接入 Momentum 的设备清单（Tecan、培养箱、读数器等） | `/devices` API 响应截图或导出 |
| 现有 Process 定义 | 设施已配置的自动化流程模板 | Process XML / JSON |
| Workqueue 状态查询 | 了解任务排队和执行机制 | `/workqueue` API 响应示例 |
| Scheduling Log 样例 | 证据链核心材料 | 带时间戳 + Job ID 的 `.csv` / `.log` |
| Container/Nest 配置 | 样本容器和位置管理 | `/containers`、`/nests` API 响应示例 |

**已有 API Client 能力（`momentum_ws.py`）：**

```python
# 已实现的方法
client.get_status()          # 系统状态
client.get_version()         # 版本信息
client.get_devices()         # 设备列表
client.get_containers()      # 容器管理
client.get_nests()           # 位置管理
client.get_processes()       # 进程列表
client.get_workqueue()       # 工作队列
client.start()               # 启动调度
client.stop()                # 停止调度
client.simulate()            # 模拟运行
client.run_process(...)      # 执行指定进程
client.run_worklist(...)     # 执行工作列表
client.run_experiment(...)   # 执行完整实验
```

**需要设施补充：**
- 可访问的 Web Services URL（内网地址或 VPN 配置）
- API 认证 Token
- 确认上述 API 在设施环境中的可用性

### 3.3 自动化培养系统

负责：文库转化后的大肠杆菌/铜绿假单胞菌高通量培养。

| 需求项 | 说明 | 期望交付形式 |
|--------|------|-------------|
| 培养箱型号 | 确定控制接口（Liconic STX/XTR、Thermo Cytomat 等） | 型号 + 设备手册 |
| 控制方式 | Momentum 统一调度 vs. 独立 API vs. 仅面板操作 | 控制接口文档 |
| 可编程参数 | 温度范围、湿度、振荡转速/振幅、CO₂ 浓度 | 参数范围表 |
| 板传输机制 | 机械臂自动取放 vs. 手动干预 | 传输协议描述 |
| 培养运行日志 | 温控曲线 + 时间戳（证据链关键材料） | 历史实验 log 文件 |

**集成路径（取决于控制方式）：**

```
路径 A（Momentum 管理）:
  CLI → Momentum API → 调度培养箱（内置在 workflow 中）

路径 B（独立 API）:
  CLI → 培养箱 HTTP/Serial API → 设定温度/振荡参数 + 读取状态

路径 C（文件约定）:
  CLI → 生成培养条件配置文件 → 设施操作员手动输入
```

### 3.4 RapidFire MS（RF-MS，高通量表型筛选）

负责：鼠李糖脂产量等代谢物的高通量定量检测（~1 sample/sec）。

| 需求项 | 说明 | 期望交付形式 |
|--------|------|-------------|
| RapidFire 型号 + 软件版本 | 确定自动化接口能力 | RF 型号 + 软件版本号 |
| RF 控制接口 | 是否支持远程启动采集、方法切换 | API 文档 / CLI 工具 |
| MassHunter 版本 | 数据采集与分析软件，确定导出格式 | 版本号 |
| 数据导出格式 | 原始数据 (.d) vs. 处理后数据 (.csv) | 示例数据文件 |
| 现有采集方法文件 | AI 可基于已有方法调参 | 方法文件 (.xml / .m) |
| Plate map 对应关系 | well 位置与 MS 信号 mapping | Sample list template |
| Acquisition log | 采集时间戳 + 样本序列（证据链） | 历史实验 log |

**集成路径：**

```
CLI → 生成 sample list + 方法参数
    → 提交到 RF 控制软件（API / 文件导入）
    → RF 自动进样采集
    → 数据文件回传（.d / .csv）
    → phenotype-tensor-processor skill 处理
```

---

## 4. SOP 与 Protocol 数字化需求

LLM 自主调研已有 SOP 是本项目的核心叙事。需要设施提供以下材料：

| 材料 | 用途 | 格式要求 |
|------|------|---------|
| PCR Protocol | AI 根据目标片段自动优化退火温度、循环数、体系配置 | 结构化文档（Markdown / JSON / 表格） |
| Gibson Assembly Protocol | AI 设计重叠区、计算浓度比、配置反应体系 | 同上 |
| 转化 Protocol（化学 / 电转） | AI 确定感受态用量、热激参数、复苏条件 | 同上 |
| 培养基配方 | AI 根据菌株选择培养基、抗生素浓度 | 配方表 |
| 引物合成规格 | AI 确认引物长度限制、纯化方式、交付周期 | 规格表 |
| 阳性/阴性对照方案 | AI 自动设计对照实验 | 对照设计文档 |
| FluentControl method 文件 | 已有自动化流程可直接复用 | `.prg` / `.fsm` 文件 |

**材料越结构化，LLM 解析和自主推理的准确度越高。** 纯 PDF/Word 也可接受，但需要额外的解析步骤。

---

## 5. 证据链需求

为向评审方/合作方证明实验确由自动化系统端到端执行，需要一条不可篡改、时间连续、多系统交叉验证的证据链。

### 5.1 全链路数据流

```
引物设计(CLI log + 设计输出)
    ↓
文库构建(Tecan worklist + FluentControl run report)
    ↓
培养(Momentum scheduling log + 培养箱温控 log)
    ↓
RF-MS 采集(MS acquisition log + raw data)
    ↓
数据分析(phenotype-tensor-processor 输出 + 分析脚本 log)
```

### 5.2 证据材料清单

| 证据材料 | 来源系统 | 包含信息 | 证明什么 |
|----------|---------|---------|---------|
| **CLI session log** | Biofoundry Agent CLI | 用户指令、LLM 推理过程、工具调用记录 | 证明 LLM 自主完成设计和决策 |
| **Tecan worklist 文件** | CLI 生成 | 移液步骤、体积、板位映射 | 证明移液指令由 AI 生成 |
| **FluentControl run report** | Tecan Fluent | 每步执行时间戳、实际体积、完成状态 | 证明移液确实由设备执行 |
| **Momentum scheduling log** | Momentum | Job ID、任务下发时间、调度顺序、设备分配 | 证明多设备协同由调度器自动管理 |
| **培养箱环境 log** | Liconic/培养箱 | 温度曲线、振荡状态、持续时间（带时间戳） | 证明培养条件被自动维持 |
| **RF-MS acquisition log** | RapidFire | 采集时间戳、样本序列、方法参数 | 证明样品被自动采集和分析 |
| **MS raw data (.d)** | MassHunter | 原始质谱数据（含采集时间戳 metadata） | 证明数据来自真实仪器采集 |
| **样本追踪记录** | Momentum / LIMS | Barcode → well 位置 → 设备流转记录 | 证明 chain of custody 完整 |

### 5.3 证据链验证原则

1. **Machine-generated timestamp**：每个环节必须有系统自动生成的时间戳，不可人工填写
2. **Unique ID 贯穿**：从设计到检测，样本/任务 ID 必须可追溯
3. **多系统交叉**：同一操作在至少两个系统中留有记录（如 Momentum log + 设备 log）
4. **时间连续性**：相邻步骤的时间戳必须合理衔接，无人工干预的空白间隙
5. **原始数据完整**：MS 等检测数据保留原始格式（.d），不可仅提供处理后的汇总表

---

## 6. 体系兼容性需求

### 6.1 数据格式映射

设施侧输出与本 CLI 技能栈的对接关系：

```
设施输出                           CLI 技能模块
──────────────                     ──────────────
Momentum workflow JSON          →  momentum-automation skill（解析 + 提交）
Tecan worklist (.gwl)           →  sequence-space-parser skill（生成 → 提交）
RF-MS 结果 (.csv / .d)          →  phenotype-tensor-processor skill（查询 + 分析）
培养 log                        →  momentum-workflow skill（编排 + 记录）
LIMS sample ID / barcode        →  全流程追踪 ID
```

### 6.2 接口协议

| 方案 | 复杂度 | 适用阶段 |
|------|--------|---------|
| 共享目录 + 文件约定 | 低 | Phase 1（跑通流程） |
| REST API（Momentum / LIMS） | 中 | Phase 2（生产级） |
| SiLA2 / OPC-UA 标准协议 | 高 | Phase 3（长期目标） |
| 消息队列（MQTT / Kafka） | 中 | 实时监控场景 |

### 6.3 技术栈兼容

| 设施侧 | CLI 侧 | 兼容要求 |
|--------|--------|---------|
| Momentum Web Services (REST) | `momentum_ws.py`（requests + token auth） | URL 可达 + 认证可用 |
| FluentControl Worklist | `.gwl` 文本文件生成 | 文件格式兼容 FluentControl 版本 |
| RF-MS 数据导出 | Python（pandas / pyOpenMS） | 数据可读（.csv 或 .d 可解析） |
| LIMS API（如有） | CLI tools / MCP | REST 或文件接口 |

---

## 7. 设施确认清单

以下清单用于与设施对齐，建议逐项确认：

### 7.1 设备接口

- [ ] **Momentum API 接入方式已确认**：□ REST API □ 文件导入 □ 仅 GUI
- [ ] **Momentum Web Services URL 已提供**：`________________`
- [ ] **Momentum API Token / 认证凭据已提供**：□ 是 □ 待申请
- [ ] **Tecan Fluent 工作模式**：□ Worklist 导入 □ Momentum 调度 □ 仅 GUI 手动
- [ ] **RF-MS 远程控制方式**：□ API □ 文件导入 □ 仅手动
- [ ] **培养箱自动化程度**：□ Momentum 调度 □ 独立 API □ 手动设定
- [ ] **设备间样本转运**：□ 全自动（机械臂/传送带）□ 半自动 □ 手动

### 7.2 SOP 与 Protocol

- [ ] **PCR Protocol 文档已提供**（□ 结构化 □ PDF/Word）
- [ ] **Gibson Assembly Protocol 已提供**
- [ ] **转化 Protocol 已提供**
- [ ] **培养基配方表已提供**
- [ ] **FluentControl method 文件已提供**（`.prg` / `.fsm`）
- [ ] **RF-MS 方法文件已提供**

### 7.3 证据材料

- [ ] **Momentum scheduling log 样例已提供**（含 Job ID + 时间戳）
- [ ] **FluentControl run report 样例已提供**
- [ ] **培养箱运行 log 样例已提供**（温控曲线）
- [ ] **RF-MS acquisition log 样例已提供**
- [ ] **MS raw data 样例已提供**（`.d` 文件）
- [ ] **样本追踪/Barcode 体系已确认**

### 7.4 Labware 与配置

- [ ] **Tecan Labware definition 文件已提供**（`.ldf` / `.ddf`）
- [ ] **Deck layout 配置已提供**
- [ ] **液面校准参数已提供**
- [ ] **RF-MS sample list template 已提供**

### 7.5 网络与安全

- [ ] **网络访问策略已确认**：□ VPN □ 内网直连 □ 离线文件传输
- [ ] **文件传输方式已确认**：□ 共享目录 □ SFTP □ API
- [ ] **设备校准报告已提供**
- [ ] **安全审批流程已确认**

### 7.6 联系人

| 角色 | 姓名 | 联系方式 |
|------|------|---------|
| 设施技术对接人 | ________ | ________ |
| Momentum 管理员 | ________ | ________ |
| 设备操作负责人 | ________ | ________ |
| 安全/审批负责人 | ________ | ________ |

---

## 8. 实施路径

### Phase 1：材料收集与环境验证（2-3 周）

```
目标：拿到所有接口文档、配置文件、示例数据

任务：
├── 收集上述清单中的全部材料
├── 验证 Momentum API 连通性（使用 momentum_ws.py）
├── 分析 FluentControl worklist 格式，确认 CLI 生成兼容性
├── 解析 RF-MS 数据格式，确认 phenotype-tensor-processor 可处理
└── 编写 mock 测试（MOMENTUM_MOCK=1）验证全链路逻辑
```

### Phase 2：Dry Run（2-4 周）

```
目标：用虚拟板 / mock 数据跑通全链路

任务：
├── 实现 momentum-workflow skill（编排多步骤工作流）
├── CLI 生成示例 worklist + Momentum workflow 配置
├── 模拟提交 → 模拟执行 → 模拟数据回传
├── 验证证据链完整性（每一步都有对应 log / report）
└── 确认所有证据材料可被 CLI 自动采集和整理
```

### Phase 3：Wet Run（4-6 周）

```
目标：真实设备执行，产出完整证据链

任务：
├── 与设施联合调试（Tecan + 培养箱 + RF-MS）
├── CLI 生成真实实验指令 → Momentum 调度 → 设备执行
├── 数据自动回传 → phenotype-tensor-processor 分析
├── 生成全链路证据报告（含所有 log + raw data + 分析结果）
└── 迭代优化：根据真实执行反馈调整指令生成逻辑
```

### Phase 4：闭环验证（2-4 周）

```
目标：证明 LLM 自主迭代闭环

任务：
├── Round 1：LLM 设计 → 自动执行 → 数据回传
├── LLM 分析 Round 1 数据 → 自主生成 Round 2 设计
├── Round 2：LLM 新设计 → 自动执行 → 数据回传
├── 输出完整证据链报告（两轮迭代的全部自动化记录）
└── 撰写对接报告，归档所有设施提供的材料
```

---

## 9. 预期交付物

完成全部对接后，本项目将产出以下可交付成果：

| 交付物 | 说明 |
|--------|------|
| Momentum 集成模块 | 基于 `momentum_ws.py` 的完整自动化调度能力 |
| Tecan Worklist 生成器 | 根据实验设计自动生成 `.gwl` 文件 |
| RF-MS 数据处理管线 | `phenotype-tensor-processor` 扩展 RF-MS 数据解析 |
| 全链路证据报告 | 从设计到检测的完整自动化记录，含所有系统 log |
| 自动化 SOP 执行记录 | LLM 自主调用 SOP 并驱动设备执行的完整日志 |
| 迭代闭环报告 | 多轮 LLM 自主设计-执行-分析-再设计的完整记录 |

---

## 附录 A：已有 Momentum API Client 方法参考

`momentum_ws.py` 已实现的完整 API 方法列表：

```python
class Momentum:
    """Momentum Web Services REST API Client"""

    # 系统
    get_status()              # GET /status — 系统运行状态
    get_version()             # GET /version — 软件版本

    # 设备
    get_devices()             # GET /devices — 已注册设备列表

    # 容器与位置
    get_containers()          # GET /containers — 容器清单
    get_nests()               # GET /nests — 位置/载台信息

    # 进程与队列
    get_processes()           # GET /processes — 可用进程列表
    get_workqueue()           # GET /workqueue — 工作队列状态

    # 控制
    start()                   # POST /start — 启动调度
    stop()                    # POST /stop — 停止调度
    simulate()                # POST /simulate — 模拟运行

    # 执行
    run_process(name, params) # 执行指定进程
    run_worklist(steps)       # 执行工作列表（XML 格式）
    run_experiment(config)    # 执行完整实验流程

    # 查询
    get_inventory()           # 库存查询
    query_barcode(code)       # Barcode 查询
```

Mock 模式：设置 `MOMENTUM_MOCK=1` 可在不连接真实 Momentum 的情况下测试全部 API 调用。

## 附录 B：项目中与设施对接相关的技能清单

| 技能 | 路径 | 状态 | 设备关联 |
|------|------|------|---------|
| `momentum-automation` | `Knowledge/biofoundry-skills/skills/momentum-automation/` | 已实现 | Momentum |
| `momentum-workflow` | `Knowledge/biofoundry-skills/skills/momentum-workflow/` | 仅定义 | Momentum |
| `sequence-space-parser` | `Knowledge/biofoundry-skills/skills/sequence-space-parser/` | 已实现 | Tecan / Opentrons |
| `phenotype-tensor-processor` | `Knowledge/biofoundry-skills/skills/phenotype-tensor-processor/` | 已实现 | RF-MS / MS |
| `dna-assembly` | `Knowledge/biofoundry-skills/skills/dna-assembly/` | 已实现 | 组装模拟 |
| `lcms-analysis` | `Knowledge/biofoundry-skills/skills/lcms-analysis/` | 已实现 | LC-MS |
| `dms-analysis` | `Knowledge/biofoundry-skills/skills/dms-analysis/` | 已实现 | DMS 数据 |
| `epistasis-analysis` | `Knowledge/biofoundry-skills/skills/epistasis-analysis/` | 已实现 | 上位性分析 |
