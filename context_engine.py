MAX_CONTEXT_TURNS = 3
HIGH_CONFIDENCE = 0.75
LOW_CONFIDENCE = 0.4


class ContextEngine:
    def __init__(self):
        self.context = None

    def resolve_intent(self, new_intent, new_confidence):

        # First message ever
        if self.context is None:
            self.context = {
                "intent": new_intent,
                "confidence": new_confidence,
                "turns": 0
            }
            return new_intent

        # Increase turn count
        self.context["turns"] += 1

        # HIGH confidence → override immediately
        if new_confidence >= HIGH_CONFIDENCE:
            self.context = {
                "intent": new_intent,
                "confidence": new_confidence,
                "turns": 0
            }
            return new_intent

        # MEDIUM confidence
        elif new_confidence >= LOW_CONFIDENCE:
            if self.context["turns"] <= MAX_CONTEXT_TURNS:
                return self.context["intent"]
            else:
                self.context = {
                    "intent": new_intent,
                    "confidence": new_confidence,
                    "turns": 0
                }
                return new_intent

        # LOW confidence
        else:
            if self.context["turns"] <= MAX_CONTEXT_TURNS:
                return self.context["intent"]
            else:
                return "clarify"