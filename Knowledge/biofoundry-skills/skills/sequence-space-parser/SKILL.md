---
name: sequence-space-parser
description: Use this skill to translate digital genotypes into robotic execution protocols. This includes designing Golden Gate assembly pathways for combinatorial libraries and generating liquid handling scripts for Opentrons robots, specifically for E. coli and P. aeruginosa.
---

# Sequence Space Parser

## Overview
This skill handles the conversion of abstract genetic designs into executable laboratory protocols. It focuses on DNA assembly planning and robotic script generation.

## Capabilities
- **Design Golden Gate Assembly**: Calculate optimal assembly paths for combinatorial libraries.
- **Compile Opentrons Scripts**: Generate Python protocols for Opentrons liquid handlers.

## Usage
- "Design a Golden Gate assembly strategy for a library of 24 promoters and 12 RBS sequences."
- "Generate an Opentrons script to assemble these plasmids in E. coli."

## Example: Golden Gate Design
```python
from Bio.Seq import Seq
# Pseudo-code for library design
parts = {
    "promoters": ["P1", "P2", "P3"],
    "rbs": ["RBS1", "RBS2"],
    "cds": ["GFP"]
}
# The skill would output a CSV of well combinations and a transfer map.
```
