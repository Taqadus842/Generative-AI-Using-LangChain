from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a short summary about {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Improve this summary and make it more engaging:\n{text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
parser=StrOutputParser()

summary_gen_chain= RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel(
    {
        "summary": RunnablePassthrough(),
        "summary_improved": RunnableSequence(prompt2,model,parser)
    }
)
final_chain=RunnableSequence(summary_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'AI'})
print(result)

