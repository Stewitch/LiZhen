from loguru import logger



logger.remove()

timefmt = "%Y-%m-%d %H:%M:%S"
logfmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"



# 作为主程序模块导入时
if __name__ == "utils.log":
    from .path import UnchangablePaths
    from .stream import stderr
    logger.add(
        UnchangablePaths.path("LOGS") / "launcher.log",
        rotation="00:00",
        format=logfmt,
        level="DEBUG",
        enqueue=True,
        retention="3 days"
    )
    logger.add(
        stderr,
        format=logfmt,
        level="DEBUG",
        colorize=True,
        enqueue=True
    )

# 作为同级模块导入时
if __name__ == "log":
    pass

# 单测
if __name__ == "__main__":
    import sys
    logger.add(sys.stderr, format=logfmt, level="DEBUG", colorize=True)
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")