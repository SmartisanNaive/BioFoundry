---
name: hypothesis-generation-network
description: Generate mechanism-based hypotheses and design validation experiments. Use this skill to design control experiments (e.g., using nonsense mutations as knockouts) and reconstruct plasmid pathways (e.g., switching between pathway-level and enzyme-level analysis).
license: MIT
compatibility: Python 3.10+; local filesystem.
metadata:
  skill-author: BioFoundry Agent
---

# Deep Hypothesis Generation & Experiment Reconstruction Network

This skill assists in the scientific reasoning process by proposing specific experiments to test hypotheses about enzyme function and pathway dynamics.

## Tools

### design_control_experiment

Designs control experiments to validate findings or rule out artifacts. Specifically, it can identify and leverage nonsense mutations (STOP codons) within NNK libraries to serve as internal "knockout" controls for distinguishing true activity from background noise.

**Usage:**

```python
import subprocess
import json

def design_control_experiment(experiment_type, library_context=None):
    """
    Design a control experiment based on the hypothesis type.
    
    Args:
        experiment_type (str): Type of control needed (e.g., "nonsense_knockout", "wildtype_baseline").
        library_context (dict): Context about the library (e.g., codon usage, positions).
    
    Returns:
        dict: Experimental design including selected variants and expected outcomes.
    """
    cmd = [
        "python", 
        "scripts/design_control_experiment.py", 
        "--type", experiment_type
    ]
    if library_context:
        cmd.extend(["--context", json.dumps(library_context)])
        
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

### reconstruct_plasmid_pathway

Designs molecular biology protocols to modify pathway architecture. It is used to transition between different experimental setups, such as removing a downstream enzyme (RhlB) to study the upstream enzyme (RhlA) in isolation.

**Usage:**

```python
import subprocess
import json

def reconstruct_plasmid_pathway(operation, plasmid_map, target_gene):
    """
    Design a protocol to reconstruct a plasmid pathway.
    
    Args:
        operation (str): Operation to perform (e.g., "remove_gene", "add_gene").
        plasmid_map (str): Identifier or map of the source plasmid.
        target_gene (str): Gene to target for the operation.
    
    Returns:
        dict: Protocol steps, primer designs, and verification methods.
    """
    cmd = [
        "python", 
        "scripts/reconstruct_plasmid_pathway.py", 
        "--op", operation,
        "--plasmid", plasmid_map,
        "--gene", target_gene
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

## Examples

### Designing Nonsense Controls

To find STOP codon variants in an NNK library at position 102:

```bash
python scripts/design_control_experiment.py --type "nonsense_knockout" --context '{"codon_scheme": "NNK", "target_residues": [102]}'
```

### Removing RhlB for Enzyme-Level Analysis

To design a Gibson assembly protocol to remove the RhlB gene from the pRhlAB plasmid:

```bash
python scripts/reconstruct_plasmid_pathway.py --op "remove_gene" --plasmid "pRhlAB" --gene "RhlB"
```
