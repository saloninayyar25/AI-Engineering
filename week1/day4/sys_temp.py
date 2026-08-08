import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"

prompt = "You are a helpful assistant. Please provide a brief summary of the latest advancements in artificial intelligence, focusing on natural language processing and machine learning techniques."
# SYSTEM PROMPT
message = {
    "role" : role,
    "content" : "You are a helpful assistant."
}

message = {
    "role" : role,
    "content" : prompt
}
messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    temperature=0.5
)
answer = response.choices[0].message.content
print(answer)