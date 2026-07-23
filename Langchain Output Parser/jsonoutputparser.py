from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic}\n{format_instructions}',
    input_variables=["topic"],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)
#without chain
prompt = template.format(topic='black hole')

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

#with chain
chain= template|model|parser
result1=chain.invoke({'topic':'blackhole'})
print(result1)
