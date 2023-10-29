import logging, sys

from src.constants import Constants

def get_logger(name: str = None, level: str = Constants.log_level, is_stdout: bool = False):
    logging.Formatter.default_time_format = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s")

    logger = logging.getLogger(name)
    logger.setLevel(logging.getLevelName(level))
    if is_stdout:
        handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(handler)
    return logger
