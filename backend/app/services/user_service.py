from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.security.password_hasher import PasswordHasher
from backend.app.models.user import User

from datetime import datetime, timezone


async def create_user(
    db: AsyncSession,
    username: str,
    email: EmailStr,
    password: str,
) -> User:
    user = User(
        username=username,
        email=str(email),
        hashed_password=PasswordHasher.hash(password),
        created_at=datetime.now(timezone.utc),
        is_active=True,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
