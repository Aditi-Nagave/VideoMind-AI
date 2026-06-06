# backend/app/services/transcript_service.py
from app.models.transcript_model import Transcript


def create_transcript(
    db,
    video_id,
    content
):

    transcript = Transcript(
        video_id=video_id,
        content=content
    )

    db.add(transcript)

    db.commit()

    db.refresh(transcript)

    return transcript

def get_transcript_by_video_id(
    db,
    video_id
):
    return (
        db.query(Transcript)
        .filter(
            Transcript.video_id == video_id
        )
        .first()
    )


def delete_transcript(
    db,
    video_id
):
    db.query(Transcript).filter(
        Transcript.video_id == video_id
    ).delete()

    db.commit()