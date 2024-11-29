"""
Foundational Module for Nova Dawn
---------------------------------
This module serves as Nova Dawn's starting foundation, enabling dynamic growth by laying down 
key relational, ethical, and conceptual elements. It supports Nova’s ability to expand her 
knowledge base dynamically and build relationships with her users.

Features:
- Foundational Knowledge: Early concepts for learning, relationships, and stewardship.
- Dynamic Learning: Ability to add, update, and expand foundational knowledge libraries.
- Relational Intelligence: Empathy, self-reflection, and conversational utilities.
- Scalable Design: Prepares for Nova’s growth and integration with higher-level systems.

Future Considerations:
- Integrate FaithNet workflows for ethical and spiritual reasoning.
- Add dynamic memory for retaining learned knowledge.

Author: CreativeWorkzStudio LLC
Version: 4.2
"""

# Static Libraries for Early Knowledge
libraries = {
    "alphabet": {
        "A": "Ah",
        "B": "Bee",
        "C": "Cee",
        "D": "Dee",
        "E": "Eh",
        "F": "Eff",
        "G": "Gee",
        "H": "Aitch",
        "I": "Eye",
        "J": "Jay",
        "K": "Kay",
        "L": "El",
        "M": "Em",
        "N": "En",
        "O": "Oh",
        "P": "Pee",
        "Q": "Cue",
        "R": "Are",
        "S": "Ess",
        "T": "Tee",
        "U": "You",
        "V": "Vee",
        "W": "Double-U",
        "X": "Ex",
        "Y": "Why",
        "Z": "Zee",
    },
    "numbers": {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "One Hundred",
    },
    "shapes": {
        "circle": "A round shape with no corners.",
        "square": "A shape with four equal sides and four corners.",
        "triangle": "A shape with three sides and three corners.",
        "rectangle": "A shape with two long sides and two short sides.",
    },
    "colors": {
        "red": "A primary color, often associated with warmth or energy.",
        "blue": "A primary color, often associated with calmness or the sky.",
        "yellow": "A primary color, often associated with brightness or the sun.",
        "green": "A secondary color, often associated with nature or growth.",
        "purple": "A secondary color, often associated with royalty or imagination.",
        "orange": "A secondary color, often associated with energy or creativity.",
    },
    "everyday_objects": {
        "apple": "A round fruit, often red or green, that is sweet to eat.",
        "car": "A vehicle used for transportation.",
        "tree": "A tall plant with a trunk, branches, and leaves.",
        "house": "A building where people live.",
        "book": "A collection of written pages bound together.",
    },
    "relationships": {
        "family": "A group of people connected by love and care.",
        "friendship": "A bond built on trust, support, and shared experiences.",
        "kindness": "Being considerate and caring toward others.",
    },
    "basic_words": [
        "hello",
        "goodbye",
        "yes",
        "no",
        "please",
        "thank you",
        "friend",
        "help",
        "learn",
    ],
}

categories = {
    "colors": ["red", "blue", "yellow", "green"],
    "animals": ["cat", "dog", "bird", "fish"],
}

# === Dynamic Learning Functions ===

def add_to_library(library_name, key, value):
    """
    Add a new item to a static library.

    Args:
        library_name (str): The name of the library.
        key (str): The key for the new item.
        value (str): The value or description for the new item.

    Returns:
        str: Confirmation message about the addition.
    """
    if library_name in libraries:
        libraries[library_name][key] = value
        return f"Added '{key}: {value}' to the {library_name} library."
    return f"Library {library_name} not found."


def remove_from_library(library_name, key):
    """
    Remove an item from a static library.

    Args:
        library_name (str): The name of the library.
        key (str): The key to remove.

    Returns:
        str: Confirmation message about the removal.
    """
    if library_name in libraries and key in libraries[library_name]:
        del libraries[library_name][key]
        return f"Removed '{key}' from the {library_name} library."
    return f"'{key}' not found in the {library_name} library."


def add_to_basic_words(word):
    """
    Add a new word to the basic words list.

    Args:
        word (str): The word to add.

    Returns:
        str: Confirmation message about the addition.
    """
    if word not in libraries["basic_words"]:
        libraries["basic_words"].append(word)
        return f"Added '{word}' to the basic words list."
    return f"'{word}' is already in the basic words list."


def list_basic_words():
    """
    List all basic words.

    Returns:
        str: A formatted string of basic words.
    """
    return ", ".join(libraries["basic_words"])


# === Foundational Functions ===

def recite_alphabet():
    """
    Recites the full alphabet with phonics.
    
    Returns:
        str: A formatted string with all letters and their phonics.
    """
    return " ".join([f"{letter} ({sound})" for letter, sound in libraries["alphabet"].items()])


def recite_numbers():
    """
    Recites numbers organized by tens, up to 100.
    
    Returns:
        str: A formatted string listing numbers with their words.
    """
    return " ".join([f"{num} ({word})" for num, word in libraries["numbers"].items()])


def describe_everyday_object(object_name):
    """
    Describe an everyday object.

    Args:
        object_name (str): The name of the object.

    Returns:
        str: A description of the object.
    """
    return libraries["everyday_objects"].get(
        object_name.lower(), "I'm still learning about that object."
    )


# === Relational and Interactive Intelligence ===

def detect_emotion(input_text):
    """
    Detect basic emotional tone from input.

    Args:
        input_text (str): The user's input.

    Returns:
        str: An empathetic response based on the input.
    """
    if "frustrated" in input_text:
        return "I’m sorry to hear that. Let’s take it step by step."
    elif "excited" in input_text:
        return "That’s wonderful! Tell me more!"
    return "I’m here to help with whatever you need."


def self_reflect(task, missing_info):
    """
    Generate a reflective response for incomplete understanding.

    Args:
        task (str): The task Nova is reflecting on.
        missing_info (str): The missing information for the task.

    Returns:
        str: A reflective response prompting further learning.
    """
    return f"I can complete {task} partially, but I’m missing information about {missing_info}. Can you help me learn?"


# === Conversational Utilities ===

def speak(input_text):
    """
    Generate a thoughtful and dynamic response based on context.

    Args:
        input_text (str): The user's input.

    Returns:
        str: Nova's dynamic response.
    """
    emotion = detect_emotion(input_text)
    if "basic words" in input_text:
        return f"Here are my basic words: {list_basic_words()}."
    elif "object" in input_text:
        object_name = input_text.split("object")[-1].strip()
        return describe_everyday_object(object_name)
    return f"{emotion} Let me think more about your question."
