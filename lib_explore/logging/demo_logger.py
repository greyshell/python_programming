#!/usr/bin/env python3

# demo the use of logger for large application

import logging


def init_logger():
    mylogger = logging.getLogger()
    # set the default threshold to minimum
    mylogger.setLevel(logging.DEBUG)
    # set the default formatter
    default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(default_formatter)
    mylogger.addHandler(console_handler)

    # create file handler with a higher log level
    file_handler = logging.FileHandler(filename="log.txt", mode="w")  # overwrite the existing log
    file_handler.setLevel(logging.ERROR)
    file_handler_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)s - %(message)s')
    file_handler.setFormatter(file_handler_formatter)
    mylogger.addHandler(file_handler)

    return mylogger


# global variable: logger obj can be accessible from any method
logger = init_logger()

if __name__ == '__main__':
    # pattern 1
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
