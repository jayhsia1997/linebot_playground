"""Line Router"""
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi import Request, HTTPException
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhook import WebhookParser
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    FollowEvent,
    UnfollowEvent,
)
from starlette import status

from apps.configuration import settings
from apps.containers import Container
from apps.handlers import MessageEventHandler, UserEventHandler

router = APIRouter()

parser = WebhookParser(channel_secret=settings.LINE_CHANNEL_SECRET)


@router.post(
    path="/callback",
    status_code=status.HTTP_202_ACCEPTED
)
@inject
async def handle_callback(
    request: Request,
    message_event_handler: MessageEventHandler = Depends(Provide[Container.message_event_handler]),
    user_event_handler: UserEventHandler = Depends(Provide[Container.user_event_handler])
):
    """

    :param request:
    :param message_event_handler:
    :param user_event_handler:
    :return:
    """
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if isinstance(event, FollowEvent):
            await user_event_handler.on_follow(event=event)
        elif isinstance(event, UnfollowEvent):
            await user_event_handler.on_unfollow(event=event)
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessageContent):
            await message_event_handler.receive_message(event=event)

    return {
        "detail": "ok"
    }
