from fastapi import FastAPI

from app.api.routes.upload import router as upload_router
from app.api.routes.summary import router as summary_router
from app.api.routes.chat import router as chat_router
from app.api.routes.extraction import router as extraction_router
from app.api.routes.auth import router as auth_router

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