from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
model2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
prompt1=PromptTemplate(
    template='Generate short and simple notes from {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short questions answers from {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="""
Create a single document by combining the notes and quiz.

Notes:
{notes}

Quiz:
{quiz}

Make the final document well formatted with headings.
""",
    input_variables=["notes", "quiz"]
)

parser=StrOutputParser()

parallel_chain= RunnableParallel({
    'notes':prompt1|model1|parser,
    'quiz':prompt2|model2|parser
}
)

merge_chain=prompt3|model1|parser

chain=parallel_chain|merge_chain

text = """
Artificial Intelligence (AI) is a branch of computer science that enables machines 
to perform tasks that usually require human intelligence. These tasks include 
learning, reasoning, problem-solving, understanding language, and recognizing images.

Machine Learning is a subset of AI where models learn patterns from data and improve 
their performance without being explicitly programmed. Deep Learning uses neural 
networks with multiple layers to solve complex problems such as image recognition 
and natural language processing.

Generative AI is a type of AI that can create new content such as text, images, 
audio, and code. Large Language Models (LLMs) like Gemini and Claude are examples 
of generative AI systems.
"""

result=chain.invoke({'text':text})
print(result)



