from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=0,max_completion_tokens=1)
result=model.invoke("What is capital of Pakistan?")

print(result.content)