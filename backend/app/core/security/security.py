from __future__ import annotations

from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext

import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:

    return pwd_context.verify(plain, hashed)

class JWTUtils:

    @staticmethod
    def create_access_token():