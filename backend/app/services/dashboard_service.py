from app.models.video_model import Video
from app.models.summary_model import Summary
from app.models.chat_model import Chat


def get_dashboard_stats(
    db,
    user_id
):

    total_videos = (
        db.query(Video)
        .filter(
            Video.user_id == user_id
        )
        .count()
    )

    video_ids = [
        video.id
        for video in db.query(Video)
        .filter(
            Video.user_id == user_id
        )
        .all()
    ]

    total_summaries = (
        db.query(Summary)
        .filter(
            Summary.video_id.in_(video_ids)
        )
        .count()
    )

    total_chats = (
        db.query(Chat)
        .filter(
            Chat.video_id.in_(video_ids)
        )
        .count()
    )

    total_questions = total_chats

    return {
        "total_videos": total_videos,
        "total_summaries": total_summaries,
        "total_questions": total_questions,
        "total_chats": total_chats
    }