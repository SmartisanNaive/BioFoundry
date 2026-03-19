import argparse
import json
import sys

def design_controls(exp_type, context):
    """
     designs control experiments.
    """
    design = {
        "experiment_type": exp_type,
        "controls": [],
        "rationale": ""
    }
    
    if exp_type == "nonsense_knockout":
        design["rationale"] = "Use nonsense mutations as natural null controls to establish background signal levels."
        
        codon_scheme = context.get("codon_scheme", "NNK")
        target_residues = context.get("target_residues", [])
        
        if codon_scheme == "NNK":
            # NNK (N=A/C/G/T, K=G/T) encodes 32 codons, including 1 stop (TAG - Amber)
            # Depending on the host, TAG might be suppressed, but generally it's a stop.
            # TAA (Ochre) and TGA (Opal) are not in NNK (TGA is T, G, A -> N, N, K? No. K is G/T. TGA requires A at 3rd pos.)
            # Wait, NNK: 
            # 1: A,C,G,T
            # 2: A,C,G,T
            # 3: G,T
            # Stops: TAA, TAG, TGA
            # TAA: T, A, A (3rd pos A is not in G/T) -> Not in NNK
            # TAG: T, A, G (3rd pos G is in G/T) -> In NNK
            # TGA: T, G, A (3rd pos A is not in G/T) -> Not in NNK
            # So only TAG is the stop in NNK.
            
            for resid in target_residues:
                design["controls"].append({
                    "variant_id": f"STOP_{resid}",
                    "mutation": f"{resid}*",
                    "codon": "TAG",
                    "expected_phenotype": "inactive (unless artifact)"
                })
        else:
             design["controls"].append({"note": " codon scheme logic not implemented for non-NNK"})

    elif exp_type == "wildtype_baseline":
        design["rationale"] = "Establish baseline activity and specificity."
        design["controls"].append({
             "variant_id": "WT_Control",
             "description": "Wild-type sequence plasmid"
        })
        
    return design

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Design Control Experiments.")
    parser.add_argument("--type", required=True, help="Experiment type")
    parser.add_argument("--context", default="{}", help="JSON context")
    
    args = parser.parse_args()
    
    try:
        context = json.loads(args.context)
        result = design_controls(args.type, context)
        print(json.dumps(result, indent=2))
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for context.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
