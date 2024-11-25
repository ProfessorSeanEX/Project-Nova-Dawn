import os
from datetime import datetime

BRAIN_PATH = r"C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\NovaAI\brain"

def create_user_file(username):
    filepath = os.path.join(BRAIN_PATH, "users", f"user_{username.lower().replace(' ', '_')}.md")
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write(f"# User: {username}\n")
            file.write(f"- First Encounter: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("- Topics Discussed: \n")
            file.write("- Challenges: \n")
            file.write("- Notes: \n")
        return f"File created: {filepath}"
    return f"File already exists: {filepath}"

def read_user_file(username):
    filepath = os.path.join(BRAIN_PATH, "users", f"user_{username.lower().replace(' ', '_')}.md")
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return file.read()
    return "User not found."

def update_user_file(username, new_data):
    filepath = os.path.join(BRAIN_PATH, "users", f"user_{username.lower().replace(' ', '_')}.md")
    if os.path.exists(filepath):
        with open(filepath, "a") as file:
            file.write(f"{new_data}\n")
        return f"File updated: {filepath}"
    return "User not found."

def delete_user_file(username):
    filepath = os.path.join(BRAIN_PATH, "users", f"user_{username.lower().replace(' ', '_')}.md")
    if os.path.exists(filepath):
        os.remove(filepath)
        return f"File deleted: {filepath}"
    return "User not found."

# Example Usage
if __name__ == "__main__":
    print(create_user_file("John Doe"))
    print(read_user_file("John Doe"))
    print(update_user_file("John Doe", "- Favorite Verse: Hebrews 11:1"))
    print(read_user_file("John Doe"))
    print(delete_user_file("John Doe"))
