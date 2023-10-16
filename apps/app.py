"""
FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.configuration import settings
from apps.containers import Container
from apps.routers import base_router
from apps.routing import LogRouting


def register_router(application: FastAPI) -> None:
    """
    register router
    :param application:
    :return:
    """
    application.include_router(base_router)


def register_middleware(application: FastAPI) -> None:
    """
    register middleware
    :param application:
    :return:
    """
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS if settings.CORS_ALLOWED_ORIGINS else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=settings.CORS_EXPOSE_HEADERS,
        allow_origin_regex=settings.CORS_ALLOW_ORIGINS_REGEX
    )


def get_application() -> FastAPI:
    """
    get application
    """
    application = FastAPI(title=settings.APP_NAME)
    # set route class
    application.router.route_class = LogRouting
    # set container
    container = Container()
    application.container = container

    register_middleware(application=application)
    register_router(application=application)

    return application


app = get_application()
