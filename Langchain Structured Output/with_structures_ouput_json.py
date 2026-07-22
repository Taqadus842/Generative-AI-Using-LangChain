from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


review_schema = {
    "title": "Review",
    "description": "A structured review analysis",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all key themes discussed in the review in a list"
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": [
                "positive",
                "negative",
                "neutral"
            ],
            "description": "Return sentiment of the review either negative, positive or neutral"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all pros inside a list"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all cons inside a list"
        },
        "name": {
            "type": "string",
            "description": "Write name of reviewer"
        }
    },
    "required": [
        "key_themes",
        "summary",
        "sentiment",
        "pros",
        "cons",
        "name"
    ]
}


structured_model = model.with_structured_output(review_schema)


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