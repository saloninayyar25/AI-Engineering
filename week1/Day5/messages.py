from dotenv import load_dotenv
from groq import Groq
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about Data engineering."),
]

role_map = {"system": "system", "human": "user", "ai": "assistant"}
api_messages = [{"role": role_map[m.type], "content": m.content} for m in messages]

result = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=api_messages
)

messages.append(AIMessage(content=result.choices[0].message.content))
print(messages)