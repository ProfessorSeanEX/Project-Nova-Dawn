import os
from difflib import get_close_matches

def load_identity(file_path = r"C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\NovaAI\Docs\Identity.md"):
    """
    Load and parse the Identity.md file.
    
    Args:
        file_path (str): Path to the Identity.md file.
    
    Returns:
        dict: Parsed sections of Identity.md, or None if an error occurs.
    """
    print(f"Loading Identity.md from {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Split content into sections based on Markdown headers
        sections = parse_markdown_sections(content)
        print("Identity.md loaded and parsed successfully.")
        return sections
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except UnicodeDecodeError as e:
        print(f"Error decoding {file_path}: {e}")
        return None

def parse_markdown_sections(content):
    """
    Parse Markdown content into sections based on headers.
    
    Args:
        content (str): The Markdown content.
    
    Returns:
        dict: A dictionary of sections with header titles as keys.
    """
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
    
    if current_header:  # Add the last section
        sections[current_header] = "\n".join(current_content).strip()

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
    print(f"Searching for '{keyword}' in Identity.md...")
    results = {}
    for section, content in sections.items():
        matches = [line for line in content.splitlines() if keyword.lower() in line.lower()]
        if matches:
            results[section] = matches
    return results

def relate_sections(sections):
    """
    Build relationships between sections of Identity.md.
    
    Args:
        sections (dict): Parsed sections of Identity.md.
    
    Returns:
        dict: A relational map showing connections between sections.
    """
    relationships = {}
    if "Core Identity" in sections and "Motivations" in sections:
        relationships["Identity to Motivation"] = (
            "Core Identity describes purpose and connection to Motivations."
        )
    if "Strengths and Limitations" in sections and "Values" in sections:
        relationships["Strengths to Values"] = (
            "Strengths are grounded in values, reflecting faith and service."
        )
    return relationships

def store_insight(insights, key, value):
    """
    Store key-value insights in a simple dictionary.
    
    Args:
        insights (dict): Dictionary for storing insights.
        key (str): Key for the insight.
        value (str): Value of the insight.
    """
    insights[key] = value
    print(f"Insight stored: {key} -> {value}")

def retrieve_insight(insights, key):
    """
    Retrieve stored insights by key.
    
    Args:
        insights (dict): Dictionary of stored insights.
        key (str): Key for the insight to retrieve.
    
    Returns:
        str: Retrieved insight or a default message if not found.
    """
    return insights.get(key, "I don't recall anything about that.")

def summarize_section(sections, section_name):
    """
    Provide a summary of a specific section.
    
    Args:
        sections (dict): Parsed sections of Identity.md.
        section_name (str): Name of the section to summarize.
    
    Returns:
        str: A summary or message if the section doesn't exist.
    """
    if section_name in sections:
        content = sections[section_name]
        # Create a simple summary using the first few lines
        return "\n".join(content.splitlines()[:3]) + "..."
    return f"Section '{section_name}' not found in Identity.md."
