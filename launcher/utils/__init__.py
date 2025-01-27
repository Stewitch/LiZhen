from .common import FASTERINIT
from .paths import UPDATER_CONFIG
from .log import logger

import json



with open(UPDATER_CONFIG, "r", encoding="utf-8") as f:
    ucfg = json.load(f)

VERSION = ucfg.get("version", "v0.5.0-Pre_release")

logger.info("utils 初始化")