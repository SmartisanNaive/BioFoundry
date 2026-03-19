# BioFoundry Skills

This repository contains Claude Skills tailored for BioFoundry and Synthetic Biology workflows.
It follows the structure of [anthropics/skills](https://github.com/anthropics/skills).

## Skills List

- **dna-assembly**: Tools for DNA assembly simulation (Golden Gate, Gibson) and primer analysis.

## How to Use in Claude Code

1. **Publish to GitHub**: Push this repository to GitHub.
2. **Add Plugin**: Run the following command in Claude Code:
   ```bash
   /plugin marketplace add <your-github-username>/biofoundry-skills
   ```
3. **Install Skill**:
   ```bash
   /plugin install dna-assembly@biofoundry-skills
   ```
4. **Usage**:
   Simply ask Claude to "Help me design a Golden Gate assembly for this sequence..."

## Directory Structure
- `skills/`: Contains all skill definitions.
  - `<skill-name>/`: Specific skill folder.
    - `SKILL.md`: The instruction file for Claude.
    - `scripts/`: Helper scripts and resources.
