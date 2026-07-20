from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful {domain} expert."),
        ("human", "Explain in simple terms, what is {topic}?")
    ]
)

prompt = chat_prompt.invoke(
    {
        "domain": "cricket",
        "topic": "LangChain"
    }
)

print(prompt)