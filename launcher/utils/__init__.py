from .common import FASTERINIT
from .paths import UPDATER_CONFIG
from .log import logger

import json


def getVersion() -> str:
    with open(UPDATER_CONFIG, "r", encoding="utf-8") as f:
        ucfg = json.load(f)
    return ucfg.get("version")

VERSION = getVersion()

logger.info("utils 初始化")