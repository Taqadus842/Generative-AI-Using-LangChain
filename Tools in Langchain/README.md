# LangChain Tools

This folder contains examples demonstrating how to use **LangChain Tools** to extend the capabilities of Large Language Models (LLMs). Tools enable an LLM to interact with external functions, APIs, search engines, databases, and custom Python functions to perform real-world tasks.

## Topics Covered

- Creating custom tools
- Using `@tool` decorator
- `StructuredTool`
- Tool calling with LLMs
- Binding tools using `bind_tools()`
- Executing tool calls
- Built-in LangChain tools
- Search tools (e.g., DuckDuckGo)
- Custom function tools

## Technologies Used

- Python
- LangChain
- LangChain Core
- LangChain Community
- Pydantic
- Google Gemini (or any tool-calling compatible LLM)

## Learning Objectives

- Understand what tools are in LangChain.
- Build custom tools with input validation.
- Enable LLMs to invoke tools automatically.
- Process and execute tool calls.
- Integrate external capabilities into AI applications.

## Prerequisites

Install the required dependencies:

```bash
pip install -U langchain langchain-core langchain-community pydantic
```

For search tools:

```bash
pip install -U ddgs
```

## References

- LangChain Documentation: https://python.langchain.com/
- LangChain GitHub: https://github.com/langchain-ai/langchain

---

This folder is part of the **Generative AI Using LangChain** learning repository and serves as a hands-on guide to understanding and implementing LangChain tools in AI applications.