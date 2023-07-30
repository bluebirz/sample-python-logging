import logging

if __name__ == "__main__":
    logger = logging.getLogger("myLogger")
    logger.setLevel(logging.DEBUG)

    streamhandler = logging.StreamHandler()
    streamhandler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
    )
    logger.addHandler(streamhandler)

    logger.debug("this is a debug message.")
    logger.info("this is an info message.")
    logger.warning("this is a warning message.")
    logger.error("this is an error message.")
    logger.critical("this is a critical message.")
