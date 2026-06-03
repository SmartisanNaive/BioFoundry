# 05 — 关键数据参考

> 从 Excel 文件中提取的原始数据，供 AI 直接使用。

## RhlA 基因序列（888 bp, 296 codons）

```
atgcggcgcgaaagtctgttggtatcggtttgcaagggcctgcgggtacatgtcgagcgc
gttgggcaggatcccgggcgcagcacggtgatgctggtcaacggcgcgatggcgaccacc
gcctcgttcgcccggacctgcaagtgcctggccgaacatttcaacgtggtgctgttcgac
ctgcccttcgccgggcagtcgcgtcagcacaacccgcagcgcgggttgatcaccaaggac
gacgaggtggaaatcctcctggcgctgatcgagcgcttcgaggtcaatcacctggtctcc
gcgtcctggggcggtatctccacgctgctggcgctgtcgcgcaatccgcgcggcatccg
cagctcggtggtgatggcattcgcccctggactgaaccaggcgatgctcgactacgtcgg
gcgggcgcaggcgctgatcgagctggacgacaagtcggcgatcggccatctgctcaacga
gaccgtcggcaaatacctgccgcagcgcctgaaagccagcaaccatcagcacatggcttc
gctggccaccggcgaatacgagcaggcgcgctttcacatcgaccaggtgctggcgctca
acgatcggggctacttggcttgcctggagcggatccagagccacgtgcatttcatcaacg
gcagctgggacgaatacaccaccgccgaggacgcccgccagttccgcgactacctgccgc
actgcagtttctcgcgggtggagggcaccgggcatttcctcgacctggagtccaagctgg
cagcggtacgcgtgcaccgcgccctgctcgagcacctgctgaagcaaccggagccgcag
cgggcggaacgcgcggcgggattccacgagatggccatcggctacgcctga
```

**注：** 最后 3bp `tga` 为终止密码子。

## 载体侧翼序列

```
15bp-Left  (上游): gcagatctcaattgg
15bp-Right (下游): ggtaccctcgagtct
```

## 分组与引物对照表

### 全部 37 组汇总

| Group | Codon 范围 | Start Position | GA-arm | Rev Primer |
|-------|-----------|----------------|--------|------------|
| 0 | 2-9 | 4 | `gatctcaattggatg` | `catccaattgagatc` |
| 1 | 10-17 | 28 | `agtctgttggtatcg` | `cgataccaacagact` |
| 2 | 18-25 | 52 | `ggcctgcgggtacat` | `atgtacccgcaggcc` |
| 3 | 26-33 | 76 | `gttgggcaggatccc` | `gggatcctgcccaac` |
| 4 | 34-41 | 100 | `acggtgatgctggtc` | `gaccagcatcaccgt` |
| 5 | 42-49 | 124 | `gcgatggcgaccacc` | `ggtggtcgccatcgc` |
| 6 | 50-57 | 148 | `cctcgttcgcccgga` | `tccgggcgaacgagg` |
| 7 | 58-65 | 172 | `ctgcaagtgcctggc` | `gccaggcacttgcag` |
| 8 | 66-73 | 196 | `aacatttcaacgtgg` | `ccacgttgaaatgtt` |
| 9 | 74-81 | 220 | `ctgttcgacctgccc` | `gggcaggtcgaacag` |
| 10 | 82-89 | 244 | `gccgggcagtcgcgt` | `acgcgactgcccggc` |
| 11 | 90-97 | 268 | `cagcacaacccgcag` | `ctgcgggttgtgctg` |
| 12 | 98-105 | 292 | `cgggttgatcaccaa` | `ttggtgatcaacccg` |
| 13 | 106-113 | 316 | `gacgacgaggtggaa` | `ttccacctcgtcgtc` |
| 14 | 114-121 | 340 | `atcctcctggcgctg` | `cagcgccaggaggat` |
| 15 | 122-129 | 364 | `atcgagcgcttcgag` | `ctcgaagcgctcgat` |
| 16 | 130-137 | 388 | `gtcaatcacctggtc` | `gaccaggtgattgac` |
| 17 | 138-145 | 412 | `ccgcgtcctggggcg` | `cgccccaggacgcgg` |
| 18 | 146-153 | 436 | `tatctccacgctgct` | `agcagcgtggagata` |
| 19 | 154-161 | 460 | `gcgctgtcgcgcaat` | `attgcgcgacagcgc` |
| 20 | 162-169 | 484 | `cgcgcggcatccgca` | `tgcggatgccgcgcg` |
| 21 | 170-177 | 508 | `ctcggtggtgatggc` | `gccatcaccaccgag` |
| 22 | 178-185 | 532 | `tcgcccctggactga` | `tcagtccaggggcga` |
| 23 | 186-193 | 556 | `ccaggcgatgctcga` | `tcgagcatcgcctgg` |
| 24 | 194-201 | 580 | `ctacgtcgggcgggc` | `gcccgccgacgtag` |
| 25 | 202-209 | 604 | `caggcgctgatcgag` | `ctcgatcagcgcctg` |
| 26 | 210-217 | 628 | `ctggacgacaagtcg` | `cgacttgtcgtccag` |
| 27 | 218-225 | 652 | `cgatcggccatctgc` | `gcagatggccgatcg` |
| 28 | 226-233 | 676 | `caacgagaccgtcgg` | `ccgacggtctcgttg` |
| 29 | 234-241 | 700 | `aaatacctgccgcag` | `ctgcggcaggtattt` |
| 30 | 242-249 | 724 | `cctgaaagccagcaa` | `ttgctggctttcagg` |
| 31 | 250-257 | 748 | `catcagcacatggct` | `agccatgtgctgatg` |
| 32 | 258-265 | 772 | `gctggccaccggcga` | `tcgccggtggccagc` |
| 33 | 266-273 | 796 | `acgagcaggcgcgct` | `agcgcgcctgctcgt` |
| 34 | 274-281 | 820 | `cgagcacctgctg`* | — |
| 35 | 282-289 | 844 | `gagccgcagcgggcg` | `cgcccgctgcggctc` |
| 36 | 290-295 | 868 | `gcgggattccacgag` | `ctcgtggaatcccgc` |

> *Group 34 的 GA-arm 和 Rev Primer 需从完整数据中验证。

## Codon-WT 氨基酸对照（前 20 位）

| Codon | 位置 (bp) | WT 密码子 | 氨基酸 |
|-------|-----------|----------|--------|
| 1 | 0-2 | ATG | Met (M) |
| 2 | 3-5 | CGG | Arg (R) |
| 3 | 6-8 | CGC | Arg (R) |
| 4 | 9-11 | GAA | Glu (E) |
| 5 | 12-14 | AGT | Ser (S) |
| 6 | 15-17 | CTG | Leu (L) |
| 7 | 18-20 | TTG | Leu (L) |
| 8 | 21-23 | GTA | Val (V) |
| 9 | 24-26 | TCG | Ser (S) |
| 10 | 27-29 | GTT | Val (V) |
| 11 | 30-32 | TGC | Cys (C) |
| 12 | 33-35 | AAG | Lys (K) |
| 13 | 36-38 | GGC | Gly (G) |
| 14 | 39-41 | CTG | Leu (L) |
| 15 | 42-44 | CGG | Arg (R) |
| 16 | 45-47 | GTA | Val (V) |
| 17 | 48-50 | CAT | His (H) |
| 18 | 51-53 | GTC | Val (V) |
| 19 | 54-56 | GAG | Glu (E) |
| 20 | 57-59 | CGC | Arg (R) |
