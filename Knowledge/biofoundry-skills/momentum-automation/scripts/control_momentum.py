import argparse
import json
import sys
import os
from typing import Any, Dict, List, Optional
from dotenv import dotenv_values

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from momentum_ws import Momentum

class MockMomentum:
    def __init__(self) -> None:
        self._state = {
            "Simulated": True,
            "Attended": True,
            "State": {"Status": "Idle"},
        }

    def get_status(self) -> Dict[str, Any]:
        return self._state

    def get_version(self) -> Dict[str, Any]:
        return {"Version": "0.0.0-mock"}

    def start(self) -> None:
        self._state["State"] = {"Status": "Running"}
        return {"Status": "Running"}

    def simulate(self) -> None:
        self._state["State"] = {"Status": "SimulateRunning"}
        return {"Status": "SimulateRunning"}

    def stop(self) -> None:
        self._state["State"] = {"Status": "Stopped"}
        return {"Status": "Stopped"}

    def get_devices(self) -> List[Dict[str, Any]]:
        return [
            {
                "Id": "dev-1",
                "Name": "Hotel_1",
                "IsInstrument": True,
                "IsSimulated": True,
                "State": "Online",
            }
        ]

    def get_nests(self) -> List[Dict[str, Any]]:
        return [
            {
                "Name": "Hotel_1:Nests:Nest 1",
                "DeviceName": "Hotel_1",
                "Content": None,
                "IsStack": False,
                "StackContents": [],
            }
        ]

    def get_processes(self) -> List[Dict[str, Any]]:
        return [{"Id": "proc-1", "Name": "MockProcess"}]

    def get_workqueue(self) -> List[Dict[str, Any]]:
        return []

    def run_process(self, *args, **kwargs):
        return {"Details": "mock run_process accepted", "args": args, "kwargs": kwargs}


def main():
    parser = argparse.ArgumentParser(description="Control Momentum Automation System")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Status commands
    subparsers.add_parser("status", help="Get system status")
    subparsers.add_parser("version", help="Get system version")
    subparsers.add_parser("devices", help="Get devices list")
    subparsers.add_parser("nests", help="Get nests list")
    subparsers.add_parser("processes", help="Get processes list")
    subparsers.add_parser("workqueue", help="Get workqueue")

    # Control commands
    subparsers.add_parser("start", help="Start system")
    subparsers.add_parser("stop", help="Stop system")
    subparsers.add_parser("simulate", help="Start simulation mode")

    # Run Process
    run_parser = subparsers.add_parser("run_process", help="Run a process")
    run_parser.add_argument("--process", required=True, help="Process name")
    run_parser.add_argument("--variables", help="JSON string or key=value pairs (semicolon separated)")
    run_parser.add_argument("--batch", default="Batch", help="Batch name")
    run_parser.add_argument("--iterations", type=int, default=1, help="Number of iterations")
    run_parser.add_argument("--append", action="store_true", default=True, help="Append to existing workunit")
    run_parser.add_argument("--delay", type=int, default=0, help="Minimum delay")
    run_parser.add_argument("--workunit", help="Workunit name")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Determine if we should use Mock
    env_path = ".env"
    if not os.path.exists(env_path):
         # Try fallback
         potential_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../LLMpyMomentum/.env"))
         if os.path.exists(potential_path):
             env_path = potential_path
    
    config = dotenv_values(env_path)
    use_mock = config.get("MOMENTUM_MOCK", os.environ.get("MOMENTUM_MOCK", "0"))

    try:
        if str(use_mock).lower() in ("1", "true", "yes", "on"):
            client = MockMomentum()
        else:
            client = Momentum()
    except Exception as e:
        print(json.dumps({"error": str(e), "hint": "Check .env file or credentials"}))
        sys.exit(1)

    try:
        if args.command == "status":
            print(json.dumps(client.get_status(), indent=2))
        elif args.command == "version":
            print(json.dumps(client.get_version(), indent=2))
        elif args.command == "devices":
            print(json.dumps(client.get_devices(), indent=2))
        elif args.command == "nests":
            print(json.dumps(client.get_nests(), indent=2))
        elif args.command == "processes":
            print(json.dumps(client.get_processes(), indent=2))
        elif args.command == "workqueue":
            print(json.dumps(client.get_workqueue(), indent=2))
        elif args.command == "start":
            res = client.start()
            print(json.dumps(res if res else {"status": "started"}, indent=2))
        elif args.command == "stop":
            res = client.stop()
            print(json.dumps(res if res else {"status": "stopped"}, indent=2))
        elif args.command == "simulate":
            res = client.simulate()
            print(json.dumps(res if res else {"status": "simulation_started"}, indent=2))
        elif args.command == "run_process":
            variables = {}
            if args.variables:
                try:
                    variables = json.loads(args.variables)
                except json.JSONDecodeError:
                    # Try parsing key=value;key=value
                    for part in args.variables.split(";"):
                        if "=" in part:
                            k, v = part.split("=", 1)
                            variables[k.strip()] = v.strip()
            
            res = client.run_process(
                process=args.process,
                variables=variables,
                batch_name=args.batch,
                append=args.append,
                iterations=args.iterations,
                minimum_delay=args.delay,
                workunit_name=args.workunit
            )
            print(json.dumps(res if res else {"status": "process_submitted"}, indent=2))
            
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
