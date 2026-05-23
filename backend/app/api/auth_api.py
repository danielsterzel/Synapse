"""TODO:
- Implement OAuth for Google and maybe GitHub
- Implement Email verification -[in progress]
- Implement password change
- [Optional] implement email change
- Implement refresh token exchange

"""

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from backend.app.services.auth_service import validate_user_credentials, create_auth_response
from backend.app.models.user import User
from backend.app.schemas.auth_schemas import (
    LoginRequest,
    AuthResponse,
    RegisterRequest,
)

from backend.app.core.database import get_db
import backend.app.services.user_service as user_service

router = APIRouter(prefix="auth", tags=["auth"])


@router.post("/login", response_model=AuthResponse)
async def login(
    data: LoginRequest, db: Annotated[AsyncSession, Depends(get_db)]
) -> AuthResponse:

    user: User = await validate_user_credentials(data.login, data.password, db)

    return create_auth_response(user, message="Login successful")


@router.post("/register", response_model=AuthResponse)
async def register(
    data: RegisterRequest, db: Annotated[AsyncSession, Depends(get_db)]
) -> AuthResponse:
    """Add user email validation via sending verification code"""

    existing = await db.execute(
        select(User).where(
            or_(User.username == data.username, User.email == data.email)
        )
    )

    existing = existing.scalar_one_or_none()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with given credentials already exists",
        )

    user: User = await user_service.create_user(
        db, data.username, data.email, data.password
    )

    return create_auth_response(user, message="Registration successful")
