from pathlib import Path
from ruamel.yaml import YAML
from collections.abc import MutableMapping

import tomlkit as toml



class Bridge:
    
    """Yaml 和 Toml 的桥接器
    
    将 Yaml 文件转换为适合表单生成的 Toml 文件，或者将 Toml 文件反向合并到 Yaml 文件中
    
    注意：
    * 合并操作会保留原文件主要结构，但不会保留注释
    * 请注意转换方向对文件的要求
    * 开销较大，不适合大文件
    """
    
    def __init__(
            self,
            preserve_quotes: bool = False,
            width: int = 4096,
            mapping: int = 2,
            sequence: int = 4,
            offset: int = 2
        ) -> None:
        
        """桥接器仅需配置 Yaml 解析器
         
        解析器默认配置：
        * 不保留引号，最大单行长度`4096`
        * 映射缩进`2`，序列缩进`4`，偏移`2`
        """
        
        self.yamlParser = YAML(typ='rt')
        self.yamlParser.preserve_quotes = preserve_quotes
        self.yamlParser.width = width
        self.yamlParser.indent(
            mapping=mapping, sequence=sequence, offset=offset
        )
    
    
    def __path(self, path: str | Path) -> Path:
        
        """通用路径转换方法"""
        
        return path if isinstance(path, Path) else Path(path)
    
    
    def __mergeDoc(self, original: toml.TOMLDocument, new: toml.TOMLDocument) -> toml.TOMLDocument:
        
        """合并两个Toml文档
        
        已经存在的旧键值对将保留，新键值对中不存在的键值对将被删除
        """
        
        for newKey, newValue in new.items():
            if newKey not in original:
                original[newKey] = newValue
            else:
                if isinstance(newValue, MutableMapping):
                    self.__mergeDoc(original[newKey], newValue)
        
        # 不能在循环中删除键值对，会导致迭代错误(大小改变)
        needToDelete = []
        for key in original.keys():
            if key not in new:
                needToDelete.append(key)
        # 所以只好用两个循环
        for key in needToDelete:
            original.pop(key)
        
        return original
    
    
    def __unpackToml(self, data: dict, parentDict: dict, currentPath: list):
        
        """解构 Toml 数据，最终与 Yaml 读取出来的数据结构一致
        
        会将数据放到传入的 `parentDict` 中哦
        """
        
        for key, value in data.items():
            # 构建路径
            newPath = currentPath + [key]
            currentDict = parentDict
            for path in newPath:
                if path not in currentDict and "value" not in value:
                    currentDict[path] = {}
                    currentDict = currentDict[path]
                newPath.pop(0)
            
            # 获得 value 字段
            if "value" in value:
                currentDict[path] = value["value"]
            else:
                # 递归解构
                self.__unpackToml(value, currentDict, newPath)
    
    
    def __buildToml(self, data: dict, parentTable: toml.TOMLDocument, currentPath: list) -> None:
        
        """构建Toml数据"""
        
        for key, value in data.items():
            # 构建路径
            newPath = currentPath + [key]
            currentTable = parentTable
            for path in newPath:
                if path not in currentTable:
                    currentTable[path] = toml.table()
                currentTable = currentTable[path]
                newPath.pop(0) # 卡了我一个小时的bug
                
            # 构建数据表
            if not isinstance(value, MutableMapping):
                currentTable["value"] = value
                currentTable["type"] = type(value).__name__
                currentTable["readonly"] = False
                currentTable["required"] = False
                currentTable["default"] = value
                
                currentTable["title"] = toml.inline_table()
                currentTable["title"]["zh"] = "默认标题"
                currentTable["title"]["en"] = "Default Title"
                
                currentTable["description"] = toml.inline_table()
                currentTable["description"]["zh"] = "默认描述"
                currentTable["description"]["en"] = "Default Description"
                    
                # 类型特殊处理
                typ = currentTable["type"]
                match typ:
                    case "int":
                        currentTable["range"] = [0, 999999]
                    case "DoubleQuotedScalarString":
                        currentTable["type"] = "str"
                    case "LiteralScalarString":
                        currentTable["type"] = "str"
                    case "ScalarFloat":
                        currentTable["type"] = "float"
                        
            else:
                # 递归构建
                self.__buildToml(value, currentTable, newPath)
    
    
    def readToml(self, tomlPath: str | Path) -> dict:
        
        """读取 Toml 文件"""
        
        tomlPath = self.__path(tomlPath)
        if tomlPath.exists() and tomlPath.suffix == '.toml':
            with tomlPath.open('r', encoding='utf-8') as f:
                return toml.load(f)
        else:
            raise FileNotFoundError(f'文件 {tomlPath} 不存在或不是 Toml 文件 (.toml)')
    
    
    def readYaml(self, yamlPath: str | Path) -> dict:
        
        """读取 Yaml 文件"""
        
        yamlPath = self.__path(yamlPath)
        if yamlPath.exists() and yamlPath.suffix in ['.yaml', '.yml']:
            with yamlPath.open('r', encoding='utf-8') as f:
                return self.yamlParser.load(f)
        else:
            raise FileNotFoundError(f'文件 {yamlPath} 不存在或不是 Yaml 文件 (.yaml/.yml)')

    
    def yamlToToml(self, yamlPath: str | Path, tomlPath: str | Path = None, force: bool = False):
        
        """**小心使用，开销较大(相对)**
        
        将 Yaml 文件转换为 Toml 文件，如果 Toml 文件已经存在，将会**合并**文件内容
        * 可以设置 force 参数，强制覆盖 Toml 文件
        
        Yaml 文件必须存在，Toml 文件可以不存在
        """
        
        data = self.readYaml(yamlPath)
            
        tomlDoc = toml.document()
        self.__buildToml(data, tomlDoc, [])
        
        originalDoc = toml.document()
        
        if not force:
            try:
                originalDoc = self.readToml(tomlPath)
            except FileNotFoundError:
                pass
            mergedDoc = self.__mergeDoc(originalDoc, tomlDoc)
        else:
            mergedDoc = tomlDoc
        
        with tomlPath.open('w', encoding='utf-8') as f:
            toml.dump(mergedDoc, f)
    
    
    def tomlToYaml(self, tomlPath: str | Path, yamlPath: str | Path = None):
        
        """**小心使用，开销较大(相对)**
        
        将 Toml 文件转换为 Yaml 文件，如果 Yaml 文件已经存在，将会**合并**文件内容
        * 没有 force 选项 :) 会保留原文件，只对值进行更新
        
        Toml 文件必须存在，Yaml 文件可以不存在
        """
        
        tomlData = self.readToml(tomlPath)
        
        try:
            yamlData = self.readYaml(yamlPath)
        except FileNotFoundError:
            yamlData = {}

        unpackedData = {}
        self.__unpackToml(tomlData, unpackedData, [])
        
        if yamlData:
            yamlData.update(unpackedData)
        else:
            yamlData = unpackedData
        
        with yamlPath.open('w', encoding='utf-8') as f:
            self.yamlParser.dump(yamlData, f)

        

if __name__ == '__main__':
    
    bridge = Bridge()
    print(bridge.readToml("conf.toml"))