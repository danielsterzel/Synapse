import uuid
from typing import Annotated

import hashlib
import logging
import secrets

import resend

from fastapi import HTTPException, status

from jinja2 import Environment, FileSystemLoader

from backend.app.core.settings import settings
from backend.app.redis.redis_operations import RedisStorageManager

logger = logging.getLogger(__name__)

""" Refactor so there is no code duplication """


class EmailService:

    DEFAULT_EXPIRATION: int = 1800
    RESEND_COOLDOWN: int = 60

    verification_storage = RedisStorageManager("email_verification")

    password_reset_storage = RedisStorageManager("password_reset")

    cooldown_storage = RedisStorageManager("user")

    resend.api_key = settings.resend_api_key

    env = Environment(loader=FileSystemLoader("../../../templates"))

    def __init__(
        self,
        expiration: Annotated[
            int,
            "Expiration is set in seconds",
        ] = DEFAULT_EXPIRATION,
    ):
        self.expiration = expiration

    @staticmethod
    def email_token_hasher(token: str) -> str:
        return hashlib.sha256(token.encode()).hexdigest()

    async def can_send_verification_email(
        self,
        user_id: uuid.UUID,
    ) -> bool:

        cooldown_key = f"{user_id}:email_verification:cooldown"

        allowed = await self.cooldown_storage.acquire_lock(
            cooldown_key,
            self.RESEND_COOLDOWN,
        )

        return bool(allowed)

    async def send_verification_email(
        self,
        user_id: uuid.UUID,
        user_email: str,
    ) -> None:

        if not await self.can_send_verification_email(user_id):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Cannot resend verification email at this moment",
            )

        token = secrets.token_urlsafe(32)

        hashed = self.email_token_hasher(token)

        try:

            await self.verification_storage.insert_into_redis_storage(
                key=hashed,
                value=str(user_id),
                expiration=self.expiration,
            )

            verification_url = (
                f"{settings.frontend_url}" f"/register-verify-email?token={token}"
            )

            template = self.env.get_template("verification_email.html")

            html = template.render(verification_url=verification_url)

            await resend.Emails.send_async(
                {
                    "from": "onboarding@resend.dev",
                    "to": user_email,
                    "subject": "Verify your email",
                    "html": html,
                }
            )

        except Exception:

            await self.verification_storage.remove_from_redis_storage(hashed)

            logger.exception(f"Failed to send verification email for user {user_id}")

            raise HTTPException(
                status_code=500,
                detail="Could not send verification email",
            )

        logger.info(f"Sent verification email to user:{user_id}")

    async def can_send_password_reset_email(
        self,
        user_id: uuid.UUID,
    ) -> bool:

        cooldown_key = f"{user_id}:password_reset:cooldown"

        allowed = await self.cooldown_storage.acquire_lock(
            cooldown_key,
            self.RESEND_COOLDOWN,
        )

        return bool(allowed)

    async def send_password_reset_email(
        self,
        user_id: uuid.UUID,
        user_email: str,
    ) -> None:

        token = secrets.token_urlsafe(32)

        hashed = self.email_token_hasher(token)

        try:

            await self.password_reset_storage.insert_into_redis_storage(
                key=hashed,
                value=str(user_id),
                expiration=self.expiration,
            )

            reset_url = f"{settings.frontend_url}" f"/reset-password?token={token}"

            template = self.env.get_template("password_reset_email.html")

            html = template.render(reset_url=reset_url)

            await resend.Emails.send_async(
                {
                    "from": "onboarding@resend.dev",
                    "to": user_email,
                    "subject": "Reset your password",
                    "html": html,
                }
            )

        except Exception:

            await self.password_reset_storage.remove_from_redis_storage(hashed)

            logger.exception(f"Failed to send password reset email for user {user_id}")

            raise HTTPException(
                status_code=500,
                detail="Could not send password reset email",
            )

        logger.info(f"Sent password reset email to user:{user_id}")
