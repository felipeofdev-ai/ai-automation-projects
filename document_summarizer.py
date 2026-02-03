"""
AI-powered document summarizer.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_document(text: str) -> str:
    prompt = (
        "Summarize the following document in a clear and concise way:\n\n"
        f"{text}"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    document_text = (
        "Artificial intelligence is transforming how companies operate. "
        "By automating repetitive tasks and enabling data-driven decisions, "
        "AI helps organizations improve efficiency and reduce costs."
    )

    summary = summarize_document(document_text)
    print("Summary:\n")
    print(summary)
