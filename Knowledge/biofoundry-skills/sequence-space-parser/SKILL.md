---
name: sequence-space-parser
description: Design and compile automated protocols for constructing genetic variants. Use this skill to calculate Golden Gate assembly paths for combinatorial libraries or generate Opentrons liquid handling scripts for E. coli or P. aeruginosa chassis. Key functions include optimizing fragment combinations and adapting protocols for specific organisms.
license: MIT
compatibility: Python 3.10+; local filesystem.
metadata:
  skill-author: BioFoundry Agent
---

# Sequence Space Parser & Protocol Compiler

This skill provides tools for translating digital genotype designs into physical execution protocols. It handles the complexity of combinatorial assembly and generates machine-executable scripts for liquid handling robots.

## Tools

### design_golden_gate

Calculates optimal Golden Gate assembly paths from a library of DNA fragments. It can handle large combinatorial spaces (up to 663,552 combinations) and optimize for efficient construction.

**Usage:**

```python
import json
import subprocess

def design_golden_gate(target_variants, fragment_library_path):
    """
    Design Golden Gate assembly paths for target variants.
    
    Args:
        target_variants (list): List of variant specifications (e.g., mutation codes or sequences).
        fragment_library_path (str): Path to the fragment library definition file.
    
    Returns:
        dict: Assembly plan including well allocations and mixing instructions.
    """
    cmd = [
        "python", 
        "scripts/design_golden_gate.py", 
        "--variants", json.dumps(target_variants),
        "--library", fragment_library_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

### compile_opentrons_script

Generates Python scripts for Opentrons liquid handling robots. It supports cross-chassis adaptation, allowing protocols to be generated for *E. coli* or *P. aeruginosa* workflows.

**Usage:**

```python
import subprocess

def compile_opentrons_script(protocol_type, parameters, chassis="E_coli"):
    """
    Compile an Opentrons script for a specific protocol.
    
    Args:
        protocol_type (str): Type of protocol (e.g., "transformation", "assembly", "transfer").
        parameters (dict): Protocol-specific parameters (e.g., volumes, incubation times).
        chassis (str): Target organism ("E_coli" or "P_aeruginosa").
    
    Returns:
        str: Generated Python script content for Opentrons.
    """
    cmd = [
        "python", 
        "scripts/compile_opentrons_script.py", 
        "--type", protocol_type,
        "--params", json.dumps(parameters),
        "--chassis", chassis
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
```

## Examples

### Designing a Combinatorial Library

To design assembly paths for a set of variants:

```bash
python scripts/design_golden_gate.py --variants '[{"id": "var1", "mutations": ["F43Q", "R74C"]}, {"id": "var2", "mutations": ["F43W", "R74H"]}]' --library "data/fragments.json"
```

### Generating a Transformation Protocol

To generate a transformation script for *P. aeruginosa*:

```bash
python scripts/compile_opentrons_script.py --type "transformation" --params '{"temp": 42, "time": 45}' --chassis "P_aeruginosa"
```
