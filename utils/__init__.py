from .path import UnchangeablePaths as UP
from .log import logger

import json


    
def getVersion() -> str:
        
    """获取版本号"""
            
    with open(UP.path("UPDATER_CFG"), "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["version"]


CURRENT_VERSION = getVersion()
    
logger.info(f"当前版本号: {CURRENT_VERSION}")