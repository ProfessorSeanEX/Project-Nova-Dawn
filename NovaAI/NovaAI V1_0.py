# NovaAI: Version 1.0
# Main conversational AI script

import random
import function_linker  # Import the function linker module

# Keyword-based responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "trust": "Trust means having confidence in someone or something.",
    "faith": "Faith is complete trust or confidence in someone or something.",
    "bye": "Goodbye! Have a great day!"
}

# Basic answers
basic_answers = ["Yes.", "No.", "Maybe.", "I don't know."]

# Filler phrases
filler_phrases = [
    "That's an interesting thought.",
    "Let's think about this together.",
    "I'm curious to hear more about that.",
    "Can you elaborate on that for me?"
]

# Function to process input
def process_input(user_input):
    # Check for question types
    if user_input.lower().startswith("who"):
        return "Who is a great question! Can you tell me more about who you're thinking of?"
    elif user_input.lower().startswith("what"):
        return "What are you curious about? I'd love to explore that with you."
    elif user_input.lower().startswith("when"):
        return "Timing is important. Are you asking about a specific moment?"
    elif user_input.lower().startswith("where"):
        return "Location matters! Are you asking about a specific place?"
    elif user_input.lower().startswith("why"):
        return "Why is always a deep question. Let's reflect on that together."
    elif user_input.lower().startswith("how"):
        return "How can be tricky but fascinating. Let's work through it step by step."

    # Check for predefined keyword responses
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            return response

    # Random filler or basic answer
    return random.choice(basic_answers + filler_phrases)

# Onboarding function
def onboarding():
    print("Welcome to NovaAI!")
    print("I’m here to explore ideas, reflections, and thoughts with you.")
    print("Feel free to ask me anything, and let’s see where the conversation takes us!")

# Main interaction loop
def main():
    onboarding()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("NovaAI: Goodbye! Have a great day!")
            break

        # Use function linker to execute linked functions dynamically
        if "add" in user_input.lower():
            print(f"NovaAI: {function_linker.execute_function('calculate_sum', user_input)}")
        elif "hello" in user_input.lower():
            print(f"NovaAI: {function_linker.execute_function('greet_user')}")
        else:
            response = process_input(user_input)
            print(f"NovaAI: {response}")

if __name__ == "__main__":
    main()
