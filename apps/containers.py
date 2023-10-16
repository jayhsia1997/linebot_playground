"""Containers module."""
from dependency_injector import containers, providers

from apps.handlers import (
    DemoHandler,
    MessageEventHandler,
    UserEventHandler,
)
from apps.libs.database.aio_redis import RedisPool


class Container(containers.DeclarativeContainer):
    """Container"""

    wiring_config = containers.WiringConfiguration(
        modules=[],
        packages=[
            "apps.handlers",
            "apps.routers"
        ],
    )

    # [database]
    redis_pool = providers.Resource(RedisPool)

    # handlers
    demo_handler = providers.Factory(DemoHandler)
    message_event_handler = providers.Factory(MessageEventHandler)
    user_event_handler = providers.Factory(
        UserEventHandler,
        redis=redis_pool
    )
