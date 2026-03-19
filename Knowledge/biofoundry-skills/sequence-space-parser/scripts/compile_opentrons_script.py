import argparse
import json
import sys

def generate_opentrons_protocol(protocol_type, params, chassis):
    """
    Generates a Python script for Opentrons based on the protocol type and chassis.
    """
    
    header = f"""
from opentrons import protocol_api

metadata = {{
    'protocolName': '{protocol_type} for {chassis}',
    'author': 'BioFoundry Agent',
    'description': 'Automated {protocol_type} protocol adapted for {chassis}',
    'apiLevel': '2.13'
}}

def run(protocol: protocol_api.ProtocolContext):
    # Labware setup
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    # Protocol Parameters
    params = {json.dumps(params, indent=4)}
    chassis = "{chassis}"
    
    protocol.comment(f"Starting {{metadata['protocolName']}}")
"""

    body = ""
    
    if protocol_type == "transformation":
        if chassis == "E_coli":
            body = """
    # E. coli Transformation Protocol
    # 1. Add DNA to cells
    # 2. Heat shock
    # 3. Recovery
    
    protocol.comment("Dispensing DNA...")
    p300.transfer(2, plate['A1'], plate['B1'], mix_after=(3, 10))
    
    protocol.comment("Heat shock at 42C for 45s (simulated on temp module if available)")
    protocol.delay(seconds=45)
    
    protocol.comment("Adding recovery media...")
    p300.transfer(100, plate['A12'], plate['B1'], mix_after=(5, 50))
"""
        elif chassis == "P_aeruginosa":
             body = """
    # P. aeruginosa Transformation Protocol (Electroporation prep or chemical)
    # Note: P. aeruginosa often requires different competency steps or electroporation
    # This is a mock for chemical transformation adaptation
    
    protocol.comment("Dispensing DNA...")
    p300.transfer(5, plate['A1'], plate['B1'], mix_after=(5, 20))
    
    protocol.comment("Incubating on ice (simulated)")
    protocol.delay(minutes=30)
    
    protocol.comment("Heat shock at 42C for 90s")
    protocol.delay(seconds=90)
    
    protocol.comment("Adding recovery media (LB-Lennox)...")
    p300.transfer(500, plate['A12'], plate['B1'], mix_after=(3, 100))
"""
        else:
            body = f"\n    protocol.comment('Unknown chassis: {chassis}')\n"

    elif protocol_type == "assembly":
        body = """
    # Golden Gate Assembly Setup
    protocol.comment("Setting up Golden Gate assembly reaction...")
    # Transfer Master Mix
    p300.transfer(15, plate['A1'], plate['B1'])
    # Transfer DNA parts
    p300.transfer(2, plate['A2'], plate['B1'])
    p300.transfer(2, plate['A3'], plate['B1'])
"""

    else:
        body = f"\n    protocol.comment('Generic protocol step for {protocol_type}')\n"

    footer = """
    protocol.comment("Protocol complete.")
"""

    return header + body + footer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile Opentrons script.")
    parser.add_argument("--type", required=True, help="Protocol type")
    parser.add_argument("--params", required=True, help="JSON string of parameters")
    parser.add_argument("--chassis", default="E_coli", help="Target organism chassis")
    
    args = parser.parse_args()
    
    try:
        params = json.loads(args.params)
        script = generate_opentrons_protocol(args.type, params, args.chassis)
        print(script)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for params.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
