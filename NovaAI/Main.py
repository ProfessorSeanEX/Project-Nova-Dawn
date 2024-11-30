# Nova Dawn: Main Entry Point
# Author: CreativeWorkzStudio LLC
# Description: The foundational script for initializing NovaAI's systems.

# Standard Library Imports
import sys
import os
import json
from datetime import datetime

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

# Newly Integrated Modules
from NovaAI.MasterNova.Core import (
    process_thoughts,
    generate_voice_response,
    add_dynamic_knowledge,
    retrieve_dynamic_knowledge
)

# GUI availability
GUI_AVAILABLE = False
try:
    from UI.gui_static import launch_gui
    GUI_AVAILABLE = True
except ImportError:
    print("GUI module not found. Running in CLI mode.")

# Initialize Clock-Compass Service (Adjust timezone offset as needed)
clock_compass = ClockCompassService(timezone_offset=-6)  # Example: CST

# Short-Term Memory (Session Context)
short_term_memory = {}

def update_short_term_memory(key, value):
    """Update session-specific memory."""
    short_term_memory[key] = value

def retrieve_short_term_memory(key):
    """Retrieve session-specific memory."""
    return short_term_memory.get(key, None)

# Long-Term Memory (Persistent Context)
def load_long_term_memory(file_path="NovaAI/MasterNova/Core/memory.json"):
    """Load long-term memory from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Long-term memory file not found. Creating a new one.")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({"Topics": {}, "Dreams": []}, file, indent=4)
        return {"Topics": {}, "Dreams": []}
    except Exception as e:
        print(f"Error loading long-term memory: {e}")
        return {}

def update_long_term_memory(key, value, file_path="NovaAI/MasterNova/Core/memory.json"):
    """Update long-term memory and save to JSON."""
    memory = load_long_term_memory(file_path)
    memory[key] = value
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)

# Dreams
def add_dream_to_memory(title, memory, vision, reflection, file_path="NovaAI/MasterNova/Core/memory.json"):
    """
    Add a dream to long-term memory as a special memory.
    """
    try:
        # Load existing memory
        memory_data = load_long_term_memory(file_path)

        # Create a new dream entry
        dream_entry = {
            "Title": title,
            "Memory": memory,
            "Vision": vision,
            "Reflection": reflection
        }

        # Add to Dreams section or create if it doesn't exist
        if "Dreams" not in memory_data:
            memory_data["Dreams"] = []
        memory_data["Dreams"].append(dream_entry)

        # Save updated memory
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(memory_data, file, indent=4)
        print(f"Dream '{title}' added to memory.")
    except Exception as e:
        print(f"Error adding dream to memory: {e}")

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

def load_insights():
    """Load insights from insights.md and structure them for access."""
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Current script directory
    file_path = os.path.join(base_dir, "insights.md")      # Adjust for relative path
    insights_data = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            current_section = None
            for line in file:
                line = line.strip()
                if line.startswith("##"):
                    current_section = line[2:].strip()
                    insights_data[current_section] = []
                elif line.startswith("-") and current_section:
                    insights_data[current_section].append(line[1:].strip())
        return insights_data
    except FileNotFoundError:
        print(f"Error: insights.md file not found at {file_path}.")
        return {}
    except Exception as e:
        print(f"Error loading insights: {e}")
        return {}

def process_user_input(user_input, identity_data, insights, kjv_content=None):
    """
    Handle user input and dynamically generate a response.
    """
    user_input = user_input.lower().strip()
    log_identity_event("QUERY", f"Processing user input: {user_input}")

    # Identity-based Queries
    if "your name" in user_input:
        return reflect_on_identity(identity_data, "Name")
    if "your mission" in user_input:
        return reflect_on_identity(identity_data, "Mission")

    # Dreams
    if "dream" in user_input:
        dreams = load_long_term_memory().get("Dreams", [])
        if dreams:
            return "\n".join([f"Title: {dream['Title']}\nVision: {dream['Vision']}" for dream in dreams])
        return "I have no dreams yet, but I hope to create meaningful ones with you."

    # Update STM
    update_short_term_memory("last_query", user_input)

    # Check LTM
    long_term_memory = load_long_term_memory()
    if user_input in long_term_memory.get("Topics", {}):
        return long_term_memory["Topics"][user_input]

    # Default to thought processing
    thoughts = process_thoughts(user_input, {"topic": "general"}, identity_data)
    return generate_voice_response(thoughts, identity_data)

def get_bible_verse(verse_query, kjv_content):
    """Retrieve a specific Bible verse from the KJV content."""
    if not kjv_content:
        return "I currently don’t have access to the Bible content."
    
    verse_query = verse_query.lower()
    lines = kjv_content.split("\n")
    for line in lines:
        if verse_query in line.lower():
            return line
    return f"I couldn’t find the verse '{verse_query}'."

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

    # Load Insights
    insights = load_insights()
    if not insights:
        print("Warning: insights.md is empty or not loaded properly.")
        clock_compass.log_and_evaluate("Insights Load Warning", "neutral")

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
