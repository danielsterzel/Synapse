from __future__ import annotations

from typing import Literal, Annotated
from enum import Enum

from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer

import jwt
from jwt.exceptions import InvalidTokenError

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession


from pydantic import BaseModel
from datetime import datetime, timedelta

from backend.app.models.user import User
from backend.app.core.database import get_db
from backend.app.core.security.authenticate.config import (
    PRIVATE_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
    PUBLIC_KEY,
)
from backend.app.core.security.security import PasswordHasher
from backend.app.schemas.auth_schemas import (
    AuthResponse,
    UserSchema,
    AuthTokenContainer,
)

"""
    BEGIN ---data structs---
"""


class TokenType(str, Enum):
    ACCESS_TOKEN = "access"
    REFRESH_TOKEN = "refresh"


class TokenPayload(BaseModel):

    sub: str
    type: TokenType
    exp: datetime


class AuthToken(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"


"""
   END ---data structs---
"""


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


class AuthUtils:

    @staticmethod
    def _create_token(payload: TokenPayload) -> str:
        return jwt.encode(
            payload=payload.model_dump(), key=PRIVATE_KEY, algorithm=ALGORITHM
        )

    @staticmethod
    def create_access_token(
        subject: str, expires_delta: timedelta | None = None
    ) -> str:

        expire = (
            datetime.now() + expires_delta
            if expires_delta
            else datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )

        payload = TokenPayload(sub=subject, type=TokenType.ACCESS_TOKEN, exp=expire)

        return AuthUtils._create_token(payload)

    @staticmethod
    def create_refresh_token(
        subject: str, expires_delta: timedelta | None = None
    ) -> str:

        expire = (
            datetime.now() + expires_delta
            if expires_delta
            else datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        )

        payload = TokenPayload(sub=subject, type=TokenType.REFRESH_TOKEN, exp=expire)

        return AuthUtils._create_token(payload)


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate user credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
user_missing_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No user with given id exists in the database",
    headers={"WWW-Authenticate": "Bearer"},
)


async def authenticate_user(login: str, input_password: str, db: AsyncSession):
    stmt = select(User).where(or_(User.username == login, User.email == login))

    result = await db.execute(stmt)

    user: User = result.scalar_one_or_none()

    if not user:
        raise user_missing_exception

    verified = PasswordHasher.verify_(input_password, user.hashed_password)

    if not verified:
        raise credentials_exception

    return user


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:

    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        token_data = TokenPayload(**payload)

    except InvalidTokenError:
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == token_data.sub))

    user = result.scalar_one_or_none()

    if user is None:
        raise user_missing_exception

    return user


def create_auth_response(
    user: User, msg: str = "Authentication successful"
) -> AuthResponse:

    str_user_id = str(user.id)

    access_token = AuthUtils.create_access_token(str_user_id)

    refresh_token = AuthUtils.create_refresh_token(str_user_id)

    schema = UserSchema.model_validate(user)

    return AuthResponse(
        message=msg,
        user=schema,
        success=True,
        tokens=AuthTokenContainer(
            access_token=access_token, refresh_token=refresh_token
        ),
    )
