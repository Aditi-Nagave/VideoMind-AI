# backend/app/api/routes/video.py
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.models.user_model import User
from app.models.video_model import Video

router = APIRouter(
    prefix="/api",
    tags=["Videos"]
)


@router.get("/videos")
def get_my_videos(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    videos = db.query(Video).filter(
        Video.user_id == current_user.id
    ).all()

    return [
        {
            "id": video.id,
            "title": video.title
        }
        for video in videos
    ]