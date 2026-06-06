# backend/app/services/chat_db_service.py
from app.models.chat_model import Chat


def create_chat(
    db,
    video_id,
    question,
    answer
):

    chat = Chat(
        video_id=video_id,
        question=question,
        answer=answer
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat

def get_chats_by_video_id(
    db,
    video_id
):
    return (
        db.query(Chat)
        .filter(
            Chat.video_id == video_id
        )
        .all()
    )


def delete_chats(
    db,
    video_id
):
    db.query(Chat).filter(
        Chat.video_id == video_id
    ).delete()

    db.commit()