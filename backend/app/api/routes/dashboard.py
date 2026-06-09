# backend/app/api/routes/dashboard.py
from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import (
    get_current_user
)

from app.models.user_model import User

from app.services.dashboard_service import (
    get_dashboard_stats
)

router = APIRouter(
    prefix="/api",
    tags=["Dashboard"]
)


@router.get("/dashboard")
def dashboard(

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(
        get_db
    )
):

    return get_dashboard_stats(
        db,
        current_user.id
    )