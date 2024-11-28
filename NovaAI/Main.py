# Nova Dawn: Main Entry Point
# Author: CreativeWorkzStudio LLC
# Description: The foundational script for initializing NovaAI's systems.

# Core imports
import sys
import os
sys.path.append(os.path.dirname(__file__))
from UI.gui_static import launch_gui
from identity_module import load_identity, query_identity, store_insight, retrieve_insight
from Foundations.foundational_module import recite_alphabet, recite_numbers, describe_shape, speak, add_to_list, basic_words
from Utilities.clock_compass import ClockCompassService  # Import Clock-Compass System
import json
from datetime import datetime

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
def initialize_millennium_os():
    """Initialize MillenniumOS for NovaAI."""
    print("Initializing MillenniumOS...")
    clock_compass.log_and_evaluate("MillenniumOS Initialization", "neutral")  # Log initialization event
    return True

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

def process_user_input(user_input, identity_data, kjv_content, insights, basic_words):
    """
    Handle user input and dynamically generate a response.
    
    Args:
        user_input (str): The user's input.
        identity_data (dict): Loaded Identity.md data.
        kjv_content (str): Loaded KJV Bible content.
        insights (dict): Insights storage.
        basic_words (list): Dynamic list of known words.

    Returns:
        str: A dynamically generated response.
    """
    user_input = user_input.lower().strip()
    clock_compass.log_and_evaluate(f"User Input: {user_input}", "relational")  # Log user input

    # Identity Queries
    if user_input.startswith("identity"):
        keyword = user_input[9:].strip()
        response = query_identity(identity_data, keyword)
        if response:
            clock_compass.log_and_evaluate("Identity Query Processed", "relational")
            return "\n".join(f"From {section}:\n  - {line}" for section, lines in response.items() for line in lines)
        return "I couldn't find anything matching your query in my identity."

    # Scripture Search
    if user_input.startswith("search"):
        keyword = user_input[7:].strip()
        results = [line.strip() for line in kjv_content.splitlines() if keyword.lower() in line.lower()]
        if results:
            clock_compass.log_and_evaluate(f"Scripture Search for '{keyword}'", "kairos")
            return f"Found {len(results)} results:\n" + "\n".join(results[:5])
        return "No results found for your search."

    # Teach Me (Dynamic Learning)
    if "teach me" in user_input:
        try:
            # Extract the word to learn
            new_word = user_input.replace("teach me", "").strip()
            if new_word:
                # Handle list-based dynamic learning
                if isinstance(basic_words, list):  # Check if library is list
                    result = add_to_list(basic_words, new_word)
                else:
                    result = add_to_library(basic_words, new_word, f"A newly learned word: {new_word}.")
                clock_compass.log_and_evaluate(f"Word Taught: {new_word}", "relational")
                return result
            else:
                return "I need a word to learn. Please say something like 'Teach me apple.'"
        except Exception as e:
            return f"An error occurred while learning: {e}"

    # Foundational Knowledge Commands
    if user_input == "recite alphabet":
        return recite_alphabet()
    if user_input == "recite numbers":
        return recite_numbers()
    if "what is a" in user_input or "describe" in user_input:
        shape_name = user_input.split()[-1]
        response = describe_shape(shape_name)
        clock_compass.log_and_evaluate(f"Shape Described: {shape_name}", "relational")
        return response

    # Small Talk (Greeting or Check-In)
    if user_input in ["how are you", "hello", "hi", "nova how are you"]:
        return "I'm doing well, thank you! How can I help you today?"

    # Default Response
    clock_compass.log_and_evaluate("Default Response Triggered", "neutral")
    return speak(user_input)

# Main Application Flow
if __name__ == "__main__":
    print("=== Nova Dawn: Main Entry Point ===")
    clock_compass.log_and_evaluate("Session Started", "neutral")  # Log session start
    start_time = datetime.now()

    # Initialize OS
    if initialize_millennium_os():
        print("MillenniumOS initialized successfully.")

    # Load Identity Data
    identity_data = load_identity()
    if not identity_data:
        print("Error: Unable to load Identity.md.")
        clock_compass.log_and_evaluate("Identity Load Failed", "neutral")
        exit(1)

    # Load Bibles
    kjv_content = load_bible("KJV")
    if not kjv_content:
        kjv_content = ""

    # Launch Interface or CLI Interaction
    if GUI_AVAILABLE:
        print("Launching GUI...")
        clock_compass.log_and_evaluate("GUI Launched", "neutral")
        launch_gui(lambda user_input: process_user_input(user_input, identity_data, kjv_content, insights, basic_words))
    else:
        print("GUI unavailable. Starting CLI interaction.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Nova: Goodbye! Stay blessed!")
                break

            response = process_user_input(user_input, identity_data, kjv_content, insights)
            print(f"Nova: {response}")

    end_time = datetime.now()
    clock_compass.log_and_evaluate("Session Ended", "neutral")
    print(f"\nSession ended. Duration: {end_time - start_time}")


