# 🚀 Generative AI Using LangChain

A comprehensive collection of hands-on projects, examples, and implementations built while learning **LangChain**. This repository covers the core concepts required to build LLM-powered applications, including chains, prompts, retrieval, vector databases, output parsers, runnables, tools, and more.

---

## 📂 Repository Structure

```
Generative-AI-Using-LangChain/
│
├── LangChain Chains/
├── Langchain Document Loaders/
├── Langchain Models/
├── Langchain Output Parser/
├── Langchain Prompts/
├── Langchain Retrievers/
├── Langchain Runnables/
├── Langchain Structured Output/
├── Langchain Text Splitters/
├── Langchain Vector Stores/
├── Tools in langchain/
└── README.md
```

---

## 📖 Topics Covered

### 🔗 LangChain Chains
- Sequential Chains
- Parallel Chains
- LLM Chains
- Chaining multiple components
- Prompt → Model → Output pipeline

---

### 📄 Document Loaders
Learn how to load data from different sources.

Examples include:
- Text files
- PDF files
- Web pages
- Directories
- Multiple documents

---

### 🤖 LangChain Models
Working with different Large Language Models.

Examples:
- Google Gemini
- OpenAI
- Ollama
- Hugging Face

Topics:
- Chat Models
- Completion Models
- Model Parameters
- Temperature
- Max Tokens

---

### 📝 Prompts
Prompt engineering using LangChain.

Topics:
- PromptTemplate
- ChatPromptTemplate
- System Messages
- Human Messages
- Partial Prompts

---

### 📤 Output Parsers
Convert LLM responses into structured formats.

Examples:
- StrOutputParser
- JsonOutputParser
- PydanticOutputParser

---

### 🗂 Text Splitters
Splitting large documents for Retrieval-Augmented Generation (RAG).

Covered:
- RecursiveCharacterTextSplitter
- CharacterTextSplitter
- Chunk Size
- Chunk Overlap

---

### 🧠 Vector Stores
Store and retrieve embeddings efficiently.

Examples:
- FAISS
- ChromaDB

Topics:
- Similarity Search
- Metadata Filtering
- MMR Search

---

### 🔍 Retrievers
Different retrieval techniques.

Examples:
- Basic Retriever
- Similarity Search
- MMR Retriever
- Contextual Compression Retriever
- Multi Query Retriever

---

### ⚙️ Runnables
LangChain Expression Language (LCEL).

Topics:
- RunnableLambda
- RunnableSequence
- RunnableParallel
- RunnablePassthrough
- Pipeline Composition

---

### 📦 Structured Output
Generate structured responses from LLMs.

Examples:
- Pydantic Models
- JSON Output
- Validation
- Typed Responses

---

### 🛠 Tools in LangChain
Learn how LLMs interact with external tools.

Topics:
- Tool Creation
- StructuredTool
- Tool Calling
- Custom Tools
- Agent Tools

---

## 🛠 Technologies Used

- Python 3
- LangChain
- Google Gemini
- Ollama
- FAISS
- ChromaDB
- Hugging Face
- Pydantic

---

## 🎯 Learning Objectives

This repository demonstrates how to:

- Build applications using LangChain
- Connect Large Language Models
- Create reusable prompt templates
- Load and process documents
- Split text into chunks
- Generate embeddings
- Store embeddings in vector databases
- Retrieve relevant context
- Parse structured outputs
- Build custom tools
- Compose workflows using LCEL

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/Taqadus842/Generative-AI-Using-LangChain.git
```

### Navigate to the Project

```bash
cd Generative-AI-Using-LangChain
```

### Create a Virtual Environment

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📚 Skills You'll Learn

- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Tool Calling
- Output Parsing
- LCEL
- Document Processing
- LLM Application Development
- Agent Development Fundamentals

---

## 📌 Prerequisites

- Python 3.10+
- Basic Python Knowledge
- API Key (Google Gemini/OpenAI) *(if required)*
- pip

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, improve existing examples, or add new LangChain implementations.

---

## ⭐ Support

If you find this repository helpful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and learning purposes.