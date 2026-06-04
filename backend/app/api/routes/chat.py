# backend/app/api/routes/chat.py
from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.chat_schema import (
    ChatRequest
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

    db: Session = Depends(get_db)
):

    try:

        rag_chain = build_rag_chain(
            request.transcript,
            request.video_id
        )

        answer = ask_question(
            rag_chain,
            request.question
        )

        # SAVE CHAT

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