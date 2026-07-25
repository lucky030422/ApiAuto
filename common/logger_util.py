import logging
from pathlib import Path
from common.base_path import BASE_DIR

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "interface.log"

logger=logging.getLogger("interface")

logger.setLevel(logging.INFO)

console_handler=logging.StreamHandler()

console_handler.setLevel(logging.INFO)

file_handler=logging.FileHandler(LOG_FILE,encoding="utf-8")
file_handler.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s | %(message)s")
file_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

class LoggerUtil:

    @staticmethod
    def info(msg):
        logger.info(msg)

    @staticmethod
    def error(msg):
        logger.error(msg)

    @staticmethod
    def warning(msg):
        logger.warning(msg)
