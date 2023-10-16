"""
AioRedis
"""
from redis.asyncio import Redis, from_url

from apps.configuration import settings


class RedisPool:
    """RedisPool"""
    def __init__(self):
        if settings.REDIS_SSL:
            self._uri = f"rediss://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}"
        else:
            self._uri = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}"
        self._redis = None

    def create(self) -> Redis:
        """

        :return:
        """
        if self._redis:
            return self._redis
        session = from_url(
            url=self._uri,
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DB,
            encoding="utf-8"
        )
        self._redis = session
        return session
