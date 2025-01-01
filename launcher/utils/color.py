from PySide6.QtGui import QColor

import re



class Color:
    RED = QColor(255, 0, 0)
    GREEN = QColor(0, 255, 0)
    BLUE = QColor(0, 0, 255)
    LIME_GREEN = QColor(50, 205, 50)
    GOLD = QColor(255, 215, 0)



ANSI_MAP = {
    # 标准前景色
    '30': 'color: black',
    '31': 'color: red',
    '32': 'color: #32CD32',
    '33': 'color: #ffe644',
    '34': 'color: #00CDCD',
    '35': 'color: magenta',
    '36': 'color: #008B8B',
    '37': 'color: white',
    
    # 亮色前景色
    '90': 'color: gray',
    '91': 'color: #ff4444',
    '92': 'color: #44ff44',
    '93': 'color: #ffff44',
    '94': 'color: #00CDCD',
    '95': 'color: #ff44ff',
    '96': 'color: #00CDCD',
    '97': 'color: #ffffff',
    
    # 标准背景色
    '40': 'background-color: black',
    '41': 'background-color: red',
    '42': 'background-color: green',
    '43': 'background-color: yellow',
    '44': 'background-color: blue',
    '45': 'background-color: magenta',
    '46': 'background-color: cyan',
    '47': 'background-color: white',
    
    # 亮色背景色
    '100': 'background-color: gray',
    '101': 'background-color: #ff4444',
    '102': 'background-color: #44ff44',
    '103': 'background-color: #ffff44',
    '104': 'background-color: #4444ff',
    '105': 'background-color: #ff44ff',
    '106': 'background-color: #44ffff',
    '107': 'background-color: #ffffff',
    
    # 文本样式
    '0': '',  # 重置
    '1': 'font-weight: bold',  # 粗体
    '2': 'opacity: 0.8',  # 暗淡
    '3': 'font-style: italic',  # 斜体
    '4': 'text-decoration: underline',  # 下划线
    '5': 'text-decoration: blink',  # 闪烁
    '7': 'filter: invert(100%)',  # 反显
    '8': 'opacity: 0',  # 隐藏
    '9': 'text-decoration: line-through',  # 删除线
}



def ansi_to_html(text: str) -> str:
    """将ANSI代码（包括颜色和粗体）转换为HTML格式
    ONLY FOR WINDOWS
    """
    
    opened_spans = 0  # 跟踪打开的span标签数量
    
    def replace_codes(match):
        nonlocal opened_spans
        codes = match.group(1).split(';')
        styles = []
        
        # 如果是重置代码(0)，关闭所有标签
        if '0' in codes:
            result = '</span>' * opened_spans
            opened_spans = 0
            return result
            
        for code in codes:
            if code in ANSI_MAP:
                styles.append(ANSI_MAP[code])
        
        if not styles:
            if opened_spans > 0:
                opened_spans -= 1
                return '</span>'
            return ''
            
        opened_spans += 1
        return f'<span style="{"; ".join(styles)}">'
    
    # 替换所有ANSI代码
    result = re.sub(r'\x1b\[([0-9;]+)m|\033\[([0-9;]+)m', replace_codes, text)
    
    # 确保所有标签都被关闭
    if opened_spans > 0:
        result += '</span>' * opened_spans
    
    return result