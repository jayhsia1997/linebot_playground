"""
Base router for all routers
"""
from fastapi import APIRouter

from apps.routing import LogRouting
from .demo import router as demo_router
from .webhooks import webhook_router

base_router = APIRouter(route_class=LogRouting)

base_router.include_router(router=demo_router, prefix="/demo", tags=["Demo"])
base_router.include_router(router=webhook_router, prefix="/webhooks")

