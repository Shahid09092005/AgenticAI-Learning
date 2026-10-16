import os
from dotenv import load_dotenv
from groq import Groq

# Activate your virtual environment before running the script
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
        "role": "system", # system role
        "content": "You are expert for creating brand names."
    },
    {
        "role": "user",
        "content": "suggest me 2 name for my goat farming businees."
    }
]

# Send the request
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2, #randomness of creating answer
)

print(response.choices[0].message.content)