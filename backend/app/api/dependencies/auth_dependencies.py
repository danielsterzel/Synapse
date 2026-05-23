from fastapi.security import OAuth2PasswordBearer

from typing import Annotated
from fastapi import Depends
from jwt import InvalidTokenError

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_db
from backend.app.core.exceptions.exceptions import InvalidCredentialsException, UserNotFoundException
from backend.app.core.security.jwt import JWTService
from backend.app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:

    try:
        token_data = JWTService.decode_token(token)

    except InvalidTokenError:
        raise InvalidCredentialsException()

    result = await db.execute(select(User).where(User.id == token_data.sub))

    user = result.scalar_one_or_none()

    if user is None:
        raise UserNotFoundException()

    return user
