"""
AI-powered task generator.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tasks(goal: str) -> str:
    prompt = (
        "Create a clear and practical task list to achieve the following goal:\n\n"
        f"{goal}"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    objective = "Launch a small AI-powered web application"
    tasks = generate_tasks(objective)

    print("Generated tasks:\n")
    print(tasks)
