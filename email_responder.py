"""
AI-powered email responder using Generative AI.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email_reply(email_content: str) -> str:
    prompt = (
        "You are a professional customer support assistant.\n"
        "Write a clear, polite, and professional reply to the email below:\n\n"
        f"{email_content}"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    sample_email = (
        "Hello, I would like to know more about your services "
        "and pricing options. Thank you."
    )

    reply = generate_email_reply(sample_email)
    print("Generated reply:\n")
    print(reply)
