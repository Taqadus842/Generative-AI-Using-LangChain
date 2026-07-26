from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os 

load_dotenv()

os.environ["USER_AGENT"] = "LangChain-WebLoader-Test"

prompt=PromptTemplate(
    template="Answer the following question \n {question} from following text- \n {text}",
    input_variables=['question','text']
)

model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser=StrOutputParser()

url="https://en.wikipedia.org/wiki/Artificial_intelligence"
loader=WebBaseLoader(url)
docs=loader.load()

print(len(docs))
print(type(docs))

chain=prompt |model|parser

question="what is ai?"
result=chain.invoke({'question':question,'text':docs[0].page_content})
print(result)