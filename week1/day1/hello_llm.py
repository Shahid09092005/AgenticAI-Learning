
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
# .venv\Scripts\activate   to active venv inside day1 folder
load_dotenv()

# Read the API key
groq_api_key = os.getenv("groq_api_key")

if not groq_api_key:
    raise ValueError("Groq API key not found. Check your .env file.")

# Initialize the Groq client
client = Groq(api_key=groq_api_key)

model = "openai/gpt-oss-120b"

messages = [
    {
        "role": "user",
        "content": "Do you know Padho with Pratyush?"
    }
]

# Send the request
response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
