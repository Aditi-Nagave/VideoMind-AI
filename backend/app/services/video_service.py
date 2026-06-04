# backend/app/services/video_service.py
from app.models.video_model import Video


def create_video(
    db,
    title,
    file_path=None,
    youtube_url=None,
    user_id=1
):

    video = Video(
        title=title,
        file_path=file_path,
        youtube_url=youtube_url,
        user_id=user_id
    )

    db.add(video)

    db.commit()

    db.refresh(video)

    return video

