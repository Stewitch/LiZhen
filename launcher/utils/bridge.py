from copy import deepcopy

from .logger import logger

import json, ruamel.yaml



class Conf:
    def __init__(self, filename: str = None):
        self.filename = filename
        self.conf = {}

        if self.filename is None:
            raise ValueError("You didn't provide a filename")
        
        elif self.filename.endswith('.yaml'):
            self.yaml_ = ruamel.yaml.YAML()
            self.yaml_.preserve_quotes = True
            self.type = "YAML"
        elif self.filename.endswith(".json"):
            self.type = "JSON"
        else:
            raise ValueError('Unsupported file type')
        
        self.load()

    def load(self) -> None:
        with open(self.filename, 'r', encoding='utf-8') as f:
            if self.type == "JSON":
                self.conf = json.load(f)
            elif self.type == "YAML":
                self.conf = self.yaml_.load(f)
            else:
                raise ValueError('Unsupported file type')
    
    
    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            if self.filename.endswith('.json'):
                json.dump(self.conf, f, indent=4)
            elif self.filename.endswith('.yaml') or self.filename.endswith('.yml'):
                self.yaml_.dump(self.conf, f)
            else:
                raise ValueError('Unsupported file type')



class YamlConf:
    def __init__(self, filename: str = None):
        self.filename = filename
        self.yaml_ = ruamel.yaml.YAML()
        self.yaml_.preserve_quotes = True
        self.type = "YAML"
        self.conf = {}
        
        if self.filename is not None:
            self.load()
    
    
    def load(self, filename: str = None) -> None:
        """
        从文件中加载配置文件。
        
        参数：
            filename: str
                配置文件的路径。
                如果不提供文件名，将使用初始化时提供的文件名。
                若初始化时也没有提供文件名，则会抛出 ValueError。
        """
        if filename is not None:
            self.filename = filename
        if self.filename is None:
            raise ValueError("You didn't provide a filename")
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.conf = self.yaml_.load(f)
    
    
    def save(self):
        """
        以原格式保存配置文件。
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            self.yaml_.dump(self.conf, f)
            
    
    def get(self, key: str, default = None) -> str:
        """
        读取配置文件中的一个键值对，支持多级键值对的读取。
        
        参数：
            key: str
                键值对的键，可以是多级键，用 "." 分隔。
            default: Any
                如果键值对不存在，返回的默认值。
        
        返回：
            str
                返回键值对的值。
        """
        if "." in key:
            keys = key.split(".")
            value = self.conf
            for k in keys:
                value = value.get(k, default)
                if value == default:
                    break
            return value
        else:
            return self.conf.get(key, default)
    
    
    def set(self, key: str, value, save: bool = True) -> None:
        """
        设置对应键值对的值。
        
        参数：
            key: str
                要修改的配置项键，可以是多级键，用 "." 分隔。
            value: Any
                要设置的值。
            save: bool = True
                是否保存到文件。
                
        异常：
            KeyError: 当键不存在时抛出
        """
        try:
            if "." not in key:
                self.conf[key] = value
                return

            current = self.conf
            keys = key.split(".")
            
            # 遍历到最后一个键之前
            for k in keys[:-1]:
                if k not in current:
                    raise KeyError(f"未找到键: {k}")
                current = current[k]
                
            # 设置最后一个键的值
            if keys[-1] not in current:
                raise KeyError(f"未找到键: {keys[-1]}")
            current[keys[-1]] = value

            if save:
                self.save()

        except Exception as e:
            logger.error(f"设置键值的时候出错: {str(e)}")
            raise



class ConfigBridge:
    """
    本意是要实现一个配置文件的桥接器，可以将 JSON 和 YAML 两种格式的配置文件互相转换。
    不过正在考虑这个功能是否有必要，两种格式的配置文件读取出来的 dict 完全一样，只是保存的时候格式不同。
    """
    def __init__(self, conf_j: Conf, conf_y: Conf):
        self.j = conf_j
        self.y = conf_y


    def save(self, mode: str = 'b'):
        if mode.lower() == 'j':
            self.j.save()
        elif mode.lower() == 'y':
            self.y.save()
        elif mode.lower() == 'b':
            self.j.save()
            self.y.save()
        else:
            raise ValueError('Unsupported mode')
    
    
    def sync(self, direction: str = 'j2y', copy = True):
        if direction.lower() == 'j2y':
            self.y.conf = deepcopy(self.j.conf) if copy else self.j.conf
        elif direction.lower() == 'y2j':
            self.j.conf = deepcopy(self.y.conf) if copy else self.y.conf
        else:
            raise ValueError('Unsupported direction')
    
    
    def get_dict(self, t: str = 'j'):
        if t.lower() == 'j':
            return self.j.conf
        elif t.lower() == 'y':
            return self.y.conf
        else:
            raise ValueError('Unsupported type')
    
    
    def get(self, t: str = 'j'):
        if t.lower() == 'j':
            return self.j
        elif t.lower() == 'y':
            return self.y
        else:
            raise ValueError('Unsupported type')



if __name__ == '__main__':
    j = Conf("D:\\Launcher\\Fluent\\launcher\\configs\\project.json")
    y = Conf("D:\\Launcher\\Fluent\\conf.yaml")
    bridge = ConfigBridge(j, y)
    bridge.sync("y2j")
    bridge.save("j")
    y.conf["AI_NAME"] = "LiZhen"
    print(bridge.get_dict("y"))
    y.save()