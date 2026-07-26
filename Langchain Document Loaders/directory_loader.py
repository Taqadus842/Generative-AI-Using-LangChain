from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="sample_folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

#using load
doc=loader.load()

print(f"Type: {type(doc)}\n")
print(f"Total Documents: {len(doc)}\n")

print(f"Page Content of 1st document: {doc[0].page_content}")
print(f"Meta Data of 1st document: {doc[0].metadata}")

#using lazy load
docs = loader.lazy_load()

print(f"Type: {type(docs)}\n")

for i, doc in enumerate(docs):
    print(f"Document {i+1}")
    print(f"Page Content: {doc.page_content[:200]}")
    print(f"Metadata: {doc.metadata}")
    print("-" * 50)