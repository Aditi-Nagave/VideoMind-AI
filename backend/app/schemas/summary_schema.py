from pydantic import BaseModel

class SummaryRequest(BaseModel):
    video_id: int | None = None
    transcript: str