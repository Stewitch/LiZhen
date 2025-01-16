from qfluentwidgets import (SpinBox, SwitchButton, LineEdit, BodyLabel, PasswordLineEdit)
from qfluentwidgets import FluentIcon as ICON

from ..interfaces.Widgets import TComboBox, TSwitchButton, TSpinBox



ANSI_COLOR_MAP = {
    # 前景色
    '30': 'color: black',
    '31': 'color: red',
    '32': 'color: #32CD32',
    '33': 'color: #ffe644',
    '34': 'color: #00CDCD',
    '35': 'color: magenta',
    '36': 'color: #008B8B',
    '37': 'color: white',
    
    # 背景色
    '40': 'background-color: black',
    '41': 'background-color: red',
    '42': 'background-color: green',
    '43': 'background-color: yellow',
    '44': 'background-color: blue',
    '45': 'background-color: magenta',
    '46': 'background-color: cyan',
    '47': 'background-color: white',
    
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


# Abbr.: et = Extra Type
KEY_MAP = {
    "conf_version": {
        "zh": "配置版本",
        "en": "Config Version",
        "ico": ICON.SETTING,
        "et": "UNCHANGEABLE"
    },
    "host": {
        "zh": "服务器地址",
        "en": "Server Address",
        "ico": ICON.LINK
    },
    "port": {
        "zh": "服务器端口",
        "en": "Server Port",
        "ico": ICON.INFO,
        "range": (0, 65535)
    },
    "preload_models": {
        "zh": "预加载模型",
        "en": "Preload Models",
        "ico": ICON.SEND
    },
    "config_alts_dir": {
        "zh": "自定义配置路径",
        "en": "Custom Config Directory",
        "ico": ICON.FOLDER,
        "et": "DIR"
    },
    "live2d_expression_prompt": {
        "zh": "Live2D表情提示词",
        "en": "Live2D Expression Prompt",
        "ico": ICON.QUESTION
    },
    "remove_special_char": {
        "zh": "移除特殊字符",
        "en": "Remove Special Characters",
        "ico": ICON.EMOJI_TAB_SYMBOLS
    },
    "conf_name": {
        "zh": "配置名称",
        "en": "Configuration Name",
        "ico": ICON.BOOK_SHELF
    },
    "conf_uid": {
        "zh": "配置唯一标识",
        "en": "Configuration UID",
        "ico": ICON.FLAG
    },
    "live2d_model_name": {
        "zh": "Live2D模型名称",
        "en": "Live2D Model Name",
        "ico": ICON.PEOPLE
    },
    "persona_prompt": {
        "zh": "人设提示词",
        "en": "Persona Prompt",
        "ico": ICON.HELP
    },
    "llm_provider": {
        "zh": "大语言模型后端",
        "en": "LLM Provider",
        "ico": ICON.CHAT,
        "et": "TOCOMBOBOX"
    },
    "base_url": {
        "zh": "基础 URL",
        "en": "Base URL",
        "ico": ICON.LINK,
        'et': "URL"
    },
    "llm_api_key": {
        "zh": "API 密钥",
        "en": "API Key",
        "ico": ICON.VPN,
        "et": "PWD"
    },
    "model": {
        "zh": "模型",
        "en": "Model",
        "ico": ICON.IOT
    },
    "verbose": {
        "zh": "详细日志",
        "en": "Verbose Logging",
        "ico": ICON.ALIGNMENT
    },
    "model_path": {
        "zh": "模型文件",
        "en": "Model File",
        "ico": ICON.DOCUMENT,
        "et": "FILE"
    },
    "model_dir": {
        "zh": "模型存放路径",
        "en": "Model Path",
        "ico": ICON.FOLDER,
        "et": "DIR"
    },
    "model_name": {
        "zh": "模型名称",
        "en": "Model Name",
        "ico": ICON.IOT
    },
    "admin_token": {
        "zh": "管理员令牌",
        "en": "Admin Token",
        "ico": ICON.VPN,
        "et": "PWD"
    },
    "agent_id": {
        "zh": "代理 ID",
        "en": "Agent ID",
        "ico": ICON.ROBOT
    },
    "asr_model": {
        "zh": "语音识别模型",
        "en": "ASR Model",
        "ico": ICON.IOT
    },
    "language": {
        "zh": "语言",
        "en": "Language",
        "ico": ICON.LANGUAGE
    },
    "device": {
        "zh": "设备",
        "en": "Device",
        "ico": ICON.CALORIES
    },
    "vad_model": {
        "zh": "静默检测模型",
        "en": "VAD Model",
        "ico": ICON.QUIET_HOURS
    },
    "punc_model": {
        "zh": "标点符号模型",
        "en": "Punctation Model",
        "ico": ICON.TILES
    },
    "disable_update": {
        "zh": "禁用自动更新",
        "en": "Disable Update",
        "ico": ICON.UPDATE
    },
    "ncpu": {
        "zh": "线程数",
        "en": "Threads",
        "ico": ICON.LAYOUT
    },
    "hub": {
        "zh": "模型站",
        "en": "Model Hub",
        "ico": ICON.CLOUD_DOWNLOAD
    },
    "use_itn": {
        "zh": "启用反正则化",
        "en": "Enable ITN",
        "ico": ICON.ROTATE
    },
    "tts_on": {
        "zh": "启用语音合成",
        "en": "Enable TTS",
        "ico": ICON.VOLUME
    },
    "tts_model": {
        "zh": "语音合成模型",
        "en": "TTS Model",
        "ico": ICON.IOT
    },
    "voice": {
        "zh": "音色",
        "en": "Voice",
        "ico": ICON.FONT_INCREASE
    },
    "speed": {
        "zh": "语速",
        "en": "Speed",
        "ico": ICON.SPEED_OFF
    },
    "lang": {
        "zh": "语言",
        "en": "Language",
        "ico": ICON.LANGUAGE
    },
    "region": {
        "zh": "地区",
        "en": "Region",
        "ico": ICON.GLOBE
    },
    "voice": {
        "zh": "声线",
        "en": "Voice",
        "ico": ICON.PEOPLE
    },
    "pitch": {
        "zh": "音调增量",
        "en": "Pitch",
        "ico": ICON.MARKET,
        "et": "INT"
    },
    "rate": {
        "zh": "语速",
        "en": "Speech Rate",
        "ico": ICON.SPEED_OFF,
        "et": "INT"
    },
    "client_url": {
        "zh": "WebUI 链接",
        "en": "WebUI Url",
        "ico": ICON.LINK
    },
    "mode_checkbox_group": {
        "zh": "推理模式",
        "en": "Reasoning Mode",
        "ico": ICON.SCROLL
    },
    "sft_dropdown": {
        "zh": "预训练音色",
        "en": "Pre Trained Timbre",
        "ico": ICON.PEOPLE
    },
    "prompt_text": {
        "zh": "提示词文本",
        "en": "Prompt Text",
        "ico": ICON.DICTIONARY_ADD
    },
    "prompt_wav_upload_url": {
        "zh": "上传Prompt音频文件 链接",
        "en": "Prompt WAV Upload Url",
        "ico": ICON.LINK
    },
    "prompt_wav_record_url": {
        "zh": "录制Prompt音频文件 链接",
        "en": "Prompt WAV Record Url",
        "ico": ICON.LINK
    },
    "instruct_text": {
        "zh": "Instruct 文本",
        "en": "Instruct Text",
        "ico": ICON.QUESTION
    },
    "seed": {
        "zh": "随机推理种子",
        "en": "Random Reasoning Seed",
        "ico": ICON.PALETTE
    },
    "api_name": {
        "zh": "API 名称",
        "en": "API Name",
        "ico": ICON.QUESTION
    },
    "api_url": {
        "zh": "API 链接",
        "en": "API URL",
        "ico": ICON.LINK
    },
    "speaker": {
        "zh": "讲述者",
        "en": "Speaker",
        "ico": ICON.PEOPLE
    },
    "speed": {
        "zh": "语速",
        "en": "Speech Speed",
        "ico": ICON.SPEED_OFF
    },
    "speaker_wav": {
        "zh": "参考音频文件",
        "en": "Reference Audio File",
        "ico": ICON.HEADPHONE
    },
    "text_lang": {
        "zh": "生成文本语言",
        "en": "Text Language",
        "ico": ICON.LANGUAGE
    },
    "ref_audio_path": {
        "zh": "参考音频文件",
        "en": "Reference Audio File",
        "ico": ICON.HEADPHONE
    },
    "prompt_lang": {
        "zh": "提示词语言",
        "en": "Prompt Language",
        "ico": ICON.LANGUAGE
    },
    "text_split_method": {
        "zh": "文本分割方式",
        "en": "Text Split Method",
        "ico": ICON.TILES
    },
    "batch_size": {
        "zh": "Batch 大小",
        "en": "Batch Size",
        "ico": ICON.FRIGID,
        "et": "INT"
    },
    "media_type": {
        "zh": "生成音频文件扩展名",
        "en": "Media Type",
        "ico": ICON.MEDIA
    },
    "streaming_mode": {
        "zh": "流式生成模式",
        "en": "Streaming Mode",
        "ico": ICON.BACK_TO_WINDOW,
        "et": "BOOL"
    },
    "reference_id": {
        "zh": "参考 ID",
        "en": "Reference ID",
        "ico": ICON.FLAG
    },
    "latency": {
        "zh": "生成策略",
        "en": "Latency",
        "ico": ICON.DICTIONARY
    },
    "sid": {
        "zh": "讲述者 ID",
        "en": "Speaker ID",
        "ico": ICON.ROBOT
    },
    "num_threads": {
        "zh": "线程数",
        "en": "Threads",
        "ico": ICON.CALORIES
    },
    "debug": {
        "zh": "调试模式",
        "en": "Debug Mode",
        "ico": ICON.DEVELOPER_TOOLS
    }
}


WIDGETS_MAP = {
    int: SpinBox,
    str: LineEdit,
    bool: SwitchButton,
    "UNCHANGEABLE": BodyLabel,
    "TOCOMBOBOX": TComboBox,
    "PWD": PasswordLineEdit,
    "BOOL": TSwitchButton,
    "INT": TSpinBox,
    "FILE": BodyLabel,
    "DIR": BodyLabel
}


NON_STANDARD_WIDGETS = [
    TComboBox, TSwitchButton, TSpinBox
]


WIDGETS_SIZE = {
    BodyLabel: 100,
    LineEdit: 200,
    SpinBox: 150,
    SwitchButton: 55,
    PasswordLineEdit: 200,
    TSwitchButton: 100,
    TSpinBox: 150,
    TComboBox: 70,
}


