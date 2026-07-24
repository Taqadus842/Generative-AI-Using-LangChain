from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

parser = StrOutputParser()


# Sentiment classifier
sentiment_prompt = PromptTemplate(
    template="""
Classify this feedback as positive or negative.
Only return one word: positive or negative.

Feedback:
{feedback}
""",
    input_variables=["feedback"]
)


sentiment_chain = sentiment_prompt | model | parser


# Response chains
positive_chain = (
    PromptTemplate(
        template="Write a thank you message for this positive feedback:\n{feedback}",
        input_variables=["feedback"]
    )
    | model
    | parser
)


negative_chain = (
    PromptTemplate(
        template="Write an apology message for this negative feedback:\n{feedback}",
        input_variables=["feedback"]
    )
    | model
    | parser
)


# RunnableBranch
branch_chain = RunnableBranch(
    (
        lambda x: "positive" in x["sentiment"].lower(),
        positive_chain
    ),
    (
        lambda x: "negative" in x["sentiment"].lower(),
        negative_chain
    ),
    positive_chain   # default branch
)


# Combine sentiment + branch
final_chain = (
    {
        "sentiment": sentiment_chain,
        "feedback": lambda x: x["feedback"]
    }
    | branch_chain
)


result = final_chain.invoke({
    "feedback": "The phone quality is amazing and I love it!"
})


print(result)