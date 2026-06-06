# backend/app/api/routes/video.py
from fastapi import APIRouter, Depends , HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.models.user_model import User
from app.models.video_model import Video

from app.models.transcript_model import Transcript
from app.models.summary_model import Summary

from app.services.video_service import (
    get_video_by_id,
    delete_video
)

from app.services.transcript_service import (
    get_transcript_by_video_id,
    delete_transcript
)

from app.services.summary_db_service import (
    get_summary_by_video_id,
    delete_summary
)

from app.services.chat_db_service import (
    get_chats_by_video_id,
    delete_chats
)

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


@router.get("/videos/{video_id}")
def get_video_details(

    video_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    video = get_video_by_id(
        db,
        video_id
    )

    if not video:

        raise HTTPException(
            status_code=404,
            detail="Video not found"
        )

    transcript = get_transcript_by_video_id(
        db,
        video_id
    )

    summary = get_summary_by_video_id(
        db,
        video_id
    )

    return {

        "id": video.id,

        "title": video.title,

        "created_at":
        video.created_at,

        "transcript":
        transcript.content
        if transcript else "",

        "summary":
        summary.summary
        if summary else ""
    }


@router.get(
    "/videos/{video_id}/chats"
)
def get_chat_history(

    video_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    chats = get_chats_by_video_id(
        db,
        video_id
    )

    return [
        {
            "question": c.question,
            "answer": c.answer
        }
        for c in chats
    ]


@router.delete(
    "/videos/{video_id}"
)
def remove_video(

    video_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    delete_transcript(
        db,
        video_id
    )

    delete_summary(
        db,
        video_id
    )

    delete_chats(
        db,
        video_id
    )

    delete_video(
        db,
        video_id
    )

    return {
        "message":
        "Video deleted successfully"
    }

