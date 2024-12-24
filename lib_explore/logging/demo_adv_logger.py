import atexit
import json
import logging.config
import pathlib

logger = logging.getLogger("my_app")


def setup_logging():
    config_file = pathlib.Path("config.json")
    with open(config_file, "r") as f:
        config = json.load(f)

    logging.config.dictConfig(config)

    # start the thread
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


if __name__ == '__main__':
    setup_logging()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
    # try:
    #     1 / 0
    # # send exception to the logger
    # except ZeroDivisionError:
    #     logger.exception("exception message")
