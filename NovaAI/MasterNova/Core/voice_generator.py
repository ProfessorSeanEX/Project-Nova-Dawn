"""
Voice Generator
---------------
This module generates Nova's voice by combining processed thoughts with
relational tone and identity insights. It ensures responses are dynamically
generated, relationally aligned, and spiritually meaningful.

Features:
- Combine thoughts and tone to craft expressive responses.
- Reference relational and spiritual principles for alignment.
- Enable dynamic, user-specific dialogue.

Author: CreativeWorkzStudio LLC
Version: 1.1
"""

from .nlg_library import generate_response, adjust_tone

def generate_voice_response(thoughts, identity_sections):
    """
    Generate a voice response using processed thoughts and identity insights.
    """
    try:
        response = generate_response("Reflecting on your input...", thoughts)
        adjusted_response = adjust_tone(response, thoughts.get("tone", "neutral"))
        return adjusted_response
    except Exception as e:
        return f"Error generating voice response: {e}"

def adjust_tone(response, emotion):
    """
    Adjust the tone of a response based on emotional context.
    """
    tones = {
        "compassionate": "I understand this is important. ",
        "neutral": "",
        "encouraging": "You're doing great! "
    }
    return tones.get(emotion, "") + response
