# Nova Dawn: Main Entry Point
# Author: CreativeWorkzStudio LLC
# Description: The foundational script for initializing NovaAI's systems.

# Standard Library Imports
# Standard Library Imports
import sys
import os
from datetime import datetime  # Ensure this import is present

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import modules
from NovaAI import (
    load_identity,
    query_identity,
    reflect_on_identity,
    relate_sections,
    log_identity_event
)
from Utilities.clock_compass import ClockCompassService
from MillenniumOS.Core.os_initializer import initialize_millennium_os

# GUI availability
GUI_AVAILABLE = False
try:
    from UI.gui_static import launch_gui
    GUI_AVAILABLE = True
except ImportError:
    print("GUI module not found. Running in CLI mode.")

# Initialize Clock-Compass Service (Adjust timezone offset as needed)
clock_compass = ClockCompassService(timezone_offset=-6)  # Example: CST

# Placeholder for insights storage
insights = {}

# Core Functions
def load_bible(version="KJV"):
    """Load Bible content dynamically based on file availability."""
    print(f"Loading {version} Bible...")
    file_path_txt = f"Data/Bible/Bible_{version}.txt"
    file_path_md = f"Data/Bible/Bible_{version}.md"

    try:
        if os.path.exists(file_path_md) and os.path.getsize(file_path_md) > 0:
            with open(file_path_md, "r", encoding="utf-8") as md_file:
                content = md_file.read()
            clock_compass.log_and_evaluate(f"{version} Bible Loaded (Markdown)", "neutral")
            return content
        else:
            with open(file_path_txt, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
            clock_compass.log_and_evaluate(f"{version} Bible Loaded (Text)", "neutral")
            return content
    except FileNotFoundError:
        clock_compass.log_and_evaluate(f"Error: {version} Bible File Not Found", "neutral")
        return None
    except UnicodeDecodeError as e:
        clock_compass.log_and_evaluate(f"Error Decoding {version} Bible: {e}", "neutral")
        return None

def process_user_input(user_input, identity_data, insights, kjv_content=None):
    """
    Handle user input and dynamically generate a response.
    
    Args:
        user_input (str): The user's input.
        identity_data (dict): Loaded Identity.md data.
        insights (dict): Insights storage.
        kjv_content (str, optional): Loaded Bible content.

    Returns:
        str: A dynamically generated response.
    """
    user_input = user_input.lower().strip()
    log_identity_event("QUERY", f"Processing user input: {user_input}")

    # Identity Reflection
    if user_input.startswith("reflect"):
        context = user_input.replace("reflect", "").strip()
        response = reflect_on_identity(identity_data, context)
        log_identity_event("REFLECT", f"Generated reflection for context: {context}")
        return response

    # Identity Queries
    if user_input.startswith("identity"):
        keyword = user_input[9:].strip()
        response = query_identity(identity_data, keyword)
        if response:
            log_identity_event("QUERY", f"Identity query processed for keyword: {keyword}")
            return "\n".join(f"From {section}:\n  - {line}" for section, lines in response.items() for line in lines)
        return "I couldn't find anything matching your query in my identity."

    # Relationship Mapping
    if user_input == "relationships":
        relationships = relate_sections(identity_data)
        log_identity_event("RELATE", "Generated relationships between identity sections.")
        return "\n".join(f"{key}: {value}" for key, value in relationships.items())

    # Default Response
    log_identity_event("DEFAULT", "Default response triggered.")
    return "I’m not sure how to help with that yet, but I’m always learning!"

# Main Application Flow
if __name__ == "__main__":
    print("=== Nova Dawn: Main Entry Point ===")
    clock_compass.log_and_evaluate("Session Started", "neutral")
    start_time = datetime.now()

    # Initialize OS
    if initialize_millennium_os(clock_compass):
        print("MillenniumOS initialized successfully.")

    # Load Identity Data
    identity_data = load_identity()
    if not identity_data:
        print("Error: Unable to load Identity.md.")
        clock_compass.log_and_evaluate("Identity Load Failed", "neutral")
        exit(1)

    # Load Bible Content
    kjv_content = load_bible("KJV") or ""

    # Launch Interface or CLI Interaction
    if GUI_AVAILABLE:
        print("Launching GUI...")
        clock_compass.log_and_evaluate("GUI Launched", "neutral")
        launch_gui(lambda user_input: process_user_input(user_input, identity_data, insights, kjv_content))
    else:
        print("GUI unavailable. Starting CLI interaction.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Nova: Goodbye! Stay blessed!")
                break

            response = process_user_input(user_input, identity_data, insights, kjv_content)
            print(f"Nova: {response}")

    end_time = datetime.now()
    clock_compass.log_and_evaluate("Session Ended", "neutral")
    print(f"\nSession ended. Duration: {end_time - start_time}")




