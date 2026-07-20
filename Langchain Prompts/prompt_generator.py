from langchain_core.prompts import PromptTemplate
import json

template=PromptTemplate(
    template="""
You are an AI research assistant.

Summarize the following research paper:

Paper: {paper}

Summary length:
{length}

Summary style:
{style}

Include:
- Research problem
- Methodology
- Key contributions
- Results
- Impact
""",
    input_variables=[
        "paper",
        "length",
        "style"
    ],
    validate_template=True
)

with open("template.json", "w") as f:
    json.dump(template.dict(), f, indent=4)