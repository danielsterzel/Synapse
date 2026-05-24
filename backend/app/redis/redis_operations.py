from redis.asyncio import Redis
from redis.exceptions import RedisError
from backend.app.core.settings import settings

import logging

log = logging.getLogger(__name__)


class RedisStorageManager:

    redis_client = Redis.from_url(settings.redis_server_url)

    def __init__(self, prefix_arg):
        self.prefix: str = prefix_arg

    async def insert_into_redis_storage(
        self, key: str, value: str, expiration: int = None
    ) -> None:

        key_pattern = f"{self.prefix}:{key}"

        stored = await self.redis_client.set(
            key_pattern,
            value,
            ex=expiration,
        )
        if not stored:
            raise RedisError(f"Failed to SET {self.prefix} inside Redis cluster")

        log.info(f"Stored value: {value} for key: {key} --- {self.prefix} ")

    async def get_from_redis_storage(self, key: str) -> str | None:

        key = f"{self.prefix}:{key}"

        value = await self.redis_client.get(key)

        if value is None:
            return None

        return value.decode()

    async def remove_from_redis_storage(self, key: str) -> None:

        key = f"{self.prefix}:{key}"

        deleted = await self.redis_client.delete(key)

        if deleted != 1:
            raise ValueError(f"Deletion of key: {key} failed --- {self.prefix}")
        log.info(f"Removed: {key} --- prefix: {self.prefix}")

    async def acquire_lock(self, key: str, expiration: int) -> bool:

        key_pattern = f"{self.prefix}:{key}"
        acquired = await self.redis_client.set(
            key_pattern,
            "blocker",
            ex=expiration,
            nx=True
        )
        return bool(acquired)