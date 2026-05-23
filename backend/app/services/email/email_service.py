import uuid
from typing import Annotated

import resend

from redis.asyncio import Redis
from redis.exceptions import RedisError

from fastapi import HTTPException, status

from jinja2 import Environment, FileSystemLoader

from backend.app.core.settings import settings

import hashlib
import secrets

import logging

"""
Currently config is hardcoded -> migrate to json or yaml file that holds information such as:
 - Verify email frontend page url
 - redis ttl
 - Synapse email service? or using resend email service?
 
    etc.
"""

logger = logging.getLogger(__name__)


class EmailService:

    DEFAULT_EXPIRATION: int = 1800
    RESEND_COOLDOWN: int = 60

    resend.api_key = settings.resend_api_key

    redis_client = Redis.from_url(settings.redis_server_url)

    env = Environment(loader=FileSystemLoader("../../../templates"))

    def __init__(
        self,
        expiration: Annotated[int, "Expiration is set in seconds"] = DEFAULT_EXPIRATION,
    ):
        self.expiration = expiration

    @staticmethod
    def email_token_hasher(token: str):
        return hashlib.sha256(token.encode()).hexdigest()

    async def _insert_into_redis_storage(
        self, user_id: uuid.UUID, hashed_verification_token: str
    ) -> None:

        token_key = f"email_verification:{hashed_verification_token}"

        stored = await self.redis_client.set(
            token_key,
            str(user_id),
            ex=self.expiration,
        )
        if not stored:
            raise RedisError(
                "Failed to SET email verification token inside Redis cluster"
            )
        logger.info(f"Stored verification token for user: {user_id}")

    async def get_from_redis_storage(self, raw_token: str) -> uuid.UUID | None:

        hashed = self.email_token_hasher(raw_token)

        key = f"email_verification:" f"{hashed}"

        user_id = await self.redis_client.get(key)

        if user_id is None:
            return None

        return uuid.UUID(user_id.decode())

    async def remove_from_redis_storage(self, raw_token: str) -> None:

        hashed = self.email_token_hasher(raw_token)

        key = f"email_verification:" f"{hashed}"

        deleted = await self.redis_client.delete(key)

        if deleted != 1:
            raise ValueError("Verification token does not exist")
        logger.info(f"Removed verification token: {hashed}")

    async def can_send_verification_email(self, user_id: uuid.UUID) -> bool:
        """used in api endpoint"""

        cooldown_key = f"user:{user_id}:email_verification:cooldown"

        allowed = await self.redis_client.set(
            cooldown_key, "1", ex=self.RESEND_COOLDOWN, nx=True
        )

        return bool(allowed)

    async def send_verification_email(
        self, user_id: uuid.UUID, user_email: str
    ) -> None:

        if not await self.can_send_verification_email(user_id):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Cannot resend verification email at this moment",
            )

        token = secrets.token_urlsafe(32)
        hashed = self.email_token_hasher(token)

        try:

            await self._insert_into_redis_storage(user_id, hashed)

            verification_url = (
                f"{settings.frontend_url}/register-verify-email?token={token}"
            )

            template = self.env.get_template("verification_email.html")
            html = template.render(verification_url=verification_url)

            await resend.Emails.send_async(
                {
                    "from": "onboarding@resend.dev",
                    "to": user_email,
                    "subject": "Token verification",
                    "html": html,
                }
            )
        except Exception:
            await self.remove_from_redis_storage(token)

            logger.exception(f"Failed to send verification email for user {user_id}")

            raise HTTPException(
                status_code=500, detail="Could not send verification email"
            )

        logger.info(
            f"Sent verification email to user:{user_id} with email: {user_email}"
        )
