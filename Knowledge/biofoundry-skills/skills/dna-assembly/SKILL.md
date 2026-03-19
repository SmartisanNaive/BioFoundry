---
name: dna-assembly
description: Use this skill for DNA assembly tasks, including simulating Golden Gate or Gibson assembly, checking overhang compatibility, and calculating primer melting temperatures.
---

# DNA Assembly Guide

## Overview
This skill provides tools and workflows for synthetic biology DNA assembly. It uses Python libraries like Biopython to simulate assembly processes.

## Capabilities
- Simulate Golden Gate Assembly
- Simulate Gibson Assembly
- Calculate Primer Tm (Melting Temperature)
- Check Overhang Compatibility

## Requirements
- `biopython`

## Examples

### Calculate Primer Tm
```python
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

sequence = Seq("ATGCGTACGTAGCTAGCTAG")
tm = mt.Tm_NN(sequence)
print(f"Melting Temperature: {tm:.2f} C")
```

### Simulate Digestion (Golden Gate)
```python
from Bio.Restriction import BsaI
from Bio.Seq import Seq

# Define a sequence with BsaI sites
seq = Seq("GGTCTC" + "A" + "ATGC" + "T" + "GAGACC")
sites = BsaI.search(seq)
print(f"BsaI sites found at: {sites}")
```

## Best Practices
1. Always verify the restriction enzyme sites are unique if required.
2. Use `Tm_NN` for nearest-neighbor melting temperature calculations.
