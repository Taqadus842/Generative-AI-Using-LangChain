from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("sample_cricket.pdf")

doc=loader.load()

print(f"Type of document: {type(doc)}\n")
print(f"Length of document: {len(doc)}\n")
print(f"Page Content: {doc[0].page_content}\n")
print(f"Meta Deta: {doc[0].metadata}\n")