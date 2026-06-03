
from app.core.database import engine, Base

from app.models.user_model import User
from app.models.video_model import Video
from app.models.transcript_model import Transcript
from app.models.summary_model import Summary
from app.models.chat_model import Chat

from fastapi import FastAPI

from app.api.routes.upload import router as upload_router
from app.api.routes.summary import router as summary_router
from app.api.routes.chat import router as chat_router
from app.api.routes.extraction import router as extraction_router
from app.api.routes.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VideoMind AI Backend"
)

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(chat_router)
app.include_router(extraction_router)
app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "message": "VideoMind AI Backend Running"
    }