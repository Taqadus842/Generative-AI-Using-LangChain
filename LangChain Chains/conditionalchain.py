from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
from typing import Literal

load_dotenv()


# Define output structure
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )


# Create Pydantic parser
parser = PydanticOutputParser(
    pydantic_object=Feedback
)


# Create prompt
prompt = PromptTemplate(
    template="""
Classify the sentiment of the following feedback text into positive or negative.

Feedback:
{feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# Create chain
classifier_chain = prompt | model | parser


# Invoke chain
result = classifier_chain.invoke(
    {
        "feedback": "This is a terrible smartphone"
    }
)

print(result)

# View chain graph
classifier_chain.get_graph().print_ascii()