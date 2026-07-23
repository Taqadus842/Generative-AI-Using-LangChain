from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)


# Define output schema using Pydantic
class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about topic")
    fact_2: str = Field(description="Fact 2 about topic")
    fact_3: str = Field(description="Fact 3 about topic")


parser = PydanticOutputParser(pydantic_object=Facts)


template = PromptTemplate(
    template="""Give 3 facts about {topic}

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


# Without chain
prompt = template.format(topic="black hole")

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
print(final_result.fact_1)


# With chain
chain = template | model | parser

result1 = chain.invoke({"topic": "black hole"})

print(result1)
print(result1.fact_1)