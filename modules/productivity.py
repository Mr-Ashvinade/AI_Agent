def handle(user_input):
    text = user_input.lower()

    if "career" in text:
        return """
=== 🚀 Career Planning Guidance ===

Step 1: Identify your target field.
Step 2: List required skills.
Step 3: Build projects.
Step 4: Improve resume.
Step 5: Prepare for interviews.

Focus on long-term growth, not shortcuts.
"""

    elif "daily" in text or "routine" in text:
        return """
=== 📅 Daily Productivity Plan ===

Morning:
- Study 1 hour
- Practice coding

Afternoon:
- Work on project

Evening:
- Revise concepts
- Plan next day

Consistency > Motivation
"""

    else:
        return """
=== ⚡ Productivity Advice ===

1. Set clear goals
2. Break tasks into small steps
3. Avoid multitasking
4. Review weekly progress
"""