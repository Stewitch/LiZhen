from loguru import logger
from sys import stderr

from .paths import LAUNCHER_LOG

logger.remove()

timefmt = "%Y-%m-%d %H:%M:%S"
fmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"

logger.add(sink=LAUNCHER_LOG, rotation="10 MB", mode='w', retention="3 days", level="INFO", format=fmt, enqueue=True)
logger.add(sink=stderr, level="DEBUG", format=fmt)

logger.info("日志系统初始化")