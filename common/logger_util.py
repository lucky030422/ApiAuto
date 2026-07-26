import logging
from pathlib import Path
from common.base_path import BASE_DIR

# ============================================================
# 日志配置
# 日志文件统一存储在 logs/ 目录下
# 同时输出到控制台和文件，便于调试和追溯
# ============================================================

# 确保日志目录存在
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 日志文件路径
LOG_FILE = LOG_DIR / "interface.log"

# 创建日志记录器
logger = logging.getLogger("interface")
logger.setLevel(logging.INFO)

# 控制台处理器：日志输出到终端
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 文件处理器：日志写入文件（UTF-8 编码支持中文）
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setLevel(logging.INFO)

# 日志格式：时间 | 级别 | 文件名 | 消息
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s | %(message)s")
file_handler.setFormatter(formatter)

# 避免重复添加处理器（模块重载时保护）
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


class LoggerUtil:
    """日志工具类，提供 info/error/warning 三个级别的静态日志方法"""

    @staticmethod
    def info(msg):
        logger.info(msg)

    @staticmethod
    def error(msg):
        logger.error(msg)

    @staticmethod
    def warning(msg):
        logger.warning(msg)
