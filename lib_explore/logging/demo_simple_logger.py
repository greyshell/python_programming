#!/usr/bin/env python3

# demo the use of logger for large application

import logging
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    filename="basic_log.txt",
    filemode="w",
    format=FORMAT
)


if __name__ == '__main__':
    # type(print(logging.INFO))
    # this is root logger
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
