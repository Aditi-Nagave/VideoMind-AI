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

