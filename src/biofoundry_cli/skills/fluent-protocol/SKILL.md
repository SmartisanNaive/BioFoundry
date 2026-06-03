---
name: fluent-protocol
description: Generate or review representative Tecan Fluent worklist/protocol artifacts for Biofoundry Agent supplementary evidence. Use when asked to turn PCR, primer plate, mutation library, Gibson assembly, or liquid-handling plans into machine-readable FluentControl-style GWL/CSV instructions, while clearly separating instruction generation from direct hardware control.
---

# Fluent Protocol Evidence

Use this skill to produce or review lightweight Tecan Fluent worklist/protocol artifacts for
paper evidence. The goal is to show that Biofoundry Agent can generate machine-readable
automation instructions from an experimental design.

## Boundary

- This skill supports protocol/worklist generation only.
- Do not claim direct Fluent hardware control, VisionX execution, or successful robot execution.
- Treat deck layout, labware definitions, liquid classes, FluentControl method compatibility, and run
  reports as facility-side confirmations unless the user provides real files.
- A generated worklist is an automation input sample, not a device run report.

## Minimum Inputs

Before generating a worklist, identify or ask for:

- Source and destination rack labels exactly as FluentControl should see them.
- Source and destination wells or numeric positions.
- Transfer volume in microliters.
- Liquid class, or use `Water Free Single` for representative examples.
- Tip policy, such as fresh tips per transfer or wash between transfers.
- Output path and intended artifact status: representative evidence vs production run input.

## GWL Conventions

Use simple Tecan GWL lines for representative evidence:

```text
C;comment
B;
A;RackLabel;;;Position;;Volume;LiquidClass;;TipMask;
D;RackLabel;;;Position;;Volume;LiquidClass;;TipMask;
W;
```

- `C` is a comment.
- `B` marks a tip break/new-tip boundary in this representative worklist style.
- `W` marks wash tips.
- `A` aspirates and `D` dispenses.
- Positions are 1-based column-major for 96-well plates: `A1=1`, `B1=2`, `H1=8`, `A2=9`.
- Keep comments that identify the design input and the boundary statement.

## Recommended Evidence Shape

For paper supplement artifacts, create:

- A small `.gwl` or `.csv` representative worklist.
- A sidecar manifest with:
  - input design reference
  - generated artifact path
  - scenario and operation summary
  - rack labels, liquid class, tip policy, and well-position convention
  - facility-confirmation fields still required
  - boundary statement that no direct Fluent execution is claimed

## RhlA Example Use

For RhlA NNK primer evidence, a compact artifact can transfer representative forward-primer
aliquots from a primer source plate into a PCR assembly plate:

- Source rack: `RhlA_Primer_Source_Plate`
- Destination rack: `RhlA_PCR_Assembly_Plate`
- Positions: `1-8` for codon 2-9 representative primers
- Volume: `2.0` uL per transfer
- Liquid class: `Water Free Single`
- Tip policy: fresh tip boundary before each transfer

Label the output as representative evidence unless the user provides facility-validated deck,
labware, liquid class, and method details.
