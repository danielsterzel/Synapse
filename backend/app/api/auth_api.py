"""TODO:
- Implement OAuth for Google and maybe GitHub
- Implement password change
- [Optional] implement email change
- Implement refresh token exchange

"""

import logging

from typing import Annotated
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from backend.app.services.auth_service import (
    validate_user_credentials,
    create_auth_response,
)
from backend.app.models.user import User
from backend.app.schemas.auth_schemas import (
    LoginRequest,
    AuthResponse,
    RegisterRequest,
    EmailVerificationRequest,
    EmailAlreadyVerified,
    RegisterResponse,
)

from backend.app.core.database import get_db
import backend.app.services.user_service as user_service
from backend.app.services.email.email_service import EmailService

log = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=AuthResponse)
async def login(
    data: LoginRequest, db: Annotated[AsyncSession, Depends(get_db)]
) -> AuthResponse:

    user: User = await validate_user_credentials(data.login, data.password, db)

    return create_auth_response(user, message="Login successful")


@router.post("/register", response_model=RegisterResponse)
async def register(
    data: RegisterRequest,
    background_tasks: BackgroundTasks,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> RegisterResponse:
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

    email_service = EmailService()

    background_tasks.add_task(
        email_service.send_verification_email, user.id, user.email
    )

    return RegisterResponse(message="Registration successful. Verify email to proceed")


@router.post("/register/verify-email", response_model=AuthResponse | EmailAlreadyVerified)
async def verify_email(
    data: EmailVerificationRequest, db: Annotated[AsyncSession, Depends(get_db)]
) -> AuthResponse | EmailAlreadyVerified:

    plain_token = data.token

    email_service = EmailService()
    user_id = await email_service.get_from_redis_storage(plain_token)

    if user_id is None:

        log.warning("Dangling token without assigned user")

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Token is invalid"
        )
    user: User | None = await user_service.get_user_by_uuid(user_id, db)

    if not user:

        log.warning(
            "Could not find user via verification email token. Db returned None"
        )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not verify email no user with user ID: {user_id} exists.",
        )

    if user.is_email_verified:

        log.info(f"User {user.id} already verified email")

        return EmailAlreadyVerified(message="Email already verified")

    user.is_email_verified = True

    await db.commit()

    await email_service.remove_from_redis_storage(plain_token)

    return create_auth_response(
        user,
        message="Email verification successful",
    )