from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel
from typing import Literal

load_dotenv()

prompt=PromptTemplate(
    template='Classify the sentiment of following feedback text  into positive or negative {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partal_varibles={format_instructions}
)

class Feedback(BaseModel):
    sentiment: Literal['positive','negative']=Field(description="Give me sentiment of ")

parser2=PydanticOutputParser(pydantic_object=Feedback)
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')
parser=PydanticOutputParser()

classifier_chain=prompt |model|parser

result=classifier_chain.invoke({"feedback":"This is a terrible smart phone"})
print(result)

classifier_chain.get_graph().print_ascii()

