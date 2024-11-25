# Function Linker for NovaAI
# Parses a .md file to dynamically link functions

# Function Definitions
def greet_user():
    return "Hi there! How can I assist you today?"

def calculate_sum(input_text):
    # Extract numbers from the input
    numbers = [int(word) for word in input_text.split() if word.isdigit()]
    return f"The sum is {sum(numbers)}." if len(numbers) == 2 else "Please provide two numbers to add."

# Function Mapping
function_mapping = {
    "greet_user": greet_user,
    "calculate_sum": calculate_sum
}

# Parse Markdown File
def parse_md(file_path):
    functions = {}
    current_function = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("##"):  # Function Name
                current_function = line[2:].strip()
                functions[current_function] = {}
            elif line.startswith("- Description:"):
                functions[current_function]["description"] = line.split(":")[1].strip()
            elif line.startswith("- Example Input:"):
                functions[current_function]["example_input"] = line.split(":")[1].strip()
            elif line.startswith("- Example Output:"):
                functions[current_function]["example_output"] = line.split(":")[1].strip()

    return functions

# Function Execution
def execute_function(function_name, user_input=None):
    if function_name in function_mapping:
        func = function_mapping[function_name]
        return func(user_input) if user_input else func()
    return "Function not found."
