Align a Sanger sequencing consensus result against a reference DNA sequence.

Use this tool when the user wants to compare clone validation sequencing, `.seq` files,
FASTA files, pasted Sanger reads, or mutation-confirmation reads against a known construct,
gene, insert, or plasmid reference.

Inputs may be inline DNA sequence text or a file path. Supported file-like inputs include
plain `.seq` files, `.txt`, `.fa`, `.fasta`, and `.fna`. This tool does not parse `.ab1` or
chromatogram quality traces.

The tool automatically tries the query in the forward and reverse-complement orientations,
chooses the better local alignment, and reports identity, coverage, orientation, query N ratio,
mismatches, insertions, deletions, and optional expected mutation checks.

Use `expected_mutations` for clone validation checks such as:

- `A123G`: reference base A at position 123 should appear as G in the query.
- `del45`: any deletion starting at reference position 45 should be present.
- `del45:AC`: deletion of AC starting at reference position 45 should be present.
- `ins78:T`: insertion of T after reference position 78 should be present.

Reference positions are 1-based.
