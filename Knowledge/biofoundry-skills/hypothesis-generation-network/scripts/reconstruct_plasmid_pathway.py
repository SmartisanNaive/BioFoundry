import argparse
import json
import sys

def reconstruct_pathway(op, plasmid, gene):
    """
    Simulates protocol design for plasmid modification.
    """
    protocol = {
        "operation": op,
        "target": gene,
        "source_plasmid": plasmid,
        "steps": [],
        "primers": []
    }
    
    if op == "remove_gene":
        protocol["strategy"] = "Gibson Assembly / Inverse PCR"
        protocol["description"] = f"Remove {gene} coding sequence to study upstream enzyme kinetics."
        
        # Mock primer design
        protocol["primers"] = [
            {
                "name": f"{gene}_del_F",
                "sequence": "5'-[Vector_Overlap]...[Terminator]-3'",
                "tm": 60.5
            },
            {
                "name": f"{gene}_del_R",
                "sequence": "5'-[Vector_Overlap]...[Promoter]-3'",
                "tm": 59.8
            }
        ]
        
        protocol["steps"] = [
            "1. PCR amplify plasmid backbone excluding target gene using designed primers.",
            "2. DpnI digestion to remove template plasmid.",
            "3. Gibson Assembly or KLD reaction to circularize.",
            "4. Transform into E. coli cloning strain."
        ]
        
    elif op == "add_gene":
        protocol["strategy"] = "Golden Gate / Gibson"
        protocol["steps"] = ["Protocol for adding gene not detailed in this mock."]
        
    return protocol

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reconstruct Plasmid Pathway.")
    parser.add_argument("--op", required=True, help="Operation: remove_gene or add_gene")
    parser.add_argument("--plasmid", required=True, help="Plasmid ID")
    parser.add_argument("--gene", required=True, help="Target gene")
    
    args = parser.parse_args()
    
    try:
        result = reconstruct_pathway(args.op, args.plasmid, args.gene)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
