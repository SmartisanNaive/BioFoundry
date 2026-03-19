---
name: epistasis-analysis
description: Use this skill to detect and quantify epistatic interactions between mutations. This includes identifying pairwise interactions and quantifying their strength.
---

# Epistasis Analysis

## Overview
This skill analyzes genetic interactions, specifically epistasis, where the effect of one mutation depends on the presence of another.

## Capabilities
- **Detect Epistasis**: Find non-additive interactions.
- **Compute Epistasis Strength**: Measure the magnitude of deviation from additivity.

## Usage
- "Analyze the double mutants for epistasis."
- "Is the interaction between mutation A and mutation B positive or negative?"

## Example: Epistasis Calculation
Epistasis (ε) = Fitness(AB) - Fitness(A) - Fitness(B) + Fitness(WT)
