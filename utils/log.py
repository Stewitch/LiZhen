# Copyright (c) Stewitch
# SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-only
# Source from: https://github.com/Stewitch/XinYuan
# 在本项目中自动适用 GPLv3，单独使用时可选 Apache-2.0

from loguru import logger



logger.remove()

timefmt = "%Y-%m-%d %H:%M:%S"
logfmt = "<green>{time:"+ timefmt +"}</green> |[<level>{level}</level>]| <cyan>{name} | line: {line}</cyan> | <level>{message}</level>"



# 作为主程序模块导入时
if __name__ == "utils.log":
    
    from .path import UnchangeablePaths as UP
    from .stream import stderr
    
    logger.add(
        UP.LOGS / "launcher.log",
        mode="a",
        encoding="utf-8",
        rotation="00:00",
        format=logfmt,
        level="DEBUG",
        enqueue=True,
        retention="3 days"
    )
    
    consoleHandler = logger.add(
        stderr,
        format=logfmt,
        level="DEBUG",
        colorize=True,
        enqueue=True
    )
    
    def switchConsoleLogLevel(level: str) -> int:
        
        """切换控制台日志等级"""
        
        global consoleHandler
        
        logger.remove(consoleHandler)
        
        consoleHandler = logger.add(
            stderr,
            format=logfmt,
            level=level,
            colorize=True,
            enqueue=True
        )


# 作为同级模块导入时
if __name__ == "log":
    
    import sys
    
    logger.add(sys.stderr, format=logfmt, level="DEBUG", colorize=True)


# 单测
if __name__ == "__main__":
    
    import sys
    
    logger.add(sys.stderr, format=logfmt, level="DEBUG", colorize=True)
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")