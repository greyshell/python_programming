#!/usr/bin/env python3

# demo the use of logger for large application

import logging


def make_logger():
    logger_ = logging.getLogger()
    # set the default thresold to minimum
    logger_.setLevel(logging.DEBUG)
    # set the default formatter
    default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(default_formatter)
    logger_.addHandler(console_handler)

    # create file handler with a higher log level
    file_handler = logging.FileHandler(filename="log.txt", mode="w")
    file_handler.setLevel(logging.ERROR)
    file_handler_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)s - %(message)s')
    file_handler.setFormatter(file_handler_formatter)
    logger_.addHandler(file_handler)

    return logger_


# global variable: logger obj can be accessible from any method
logger = make_logger()

if __name__ == '__main__':
    # pattern 1
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
