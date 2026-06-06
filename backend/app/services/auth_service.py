# backend/app/services/auth_service.py
from sqlalchemy.orm import Session

from app.services.user_service import (
    create_user,
    get_user_by_email
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def signup_user(
    db: Session,
    name: str,
    email: str,
    password: str
):

    existing_user = get_user_by_email(
        db,
        email
    )

    if existing_user:

        raise Exception(
            "Email already registered"
        )

    hashed_password = hash_password(
        password
    )

    user = create_user(
        db=db,
        name=name,
        email=email,
        password=hashed_password
    )

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:

        return None

    if not verify_password(
        password,
        user.password
    ):

        return None

    return user


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = authenticate_user(
        db,
        email,
        password
    )

    if not user:

        raise Exception(
            "Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "name": user.name,
        "email": user.email
    }