# backend/app/api/routes/auth.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.get("/health")
def auth_health():

    return {
        "message": "Auth route working"
    }