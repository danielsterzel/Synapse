import jwt

from enum import Enum
from typing import Literal

from pydantic import BaseModel
from datetime import timedelta, datetime


from backend.app.core.security.jwt_config import (
    PRIVATE_KEY,
    PUBLIC_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
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


"""
   END ---data structs---
"""


class JWTService:

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

        return JWTService._create_token(payload)

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

        return JWTService._create_token(payload)

    @staticmethod
    def decode_token(jwt_token: str) -> TokenPayload:

        payload = jwt.decode(jwt_token, key=PUBLIC_KEY, algorithms=[ALGORITHM])

        return TokenPayload(**payload)
