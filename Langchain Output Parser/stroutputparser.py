from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

#1st prompt ->detailed report
template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)
#2nd prompt ->summary
template2=PromptTemplate(
    template="Write a 5 line summary on following text. /n {text}",
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'black hole'})
response1=model.invoke(prompt1)

prompt2=template2.invoke({'text':response1.content})
result=model.invoke(prompt1)

print(result.content)