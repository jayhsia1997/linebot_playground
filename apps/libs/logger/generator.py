import logging
import sys
from .json_stream_handler import JsonStreamHandler
from .const import (
    DEFAULT_LOG_LEVEL,
    MAP_ENV_LEVEL,
    DEFAULT_FORMAT,
    DEFAULT_FORMAT_DATE
)


class LoggerGenerator:
    def __init__(self, logger_name):
        self.logger_name = logger_name
        self.formatter = logging.Formatter(
            DEFAULT_FORMAT,
            datefmt=DEFAULT_FORMAT_DATE
        )
        self.log_level = DEFAULT_LOG_LEVEL
        self.handlers = []

    class __LogLevelFilter(logging.Filter):
        def __init__(self, levels: tuple):
            super().__init__()
            self.target_levels = levels

        def filter(self, rec):
            return rec.levelno in self.target_levels

    def with_log_level_by_env(self, env):
        if env in MAP_ENV_LEVEL.keys():
            self.log_level = MAP_ENV_LEVEL[env]
        else:
            self.log_level = logging.INFO
        return self

    def with_json_handler(self):
        handler = JsonStreamHandler()
        handler.setLevel(self.log_level)
        handler.setFormatter(self.formatter)
        self.handlers.append(handler)
        return self

    def with_stdout_handler(self):
        handler = logging.StreamHandler()
        handler.setLevel(self.log_level)
        handler.setFormatter(self.formatter)
        self.handlers.append(handler)
        return self

    def split_stream_handlers_on_level(self, log_level=logging.INFO):
        """
        :param log_level
        Redirect STDOUT: all levels <= log_level
        Redirect STDERR: all levels > log_level
        """
        stdout_levels = tuple(level for level in logging._levelToName if level <= log_level)
        stderr_levels = tuple(level for level in logging._levelToName if level > log_level)

        for handler in [handler for handler in self.handlers if isinstance(handler, logging.StreamHandler)]:
            stdout_handler = JsonStreamHandler(sys.stdout) if isinstance(handler, JsonStreamHandler) else logging.StreamHandler(sys.stdout)
            stdout_handler.setLevel(handler.level)
            stdout_handler.setFormatter(handler.formatter)
            stdout_handler.addFilter(self.__LogLevelFilter(stdout_levels))
            self.handlers.append(stdout_handler)

            handler.addFilter(self.__LogLevelFilter(stderr_levels))
        return self

    def get(self):
        logger = logging.getLogger(self.logger_name)

        logger.handlers.clear()  # To sure there is no duplicate logger in the same logger_name
        logger.addHandler(logging.NullHandler())

        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.log_level)

        for handler in self.handlers:
            logger.addHandler(handler)

        return logger
