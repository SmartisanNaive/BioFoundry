import argparse
import json
import sys
import traceback

def execute_sandbox(code, data):
    """
    Executes Python code in a restricted environment.
    The 'data' variable is injected into the local scope.
    """
    
    # scope for execution
    local_scope = {
        "data": data,
        "json": json,
        "print": print
    }
    
    # Try to import common data science libs if available
    try:
        import math
        local_scope["math"] = math
    except ImportError:
        pass
        
    try:
        exec(code, {}, local_scope)
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Python Sandbox.")
    parser.add_argument("--code", required=True, help="Python code to execute")
    parser.add_argument("--data", default="[]", help="JSON data input")
    
    args = parser.parse_args()
    
    try:
        input_data = json.loads(args.data)
        execute_sandbox(args.code, input_data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for data.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
