from app.models.chat_model import Chat


def get_chat_history(
    db,
    video_id: int,
    limit: int = 10
):

    return (
        db.query(Chat)
        .filter(
            Chat.video_id == video_id
        )
        .order_by(Chat.id.asc())
        .limit(limit)
        .all()
    )


def format_chat_history(
    chats
):

    if not chats:

        return "No previous conversation."

    history = []

    for chat in chats:

        history.append(
            f"User: {chat.question}"
        )

        history.append(
            f"Assistant: {chat.answer}"
        )

    return "\n".join(history)