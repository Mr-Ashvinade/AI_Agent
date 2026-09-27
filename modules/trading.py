def handle(user_input):
    text = user_input.lower()

    if "risk" in text:
        return """
=== 📊 Risk Management Basics ===

1. Never risk more than 2% of capital per trade.
2. Always use stop-loss.
3. Avoid emotional trading.
4. Maintain risk-reward ratio of at least 1:2.
"""

    elif "analysis" in text or "strategy" in text:
        return """
=== 📈 Basic Trading Strategy ===

1. Identify trend (uptrend/downtrend).
2. Use support & resistance levels.
3. Confirm with volume.
4. Enter with clear stop-loss.
"""

    else:
        return """
=== 💹 Trading Guidance ===

Trading requires:
- Discipline
- Risk management
- Backtesting strategies
- Emotional control

Never trade without proper learning.
"""