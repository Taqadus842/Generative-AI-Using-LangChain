# LangChain Output Parser

This folder contains examples of different **LangChain Output Parsers** used to control and structure LLM responses.

Output parsers help convert raw LLM responses into a predictable format such as strings, JSON objects, or validated Python objects.

## Types Covered

### 1. String Output Parser

String output parser is used when you want the LLM response as plain text.

**Use when:**
- You need a simple text response.
- No structured format or validation is required.
- Example use cases:
  - Summaries
  - Explanations
  - General Q&A

---

### 2. JSON Output Parser

JSON output parser converts LLM responses into a JSON format with predefined fields.

**Use when:**
- You need structured data from the model.
- You want key-value pairs in the output.
- You need to pass LLM output to another application or API.

Example use cases:
- Extracting information
- Generating structured responses
- Building automation workflows

---

### 3. Pydantic Output Parser

Pydantic output parser uses Python Pydantic models to define and validate the expected output structure.

**Use when:**
- You need strict schema validation.
- Your application requires reliable structured responses.
- You want type-safe outputs.

Example use cases:
- Production AI applications
- API response generation
- Agent workflows
- RAG pipelines

---

## Parser Selection Guide

| Parser | Use When |
|--------|----------|
| String Output Parser | Need plain text response |
| JSON Output Parser | Need flexible JSON structure |
| Pydantic Output Parser | Need validated and type-safe structured output |

---

## Key Concepts Practiced

- Creating output schemas
- Formatting prompts with parser instructions
- Parsing LLM responses
- Handling structured outputs
- Using parsers with LangChain Expression Language (LCEL)

---

## Requirements

Install dependencies:

```bash
pip install langchain langchain-core langchain-huggingface python-dotenv pydantic