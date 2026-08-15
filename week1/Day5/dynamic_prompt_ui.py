import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "DALL·E: Creating Images from Text",
    "AlphaFold: Using AI for scientific discovery"
])

style_input = st.selectbox("Select Explanation Style", [
    "Begineer-Friendly", "Technical", "Code-Oriented",
    "Research-Oriented", "Business-Oriented", "Creative Writing", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

template = load_prompt('template.json')

# fill the placeholders
prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)

if st.button('Summarise'):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(response.choices[0].message.content)










# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from groq import Groq
# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate

# load_dotenv()
# model = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))

# st.header('Research Tool')


# paper_input = st.selectbox("Select Research Paper Name",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis", "DALL·E: Creating Images from Text", "AlphaFold: Using AI for scientific discovery"])

# style_input = st.selectbox("Select Explanation Style",["Begineer-Friendly","Technical","Code-Oriented", "Research-Oriented", "Business-Oriented", "Creative Writing","Mathematical"])

# length_input = st.selectbox("Select Explanation Length",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explanation)"])

# # Template
# template = PromptTemplate(
#     template="""
# Please summarise the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical details:
#     - include relevant mathematical equations if present in the paper.
#     - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
# 2. Analogies:
#     - Use relatable analogies to simplify complex concepts and make them easier to understand.
# 3. Visualizations:
#     - Provide visual representations of key concepts, algorithms, or processes discussed in the paper.
# If certain information is not available in the paper, respond with: "Insufficient Information available" instead of guessing. Ensure that the summary is clear, concise, and accessible to a wide audience, including those without a technical background.
# """, 
# input_variables=["paper_input", "style_input", "length_input"]
# )

# # fill the placeholders
# prompt = template.invoke({ "paper_input": paper_input,
#                            "style_input": style_input, 
#                            "length_input": length_input 
# })

# if st.button('Summarise'):
#     result = model.invoke(prompt)
#     st.write(result.content)