from logging import StreamHandler
import json


class JsonStreamHandler(StreamHandler):
    """
    This Customized StreamHandler will wrapped <string> message with double quotes, to inject into JSON format correctly
    For example, for a json wrapped formatter:
        {"time": "%(asctime)s", "msg": ${message}}
    With actions if logged with <list>, <dict> and <tuple>
        logger.info("some message")
        logger.info({"somekey": "somevalue"})
    """

    def __init__(self, *args):
        super().__init__(*args)

    def emit(self, record):
        """
        :param record: logging.LogRecord object
        Decorated message, and emit parent StreamHandler.emit function
        """
        if isinstance(record.msg, (list, dict, tuple)):
            record.msg = json.dumps(record.msg)
        if isinstance(record.msg, set):
            record.msg = json.dumps(list(record.msg))

        super().emit(record)
