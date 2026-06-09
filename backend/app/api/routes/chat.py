# backend/app/api/routes/chat.py

from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.models.user_model import User

from app.core.database import get_db

from app.schemas.chat_schema import (
    ChatRequest
)

from app.services.chat_memory_service import (
    get_chat_history,
    format_chat_history
)

from app.services.rag_service import (
    build_rag_chain,
    ask_question
)

from app.services.chat_db_service import (
    create_chat
)

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post("/chat")
async def chat_with_video(

    request: ChatRequest,

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(
        get_db
    )
):

    try:

        # =========================
        # LOAD PREVIOUS CHATS
        # =========================

        previous_chats = get_chat_history(
            db,
            request.video_id
        )

        history = format_chat_history(
            previous_chats
        )

        # =========================
        # BUILD CONVERSATIONAL RAG
        # =========================

        rag_chain = build_rag_chain(
            request.transcript,
            request.video_id,
            history
        )

        # =========================
        # ASK QUESTION
        # =========================

        answer = ask_question(
            rag_chain,
            request.question
        )

        # =========================
        # SAVE CHAT
        # =========================

        create_chat(
            db=db,
            video_id=request.video_id,
            question=request.question,
            answer=answer
        )

        return {

            "question":
            request.question,

            "answer":
            answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get(
    "/chat/history/{video_id}"
)
def get_history(
    video_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    chats = get_chat_history(
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