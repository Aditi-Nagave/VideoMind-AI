from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth_schema import (
    SignupRequest
)

from app.services.auth_service import (
    signup_user,
    login_user
)

from app.core.security import (
    get_current_user
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


# =========================
# SIGNUP
# =========================

@router.post("/signup")
def signup(

    request: SignupRequest,

    db: Session = Depends(get_db)
):

    try:

        user = signup_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password
        )

        return {
            "message": "User created successfully",
            "user_id": user.id,
            "name": user.name,
            "email": user.email
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# LOGIN
# =========================

@router.post("/login")
def login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)
):

    try:

        return login_user(
            db=db,
            email=form_data.username,
            password=form_data.password
        )

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )


# =========================
# CURRENT USER
# =========================

@router.get("/me")
def current_user(

    user=Depends(get_current_user)
):

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }