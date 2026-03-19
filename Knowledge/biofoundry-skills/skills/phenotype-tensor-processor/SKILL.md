---
name: phenotype-tensor-processor
description: Use this skill to ingest and analyze high-dimensional phenotypic data. This includes querying mass spectrometry databases, detecting artifacts (e.g., false positives from low signals), and running custom Python analysis for visualization and anomaly detection.
---

# Phenotype Tensor Processor

## Overview
This skill processes complex phenotypic data, particularly from high-throughput screening and mass spectrometry.

## Capabilities
- **Query MS Database**: Retrieve mass spec data and filter noise.
- **Run Python Sandbox**: Execute analysis scripts for data visualization and outlier detection.

## Usage
- "Analyze the mass spec data for plate 3 and identify potential artifacts."
- "Visualize the growth curves from the latest run and highlight anomalies."

## Example: Artifact Detection
```python
import pandas as pd
import numpy as np

def detect_artifacts(data, threshold=1000):
    """
    Identify wells with signal intensity below a noise threshold.
    """
    return data[data['intensity'] < threshold]
```
