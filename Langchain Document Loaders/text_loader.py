from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt=PromptTemplate(
    template="Write a summary of following text: \n {text}",
    input_variables=['text']
)

parser=StrOutputParser()

loader=TextLoader("cricket.txt",encoding="utf-8")

doc=loader.load()
print(type(doc))

print(len(doc))

print(type(doc[0]))

print(doc)

chain=prompt|model|parser
print("\n SUMMARY \n")
print(chain.invoke({'text':doc[0].page_content}))