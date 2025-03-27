# Note：不要导入其他模块
from pathlib import Path



# class UnchangablePaths(Enum):
    
#     """不可变路径枚举
#     保存了一些不可变的路径，用于在程序中引用
    
#     类方法:
    
#     `UnchangablePaths.get(name: str)` 获得枚举对象
    
#     `UnchangablePaths.path(name: str)` 获取对应的路径
#     """
    
#     # 基础路径
#     CWD = Path.cwd()
#     HOME = Path.home()
    
#     # 资源路径
#     ASSETS = CWD / 'assets' / 'launcher'
    
#     # 子资源路径
#     CONFIGS = ASSETS / 'configs'
#     IMAGES = ASSETS / 'images'
#     FONTS = ASSETS / 'fonts'
#     LOGS = ASSETS / 'logs'
#     QSS = ASSETS / 'qss'
    
#     # 特定配置文件路径
#     LAUNCHER_CFG = CONFIGS / 'launcher.json'
#     UPDATER_CFG = CONFIGS / 'updater.json'
#     PROJECT_TOML = CONFIGS / 'project.toml'
#     PROJECT_YAML = CWD / 'conf.yaml'
    
#     @classmethod
#     def get(cls, name: str) -> 'UnchangablePaths':
#         """通过给定 `name: str` 获取对应的枚举对象"""
#         return cls.__dict__.get(name.upper())
    
#     @classmethod
#     def path(cls, name: str) -> Path:
#         """通过给定 `name: str` 获取对应的 `Path` 对象"""
#         return cls.get(name).value
    
#     @classmethod
#     def list(cls) -> list[str]:
#         """获取所有路径名称"""
#         all_ = list(cls.__dict__.keys())
#         return [name for name in all_ if name.isupper()]

# 2025/3/12 Note: 由于 `UnchangablePaths` 仅用于保存路径，因此不再需要枚举类，直接使用类属性即可


class UnchangeablePaths:
    
    """不可变路径
    保存了一些不可变的路径，用于在程序中引用
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
    UPDATER_CFG = CONFIGS / 'updater.json'
    PROJECT_TOML = CONFIGS / 'project.toml'
    PROJECT_YAML = CWD / 'conf.yaml'
    
    @classmethod
    def get(cls, name: str) -> Path:
        """通过给定 `name: str` 获取对应的路径"""
        return getattr(cls, name.upper()) if hasattr(cls, name.upper()) else None
    
    @classmethod
    def list(cls) -> list[str]:
        """获取所有路径名称"""
        all_ = list(cls.__dict__.keys())
        return [name for name in all_ if name.isupper()]



# 单测
if __name__ == "__main__":
    
    print(UnchangeablePaths.CWD)
    print(UnchangeablePaths.HOME)
    print(UnchangeablePaths.list())