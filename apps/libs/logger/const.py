import logging

DEFAULT_LOG_LEVEL = logging.DEBUG

MAP_ENV_LEVEL = {
    'dev': logging.DEBUG,
    'DEV': logging.DEBUG,
    'stg': logging.INFO,
    'STG': logging.INFO,
    'prod': logging.INFO,
    'PROD': logging.INFO,
}

DEFAULT_FORMAT = "[%(asctime)s] %(name)s %(levelname)-8s %(message)s"
DEFAULT_FORMAT_DATE = "%Y-%m-%dT%H:%M:%S%z"  # ISO8601
