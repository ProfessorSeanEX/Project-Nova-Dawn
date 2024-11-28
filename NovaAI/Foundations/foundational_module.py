# Static Libraries (Initialized Dynamically for Mutability)
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
    "Z": "Zee"
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
    10: "Ten"
}

shapes = {
    "circle": "A round shape with no corners.",
    "square": "A shape with four equal sides and four corners.",
    "triangle": "A shape with three sides and three corners."
}

categories = {
    "colors": ["red", "blue", "yellow", "green"],
    "animals": ["cat", "dog", "bird", "fish"]
}

basic_words = ["hello", "goodbye", "yes", "no", "please", "thank you"]

# Dynamic Library Management Functions
def add_to_list(library, item):
    """Add an item to a list-based library."""
    if item in library:
        return f"{item} is already in the library."
    library.append(item)
    return f"Added {item} to the library."

def update_library(library, key, new_value):
    """Update an existing entry in a library."""
    if key in library:
        library[key] = new_value
        return f"Updated {key} to: {new_value}."
    return f"{key} not found in the library."

def remove_from_library(library, key):
    """Remove an entry from a library."""
    if key in library:
        del library[key]
        return f"Removed {key} from the library."
    return f"{key} not found in the library."

def add_to_category(category_name, item):
    """Add an item to a category."""
    if category_name not in categories:
        categories[category_name] = []
    if item not in categories[category_name]:
        categories[category_name].append(item)
        return f"Added {item} to the {category_name} category."
    return f"{item} is already in the {category_name} category."

def remove_from_category(category_name, item):
    """Remove an item from a category."""
    if category_name in categories and item in categories[category_name]:
        categories[category_name].remove(item)
        return f"Removed {item} from the {category_name} category."
    return f"{item} not found in the {category_name} category."

def list_category_items(category_name):
    """List all items in a specific category."""
    return ", ".join(categories.get(category_name, []))

# Foundational Knowledge Functions
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
    description = shapes.get(shape_name.lower())
    if description:
        return description
    return "I'm still learning about that shape."

def list_library_items(library):
    """List all items in a library."""
    return "\n".join([f"{key}: {value}" for key, value in library.items()])

def construct_sentence(subject, verb, obj, adjectives=None):
    """Dynamically generate a sentence."""
    description = " ".join(adjectives) if adjectives else ""
    return f"The {description} {subject} {verb} the {obj}."

# Relational and Emotional Functions
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

# Conversational Functions
def speak(input_text):
    """Generate a thoughtful and dynamic response based on context."""
    # Detect emotion
    emotion_response = detect_emotion(input_text)

    # Analyze input and generate response
    if "shape" in input_text:
        shape_name = input_text.split()[-1]  # Get the last word as the shape
        response = describe_shape(shape_name)
    elif "relationship" in input_text:
        items = input_text.split(" and ")
        if len(items) == 2:
            response = f"I think there might be a connection between {items[0]} and {items[1]}."
        else:
            response = "Can you clarify what you're asking about?"
    elif "teach me" in input_text:
        # Learn a new word
        new_word = input_text.replace("teach me", "").strip()
        response = teach_word(new_word)
    elif "what is" in input_text and "category" in input_text:
        category_name = input_text.split("category")[-1].strip()
        response = list_category_items(category_name)
    else:
        response = "That’s an interesting thought! Let me think about it more."

    # Combine emotion and response
    return f"{emotion_response} {response}"

