# BioFoundry Agent Skills

English | [中文](./README_zh.md)

This directory contains a set of Claude Code skills designed to implement the autonomous biofoundry agent architecture described in the paper *"Autonomous biofoundry reveals hierarchical epistasis emergence from enzyme to pathway"*.

These skills correspond to the four core modules of the agent system:

## 1. Sequence Space Parser & Protocol Compiler (`sequence-space-parser`)

**Purpose:** Transform digital genotypes into robotic execution protocols.
- **`design_golden_gate`**: Calculate optimal Golden Gate assembly paths for combinatorial libraries.
- **`compile_opentrons_script`**: Generate liquid handling scripts for *E. coli* and *P. aeruginosa*.

## 2. Multimodal Phenotype Tensor Processor (`phenotype-tensor-processor`)

**Purpose:** Ingest and analyze high-dimensional phenotypic data.
- **`query_ms_database`**: Retrieve mass spectrometry data and perform artifact detection (e.g., identifying false positives with low signals).
- **`run_python_sandbox`**: Execute custom analysis for visualization and anomaly detection.

## 3. Deep Hypothesis Generation & Experimental Reconstruction Network (`hypothesis-generation-network`)

**Purpose:** Generate mechanism-based hypotheses and design verification experiments.
- **`design_control_experiment`**: Design control experiments, such as using nonsense mutations as natural knockout controls.
- **`reconstruct_plasmid_pathway`**: Plan molecular biology operations to modify pathway architecture (e.g., removing RhlB).

## 4. Biofilm Microscopy Workflow (`biofilm-microscopy`)

**Purpose:** Capture and analyze organism-level phenotypes.
- **`trigger_microscope_imaging`**: Schedule automated time-lapse imaging tasks.
- **`analyze_biofilm_morphology`**: Extract morphological features (thickness, coverage, porosity) from biofilm images.

## 5. KEGG Database Access (`kegg-database`)

**Purpose:** Query KEGG pathway and reaction databases for metabolic network analysis.
- **`query_kegg_pathway`**: Retrieve metabolic pathway information and gene annotations.
- **`query_kegg_reaction`**: Get enzyme reaction data and EC number mapping.

## 6. PDB Database Access (`pdb-database`)

**Purpose:** Retrieve and analyze protein structures from RCSB PDB.
- **`fetch_pdb_structure`**: Download protein structure files in PDB/mmCIF format.
- **`query_pdb_by_sequence`**: Search PDB entries using sequence similarity.

## 7. Momentum Lab Automation (`momentum-automation`)

**Purpose:** Control Momentum lab automation systems for high-throughput experiments.
- **`schedule_momentum_protocol`**: Schedule and execute automated protocol runs.
- **`monitor_momentum_status`**: Monitor instrument status and task queues.

## 8. DMS Analysis (`dms-analysis`)

**Purpose:** Deep Mutational Scanning data analysis and fitness landscape construction.
- **`align_dms_sequences`**: Align mutant sequences to wild-type reference sequences.
- **`compute_fitness_scores`**: Calculate fitness scores from count data.

## 9. Epistasis Analysis (`epistasis-analysis`)

**Purpose:** Detect and quantify epistatic interactions between mutations.
- **`detect_epistasis`**: Identify pairwise epistatic interactions.
- **`compute_epistasis_strength`**: Quantify the magnitude of epistatic effects.

## 10. LC-MS Analysis (`lcms-analysis`)

**Purpose:** Liquid Chromatography-Mass Spectrometry data processing.
- **`process_lcms_data`**: Process raw LC-MS data for metabolite identification.
- **`quantify_peaks`**: Perform peak detection and quantification.

## 11. Momentum Workflow (`momentum-workflow`)

**Purpose:** Orchestrate multi-step automated workflows on Momentum systems.
- **`design_workflow`**: Design multi-step experimental workflows.
- **`execute_workflow`**: Execute and monitor workflow progress.

## 12. Pathway Engineering (`pathway-engineering`)

**Purpose:** Design and optimize metabolic pathways for target compound production.
- **`design_pathway`**: Design pathway schemes for target molecules.
- **`optimize_enzymes`**: Select and engineer enzymes to improve pathway efficiency.

## Usage

Each skill is a standalone directory containing a `SKILL.md` file that defines the tool and a `scripts/` directory containing the implementation logic. These skills are designed for AI agents to autonomously plan and execute experiments in a biofoundry environment.

## How to Load in Claude Code

Claude Code discovers skills from project-level skill directories. Common directories include:
- `.claude/skills/`
- `.github/skills/`
- `.agents/skills/`

It is recommended to link the skills from this directory to `.claude/skills/` at the repository root:

```bash
mkdir -p .claude/skills
ln -s ../../biofoundry-skills/skills/dna-assembly .claude/skills/dna-assembly
ln -s ../../biofoundry-skills/skills/sequence-space-parser .claude/skills/sequence-space-parser
ln -s ../../biofoundry-skills/skills/phenotype-tensor-processor .claude/skills/phenotype-tensor-processor
ln -s ../../biofoundry-skills/skills/hypothesis-generation-network .claude/skills/hypothesis-generation-network
ln -s ../../biofoundry-skills/skills/biofilm-microscopy .claude/skills/biofilm-microscopy
```
