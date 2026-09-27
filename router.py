def detect_intent(user_input):
    user_input = user_input.lower()

    intent_keywords = {
        "resume": ["resume", "cv", "experience", "skills"],
        "interview": ["interview", "question", "prepare", "hr"],
        "study": ["study", "learn", "teach", "course"],
        "productivity": ["productivity", "schedule", "routine", "plan"],
        "trading": ["trade", "stock", "market", "crypto"]
    }

    scores = {}

    for intent, keywords in intent_keywords.items():
        score = 0
        for word in keywords:
            if word in user_input:
                score += 1
        scores[intent] = score

    best_intent = max(scores, key=scores.get)
    best_score = scores[best_intent]

    total_score = sum(scores.values())

    if best_score == 0:
        return "unknown", 0

    confidence = best_score / total_score if total_score > 0 else 0

    return best_intent, round(confidence, 2)