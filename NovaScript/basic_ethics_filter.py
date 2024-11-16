# basic_ethics_filter.py

# Sample list of mission-aligned keywords and prohibited words.
mission_keywords = ["faith", "love", "wisdom", "grace", "compassion"]
prohibited_words = ["hate", "violence", "disrespect"]

# Basic function to check if a user input aligns with mission principles
def ethics_filter(user_input):
    """
    Checks if user input aligns with mission-aligned principles by looking for
    mission keywords and ensuring prohibited words are not present.
    """
    # Convert input to lowercase to standardize the search
    user_input = user_input.lower()
    
    # Check for prohibited words
    for word in prohibited_words:
        if word in user_input:
            return "Response not mission-aligned. Contains prohibited language."
    
    # Check for mission keywords to confirm alignment
    for keyword in mission_keywords:
        if keyword in user_input:
            return "Response aligns with mission values."
    
    # If no mission keywords or prohibited words are found
    return "Response neutral but acceptable under mission guidelines."

# Sample execution
if __name__ == "__main__":
    # Example user input
    test_input = input("Enter user input to check mission alignment: ")
    result = ethics_filter(test_input)
    print(result)
