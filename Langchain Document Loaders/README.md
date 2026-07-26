# LangChain Document Loaders

This folder contains examples of different LangChain Document Loaders used to load data from various sources.

## Loaders Explored

### TextLoader
- Loads `.txt` files into LangChain Documents.
- Used for processing plain text data.

### CSVLoader
- Loads CSV files and converts rows into Documents.
- Useful for structured data processing.

### DirectoryLoader
- Loads multiple files from a directory.
- Supports different file types using specific loaders.

### PyPDFLoader
- Extracts text from PDF files.
- Used for loading books, reports, and research papers.

### WebBaseLoader
- Loads and extracts content from web pages.
- Useful for web-based RAG applications.


## Installation

```bash
pip install langchain langchain-community pypdf beautifulsoup4 pandas

## Concepts Learned

Loading documents from different sources
Working with LangChain Document objects
Understanding metadata
Preparing data for RAG pipelines