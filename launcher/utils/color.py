from PySide6.QtGui import QColor

from .mapping import ANSI_COLOR_MAP

import re



class Color:
    RED = QColor(255, 0, 0)
    GREEN = QColor(0, 255, 0)
    BLUE = QColor(0, 0, 255)
    LIME_GREEN = QColor(50, 205, 50)
    GOLD = QColor(255, 215, 0)



def ansi_to_html(text: str) -> str:
    """将ANSI代码和日志换行转换为HTML格式"""
    
    is_progress = ('Downloading' in text or 'sherpa-onnx' in text) and '%' in text
    if is_progress:
        # 使用\r确保进度条在同一行更新
        text = text.rstrip() + '\r'
    else:
        # 普通文本处理换行
        text = text.replace('\n', '<br>')
    
    opened_spans = 0
    
    def replace_codes(match):
        nonlocal opened_spans
        codes = match.group(1).split(';')
        styles = []
        
        if '0' in codes:
            result = '</span>' * opened_spans
            opened_spans = 0
            return result
            
        for code in codes:
            if code in ANSI_COLOR_MAP:
                styles.append(ANSI_COLOR_MAP[code])
        
        if not styles:
            if opened_spans > 0:
                opened_spans -= 1
                return '</span>'
            return ''
            
        opened_spans += 1
        return f'<span style="{"; ".join(styles)}">'
    
    # 处理ANSI代码
    result = re.sub(r'\x1b\[([0-9;]+)m|\033\[([0-9;]+)m', replace_codes, text)
    
    if opened_spans > 0:
        result += '</span>' * opened_spans
    
    return result