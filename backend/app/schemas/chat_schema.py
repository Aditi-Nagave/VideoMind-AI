from pydantic import BaseModel

class ChatRequest(BaseModel):
    transcript: str
    question: str