from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Cricket is one of the most popular sports in the world.
It is played between two teams of eleven players.
The game includes batting, bowling, and fielding.
International cricket is governed by the ICC.
Test, ODI, and T20 are the main formats of the game.
"""


splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)
