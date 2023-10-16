"""
MessageEventHandler
"""
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage,
)

from apps.configuration import settings
from apps.libs.logger import logger


class MessageEventHandler:
    """MessageEventHandler"""

    def __init__(self):
        configuration = Configuration(access_token=settings.LINE_CHANNEL_ACCESS_TOKEN)
        async_api_client = AsyncApiClient(configuration)
        self.line_bot_api = AsyncMessagingApi(async_api_client)

    async def receive_message(self, event: MessageEvent) -> None:
        """

        :param event:
        :return:
        """
        if not isinstance(event.message, TextMessageContent):
            logger.warning(f"Message is not text message! event: {event}")
            return
        await self.line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

