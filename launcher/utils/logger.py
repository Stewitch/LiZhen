from loguru import logger
from platform import system

from .stream import _stderr
from .paths import LAUNCHER_LOG



SYSTEM = system()



logger.remove()

timefmt = "%Y-%m-%d %H:%M:%S"
fmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"

logger.add(sink=LAUNCHER_LOG, rotation="10 MB", mode='w', retention="3 days", level="INFO", format=fmt, enqueue=True)
id_ = logger.add(sink=_stderr, level="DEBUG", format=fmt, colorize=True)

logger.info("日志系统初始化")