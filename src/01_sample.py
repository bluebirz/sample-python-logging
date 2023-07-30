import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("myLogger")

    logger.debug("this is a debug message.")
    logger.info("this is an info message.")
    logger.warning("this is a warning message.")
    logger.error("this is an error message.")
    logger.critical("this is a critical message.")
