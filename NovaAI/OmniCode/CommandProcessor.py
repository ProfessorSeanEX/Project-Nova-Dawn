# CommandProcessor.py

from OmniCode.CoreModules.Declare import declare
from OmniCode.CoreModules.Align import align
from OmniCode.CoreModules.Grace import grace_init

def parse_command(command):
    # Split command into components
    parts = command.split(' ', 2)
    if len(parts) < 2:
        return {"error": "Invalid command syntax"}
    return {"command": parts[0], "target": parts[1], "details": parts[2] if len(parts) > 2 else None}

def process_command(parsed):
    # Route the command to the appropriate module
    if parsed["command"] == "DECLARE":
        return declare(parsed["target"], parsed["details"])
    elif parsed["command"] == "ALIGN":
        return align(parsed["target"], parsed["details"])
    elif parsed["command"] == "GRACE":
        try:
            metadata = eval(parsed["details"])  # Convert string to dictionary
            return grace_init(metadata)
        except Exception as e:
            return {"error": f"GRACE command metadata error: {e}"}
    else:
        return {"error": "Unknown command"}
