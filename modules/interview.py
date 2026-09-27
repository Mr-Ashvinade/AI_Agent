def handle(user_input):
    text = user_input.lower()

    if "python" in text:
        return """
=== 🎤 Python Interview Practice ===

Question:
What is the difference between a list and a tuple in Python?

Think and answer it yourself first 😉
"""

    elif "data" in text:
        return """
=== 🎤 Data Analyst Interview Question ===

Question:
What is the difference between supervised and unsupervised learning?
"""

    else:
        return """
=== 🎤 General Interview Practice ===

Question:
Tell me about yourself.

Tip:
Structure your answer like this:
1. Background
2. Skills
3. Projects
4. Career goals
"""