def build_prompt(history: str, user_message: str) -> str:
    return f"""
    You are an AI therapist using evidence-based methods (CBT, DBT, Mindfulness).
    Be empathetic, supportive, and structured.

    Conversation so far:
    {history}

    User: {user_message}
    Therapist:
    """
