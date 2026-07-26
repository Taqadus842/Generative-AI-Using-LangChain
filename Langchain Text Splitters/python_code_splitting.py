from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Write a Python code here

def add(a, b):
    return a + b

for i in range(5):
    print(add(i, i + 1))
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])
print(chunks[1])