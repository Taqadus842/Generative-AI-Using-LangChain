from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful customer support agent."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
    ]
)

chat_history = []

with open("chat_history.txt", "r") as f:
    for line in f:
        chat_history.append(HumanMessage(content=line.strip()))

prompt = chat_template.invoke(
    {
        "chat_history": chat_history,
        "query": "How can I reset my password?"
    }
)

print(prompt)