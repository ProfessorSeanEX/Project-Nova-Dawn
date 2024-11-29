# Declare.py

def declare(target, value):
    if not target or not value:
        return {"error": "DECLARE command requires both target and value"}
    return {"status": "Declared", "target": target, "value": value}
