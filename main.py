from router import detect_intent
from modules import resume, interview, study, productivity, trading
from context_engine import ContextEngine

import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file)

memory = load_memory()

def main():
    print("🚀 Welcome to Ashu AI Super Agent")
    print("Type 'exit' to quit.\n")

    # 🚀 Initialize Context Engine
    context_engine = ContextEngine()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye Ashu 👋")
            break

        # Memory capture
        if "my name is" in user_input.lower():
            name = user_input.split("is")[-1].strip()
            memory["name"] = name
            save_memory(memory)

        # Step 1: Detect raw intent
        intent, confidence = detect_intent(user_input)

        # Step 2: Let Context Engine resolve final intent
        final_intent = context_engine.resolve_intent(intent, confidence)

        print(f"(Intent: {intent} | Confidence: {confidence} | Final: {final_intent})")

        # If clarification needed
        if final_intent == "clarify":
            print("Agent (Ashu): Can you clarify what you mean?")
            print("-" * 50)
            continue

        # Route based on final_intent
        if final_intent == "study":
            response = study.handle(user_input)

        elif final_intent == "productivity":
            response = productivity.handle(user_input)

        elif final_intent == "resume":
            response = resume.handle(user_input)

        elif final_intent == "interview":
            response = interview.handle(user_input)

        elif final_intent == "trading":
            response = trading.handle(user_input)

        else:
            response = "Sorry, I don't understand that request."

        if "name" in memory:
            print(f"\nAgent ({memory['name']}):", response)
        else:
            print("\nAgent:", response)

        print("-" * 50)


if __name__ == "__main__":
    main()