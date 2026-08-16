from groq import Groq
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
console = Console(width=120)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

role_map = {"system": "system", "human": "user", "ai": "assistant"}

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break

    chat_history.append(HumanMessage(content=user_input))

    api_messages = [{"role": role_map[m.type], "content": m.content} for m in chat_history]

    result = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=api_messages,
        max_tokens=2048
    )

    ai_reply = result.choices[0].message.content
    chat_history.append(AIMessage(content=ai_reply))
    console.print("[bold cyan]AI:[/bold cyan]")
    console.print(Markdown(ai_reply))

print(chat_history)

# from groq import Groq
# from dotenv import load_dotenv
# from rich.console import Console
# from rich.markdown import Markdown
# import os
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# console = Console(width=120)

# chat_history = [
#     SystemMessage(content="You are a helpful AI assistant."),

#     # {
#     #     "role": "system",
#     #     "content": "Answer naturally in plain prose by default. Only use a Markdown table when the user explicitly asks for a comparison or the data is genuinely tabular. Avoid tables, bullet lists, and headers for simple or conversational questions."
#     # }
# ]

# while True:
#     user_input = input('You: ')
#     if user_input.lower() in ['exit', 'quit']:
#         print("Exiting the chatbot. Goodbye!")
#         break

#     chat_history.append(HumanMessage(content=user_input))

#     result = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=chat_history,
#         max_tokens=2048
#     )

#     ai_reply = result.choices[0].message.content
#     chat_history.append(AIMessage(content=ai_reply))
#     console.print("[bold cyan]AI:[/bold cyan]")
#     console.print(Markdown(ai_reply))

# print(chat_history)  # debug: see the full history being sent



# # from groq import Groq
# # from dotenv import load_dotenv
# # from rich.console import Console
# # from rich.markdown import Markdown
# # import os

# # load_dotenv()
# # client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# # console = Console()

# # while True:
# #     user_input = input('You: ')
# #     if user_input.lower() in ['exit', 'quit']:
# #         console.print("Exiting the chatbot. Goodbye!")
# #         break
# #     result = client.chat.completions.create(
# #         model="openai/gpt-oss-20b",
# #         messages=[
# #             {"role": "user", "content": user_input}
# #         ]
# #     )
# #     console.print("[bold cyan]AI:[/bold cyan]")
# #     console.print(Markdown(result.choices[0].message.content))

# from groq import Groq
# from dotenv import load_dotenv
# from rich.console import Console
# from rich.markdown import Markdown
# import os

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# console = Console(width=120)

# chat_history = []

# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input.lower() in ['exit', 'quit']:
#         print("Exiting the chatbot. Goodbye!")
#         break
#     result = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "Answer naturally in plain prose by default. Only use a Markdown table when the user explicitly asks for a comparison or the data is genuinely tabular. Avoid tables, bullet lists, and headers for simple or conversational questions."
#             },
#             {"role": "user", "content": user_input}
#         ],
#         max_tokens=2048
#     )
#     console.print("[bold cyan]AI:[/bold cyan]")
#     console.print(Markdown(result.choices[0].message.content))