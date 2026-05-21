from __future__ import annotations

from typing import Literal, Annotated

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    StringConstraints,
    field_validator,
)
from datetime import datetime
import re

Username = Annotated[
    str, StringConstraints(min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_]+$")
]


class LoginRequest(BaseModel):

    login: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=8, max_length=128)


class AuthTokenContainer(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"] = "bearer"


class AuthResponse(BaseModel):

    message: str = Field(max_length=200)
    user: UserSchema
    success: bool
    tokens: AuthTokenContainer


class RegisterRequest(BaseModel):
    email: EmailStr = Field(max_length=255)
    username: Username

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain lowercase letter")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*()-_=+\[\]{}|/,.<>?'\";:]", password):
            raise ValueError("Password must contain one special character")
        return password

    password: str = Field(min_length=8, max_length=128)


class UserSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(max_length=255)
    created_at: datetime
    is_active: bool = Field(default=True)
    oauth_accounts: list[OAuthUserSchema] = Field(default_factory=list)


class OAuthUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    provider: str = Field(max_length=50)
