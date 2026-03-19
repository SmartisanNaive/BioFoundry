---
name: biofilm-microscopy
description: Automate biofilm imaging and morphological analysis. Use this skill to schedule time-lapse imaging sessions on motorized stereoscopes and extract features (thickness, coverage, porosity) from the resulting images.
license: MIT
compatibility: Python 3.10+; local filesystem; microscope control environment if triggering hardware.
metadata:
  skill-author: BioFoundry Agent
---

# Biofilm Microscopy Workflow

This skill manages the organismal-level phenotyping workflow, specifically focused on biofilm morphology. It controls imaging hardware and processes image data to quantify complex structural features.

## Tools

### trigger_microscope_imaging

Schedules and triggers imaging sessions on a motorized stereoscope. It supports time-lapse configuration for monitoring biofilm development.

**Usage:**

```python
import subprocess
import json

def trigger_microscope_imaging(session_name, interval_minutes=30, duration_hours=24):
    """
    Schedule a microscope imaging session.
    
    Args:
        session_name (str): Unique identifier for the session.
        interval_minutes (int): Time between captures.
        duration_hours (int): Total duration of the session.
    
    Returns:
        dict: Confirmation of the scheduled session.
    """
    cmd = [
        "python", 
        "scripts/trigger_microscope_imaging.py", 
        "--name", session_name,
        "--interval", str(interval_minutes),
        "--duration", str(duration_hours)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

### analyze_biofilm_morphology

Analyzes biofilm images to extract morphological features. It simulates the stitching of image tiles and the calculation of metrics like thickness, coverage, and porosity.

**Usage:**

```python
import subprocess
import json

def analyze_biofilm_morphology(image_path, variant_id):
    """
    Analyze biofilm morphology from an image set.
    
    Args:
        image_path (str): Path to the image directory or file.
        variant_id (str): ID of the variant being analyzed.
    
    Returns:
        dict: Extracted features (thickness, coverage, porosity).
    """
    cmd = [
        "python", 
        "scripts/analyze_biofilm_morphology.py", 
        "--path", image_path,
        "--variant", variant_id
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

## Examples

### Scheduling a Time-Lapse

To schedule a 48-hour session with images every 30 minutes:

```bash
python scripts/trigger_microscope_imaging.py --name "Experiment_001" --interval 30 --duration 48
```

### Analyzing Biofilm Structure

To analyze the morphology of variant QCM:

```bash
python scripts/analyze_biofilm_morphology.py --path "/data/images/exp001/QCM" --variant "QCM"
```
