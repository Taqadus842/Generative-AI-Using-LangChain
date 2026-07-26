from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough
)

load_dotenv()

# Prompt 1: Generate text
prompt1 = PromptTemplate(
    template="Generate a detailed joke about {topic}",
    input_variables=["topic"]
)

# Prompt 2: Summarize generated text
prompt2 = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()


# Generate joke chain
joke_gen_chain = (
    prompt1
    | model
    | parser
)


# Summarization chain
summary_chain = (
    {"text": RunnablePassthrough()}
    | prompt2
    | model
    | parser
)


# Branch condition
branch_chain = RunnableBranch(
    (
        lambda x: len(x.split()) > 50,
        summary_chain
    ),
    RunnablePassthrough()
)


# Final chain
final_chain = joke_gen_chain | branch_chain


result = final_chain.invoke({
    "topic": "Artificial Intelligence"
})

print(result)