# 03 — AI 理解的完整引物设计策略

> 此文档是 AI 可以直接执行的形式化策略，用于根据输入基因序列自动生成 NNK 饱和突变引物。

## 1. 输入参数

| 参数 | 说明 | 示例值 |
|------|------|--------|
| `gene_seq` | 目标基因编码区序列（不含终止密码子之后的部分） | RhlA: `atgcggcgcgaaagtc...tga`（888bp） |
| `flank_left` | 基因上游的载体同源序列（15bp） | `gcagatctcaattgg` |
| `flank_right` | 基因下游的载体同源序列（15bp） | `ggtaccctcgagtct` |
| `group_size` | 每组覆盖的 codon 数 | 8 |
| `primer_len` | Fwd Primer 总长度 | 54 |
| `arm_len` | GA 同源臂长度 | 15 |
| `excluded_codons` | 不做突变的 codon 编号列表 | [1]（起始密码子 ATG），或 [1, N]（含终止密码子） |

## 2. 核心算法

### 2.1 构建 NNK 替换序列

对于目标 codon `n`（1-indexed），将其替换为 NNK：

```python
def build_modified_seq(gene_seq: str, codon_n: int, flank_left: str, flank_right: str) -> str:
    """
    将基因序列的第 codon_n 个密码子替换为 NNK，
    在两端添加载体同源序列。
    """
    pos = (codon_n - 1) * 3  # codon_n 在 gene_seq 中的 0-indexed 起始位置
    left = gene_seq[:pos]          # NNK 位点之前的全部序列
    right = gene_seq[pos + 3:]     # NNK 位点之后的全部序列
    return flank_left + left + "NNK" + right + flank_right
```

**验证：** codon 2 → `flank_left + atg + NNK + cgcgaaagtc... + flank_right` = 918bp，与 Excel 完全一致。

### 2.2 分组

```python
def assign_group(codon_n: int, group_size: int = 8, start_codon: int = 2) -> int:
    """
    计算给定 codon 所属的分组编号（0-indexed）。
    codon 2-9 → group 0, codon 10-17 → group 1, ...
    """
    return (codon_n - start_codon) // group_size
```

### 2.3 提取 Fwd Primer

每组内所有 codon 共享同一个 Fwd Primer 提取起点：

```python
def extract_fwd_primer(modified_seq: str, group: int,
                       group_size: int = 8, primer_len: int = 54) -> str:
    """
    从 modified_seq 中提取 Fwd Primer。
    每组的提取起点 = group * (group_size * 3) + 4
    """
    start = group * (group_size * 3) + 4  # Excel 公式: I*24+4
    return modified_seq[start : start + primer_len]
```

**关键理解：** 在同一 group 内，所有 codon 的 Fwd Primer 提取窗口 **起点相同**，但 NNK 在窗口内的位置不同。这就是"滑动 NNK"的效果：

- codon 2（group 0 的第 1 个）: NNK 在位置 15（紧接 GA-arm 之后）
- codon 3（group 0 的第 2 个）: NNK 在位置 18（GA-arm + 3bp WT 之后）
- ...
- codon 9（group 0 的第 8 个）: NNK 在位置 36（GA-arm + 21bp WT 之后）

### 2.4 提取 GA-arm 和 Annealing Region

```python
def extract_ga_arm(fwd_primer: str, arm_len: int = 15) -> str:
    """GA-arm = Fwd Primer 的前 15bp"""
    return fwd_primer[:arm_len]

def extract_annealing(fwd_primer: str, arm_len: int = 15) -> str:
    """Annealing region = Fwd Primer 的后 15bp"""
    return fwd_primer[-arm_len:]
```

### 2.5 生成 Rev Primer

```python
def reverse_complement(seq: str) -> str:
    """计算反向互补序列"""
    comp = {'a': 't', 't': 'a', 'g': 'c', 'c': 'g',
            'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(comp[c] for c in reversed(seq))

def generate_rev_primer(ga_arm: str) -> str:
    """Rev Primer = GA-arm 的反向互补"""
    return reverse_complement(ga_arm)
```

## 3. 组装流程

### Gibson Assembly 引物配对结构

```
            ┌─── GA-arm (15bp) ───┐┌── NNK ──┐┌── 下游 WT 序列 ──┐
Fwd Primer: │  gatctcaattggatg    ││  cgg...  ││  cgcgaaagtctg...  │
            └─────────────────────┘└──────────┘└───────────────────┘

            ┌── GA-arm RC (15bp) ──┐
Rev Primer: │  catccaattgagatc     │   ← GA-arm 的反向互补
            └──────────────────────┘
```

### PCR 产物与 Gibson Assembly 连接

```
线性化载体 ─────────────────────────────────────────────────────
                    ↑ Gibson Assembly 连接点

片段 A（上游 PCR 产物）:
  F1 (含 GA-arm) → ← R1 (Rev, 含 GA-arm RC)
  |------- 含 NNK 突变的上游基因片段 -------|

片段 B（下游 PCR 产物）:
  F2 → ← R2 (含 GA-arm)
  |------- 下游野生型基因片段 -------|
```

### 每个 group 的引物清单

每个 group 需要：
- **1 条 Rev Primer**（组内共享）
- **8 条 Fwd Primer**（每个 codon 一条，NNK 位置滑动）
- **1 条 GA-arm**（组内共享，等于 Fwd Primer 的前 15bp）

## 4. 完整生成伪代码

```python
def generate_all_primers(gene_seq, flank_left, flank_right,
                         group_size=8, primer_len=54, arm_len=15):
    total_codons = len(gene_seq) // 3
    results = []

    for codon_n in range(2, total_codons):  # 跳过 codon 1 (ATG)
        group = (codon_n - 2) // group_size

        # 构建 NNK 替换序列
        modified = build_modified_seq(gene_seq, codon_n, flank_left, flank_right)

        # 提取 Fwd Primer
        start_pos = group * (group_size * 3) + 4
        fwd = modified[start_pos : start_pos + primer_len]

        # 处理末尾不足 primer_len 的情况
        if len(fwd) < primer_len:
            fwd = modified[start_pos:]  # 最后一组可能不足 54bp

        # 提取组件
        ga_arm = fwd[:arm_len]
        annealing = fwd[-arm_len:]
        rev = reverse_complement(ga_arm)

        # 判断是否为组内第一个 codon（需要输出 Rev Primer）
        is_group_start = (codon_n - 2) % group_size == 0

        results.append({
            'codon': codon_n,
            'fwd_primer': fwd,
            'start_position': start_pos,
            'rev_primer': rev if is_group_start else '',
            'ga_arm': ga_arm if is_group_start else '',
            'group': group,
        })

    return results
```

## 5. 边界情况处理

| 情况 | 处理方式 |
|------|---------|
| Codon 1（ATG 起始密码子） | 跳过，不生成引物 |
| 最后一个 codon（TGA 终止密码子） | 跳过，不生成引物 |
| 最后一组不足 8 个 codon | 正常处理，fwd primer 长度可能 < 54bp（如 51bp） |
| Fwd Primer 尾部不足 15bp annealing | 取实际可用长度 |

## 6. 三个文库的差异

| 文库 | RhlA 范围 | 特殊处理 |
|------|----------|---------|
| **DDSM (文库 1)** | 全部 codon 2-295 | 无 |
| **ΔHA (文库 2)** | 全部 codon 2-295，删除 HA 标签序列 | 基因序列需移除 HA tag 对应的碱基 |
| **HRA-only (文库 3)** | 仅 HRA 结构域的 codon | 需确定 HRA/RQA 结构域边界；非 HRA 区域不设计引物 |
