# backend/app/api/routes/extraction.py
from fastapi import APIRouter, HTTPException

from app.schemas.summary_schema import SummaryRequest

from app.services.extraction_service import (
    extract_action_items,
    extract_key_decisions,
    extract_questions
)

router = APIRouter(
    prefix="/api/extract",
    tags=["Extraction"]
)


@router.post("/action-items")
async def action_items(
    request: SummaryRequest
):

    try:

        result = extract_action_items(
            request.transcript
        )

        return {
            "action_items": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/questions")
async def unresolved_questions(
    request: SummaryRequest
):

    try:

        result = extract_questions(
            request.transcript
        )

        return {
            "questions": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/decisions")
async def key_decisions(
    request: SummaryRequest
):

    try:

        result = extract_key_decisions(
            request.transcript
        )

        return {
            "decisions": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )