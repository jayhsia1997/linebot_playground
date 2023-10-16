"""
UserEventHandler
"""
from linebot.v3.webhooks import FollowEvent, UnfollowEvent
from redis.asyncio import Redis

from apps.libs.database.aio_redis import RedisPool
from apps.configuration import settings


class UserEventHandler:
    """UserEventHandler"""

    def __init__(self, redis: RedisPool):
        self.redis: Redis = redis.create()

    @staticmethod
    def cache_key(user_id: str) -> str:
        """

        :param user_id:
        :return:
        """
        return f"linebot:user:{user_id}"

    async def on_follow(self, event: FollowEvent) -> None:
        """

        :param event:
        :return:
        """
        key = self.cache_key(user_id=event.source.user_id)
        source = event.to_json()
        await self.redis.set(name=key, value=source)

    async def on_unfollow(self, event: UnfollowEvent) -> None:
        """

        :param event:
        :return:
        """
        key = self.cache_key(user_id=event.source.user_id)
        await self.redis.delete(key)
