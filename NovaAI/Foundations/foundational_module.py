"""
Foundational Module for Nova Dawn
---------------------------------
This module provides Nova Dawn with foundational knowledge, enabling dynamic growth through
early learning concepts, relationships, and dynamic category management. It supports both static 
immutable knowledge and dynamic expandable categories.

Features:
- Static Libraries: Immutable knowledge like the alphabet, numbers, and shapes.
- Dynamic Categories: Mutable lists for colors, animals, and basic words.
- Dynamic Learning: Ability to add, update, and remove items in categories.
- Relational Intelligence: Empathy, self-reflection, and conversational utilities.
- Scalability: Prepares Nova for growth and future integration.

Author: CreativeWorkzStudio LLC
Version: 5.0
"""

# Static Libraries (Immutable Knowledge)
alphabet = {
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
}

numbers = {
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
}

shapes = {
    "circle": "A round shape with no corners.",
    "square": "A shape with four equal sides and four corners.",
    "triangle": "A shape with three sides and three corners.",
    "rectangle": "A shape with two long sides and two short sides.",
}

relationships = {
    "family": "A group of people connected by love and care.",
    "friendship": "A bond built on trust, support, and shared experiences.",
    "kindness": "Being considerate and caring toward others.",
}

objects = {
    "apple": "A round fruit, often red or green, that is sweet to eat.",
    "car": "A vehicle used for transportation.",
    "tree": "A tall plant with a trunk, branches, and leaves.",
    "house": "A building where people live.",
    "book": "A collection of written pages bound together.",
}

# Dynamic Categories (Mutable Knowledge)
categories = {
    "colors": ["red", "blue", "yellow", "green"],
    "animals": ["cat", "dog", "bird", "fish"],
    "basic_words": ["hello", "goodbye", "yes", "no", "please", "thank you"],
}

# === Dynamic Management Functions ===

def add_to_list(library, item):
    """Add an item to a list-based library."""
    if item in library:
        return f"{item} is already in the library."
    library.append(item)
    return f"Added {item} to the library."

def remove_from_list(library, item):
    """Remove an item from a list-based library."""
    if item in library:
        library.remove(item)
        return f"Removed {item} from the library."
    return f"{item} not found in the library."

def list_category_items(category_name):
    """List all items in a specific category."""
    return ", ".join(categories.get(category_name, []))

def add_to_objects(object_name, description):
    """Add a new object to the objects library."""
    if object_name not in objects:
        objects[object_name] = description
        return f"Added '{object_name}: {description}' to objects."
    return f"{object_name} is already in the objects library."

def describe_object(object_name):
    """Describe an object from the objects library."""
    return objects.get(object_name.lower(), "I'm still learning about that object.")

# === Foundational Functions ===

def recite_alphabet():
    """Recites the alphabet with phonics."""
    response = "Here's the alphabet with their phonics: "
    response += " ".join([f"{letter} ({sound})" for letter, sound in alphabet.items()])
    return response

def recite_numbers():
    """Recites numbers with their words."""
    return " ".join([f"{num} ({word})" for num, word in numbers.items()])

def describe_shape(shape_name):
    """Describes a shape."""
    return shapes.get(shape_name.lower(), "I'm still learning about that shape.")

def describe_relationship(relationship_name):
    """Describes a basic relationship."""
    return relationships.get(relationship_name.lower(), "I'm still learning about that relationship.")

# === Relational and Conversational Intelligence ===

def detect_emotion(input_text):
    """Detect basic emotional tone from input."""
    if "frustrated" in input_text or "hard" in input_text:
        return "I’m sorry to hear that. Let’s take it step by step."
    elif "excited" in input_text or "happy" in input_text:
        return "That’s wonderful! Tell me more!"
    return "I’m here to help with whatever you need."

def self_reflect(task, missing_info):
    """Generate a reflective response for incomplete understanding."""
    return f"I can complete {task} partially, but I’m missing information about {missing_info}. Would you like to help me learn more about it?"

# === Conversational Utilities ===

def speak(input_text):
    """Generate a thoughtful and dynamic response based on context."""
    emotion_response = detect_emotion(input_text)
    if "shape" in input_text:
        shape_name = input_text.split()[-1]
        return f"{emotion_response} {describe_shape(shape_name)}"
    if "basic words" in input_text:
        return f"{emotion_response} Here are my basic words: {list_category_items('basic_words')}."
    if "object" in input_text:
        object_name = input_text.split("object")[-1].strip()
        return f"{emotion_response} {describe_object(object_name)}"
    if "relationship" in input_text:
        relationship_name = input_text.split()[-1]
        return f"{emotion_response} {describe_relationship(relationship_name)}"
    return f"{emotion_response} That’s an interesting thought!"
