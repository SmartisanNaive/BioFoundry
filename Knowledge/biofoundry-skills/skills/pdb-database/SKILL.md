---
name: pdb-database
description: Use this skill to retrieve and analyze protein structures from the RCSB PDB. This includes fetching PDB/mmCIF files and searching for PDB entries using sequence similarity.
---

# PDB Database Access

## Overview
This skill allows interaction with the Protein Data Bank (PDB) to retrieve structural data.

## Capabilities
- **Fetch PDB Structure**: Download structure files.
- **Query PDB by Sequence**: Find structures matching a protein sequence.

## Usage
- "Download the PDB file for 1CRN."
- "Find PDB entries with >90% similarity to this sequence."

## Example: Fetch Structure
```python
from Bio.PDB import PDBList
pdbl = PDBList()
pdbl.retrieve_pdb_file('1FAT', pdir='.', file_format='pdb')
```
