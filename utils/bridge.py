from pathlib import Path
from ruamel.yaml import YAML
from tomlkit import document, table, load, dump, TOMLDocument, inline_table
from collections.abc import MutableMapping



class Bridge:
    
    """Yaml和Toml的桥接器"""
    
    def __init__(self) -> None:
        self.yamlParser = YAML(typ='rt')
        self.yamlParser.preserve_quotes = True
        self.yamlParser.width = 4096
        self.yamlParser.indent(mapping=2, sequence=4, offset=2)
    
    
    def __path(self, path: str | Path) -> Path:
        
        """通用路径转换方法"""
        
        return path if isinstance(path, Path) else Path(path)
    
    
    def __mergeDoc(self, original: TOMLDocument, new: TOMLDocument) -> TOMLDocument:
        
        """合并两个Toml文档
        
        已经存在的旧键值对将保留，新键值对中不存在的键值对将被删除
        """
        
        for newKey, newValue in new.items():
            if newKey not in original:
                original[newKey] = newValue
            else:
                if isinstance(newValue, MutableMapping):
                    self.__mergeDoc(original[newKey], newValue)
        
        needToDelete = []
        for key in original.keys():
            if key not in new:
                needToDelete.append(key)
        
        for key in needToDelete:
            original.pop(key)
        
        return original
    
    
    def __buildToml(self, data: dict, parentTable: TOMLDocument, path: list) -> None:
        
        """构建Toml数据"""
        
        if isinstance(data, MutableMapping):
            for key, value in data.items():
                # 构建路径
                newPath = path + [key]
                currentTable = parentTable
                for p in newPath:
                    if p not in currentTable:
                        currentTable[p] = table()
                    currentTable = currentTable[p]
                    newPath.pop(0) # 卡了我一个小时的bug
                
                # 构建数据表
                if not isinstance(value, MutableMapping):
                    currentTable["value"] = value
                    currentTable["type"] = type(value).__name__
                    currentTable["title"] = inline_table()
                    currentTable["title"]["zh"] = "默认标题"
                    currentTable["title"]["en"] = "Default Title"
                    currentTable["description"] = inline_table()
                    currentTable["description"]["zh"] = "默认描述"
                    currentTable["description"]["en"] = "Default Description"
                    currentTable["required"] = False
                    currentTable["default"] = value
                    
                    typ = currentTable["type"]
                    if typ == "DoubleQuotedScalarString":
                        currentTable["value"] = str(value)
                        currentTable["type"] = "str"
                    elif typ == "int":
                        currentTable["range"] = [0, 999999]
                
                else:
                    # 递归构建
                    self.__buildToml(value, currentTable, newPath)

    
    def yamlToToml(self, yamlPath: str | Path, tomlPath: str | Path = None):
        
        """小心使用，开销较大(相对)"""
        
        with self.__path(yamlPath).open('r', encoding='utf-8') as f:
            data = self.yamlParser.load(f)
            tomlDoc = document()
            self.__buildToml(data, tomlDoc, [])
        
        originalDoc = document()
        tomlPath = self.__path(tomlPath)
        if tomlPath.exists():
            with tomlPath.open('r', encoding='utf-8') as f:
                originalDoc = load(f)
        
        mergedDoc = self.__mergeDoc(originalDoc, tomlDoc)
        
        with tomlPath.open('w', encoding='utf-8') as f:
            dump(mergedDoc, f)



if __name__ == '__main__':
    bridge = Bridge()
    bridge.yamlToToml('conf.yaml', 'conf.toml')