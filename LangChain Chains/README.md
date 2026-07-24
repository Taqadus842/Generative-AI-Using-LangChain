# LangChain Chains

This folder contains implementations of different **LangChain Chain workflows** used in Generative AI applications.

## Concepts Covered

### Simple Chain
A basic pipeline where components execute step-by-step.

Flow: Prompt → LLM → Output Parser → Response


### Sequential Chain
Connects multiple chains where the output of one chain becomes the input of another.

Example: Generate Content → Summarize Content


### Parallel Chain
Runs multiple independent chains simultaneously using `RunnableParallel`.

Example:Generate Notes and Generate Quiz


### Conditional Chain
Uses conditions to decide which chain should execute using `RunnableBranch`.

Example:Input → Classification → Appropriate Chain


## Technologies Used

- Python
- LangChain
- LangChain Core
- Google Gemini API
- Output Parsers

## Learning Outcome

- Built reusable LangChain workflows
- Learned chain composition using LCEL (`|`)
- Implemented parallel and conditional execution
- Worked with prompts, LLMs, and output parsers

