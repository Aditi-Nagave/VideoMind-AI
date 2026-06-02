# app/api/routes/chat.py
from fastapi import APIRouter, HTTPException

from app.schemas.chat_schema import ChatRequest

from app.services.rag_service import (
    build_rag_chain,
    ask_question
)

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post("/chat")
async def chat_with_video(
    request: ChatRequest
):

    try:

        rag_chain = build_rag_chain(
            request.transcript
        )

        answer = ask_question(
            rag_chain,
            request.question
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )