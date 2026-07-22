from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all key themes discussed in the review in a list"
    )
    
    summary: str = Field(
        description="A brief summary of the review"
    )
    
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Return sentiment of the review either negative, positive or neutral"
    )
    
    pros: Optional[list[str]] = Field(
        description="Write down all pros inside a list"
    )
    
    cons: Optional[list[str]] = Field(
        description="Write down all cons inside a list"
    )
    
    name: Optional[str] = Field(
        description="Write name of reviewer"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """
    I recently bought this laptop and overall I am very happy with it.
    The performance is excellent, the battery lasts long, and the display quality is amazing.
    However, the laptop is slightly expensive and the speakers are not very loud.
    The build quality feels premium and delivery was also very fast.
    My name is Ahmed.
    """
)

print(result)