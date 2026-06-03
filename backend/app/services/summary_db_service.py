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

