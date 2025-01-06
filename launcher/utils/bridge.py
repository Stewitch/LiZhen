from .paths import PROJ_SRC, PROJ_CFG

import sys
sys.path.append(str(PROJ_SRC.absolute()))

from open_llm_vtuber.config_manager.utils import read_yaml, validate_config



pcfg = validate_config(read_yaml(str(PROJ_CFG)))