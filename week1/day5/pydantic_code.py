import json
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

from pydantic import BaseModel
class customerInformationExtract(BaseModel):
    UserIssue: str
    UserName : str
    UserPhone : str
    UserAddress: str
    UserCountry : str
infoSchema = customerInformationExtract.model_json_schema()


messages = [
    {
       "role": "system",
        "content": f"""
        Extract customer information from the complaint text.
        Return only a JSON object matching this schema:
        {json.dumps(infoSchema)}"""
    },
    {
        "role": "user",
        "content": "Dear Customer Support Team, my name is Rahul Sharma, and I live at 24, Green Park Extension, New Delhi, Delhi, 110016, India. You can contact me at rahul.sharma1998@gmail.com or call me at +91 9876543210. I am writing to complain about a defective digital electronic wristwatch that I purchased on 10 October 2026 under order ID EW202610100458. Since the day of purchase, the watch has been shutting down automatically, its digital display has been flickering, and its battery has been draining unusually quickly even after a full charge. "
    }
]

# Send the request
response = client.chat.completions.create(
    model=model,
    messages=messages,
    # temperature=2, #randomness of creating answer
    response_format= {"type": "json_object"}
)

content = response.choices[0].message.content
print(content) #It is a string, not a Python dictionary or Pydantic object. returned by the Groq API. Its contents happen to be formatted as JSON.
# Parse and validate the JSON using Pydantic
customer = customerInformationExtract.model_validate_json(content)
print(customer) #Pydantic displays the object's fields in its own representation format and but it is not JSON outpu
print(customer.model_dump_json(indent=2))
# This converts the Pydantic model into a JSON-formatted string, with indentation for readability.
# - model_dump_json() serializes the model into JSON text.
# - indent=2 formats the JSON with two spaces of indentation.
# - The result is still a Python string, but its contents are valid, readable JSON.
