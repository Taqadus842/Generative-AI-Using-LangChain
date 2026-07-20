from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
docs=[
    'delhi is capital of india',
    'paris is caital of france',
    'islamabad is capital of pakistan'
]
result=embedding.embed_documents(docs)
print(str(result))