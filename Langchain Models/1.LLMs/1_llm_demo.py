from langchain_openai import OpenAI
from dot_env import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("What is capital of Pakistan?")

print(result)