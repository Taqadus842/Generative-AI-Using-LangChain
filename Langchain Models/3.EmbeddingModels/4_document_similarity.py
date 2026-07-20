from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

docs = [
    "Artificial intelligence is transforming the way we solve complex problems.",
    "Machine learning algorithms learn patterns from data to make predictions.",
    "Pakistan is a country located in South Asia with Islamabad as its capital.",
    "Deep learning models use neural networks to process large amounts of information.",
    "LangChain is a framework used for building applications powered by large language models."
]

query='tell me about langchain'

doc_embeddings=embeddings.embed_documents(docs)
query_embedding=embeddings.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)

index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(docs[index])
print("similarity index is: ",score)