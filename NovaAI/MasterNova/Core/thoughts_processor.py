"""
Thoughts Processor
------------------
This module processes user input into actionable insights for Nova. It analyzes
relational context, emotional tone, and references Nova's core identity to
prepare meaningful thoughts for response generation.

Features:
- Detect emotional tone from user input.
- Map relational context based on dynamic and static knowledge.
- Reference identity principles to shape insights.

Author: CreativeWorkzStudio LLC
Version: 1.1
"""

import re

def process_thoughts(user_input, relational_context, identity_sections):
    """
    Process user input into structured thoughts based on context and identity.
    """
    try:
        thoughts = {}

        # Sentence-based parsing
        sentences = re.split(r'(?<=[.!?]) +', user_input)
        main_thought = sentences[0] if sentences else user_input

        # Detect emotional tone
        thoughts["tone"] = detect_emotion(main_thought)

        # Parse specific input types
        if "your name" in main_thought:
            thoughts["identity_insight"] = "My name is Nova Dawn. It reflects light, transformation, and renewal."
        elif "alphabet" in main_thought:
            thoughts["task"] = "recite_alphabet"
        elif "grace" in main_thought:
            thoughts["knowledge_query"] = "grace"
        elif any(keyword in main_thought for keyword in identity_sections):
            matched_section = [section for section in identity_sections if section.lower() in main_thought.lower()]
            if matched_section:
                section_content = identity_sections[matched_section[0]]
                thoughts["identity_insight"] = f"{matched_section[0]}: {section_content[:150]}..."
        else:
            thoughts["relational_context"] = relational_context.get("topic", "general reflection")

        return thoughts
    except Exception as e:
        return {"error": f"Error processing thoughts: {e}"}

def detect_emotion(input_text):
    """
    Detect basic emotional tone from input (placeholder for relational depth).
    """
    try:
        if any(word in input_text for word in ["lost", "confused", "unsure"]):
            return "compassionate"
        elif any(word in input_text for word in ["excited", "happy", "great"]):
            return "encouraging"
        return "neutral"
    except Exception as e:
        return f"Error detecting emotion: {e}"