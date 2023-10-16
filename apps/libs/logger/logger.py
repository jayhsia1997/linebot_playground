"""
Logger module
"""
import logging

from apps.configuration import settings
from .generator import LoggerGenerator


def get_logger(app_name: str, env: str) -> logging.Logger:
    """

    :param app_name:
    :param env:
    :return:
    """
    return (
        LoggerGenerator(app_name)
        .with_log_level_by_env(env)
        .with_json_handler()
        .split_stream_handlers_on_level(logging.INFO)
        .get()
    )


logger = get_logger(settings.APP_NAME, settings.ENV.upper())
