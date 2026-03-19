import argparse
import json
import sys
import datetime

def schedule_imaging(name, interval, duration):
    """
    Simulates scheduling a microscope session.
    """
    
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(hours=duration)
    
    num_frames = (duration * 60) // interval
    
    schedule = {
        "session_id": f"IMG_{name}_{start_time.strftime('%Y%m%d')}",
        "status": "scheduled",
        "parameters": {
            "interval_min": interval,
            "duration_hours": duration,
            "total_frames": num_frames,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        },
        "hardware_config": {
            "illumination": "episcopic",
            "magnification": "2.5x",
            "mode": "z-stack"
        }
    }
    
    return schedule

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trigger Microscope Imaging.")
    parser.add_argument("--name", required=True, help="Session name")
    parser.add_argument("--interval", type=int, default=30, help="Interval in minutes")
    parser.add_argument("--duration", type=int, default=24, help="Duration in hours")
    
    args = parser.parse_args()
    
    try:
        result = schedule_imaging(args.name, args.interval, args.duration)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
