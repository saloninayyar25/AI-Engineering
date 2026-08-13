# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from groq import Groq
# import streamlit as st

# load_dotenv()

# st.header('Research Tool')

# model = "llama-3.3-70b-versatile"

# user_input = st.text_input("Enter your question here:")

# if st.button('Summarise'):
#     result = model.invoke(user_input)
#     st.write('result.context')4

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.header('Research Tool')

user_input = st.text_input("Enter your question here:")

if st.button('Summarise'):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": user_input}]
    )
    result = response.choices[0].message.content
    st.write(result)