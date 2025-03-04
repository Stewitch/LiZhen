# Note：不要导入其他模块
from pathlib import Path
from enum import Enum



class UnchangablePaths(Enum):
    
    """不可变路径枚举
    保存了一些不可变的路径，用于在程序中引用
    
    类方法:
    
    `UnchangablePaths.get(name: str)` 获得枚举对象
    
    `UnchangablePaths.path(name: str)` 获取对应的路径
    """
    
    # 基础路径
    CWD = Path.cwd()
    HOME = Path.home()
    
    # 资源路径
    ASSETS = CWD / 'assets' / 'launcher'
    
    # 子资源路径
    CONFIGS = ASSETS / 'configs'
    IMAGES = ASSETS / 'images'
    FONTS = ASSETS / 'fonts'
    LOGS = ASSETS / 'logs'
    QSS = ASSETS / 'qss'
    
    # 特定配置文件路径
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
    


# 测试
if __name__ == "__main__":
    print(UnchangablePaths.CWD)
    print(UnchangablePaths.path('CWD'))