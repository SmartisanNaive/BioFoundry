---
name: pdb-database
description: Access RCSB PDB for 3D protein/nucleic acid structures. Search by text/sequence/structure, download coordinates (PDB/mmCIF), retrieve metadata, for structural biology and drug discovery.
license: Unknown
compatibility: Python 3.10+; network access to https://search.rcsb.org and https://data.rcsb.org; local filesystem.
metadata:
    skill-author: K-Dense Inc.
---

# PDB Database

## Overview

RCSB PDB is the worldwide repository for 3D structural data of biological macromolecules. Search for structures, retrieve coordinates and metadata, perform sequence and structure similarity searches across 200,000+ experimentally determined structures and computed models.

## When to Use This Skill

This skill should be used when:
- Searching for protein or nucleic acid 3D structures by text, sequence, or structural similarity
- Downloading coordinate files in PDB, mmCIF, or BinaryCIF formats
- Retrieving structural metadata, experimental methods, or quality metrics
- Performing batch operations across multiple structures
- Integrating PDB data into computational workflows for drug discovery, protein engineering, or structural biology research

## Core Capabilities

### 1. Searching for Structures

Find PDB entries using various search criteria:

**Text Search:** Search by protein name, keywords, or descriptions
```python
import subprocess
import json

def pdb_text_search(query_text, return_type="entry_id", limit=50):
    """
    Text search using RCSB Search API via curl.
    
    Args:
        query_text (str): Text to search for.
        return_type (str): Return type, usually "entry_id".
        limit (int): Maximum results to return.
    
    Returns:
        list: Matching entry IDs.
    """
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": "rcsb_entry_info.entry_title",
                "operator": "contains_phrase",
                "value": query_text
            }
        },
        "return_type": return_type,
        "request_options": {
            "pager": {
                "start": 0,
                "rows": limit
            }
        }
    }
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://search.rcsb.org/rcsbsearch/v2/query",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(query)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    return [item["identifier"] for item in payload.get("result_set", [])]

results = pdb_text_search("hemoglobin")
print(f"Found {len(results)} structures")
```

**Attribute Search:** Query specific properties (organism, resolution, method, etc.)
```python
import subprocess
import json

def pdb_attribute_search(attribute, operator, value, return_type="entry_id", limit=50):
    """
    Attribute search using RCSB Search API via curl.
    
    Args:
        attribute (str): RCSB attribute path.
        operator (str): Operator (e.g., "exact_match", "less").
        value (str|int|float): Value to match.
        return_type (str): Return type, usually "entry_id".
        limit (int): Maximum results to return.
    
    Returns:
        list: Matching entry IDs.
    """
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": attribute,
                "operator": operator,
                "value": value
            }
        },
        "return_type": return_type,
        "request_options": {
            "pager": {
                "start": 0,
                "rows": limit
            }
        }
    }
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://search.rcsb.org/rcsbsearch/v2/query",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(query)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    return [item["identifier"] for item in payload.get("result_set", [])]

# Find human protein structures
results = pdb_attribute_search(
    attribute="rcsb_entity_source_organism.scientific_name",
    operator="exact_match",
    value="Homo sapiens"
)
```

**Sequence Similarity:** Find structures similar to a given sequence
```python
import subprocess
import json

def pdb_sequence_search(sequence, evalue_cutoff=0.1, identity_cutoff=0.9, return_type="entry_id", limit=50):
    """
    Sequence similarity search using RCSB Search API via curl.
    """
    query = {
        "query": {
            "type": "terminal",
            "service": "sequence",
            "parameters": {
                "evalue_cutoff": evalue_cutoff,
                "identity_cutoff": identity_cutoff,
                "sequence_type": "protein",
                "value": sequence
            }
        },
        "return_type": return_type,
        "request_options": {
            "pager": {
                "start": 0,
                "rows": limit
            }
        }
    }
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://search.rcsb.org/rcsbsearch/v2/query",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(query)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    return [item["identifier"] for item in payload.get("result_set", [])]

results = pdb_sequence_search(
    "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQGVDDAFYTLVREIRKHKEKMSKDGKKKKKKSKTKCVIM"
)
```

**Structure Similarity:** Find structures with similar 3D geometry
```python
import subprocess
import json

def pdb_structure_similarity(entry_id, return_type="entry_id", limit=50):
    """
    Structure similarity search using RCSB Search API via curl.
    """
    query = {
        "query": {
            "type": "terminal",
            "service": "structure",
            "parameters": {
                "structure_search_type": "entry",
                "entry_id": entry_id
            }
        },
        "return_type": return_type,
        "request_options": {
            "pager": {
                "start": 0,
                "rows": limit
            }
        }
    }
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://search.rcsb.org/rcsbsearch/v2/query",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(query)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    return [item["identifier"] for item in payload.get("result_set", [])]

results = pdb_structure_similarity("4HHB")
```

**Combining Queries:** Use logical operators to build complex searches
```python
import subprocess
import json

def pdb_combined_query(queries, operator="and", return_type="entry_id", limit=50):
    """
    Combine terminal queries using logical operators.
    """
    query = {
        "query": {
            "type": "group",
            "logical_operator": operator,
            "nodes": queries
        },
        "return_type": return_type,
        "request_options": {
            "pager": {
                "start": 0,
                "rows": limit
            }
        }
    }
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://search.rcsb.org/rcsbsearch/v2/query",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(query)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    return [item["identifier"] for item in payload.get("result_set", [])]

# High-resolution human proteins
query1 = {
    "type": "terminal",
    "service": "text",
    "parameters": {
        "attribute": "rcsb_entity_source_organism.scientific_name",
        "operator": "exact_match",
        "value": "Homo sapiens"
    }
}
query2 = {
    "type": "terminal",
    "service": "text",
    "parameters": {
        "attribute": "rcsb_entry_info.resolution_combined",
        "operator": "less",
        "value": 2.0
    }
}
results = pdb_combined_query([query1, query2], operator="and")
```

### 2. Retrieving Structure Data

Access detailed information about specific PDB entries:

**Basic Entry Information:**
```python
import subprocess
import json

def pdb_entry_data(entry_id):
    """
    Fetch entry data from RCSB Data API via curl.
    """
    url = f"https://data.rcsb.org/rest/v1/core/entry/{entry_id}"
    cmd = ["curl", "-sS", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

entry_data = pdb_entry_data("4HHB")
print(entry_data["struct"]["title"])
print(entry_data["exptl"][0]["method"])
```

**Polymer Entity Information:**
```python
import subprocess
import json

def pdb_polymer_entity(entity_id):
    """
    Fetch polymer entity data from RCSB Data API via curl.
    """
    url = f"https://data.rcsb.org/rest/v1/core/polymer_entity/{entity_id}"
    cmd = ["curl", "-sS", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

entity_data = pdb_polymer_entity("4HHB_1")
print(entity_data["entity_poly"]["pdbx_seq_one_letter_code"])
```

**Using GraphQL for Flexible Queries:**
```python
import subprocess
import json

def pdb_graphql(query):
    """
    Run a GraphQL query against RCSB via curl.
    """
    payload = {"query": query}
    cmd = [
        "curl", "-sS", "-X", "POST",
        "https://data.rcsb.org/graphql",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

query = """
{
  entry(entry_id: "4HHB") {
    struct {
      title
    }
    exptl {
      method
    }
    rcsb_entry_info {
      resolution_combined
      deposited_atom_count
    }
  }
}
"""
data = pdb_graphql(query)
```

### 3. Downloading Structure Files

Retrieve coordinate files in various formats:

**Download Methods:**
- **PDB format** (legacy text format): `https://files.rcsb.org/download/{PDB_ID}.pdb`
- **mmCIF format** (modern standard): `https://files.rcsb.org/download/{PDB_ID}.cif`
- **BinaryCIF** (compressed binary): Use ModelServer API for efficient access
- **Biological assembly**: `https://files.rcsb.org/download/{PDB_ID}.pdb1` (for assembly 1)

**Example Download:**
```python
import subprocess

pdb_id = "4HHB"

# Download PDB format
pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
subprocess.run(["curl", "-sS", "-o", f"{pdb_id}.pdb", pdb_url], check=False)

# Download mmCIF format
cif_url = f"https://files.rcsb.org/download/{pdb_id}.cif"
subprocess.run(["curl", "-sS", "-o", f"{pdb_id}.cif", cif_url], check=False)
```

### 4. Working with Structure Data

Common operations with retrieved structures:

**Parse and Analyze Coordinates:**
Use structural biology libraries to work with downloaded files. Example with BioPython:
```python
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("protein", "4HHB.pdb")

# Iterate through atoms
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom.get_coord())
```

**Extract Metadata:**
```python
import subprocess
import json

def pdb_entry_data(entry_id):
    """
    Fetch entry data from RCSB Data API via curl.
    """
    url = f"https://data.rcsb.org/rest/v1/core/entry/{entry_id}"
    cmd = ["curl", "-sS", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

data = pdb_entry_data("4HHB")
resolution = data.get("rcsb_entry_info", {}).get("resolution_combined")
method = data.get("exptl", [{}])[0].get("method")
deposition_date = data.get("rcsb_accession_info", {}).get("deposit_date")

print(f"Resolution: {resolution} Å")
print(f"Method: {method}")
print(f"Deposited: {deposition_date}")
```

### 5. Batch Operations

Process multiple structures efficiently:

```python
import subprocess
import json

def pdb_entry_data(entry_id):
    """
    Fetch entry data from RCSB Data API via curl.
    """
    url = f"https://data.rcsb.org/rest/v1/core/entry/{entry_id}"
    cmd = ["curl", "-sS", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

pdb_ids = ["4HHB", "1MBN", "1GZX"]  # Hemoglobin, myoglobin, etc.

results = {}
for pdb_id in pdb_ids:
    try:
        data = pdb_entry_data(pdb_id)
        results[pdb_id] = {
            "title": data["struct"]["title"],
            "resolution": data.get("rcsb_entry_info", {}).get("resolution_combined"),
            "organism": data.get("rcsb_entity_source_organism", [{}])[0].get("scientific_name")
        }
    except Exception as e:
        print(f"Error fetching {pdb_id}: {e}")

# Display results
for pdb_id, info in results.items():
    print(f"\n{pdb_id}: {info['title']}")
    print(f"  Resolution: {info['resolution']} Å")
    print(f"  Organism: {info['organism']}")
```

## Python Package Installation

Optional: install a Python client if you prefer a library wrapper:

```bash
uv pip install rcsb-api
```

If you use the library client, update the examples accordingly.

## Common Use Cases

### Drug Discovery
- Search for structures of drug targets
- Analyze ligand binding sites
- Compare protein-ligand complexes
- Identify similar binding pockets

### Protein Engineering
- Find homologous structures for modeling
- Analyze sequence-structure relationships
- Compare mutant structures
- Study protein stability and dynamics

### Structural Biology Research
- Download structures for computational analysis
- Build structure-based alignments
- Analyze structural features (secondary structure, domains)
- Compare experimental methods and quality metrics

### Education and Visualization
- Retrieve structures for teaching
- Generate molecular visualizations
- Explore structure-function relationships
- Study evolutionary conservation

## Key Concepts

**PDB ID:** Unique 4-character identifier (e.g., "4HHB") for each structure entry. AlphaFold and ModelArchive entries start with "AF_" or "MA_" prefixes.

**mmCIF/PDBx:** Modern file format that uses key-value structure, replacing legacy PDB format for large structures.

**Biological Assembly:** The functional form of a macromolecule, which may contain multiple copies of chains from the asymmetric unit.

**Resolution:** Measure of detail in crystallographic structures (lower values = higher detail). Typical range: 1.5-3.5 Å for high-quality structures.

**Entity:** A unique molecular component in a structure (protein chain, DNA, ligand, etc.).

## Resources

This skill includes reference documentation in the `references/` directory:

### references/api_reference.md
Comprehensive API documentation covering:
- Detailed API endpoint specifications
- Advanced query patterns and examples
- Data schema reference
- Rate limiting and best practices
- Troubleshooting common issues

Use this reference when you need in-depth information about API capabilities, complex query construction, or detailed data schema information.

## Additional Resources

- **RCSB PDB Website:** https://www.rcsb.org
- **PDB-101 Educational Portal:** https://pdb101.rcsb.org
- **API Documentation:** https://www.rcsb.org/docs/programmatic-access/web-apis-overview
- **Python Package Docs:** https://rcsbapi.readthedocs.io/
- **Data API Documentation:** https://data.rcsb.org/
- **GitHub Repository:** https://github.com/rcsb/py-rcsb-api
