from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarise the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical details:
    - include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex concepts and make them easier to understand.
3. Visualizations:
    - Provide visual representations of key concepts, algorithms, or processes discussed in the paper.
If certain information is not available in the paper, respond with: "Insufficient Information available" instead of guessing. Ensure that the summary is clear, concise, and accessible to a wide audience, including those without a technical background.
""", 
    input_variables=["paper_input", "style_input", "length_input"],
    validation_template=True
)
template.save('template.json')