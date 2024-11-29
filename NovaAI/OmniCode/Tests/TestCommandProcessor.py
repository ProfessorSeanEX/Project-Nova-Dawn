# TestCommandProcessor.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from CommandProcessor import parse_command, process_command

# Test cases
def test_declare():
    command = "DECLARE mission 'Equip Believers'"
    parsed = parse_command(command)
    result = process_command(parsed)
    print("DECLARE Test:", result)

def test_align():
    command = "ALIGN workflow 'Matthew 28:19'"
    parsed = parse_command(command)
    result = process_command(parsed)
    print("ALIGN Test:", result)

def test_grace():
    command = "GRACE INIT {'truth': True, 'unity': True, 'compassion': True}"
    parsed = parse_command(command)
    result = process_command(parsed)
    print("GRACE Test:", result)

# Run Tests
if __name__ == "__main__":
    test_declare()
    test_align()
    test_grace()
