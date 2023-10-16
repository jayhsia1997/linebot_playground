"""
Webhooks router for all webhook routers
"""
from fastapi import APIRouter

from apps.routing import LogRouting
from .line import router as line_router

webhook_router = APIRouter(route_class=LogRouting)

webhook_router.include_router(router=line_router, prefix="/line", tags=["Line Webhook"])

