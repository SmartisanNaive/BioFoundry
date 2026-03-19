# BioFoundry Agent Skills

[English](./README.md) | 中文

本目录包含一套 Claude Code skills，旨在实现论文 *"Autonomous biofoundry reveals hierarchical epistasis emergence from enzyme to pathway"* 中描述的自主生物铸造厂代理架构。

这些 skills 对应于代理系统的四个核心模块：

## 1. 序列空间解析器与协议编译器 (`sequence-space-parser`)

**目的：** 将数字基因型转化为机器人执行协议。
- **`design_golden_gate`**：计算组合文库的最佳 Golden Gate 组装路径。
- **`compile_opentrons_script`**：生成适用于 *E. coli* 和 *P. aeruginosa* 的液体处理脚本。

## 2. 多模态表型张量处理器 (`phenotype-tensor-processor`)

**目的：** 摄取和分析高维表型数据。
- **`query_ms_database`**：检索质谱数据并进行伪影检测（例如识别低信号假阳性）。
- **`run_python_sandbox`**：执行自定义分析以进行可视化和异常检测。

## 3. 深度假设生成与实验重构网络 (`hypothesis-generation-network`)

**目的：** 生成基于机制的假设并设计验证实验。
- **`design_control_experiment`**：设计对照实验，例如使用无义突变作为天然敲除对照。
- **`reconstruct_plasmid_pathway`**：规划分子生物学操作以修改通路架构（例如移除 RhlB）。

## 4. 生物膜显微镜工作流 (`biofilm-microscopy`)

**目的：** 捕获和分析生物体水平的表型。
- **`trigger_microscope_imaging`**：调度自动化的延时成像任务。
- **`analyze_biofilm_morphology`**：从生物膜图像中提取形态特征（厚度、覆盖率、孔隙率）。

## 5. KEGG 数据库访问 (`kegg-database`)

**目的：** 查询 KEGG 通路和反应数据库，进行代谢网络分析。
- **`query_kegg_pathway`**：检索代谢通路信息和基因注释。
- **`query_kegg_reaction`**：获取酶反应数据和 EC 编号映射。

## 6. PDB 数据库访问 (`pdb-database`)

**目的：** 从 RCSB PDB 检索和分析蛋白质结构。
- **`fetch_pdb_structure`**：下载 PDB/mmCIF 格式的蛋白质结构文件。
- **`query_pdb_by_sequence`**：使用序列相似性搜索 PDB 条目。

## 7. Momentum 实验室自动化 (`momentum-automation`)

**目的：** 控制 Momentum 实验室自动化系统进行高通量实验。
- **`schedule_momentum_protocol`**：调度和执行自动化协议运行。
- **`monitor_momentum_status`**：监控仪器状态和任务队列。

## 8. DMS 分析 (`dms-analysis`)

**目的：** 深度突变扫描数据分析和适应性景观构建。
- **`align_dms_sequences`**：将突变序列与野生型参考序列比对。
- **`compute_fitness_scores`**：从计数数据计算适应性得分。

## 9. 上位性分析 (`epistasis-analysis`)

**目的：** 检测和量化突变之间的上位性相互作用。
- **`detect_epistasis`**：识别成对的上位性相互作用。
- **`compute_epistasis_strength`**：量化上位性效应的大小。

## 10. LC-MS 分析 (`lcms-analysis`)

**目的：** 液相色谱-质谱数据处理。
- **`process_lcms_data`**：处理原始 LC-MS 数据以鉴定代谢物。
- **`quantify_peaks`**：执行峰检测和定量。

## 11. Momentum 工作流 (`momentum-workflow`)

**目的：** 在 Momentum 系统上编排多步骤自动化工作流。
- **`design_workflow`**：设计多步骤实验工作流。
- **`execute_workflow`**：执行和监控工作流进度。

## 12. 通路工程 (`pathway-engineering`)

**目的：** 设计和优化目标化合物生产的代谢通路。
- **`design_pathway`**：为目标分子设计通路方案。
- **`optimize_enzymes`**：选择和改造酶以提高通路效率。

## 使用方法

每个 skill 都是一个独立的目录，包含定义工具的 `SKILL.md` 文件和包含实现逻辑的 `scripts/` 目录。这些 skills 旨在供 AI 代理使用，以在生物铸造厂环境中自主规划和执行实验。

## Claude Code 加载方式

Claude Code 会从项目级技能目录发现 skills，常用目录包括：
- `.claude/skills/`
- `.github/skills/`
- `.agents/skills/`

推荐在仓库根目录将本目录下的 skills 以链接方式加入 `.claude/skills/`：

```bash
mkdir -p .claude/skills
ln -s ../../biofoundry-skills/skills/dna-assembly .claude/skills/dna-assembly
ln -s ../../biofoundry-skills/skills/sequence-space-parser .claude/skills/sequence-space-parser
ln -s ../../biofoundry-skills/skills/phenotype-tensor-processor .claude/skills/phenotype-tensor-processor
ln -s ../../biofoundry-skills/skills/hypothesis-generation-network .claude/skills/hypothesis-generation-network
ln -s ../../biofoundry-skills/skills/biofilm-microscopy .claude/skills/biofilm-microscopy
ln -s ../../biofoundry-skills/skills/kegg-database .claude/skills/kegg-database
ln -s ../../biofoundry-skills/skills/pdb-database .claude/skills/pdb-database
ln -s ../../biofoundry-skills/skills/momentum-automation .claude/skills/momentum-automation
ln -s ../../biofoundry-skills/skills/dms-analysis .claude/skills/dms-analysis
ln -s ../../biofoundry-skills/skills/epistasis-analysis .claude/skills/epistasis-analysis
ln -s ../../biofoundry-skills/skills/lcms-analysis .claude/skills/lcms-analysis
ln -s ../../biofoundry-skills/skills/momentum-workflow .claude/skills/momentum-workflow
ln -s ../../biofoundry-skills/skills/pathway-engineering .claude/skills/pathway-engineering
```

完成后，Claude Code 会根据任务自动发现并按需加载这些 skills。
