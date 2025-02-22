from pathlib import Path
from enum import Enum



class UnchangablePaths(Enum):
    
    CWD = Path.cwd()
    HOME = Path.home()
    
    ASSETS = CWD / 'assets' / 'launcher'
    
    CONFIGS = ASSETS / 'configs'
    IMAGES = ASSETS / 'images'
    FONTS = ASSETS / 'fonts'
    LOGS = ASSETS / 'logs'
    QSS = ASSETS / 'qss'
    
    LAUNCHER_CFG = CONFIGS / 'launcher.json'
    PROJECT_CFG = CWD / 'conf.yaml'
    
    
    @classmethod
    def get(cls, name: str) -> 'UnchangablePaths':
        """通过给定 `name: str` 获取对应的枚举对象"""
        return cls.__dict__.get(name.upper())
    
    @classmethod
    def path(cls, name: str) -> Path:
        """通过给定 `name: str` 获取对应的 `Path` 对象"""
        return cls.get(name).value
    


if __name__ == "__main__":
    print(UnchangablePaths.CWD)
    print(UnchangablePaths.path('CWD'))