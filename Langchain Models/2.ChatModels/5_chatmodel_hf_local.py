from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm=HuggingFacePipeline(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='textGeneration',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("capital of india")