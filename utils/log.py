from loguru import logger

from .path import UnchangablePaths



logger.remove()

timefmt = "%Y-%m-%d %H:%M:%S"
logfmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"
logger.add(
    UnchangablePaths.path("LOGS") / "launcher.log",
    rotation="00:00",
    format=logfmt,
    level="DEBUG",
    enqueue=True,
    retention="3 days"
)