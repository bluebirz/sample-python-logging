import logging

if __name__ == "__main__":
    logger = logging.getLogger("myLogger")
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("./sample_log.log")
    filehandler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
    )
    logger.addHandler(filehandler)

    logger.debug("this is a debug message.")
    logger.info("this is an info message.")
    logger.warning("this is a warning message.")
    logger.error("this is an error message.")
    logger.critical("this is a critical message.")
