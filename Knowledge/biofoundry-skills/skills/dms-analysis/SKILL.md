---
name: dms-analysis
description: Use this skill for Deep Mutational Scanning (DMS) data analysis and fitness landscape construction. This includes aligning mutant sequences to wild-type references and computing fitness scores from count data.
---

# DMS Analysis

## Overview
This skill processes sequencing data from deep mutational scanning experiments to infer protein function and fitness.

## Capabilities
- **Align DMS Sequences**: Map reads to reference.
- **Compute Fitness Scores**: Calculate enrichment ratios and fitness values.

## Usage
- "Align the FASTQ reads to the TEM-1 beta-lactamase sequence."
- "Calculate fitness scores for the selection condition vs input."

## Example: Fitness Calculation
Fitness = log2(Count_selected / Count_input) - log2(WT_selected / WT_input)
