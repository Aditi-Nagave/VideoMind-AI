from pydantic import BaseModel

class ChatRequest(BaseModel):
    video_id: int
    transcript: str
    question: str