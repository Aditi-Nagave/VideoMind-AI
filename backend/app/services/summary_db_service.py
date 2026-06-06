# backend/app/services/summary_db_service.py
from app.models.summary_model import Summary


def create_summary(
    db,
    video_id,
    summary_text
):

    summary = Summary(
        video_id=video_id,
        summary=summary_text
    )

    db.add(summary)

    db.commit()

    db.refresh(summary)

    return summary

def get_summary_by_video_id(
    db,
    video_id
):
    return (
        db.query(Summary)
        .filter(
            Summary.video_id == video_id
        )
        .first()
    )


def delete_summary(
    db,
    video_id
):
    db.query(Summary).filter(
        Summary.video_id == video_id
    ).delete()

    db.commit()