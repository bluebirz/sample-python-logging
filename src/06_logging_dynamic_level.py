import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s [%(levelname)s]  %(message)s"
    )
    logger = logging.getLogger("myLogger")

    logger.log(logging.DEBUG, "this is a debug message.")
    logger.log(logging.INFO, "this is an info message.")
    logger.log(logging.WARNING, "this is a warning message.")
    logger.log(logging.ERROR, "this is an error message.")
    logger.log(logging.CRITICAL, "this is a critical message.")
