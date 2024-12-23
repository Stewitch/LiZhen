"""
本意是要实现一个配置文件的桥接器，可以将 JSON 和 YAML 两种格式的配置文件互相转换。
不过正在考虑是否有必要实现这个功能。
"""

import json, yaml

class Conf:
    def __init__(self, filename: str = None):
        self.filename = filename
        self.conf = {}
        self.type = None

    def load(self, filename: str = None) -> None:
        if filename is not None:
            self.filename = filename
        if self.filename is None:
            raise ValueError('No filename provided')
        with open(self.filename, 'r') as f:
            if self.filename.endswith('.json'):
                self.conf = json.load(f)
                self.type = "JSON"
            elif self.filename.endswith('.yaml') or self.filename.endswith('.yml'):
                self.conf = yaml.load(f, Loader=yaml.FullLoader)
                self.type = "YAML"
            else:
                raise ValueError('Unsupported file type')

class ConfigBridge:
    def __init__(self, conf_j: Conf, conf_y: Conf):
        self.conf_j = conf_j
        self.conf_y = conf_y

    def save(self, mode: str = 'b'):
        pass
    
    def sync(self, direction: str = 'j2y'):
        if direction == 'j2y':
            self.conf_y.conf = self.conf_j.conf
        elif direction == 'y2j':
            self.conf_j.conf = self.conf_y.conf
        else:
            raise ValueError('Unsupported direction')