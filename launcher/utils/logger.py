from loguru import logger
from platform import system

from .stream import _stdout, _stderr
from .paths import LAUNCHER_LOG



SYSTEM = system()



logger.remove()

stdout_p = True

timefmt = "%Y-%m-%d %H:%M:%S"
fmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"

logger.add(sink=LAUNCHER_LOG, rotation="10 MB", mode='w', retention="3 days", level="INFO", format=fmt, enqueue=True)
id_ = logger.add(sink=_stdout, level="DEBUG", format=fmt, colorize=True)


def switchStream():
    global stdout_p, id_
    logger.remove(id_)
    if stdout_p:
        id_ = logger.add(sink=_stderr, level="DEBUG", format=fmt, colorize=True)
    else:
        id_ = logger.add(sink=_stdout, level="DEBUG", format=fmt, colorize=True)
    stdout_p = not stdout_p



logger.info("日志系统初始化")