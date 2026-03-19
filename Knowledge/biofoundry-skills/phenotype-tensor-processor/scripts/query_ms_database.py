import argparse
import json
import sys
import random

def query_database(variant_ids, metrics):
    """
    Simulates querying a Mass Spectrometry database.
    """
    results = []
    
    for vid in variant_ids:
        # Mock data generation based on variant ID patterns
        
        # Default mock values
        rl_all = random.uniform(0.5, 1.5)
        rl_c18 = random.uniform(0.1, 0.8) * rl_all
        specificity = (rl_c18 / rl_all) * 100 if rl_all > 0 else 0
        
        # Simulate "Stop" codon variants (nonsense mutations)
        if "STOP" in vid:
            rl_all = random.uniform(0.01, 0.10) # Very low production
            # Artifact: low production but high apparent specificity
            specificity = random.uniform(80, 99) 
            rl_c18 = rl_all * (specificity / 100)
            
        # Simulate high performing variants
        elif "QCM" in vid:
            rl_all = 4.5
            specificity = 92.8
            rl_c18 = rl_all * (specificity / 100)
        elif "WHI" in vid:
            rl_all = 7.4
            specificity = 72.6
            rl_c18 = rl_all * (specificity / 100)
            
        record = {
            "variant_id": vid,
        }
        
        # Populate requested metrics
        if "RL_All" in metrics:
            record["RL_All"] = round(rl_all, 3)
        if "RL_C18" in metrics:
            record["RL_C18"] = round(rl_c18, 3)
        if "Specificity_Ratio" in metrics:
            record["Specificity_Ratio"] = round(specificity, 2)
            
        # Add artifact flag logic mentioned in the paper
        if rl_all < 0.11 and specificity > 50:
             record["artifact_flag"] = "POSSIBLE_LOW_SIGNAL_ARTIFACT"
             
        results.append(record)
        
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query MS Database.")
    parser.add_argument("--ids", required=True, help="JSON list of variant IDs")
    parser.add_argument("--metrics", default='["RL_All", "RL_C18", "Specificity_Ratio"]', help="JSON list of metrics")
    
    args = parser.parse_args()
    
    try:
        vids = json.loads(args.ids)
        metrics = json.loads(args.metrics)
        data = query_database(vids, metrics)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
