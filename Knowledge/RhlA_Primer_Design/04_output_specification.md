# 04 — 最终输出格式规范

> 此文档定义了 AI 生成引物时需要严格对标的输出格式，参照 Excel 的 Sheet2 和 Sheet5。

## Sheet2 格式 — 基础引物表

### 列定义

| 列 | 表头 | 内容 | 示例 |
|----|------|------|------|
| A | codon label | `codon N` | `codon 2` |
| B | Fwd Primer | 含 NNK 的正向引物序列（54bp，最后组 51bp） | `gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg` |
| C | Start position | Fwd Primer 在 modified_seq 中的提取起点 | `4` |
| D | Rev Primer | 反向引物（仅每 group 第一个 codon 输出） | `catccaattgagatc` |
| E | GA-arm | GA 同源臂（仅每 group 第一个 codon 输出） | `gatctcaattggatg` |

### 行 1：常量

```
B1: ggtaccctcgagtct   ← 这是 15bp-Right（下游载体序列）
```

### 行 2：表头

```
A2: (空)
B2: Fwd Primer
C2: Start position
D2: Rev Primer
E2: GA-arm
```

### 行 3-298：数据行

- **codon 1**（row 3）：全空（ATG 起始密码子，跳过）
- **codon 2**（row 4）：group 0 的第一个，**Rev Primer 和 GA-arm 有值**
- **codon 3-9**（row 5-11）：group 0，Rev Primer 和 GA-arm 为空
- **codon 10**（row 12）：group 1 的第一个，新的 Rev Primer 和 GA-arm
- ... 以此类推，每组 8 个 codon
- **codon 295**（row 297）：最后一个有引物的 codon
- **codon 296**（row 298）：空行

### 输出示例（前 3 组）

```
codon 1  |                                          |     |                |
codon 2  | gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg | 4   | catccaattgagatc | gatctcaattggatg
codon 3  | gatctcaattggatgcggNNKgaaagtctgttggtatcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 4  | gatctcaattggatgcggcgcNNKagtctgttggtatcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 5  | gatctcaattggatgcggcgcgaaNNKctgttggtatcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 6  | gatctcaattggatgcggcgcgaaagtNNKttggtatcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 7  | gatctcaattggatgcggcgcgaaagtctgNNKgtatcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 8  | gatctcaattggatgcggcgcgaaagtctgttgNNKtcggtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 9  | gatctcaattggatgcggcgcgaaagtctgttggtaNNKgtttgcaagggcctg | 4   |                | gatctcaattggatg
codon 10 | agtctgttggtatcgNNKtgcaagggcctgcgggtacatgtcgagcgcgttggg | 28  | cgataccaacagact | agtctgttggtatcg
codon 11 | agtctgttggtatcggttNNKaagggcctgcgggtacatgtcgagcgcgttggg | 28  |                | agtctgttggtatcg
...
```

---

## Sheet5 格式 — 带命名的完整引物表

### 布局

Sheet5 是双栏布局，每行包含 **一个 group 的共享信息 + 一条 Fwd Primer**：

**左栏（A-F）：Group 信息**
| 列 | 内容 | 示例 |
|----|------|------|
| A | Rev Primer（组内共享） | `catccaattgagatc` |
| B | 该组覆盖的起始 codon | `codon 2` |
| C | 引物命名：`RA_Co{start}-{end}_pcr2_R` | `RA_Co2-9_pcr2_R` |
| D | 修正后的 Rev（如有） | （通常为空） |
| E | 修正后的命名（如有） | （通常为空） |
| F | （空） | |

**右栏（G-N）：每条 Fwd Primer**
| 列 | 内容 | 示例 |
|----|------|------|
| G | Group 命名 | `RA_Co2-9` |
| H | GA-arm（组内共享） | `gatctcaattggatg` |
| I | Codon 编号 | `codon 2` |
| J | Fwd Primer | `gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg` |
| K-N | （空或修正列） | |

### 命名规则

```
引物命名格式: RA_Co{start}-{end}
  RA = RhlA 的缩写
  Co = Codon
  start = 该组第一个 codon 编号
  end = 该组最后一个 codon 编号

Rev 引物: RA_Co{start}-{end}_pcr2_R
  _pcr2_R = PCR2 的 Reverse 引物
```

### 输出示例

```
catccaattgagatc | codon 2  | RA_Co2-9_pcr2_R  |   |   |   | RA_Co2-9  | catccaattgagatc  | codon 2  | gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg
cgataccaacagact | codon 10 | RA_Co10-17_pcr2_R|   |   |   | RA_Co10-17| cgataccaacagact  | codon 3  | gatctcaattggatgcggNNKgaaagtctgttggtatcggtttgcaagggcctg
```

> **注意：** Sheet5 的左栏每行递进一个 group，右栏每行递进一条 Fwd Primer（跨 group 滑动）。这是一个紧凑的二维布局。

---

## AI 生成输出要求

AI 生成结果时应能输出以下两种格式：

### 格式 1：CSV / TSV（对标 Sheet2）

```csv
codon,fwd_primer,start_position,rev_primer,ga_arm
codon 1,,,,
codon 2,gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg,4,catccaattgagatc,gatctcaattggatg
codon 3,gatctcaattggatgcggNNKgaaagtctgttggtatcggtttgcaagggcctg,4,,
...
```

### 格式 2：带命名的完整表（对标 Sheet5）

```csv
rev_primer,group_start_codon,rev_name,,,,group_name,ga_arm,codon,fwd_primer
catccaattgagatc,codon 2,RA_Co2-9_pcr2_R,,,,RA_Co2-9,catccaattgagatc,codon 2,gatctcaattggatgNNKcgcgaaagtctgttggtatcggtttgcaagggcctg
cgataccaacagact,codon 10,RA_Co10-17_pcr2_R,,,,RA_Co10-17,cgataccaacagact,codon 3,gatctcaattggatgcggNNKgaaagtctgttggtatcggtttgcaagggcctg
...
```
