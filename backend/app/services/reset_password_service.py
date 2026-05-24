from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models.user import User
from backend.app.services.user_service import get_user_by_email
from backend.app.core.security.password_hasher import PasswordHasher

import logging

log = logging.getLogger(__name__)


async def update_password(
    email: str, plain_new_password: str, db: AsyncSession
) -> None:

    user: User | None = await get_user_by_email(email, db)

    if not user:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No user with provided email: {email}",
        )

    hashed = PasswordHasher.hash(plain_new_password)

    user.hashed_password = hashed

    try:
        await db.commit()
    except Exception:
        log.exception(
            "Failed to update password in database. Rolling back password change"
        )
        await db.rollback()
        raise
