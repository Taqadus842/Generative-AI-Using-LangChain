# LangChain Structured Output

This repository contains my learning and practice of **Structured Output in LangChain**.

Structured Output allows LLMs to return responses in a fixed format like JSON, Pydantic objects, or TypedDict instead of normal text. It helps make AI applications more reliable and easier to integrate.

## Concepts Covered

- Pydantic Structured Output
- TypedDict Structured Output
- JSON Schema Structured Output
- `with_structured_output()` in LangChain

## Methods

### Pydantic
Used for production applications where validation and correct data types are important.

### TypedDict
Used for simple structured responses when validation is not required.

### JSON Schema
Used when working with APIs and external systems that require JSON formats.

### with_structured_output()
LangChain method that converts LLM responses into the defined schema format.

## When to Use

- **Pydantic:** Production apps, APIs, data extraction, validation
- **TypedDict:** Learning, prototypes, simple outputs
- **JSON Schema:** API integration and system communication

## Technologies

- Python
- LangChain
- Google Gemini
- Pydantic
- JSON Schema

## Author

Ume Taqadus