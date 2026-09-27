def handle(user_input):
    text = user_input.lower()

    feedback = []

    if "project" not in text:
        feedback.append("⚠️ Add a Projects section to showcase practical work.")

    if "skill" not in text:
        feedback.append("⚠️ Include a dedicated Skills section.")

    if "experience" not in text:
        feedback.append("⚠️ Mention internships or work experience if available.")

    if "achieved" not in text and "improved" not in text:
        feedback.append("⚠️ Add measurable achievements (e.g., increased sales by 20%).")

    if not feedback:
        feedback.append("✅ Your resume structure looks good!")

    return "\n=== 📄 Resume Analysis ===\n\n" + "\n".join(feedback)