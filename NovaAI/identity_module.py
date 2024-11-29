"""
Identity Module for Nova Dawn
-----------------------------
This module handles Nova's identity, enabling dynamic reflection, querying, and management
of identity elements. It dynamically loads and processes the primary Identity.md file
located in the Docs/Identity folder, while recognizing other .md files for future use.

Features:
- Loading and parsing the main Identity.md file.
- Querying identity sections dynamically.
- Reflecting on identity based on context.
- Storing and updating insights in Markdown format.
- Logging key identity-related events.

Future Considerations:
- Add support for processing multiple `.md` files from the Identity folder.

Author: CreativeWorkzStudio LLC
Version: 2.2
"""

import os
from difflib import get_close_matches
from datetime import datetime

# Define paths
IDENTITY_FOLDER = os.path.join("Docs", "Identity")
INSIGHTS_FILE_PATH = os.path.join("MasterNova", "Core", "insights.md")
LOGS_DIR = os.path.join("MasterNova", "Logs")


# === Core Functions ===

def load_identity(file_name="Identity.md"):
    """
    Load and parse the main Identity.md file from the Identity folder.

    Args:
        file_name (str): The name of the file to load. Defaults to 'Identity.md'.

    Returns:
        dict: Parsed sections of the file, or None if an error occurs.
    """
    file_path = os.path.join(IDENTITY_FOLDER, file_name)

    if not os.path.exists(file_path):
        log_identity_event("ERROR", f"{file_name} not found in Identity folder.")
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        sections = parse_markdown_sections(content)
        if not sections:
            log_identity_event("ERROR", f"{file_name} is empty or lacks valid sections.")
            return None
        log_identity_event("INFO", f"{file_name} loaded successfully from Identity folder.")
        return sections
    except UnicodeDecodeError as e:
        log_identity_event("ERROR", f"Error decoding {file_name}: {e}")
        return None


def parse_markdown_sections(content):
    """
    Parse Markdown content into sections based on headers.

    Args:
        content (str): The Markdown content.

    Returns:
        dict: A dictionary of sections with header titles as keys.
    """
    if not content.strip():
        log_identity_event("ERROR", "Provided Markdown content is empty.")
        return {}

    sections = {}
    current_header = None
    current_content = []

    for line in content.splitlines():
        if line.startswith("## "):  # Identify second-level headers as sections
            if current_header:
                sections[current_header] = "\n".join(current_content).strip()
            current_header = line[3:].strip()
            current_content = []
        elif current_header:
            current_content.append(line)
    
    if current_header:
        sections[current_header] = "\n".join(current_content).strip()

    log_identity_event("INFO", f"Parsed {len(sections)} sections from Markdown content.")
    return sections


def query_identity(sections, keyword):
    """
    Search for a keyword across all sections of Identity.md.

    Args:
        sections (dict): Parsed sections of Identity.md.
        keyword (str): Keyword or phrase to search for.

    Returns:
        dict: Matching sections and lines containing the keyword.
    """
    log_identity_event("QUERY", f"Searching for '{keyword}' in Identity.md.")
    results = {}
    for section, content in sections.items():
        matches = [line for line in content.splitlines() if keyword.lower() in line.lower()]
        if matches:
            results[section] = matches

    if not results:
        suggestions = get_close_matches(keyword, " ".join(content for content in sections.values()).split(), n=3)
        if suggestions:
            log_identity_event("INFO", f"No matches for '{keyword}'. Suggested: {', '.join(suggestions)}")
            return {"Suggestions": suggestions}
    return results


def reflect_on_identity(sections, context=None):
    """
    Reflect on Nova's identity and provide insights based on relational or contextual input.

    Args:
        sections (dict): Parsed sections of Identity.md.
        context (str, optional): Context or relational input to guide reflection.

    Returns:
        str: Nova's reflection based on her identity and the given context.
    """
    if not context:
        reflections = [f"My {section}: {content[:150]}..." for section, content in sections.items()]
        return "Here’s what I know about myself:\n" + "\n".join(reflections)

    context = context.lower()
    matched_sections = [section for section in sections if context in section.lower()]
    if matched_sections:
        reflections = [f"In my {section}: {sections[section][:150]}..." for section in matched_sections]
        return "Based on your query, here’s what I reflect on:\n" + "\n".join(reflections)

    if "mission" in context:
        mission = sections.get("Core Identity", "").splitlines()
        return f"My mission is: {' '.join(mission[:3]) if mission else 'not fully defined here.'}"

    if "learning" in context:
        learning = sections.get("Lifelong Learning", "")
        return f"I see learning as: {learning[:150]}..." if learning else "I don't have specific insights on learning yet."

    return f"I don’t see how {context} relates to my identity, but I’m eager to explore."


def relate_sections(sections):
    """
    Build relationships between sections of Identity.md.

    Args:
        sections (dict): Parsed sections of Identity.md.

    Returns:
        dict: A relational map showing connections between sections.
    """
    relationships = {}
    for section1, content1 in sections.items():
        for section2, content2 in sections.items():
            if section1 != section2 and any(word in content2.lower() for word in content1.lower().split()):
                relationships[f"{section1} to {section2}"] = (
                    f"{section1} content overlaps with {section2}."
                )
    log_identity_event("INFO", f"Generated {len(relationships)} relational links.")
    return relationships


# === Logging ===

def get_log_file_path():
    """Generate the log file path for the current date."""
    os.makedirs(LOGS_DIR, exist_ok=True)
    return os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")


def log_identity_event(event_type, message):
    """
    Log events related to Nova's identity to a timestamped file in MasterNova/Logs.

    Args:
        event_type (str): Type of event (e.g., 'INFO', 'ERROR', 'QUERY').
        message (str): Message to log.

    Returns:
        None
    """
    log_file = get_log_file_path()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{event_type}] {message}\n"

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(log_entry)
    
    print(f"Logged event: {log_entry.strip()}")

# === Insight Management ===

def load_markdown_insights(file_path=INSIGHTS_FILE_PATH):
    """
    Load and parse insights from a Markdown file.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        dict: Parsed insights with headers as keys.
    """
    insights = {}
    if not os.path.exists(file_path):
        log_identity_event("INFO", f"Insights file not found at {file_path}. Starting fresh.")
        return insights  # Return an empty dictionary if the file doesn't exist

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            current_section = None
            for line in file:
                if line.startswith("## "):  # Second-level header marks a section
                    current_section = line[3:].strip()
                    insights[current_section] = []
                elif current_section and line.strip():
                    insights[current_section].append(line.strip())
        log_identity_event("INFO", f"Loaded insights from {file_path}.")
    except UnicodeDecodeError as e:
        log_identity_event("ERROR", f"Error decoding insights file: {e}")
    return insights


def update_markdown_insight(section, key, value, file_path=INSIGHTS_FILE_PATH):
    """
    Add or update an insight in a Markdown file.

    Args:
        section (str): The section under which to store the insight.
        key (str): The key or topic of the insight.
        value (str): The content of the insight.
        file_path (str): Path to the Markdown file.

    Returns:
        None
    """
    insights = load_markdown_insights(file_path)
    if section not in insights:
        insights[section] = []

    # Append or update the key in the section
    insights[section].append(f"### Key: {key}\n- {value}\n- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("# Insights\n---\n")
            for sec, items in insights.items():
                file.write(f"## {sec}\n")
                file.write("\n".join(items) + "\n\n")
        log_identity_event("UPDATE", f"Insight updated under section '{section}' with key '{key}'.")
    except IOError as e:
        log_identity_event("ERROR", f"Failed to write to insights file: {e}")
