---
name: sanger-sequencing-analysis
description: Use this skill to compare Sanger sequencing consensus results against reference DNA sequences for clone validation, mutation confirmation, and insert/plasmid verification.
---

# Sanger Sequencing Analysis

Use this skill when a user provides a Sanger `.seq`, `.txt`, FASTA file, or pasted consensus
sequence and asks whether it matches a reference construct, gene, insert, or expected mutant.

## Workflow

1. Identify the reference DNA sequence and the Sanger query sequence.
2. Call the `SangerAlign` tool with the reference and query as either file paths or inline DNA.
3. Include `expected_mutations` when the user names specific edits to confirm.
4. Interpret the report in clone-validation terms: orientation, covered region, identity, and
   whether mismatches/indels are expected or unexpected.

## Notes

- Reference coordinates in the report are 1-based.
- The tool supports consensus sequence files, not `.ab1` chromatogram quality traces.
- If the query only covers part of a plasmid, focus interpretation on the covered reference region.
