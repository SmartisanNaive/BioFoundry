---
name: biofilm-microscopy
description: Use this skill to capture and analyze organism-level phenotypes using automated microscopy. This includes scheduling time-lapse imaging tasks and extracting morphological features (thickness, coverage, porosity) from biofilm images.
---

# Biofilm Microscopy

## Overview
This skill manages the automated microscopy workflow for biofilm analysis, from image acquisition to feature extraction.

## Capabilities
- **Trigger Microscope Imaging**: Schedule imaging sessions.
- **Analyze Biofilm Morphology**: Quantify biofilm characteristics.

## Usage
- "Schedule a 24-hour time-lapse imaging for the biofilm plate."
- "Calculate the average thickness and roughness of the biofilm from these images."

## Example: Feature Extraction
```python
# Pseudo-code for image analysis
def analyze_image(image_path):
    # Load image
    # Thresholding
    # Calculate coverage
    return coverage_percentage
```
