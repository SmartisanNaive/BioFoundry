---
name: momentum-automation
description: Control the Momentum laboratory automation system. Use this skill to manage robotic workflows, check system status, and schedule processes.
license: MIT
compatibility: Python 3.10+; local filesystem; network access to MOMENTUM_URL; Momentum Web Services; optional .env credentials.
metadata:
  skill-author: BioFoundry Agent
---

# Momentum Automation Control

This skill interfaces with the Thermo Fisher Momentum automation software (via Web Services) to control the biofoundry's robotic workcells. It allows for querying system status, managing the scheduler, and submitting process requests.

## Setup

This skill requires Python dependencies. To set up the environment:

```bash
cd biofoundry-skills/momentum-automation
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Ensure a `.env` file exists in this directory or in the `LLMpyMomentum` project root with the necessary credentials:
```
MOMENTUM_URL="https://localhost/api/"
MOMENTUM_USER="webuser1"
MOMENTUM_PASSWD="password"
MOMENTUM_VERIFY=false
MOMENTUM_MOCK=0  # Set to 1 for simulation/mock mode
```

## Tools

### get_momentum_status

Retrieves the current status of the Momentum system, including device states, active processes, and the workqueue.

**Usage:**

```python
import subprocess
import json
import os

def get_momentum_status(target="status"):
    """
    Get status information from Momentum.
    
    Args:
        target (str): Information to retrieve. Options: "status", "devices", "nests", "processes", "workqueue", "version".
                      Default is "status".
    
    Returns:
        dict: The requested status information.
    """
    # Adjust python path to use the skill's venv if available
    python_cmd = "python"
    venv_python = os.path.join(os.path.dirname(__file__), "../.venv/bin/python")
    if os.path.exists(venv_python):
        python_cmd = venv_python

    cmd = [
        python_cmd, 
        "scripts/control_momentum.py", 
        target
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response", "stdout": result.stdout, "stderr": result.stderr}
```

### control_momentum

Controls the Momentum scheduler state (Start, Stop, Simulate).

**Usage:**

```python
import subprocess
import json
import os

def control_momentum(action):
    """
    Control the Momentum scheduler.
    
    Args:
        action (str): Action to perform. Options: "start", "stop", "simulate".
    
    Returns:
        dict: Result of the action.
    """
    if action not in ["start", "stop", "simulate"]:
        return {"error": "Invalid action. Must be 'start', 'stop', or 'simulate'."}

    # Adjust python path to use the skill's venv if available
    python_cmd = "python"
    venv_python = os.path.join(os.path.dirname(__file__), "../.venv/bin/python")
    if os.path.exists(venv_python):
        python_cmd = venv_python

    cmd = [
        python_cmd, 
        "scripts/control_momentum.py", 
        action
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response", "stdout": result.stdout, "stderr": result.stderr}
```

### run_momentum_process

Schedules a process to run on the automation system.

**Usage:**

```python
import subprocess
import json
import os

def run_momentum_process(process_name, variables=None, batch_name="Batch", iterations=1):
    """
    Run a Momentum process.
    
    Args:
        process_name (str): Name of the process to run (must match a defined process in Momentum).
        variables (dict or str): Optional variables to pass to the process. Can be a dict or a JSON string.
        batch_name (str): Name for the batch.
        iterations (int): Number of times to run the process.
    
    Returns:
        dict: Submission result.
    """
    # Adjust python path to use the skill's venv if available
    python_cmd = "python"
    venv_python = os.path.join(os.path.dirname(__file__), "../.venv/bin/python")
    if os.path.exists(venv_python):
        python_cmd = venv_python

    cmd = [
        python_cmd, 
        "scripts/control_momentum.py", 
        "run_process",
        "--process", process_name,
        "--batch", batch_name,
        "--iterations", str(iterations)
    ]
    
    if variables:
        if isinstance(variables, dict):
            variables_str = json.dumps(variables)
        else:
            variables_str = str(variables)
        cmd.extend(["--variables", variables_str])
        
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response", "stdout": result.stdout, "stderr": result.stderr}
```

## Examples

### Checking System Status

```bash
# Assuming running from skill directory and using venv
./.venv/bin/python scripts/control_momentum.py status
```

### Listing Available Processes

```bash
./.venv/bin/python scripts/control_momentum.py processes
```

### Running a Process

Run "PlateTransfer" with specific parameters:

```bash
./.venv/bin/python scripts/control_momentum.py run_process --process "PlateTransfer" --variables '{"Source":"Hotel1", "Destination":"Hotel2"}'
```
