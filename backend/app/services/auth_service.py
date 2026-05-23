from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from backend.app.core.security.jwt import JWTService
from backend.app.models.user import User
from backend.app.core.security.password_hasher import PasswordHasher
from backend.app.core.exceptions.exceptions import (
    InvalidCredentialsException,
    UserNotFoundException,
)
from backend.app.schemas.auth_schemas import (
    AuthResponse,
    UserSchema,
    AuthTokenContainer,
)


async def validate_user_credentials(login: str, input_password: str, db: AsyncSession):
    stmt = select(User).where(or_(User.username == login, User.email == login))

    result = await db.execute(stmt)

    user: User = result.scalar_one_or_none()

    if not user:
        raise UserNotFoundException()

    verified = PasswordHasher.verify_password(input_password, user.hashed_password)

    if not verified:
        raise InvalidCredentialsException()

    return user


def create_auth_response(
    user: User, message: str = "Authentication successful"
) -> AuthResponse:

    str_user_id = str(user.id)

    access_token = JWTService.create_access_token(str_user_id)

    refresh_token = JWTService.create_refresh_token(str_user_id)

    schema = UserSchema.model_validate(user)

    return AuthResponse(
        message=message,
        user=schema,
        success=True,
        tokens=AuthTokenContainer(
            access_token=access_token, refresh_token=refresh_token
        ),
    )
