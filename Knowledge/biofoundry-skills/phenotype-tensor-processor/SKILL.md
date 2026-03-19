---
name: phenotype-tensor-processor
description: Process and analyze multi-modal phenotypic data from mass spectrometry and other instruments. Use this skill to query MS databases for variant phenotyping (RL-All, RL-C18, etc.) and run custom Python analysis scripts for visualization (PCA, bubble graphs) and anomaly detection.
license: MIT
compatibility: Python 3.10+; local filesystem.
metadata:
  skill-author: BioFoundry Agent
---

# Multi-modal Phenotype Tensor Processor

This skill handles the ingestion and analysis of high-dimensional phenotypic data. It connects to the mass spectrometry database and provides a sandbox for advanced data analysis and visualization.

## Tools

### query_ms_database

Retrieves LC-MS/MS data for specific variants. It includes logic to filter artifacts (e.g., low production variants with skewed specificity ratios).

**Usage:**

```python
import json
import subprocess

def query_ms_database(variant_ids, metrics=["RL_All", "RL_C18", "Specificity_Ratio"]):
    """
    Query the MS database for variant phenotypes.
    
    Args:
        variant_ids (list): List of variant IDs to query.
        metrics (list): List of metrics to retrieve.
    
    Returns:
        list: List of dictionaries containing phenotype data for each variant.
    """
    cmd = [
        "python", 
        "scripts/query_ms_database.py", 
        "--ids", json.dumps(variant_ids),
        "--metrics", json.dumps(metrics)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

### run_python_sandbox

Executes custom Python code for data analysis and visualization. Useful for generating PCA plots, bubble graphs, or running statistical tests on retrieved data.

**Usage:**

```python
import subprocess

def run_python_sandbox(code, input_data=None):
    """
    Run Python code in a sandboxed environment.
    
    Args:
        code (str): Python code to execute.
        input_data (dict): Optional input data to be available as `data` variable in the script.
    
    Returns:
        str: Output (stdout) of the script.
    """
    cmd = ["python", "scripts/run_python_sandbox.py", "--code", code]
    if input_data:
        cmd.extend(["--data", json.dumps(input_data)])
        
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
```

## Examples

### Querying Variant Data

```bash
python scripts/query_ms_database.py --ids '["var1", "var2", "STOP_118"]'
```

### Analyzing Data with Sandbox

```bash
python scripts/run_python_sandbox.py --code "import numpy as np; print(np.mean([d['RL_All'] for d in data]))" --data '[{"RL_All": 1.2}, {"RL_All": 0.8}]'
```
