import logging
import os
import uuid


def create_folder(filepath: str) -> None:
    # get folder name from filepath and create the folder if not exists
    folder_name = os.path.dirname(filepath)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def create_logger(logger_name: str, logger_filepath: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    # make logger to log in a file
    filehandler = logging.FileHandler(logger_filepath)
    filehandler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
    )
    logger.addHandler(filehandler)
    return logger


def inner(filename: str, text: str) -> None:
    create_folder(filename)
    logger: logging.Logger = create_logger(f"inner-{str(uuid.uuid4())}", filename)
    logger.debug(f"[inner] {text}")


def outer() -> None:
    logger: logging.Logger = create_logger("outer", "outer.log")
    messages: list[dict] = [
        {"filename": "msg1/inner.log", "text": "abc"},
        {"filename": "msg2/inner.log", "text": "def"},
    ]
    logger.debug("[outer] start")
    for message in messages:
        inner(filename=message["filename"], text=message["text"])
    logger.debug("[outer] done.")


if __name__ == "__main__":
    outer()
