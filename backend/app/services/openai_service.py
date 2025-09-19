import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_response(user_message: str, history: str) -> str:
    prompt = f"""
    You are an AI therapist providing CBT, DBT, and mindfulness support.
    Be empathetic, supportive, and structured.
    
    Conversation so far:
    {history}

    User: {user_message}
    Therapist:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a supportive therapist."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content
