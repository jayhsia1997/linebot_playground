"""
Demo router
"""
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from apps.containers import Container
from apps.handlers import DemoHandler
from apps.routing import LogRouting

router = APIRouter(route_class=LogRouting)


@router.get(
    path="/"
)
@inject
async def demo(
    demo_handler: DemoHandler = Depends(Provide[Container.demo_handler])
):
    """

    :param demo_handler:
    :return:
    """
    return await demo_handler.get()
