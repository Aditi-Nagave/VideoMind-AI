# backend/app/api/routes/summary.py
from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.models.user_model import User

from app.core.database import get_db

from app.schemas.summary_schema import (
    SummaryRequest
)

from app.services.summarization_service import (
    summarize,
    generate_title
)

from app.services.summary_db_service import (
    create_summary
)

router = APIRouter(
    prefix="/api",
    tags=["Summary"]
)


@router.post("/summary")
async def generate_summary(

    request: SummaryRequest,

    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    try:

        summary = summarize(
            request.transcript
        )

        # SAVE SUMMARY

        create_summary(
            db=db,
            video_id=request.video_id,
            summary_text=summary
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
    request: SummaryRequest,
    current_user: User = Depends(get_current_user)
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

