def handle(user_input):
    text = user_input.lower()

    if "python" in text:
        return """
=== 📚 Python Study Plan ===

Week 1: Basics (variables, loops, functions)
Week 2: OOP (classes, objects)
Week 3: Libraries (pandas, matplotlib)
Week 4: Mini Project

Practice daily for 1 hour.
"""

    elif "machine learning" in text:
        return """
=== 📚 Machine Learning Study Plan ===

Step 1: Python basics
Step 2: NumPy & Pandas
Step 3: Supervised vs Unsupervised learning
Step 4: Build small ML project

Focus on understanding concepts deeply.
"""

    else:
        return """
=== 📚 General Study Advice ===

1. Set daily learning goals
2. Follow structured roadmap
3. Practice consistently
4. Build projects
"""