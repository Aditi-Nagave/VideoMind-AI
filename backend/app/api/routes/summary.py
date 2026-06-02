# app/api/routes/summary.py
from fastapi import APIRouter, HTTPException

from app.schemas.summary_schema import SummaryRequest
from app.services.summarization_service import (
    summarize,
    generate_title
)

router = APIRouter(
    prefix="/api",
    tags=["Summary"]
)


@router.post("/summary")
async def generate_summary(
    request: SummaryRequest
):

    try:

        summary = summarize(
            request.transcript
        )

        return {
            "summary": summary
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/title")
async def create_title(
    request: SummaryRequest
):

    try:

        title = generate_title(
            request.transcript
        )

        return {
            "title": title
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
