# 02 — AI 分析过程

## 使用的工具与步骤

### Step 1: 项目结构扫描

**工具：** `Bash` (ls, find), `Read`

**目的：** 了解项目整体结构，定位知识库和 skill 文件

**发现：**
- `Knowledge/Paper/` — 25 篇酶进化论文
- `Knowledge/biofoundry-skills/` — 13 个生物铸造领域 skill
- `.agents/skills/` — 8 个开发工作流 skill
- `AGENTS.md` — 完整的项目架构文档

### Step 2: Skill 内容分析

**工具：** `Agent` (Explore type × 2，并行执行)

**Agent 1 — 知识库分析：**
- 读取所有 SKILL.md 文件，了解每个 skill 的能力
- 搜索 RhlA、rhamnolipid、P. aeruginosa 相关引用
- 识别出 RhlA/RhlB 系统即为项目的实际生物目标

**Agent 2 — 源码分析：**
- 扫描 `src/biofoundry_cli/tools/`（14 个工具）
- 扫描 `src/biofoundry_cli/skills/`（2 个内嵌 skill）
- 搜索 primer、PCR、sequence、oligo 等关键词
- 确认 dna-assembly skill 仅有 `calculate_tm()` 和 `find_restriction_sites()`

### Step 3: Excel 文件解析

**工具：** `Bash` + `python3` + `openpyxl`

**操作序列：**

| # | 操作 | 关键发现 |
|---|------|---------|
| 1 | `openpyxl.load_workbook()` 查看 sheet 列表 | 8 个 sheet，核心是 `RhlA-NNK design` 和 `Sheet2` |
| 2 | 读取 `RhlA-NNK design` 前 20 行（data_only=True） | B1=15bp-Left, E1=15bp-right, B3=RhlA序列 |
| 3 | 读取公式（data_only=False） | 提取 C、D、E、F、I、J、K、L 列公式 |
| 4 | 读取 Sheet2 全部 298 行 | 最终输出格式：codon, Fwd Primer, Start position, Rev Primer, GA-arm |
| 5 | 分析 group 结构 | 37 个 group，每 group 8 个 codon，最后 group 6 个 |
| 6 | 验证 Rev = RC(GA-arm) | 确认 Rev Primer 是 GA-arm 的反向互补 |
| 7 | 分析 Sheet5 | 带引物命名编号（如 `RA_Co2-9_pcr2_R`） |

### Step 4: 公式逆向工程

从 Excel 公式中提取的核心算法：

```
C 列（构建含 NNK 替换的完整序列）：
  modified_seq = 15bp_left + LEFT(gene, (codon_N-1)*3) + "NNK" + RIGHT(gene, len-(codon_N-1)*3-3) + 15bp_right

I 列（分组编号）：
  group = INT((row - 4) / 8)  // 即 codon 2-9 → group 0, codon 10-17 → group 1, ...

E 列（提取 Fwd Primer）：
  fwd_primer = MID(modified_seq, group*24 + 4, 54)

J 列（GA-arm）：
  ga_arm = LEFT(fwd_primer, 15)

K 列（Annealing region）：
  annealing = RIGHT(fwd_primer, 15)

L 列（Rev Primer）：
  rev_primer = reverse_complement(ga_arm)
```

### Step 5: 验证

- 验证 codon 2 的 modified_seq 与 Excel 计算结果完全一致（逐字符比对通过）
- 验证 Rev Primer = GA-arm 的反向互补（通过）
- 确认 codon 1（ATG 起始密码子）被排除（group = -1，无引物）
- 确认 codon 296（TGA 终止密码子）被排除
- 确认最后一组（codon 290-295）的 fwd primer 长度为 51bp（因序列末尾不足 54bp）

## 关键数值

| 参数 | 值 |
|------|-----|
| RhlA 基因长度 | 888 bp |
| 总 codon 数 | 296 |
| 需要 NNK 引物的 codon | 2-295 = 294 个 |
| 分组大小 | 8 codons / group |
| 总分组数 | 37（前 36 组各 8 个，最后 1 组 6 个）|
| Fwd Primer 长度 | 54 bp（最后组 51 bp）|
| GA-arm 长度 | 15 bp |
| 15bp-Left | `gcagatctcaattgg` |
| 15bp-Right | `ggtaccctcgagtct` |
