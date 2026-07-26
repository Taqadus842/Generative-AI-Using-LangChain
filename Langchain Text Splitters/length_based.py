from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader=PyPDFLoader("sample_cricket.pdf")
docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
text=splitter.split_documents(docs)
print(len(text))
print(text[0].page_content)