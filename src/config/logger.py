from datetime import time
from loguru import logger

LOG_FOLDER = "logs/"


def configure_logger(verbosity_level):
    """Configure the logger.

    Removes the default logger handler/format and adds a custom one.
    """
    verbosity_level = translate_verbosity_level(verbosity_level)
    logger.remove()
    logger.add(
        LOG_FOLDER + "{time}.log",
        format="{time:%Y-%m-%d %H:%M:%S} - {level} - {message}",
        rotation="500 MB",
    )


def translate_verbosity_level(level):
    """Translates the level of verbosity of the CLI to the expected level of the library

    Library default levels:
        NAME        CODE    CALL
        TRACE       5       logger.trace()
        DEBUG       10      logger.debug()
        INFO        20      logger.info()
        SUCCESS     25      logger.success()
        WARNING     30      logger.warning()
        ERROR       40      logger.error()
        CRITICAL    50      logger.critical()

    Args:
        level (int): CLI log level code. Number from 1 to 7
    Returns:
        string: library log level name.
    """
    if level > 5:
        level = 5

    levels = {"1": "WARNING", "2": "SUCCESS", "3": "INFO", "4": "DEBUG", "5": "TRACE"}
    return levels[str(level)]
