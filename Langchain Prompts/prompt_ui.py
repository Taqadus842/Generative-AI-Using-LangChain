from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


st.header("Research Paper Summarizer")


paper = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need (Transformer)",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "Generative Adversarial Networks (GANs)",
        "AlexNet: ImageNet Classification with Deep CNNs"
    ]
)


length = st.selectbox(
    "Select Summary Length",
    [
        "Short (5 bullet points)",
        "Medium (2-3 paragraphs)",
        "Detailed (full explanation)"
    ]
)


style = st.radio(
    "Choose Summary Style",
    [
        "Simple Explanation",
        "Technical Explanation",
        "Research Review Style"
    ]
)


template = PromptTemplate(
    template="""
You are an AI research assistant.

Summarize the following research paper:

Paper: {paper}

Summary length:
{length}

Summary style:
{style}

Include:
- Research problem
- Methodology
- Key contributions
- Results
- Impact
""",
    input_variables=[
        "paper",
        "length",
        "style"
    ]
)


if st.button("Summarize"):

    prompt = template.invoke(
        {
            "paper": paper,
            "length": length,
            "style": style
        }
    )

    result = model.invoke(prompt)

    st.write(result.content)