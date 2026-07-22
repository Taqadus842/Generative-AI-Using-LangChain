from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all cons inside a list"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """
    I recently bought this laptop and overall I am very happy with it. 
    The performance is excellent, the battery lasts long, and the display quality is amazing.
    However, the laptop is slightly expensive and the speakers are not very loud.
    The build quality feels premium and delivery was also very fast.
    """
)

print(result)