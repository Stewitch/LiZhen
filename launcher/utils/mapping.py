from qfluentwidgets import FluentIcon as ICON

from ..interfaces.Cards import *
from ..interfaces.Widgets import *



ANSI_COLOR_MAP = {
    # 前景色
    '34': 'color: #228FBD',  # Debug
    '33': 'color: #F1BB00',  # Warning
    '31': 'color: #FF0000',  # Error
    '32': 'color: #32CD32',  # <green></green>
    '36': 'color: #008B8B',  # <cyan></cyan>
    
    # 背景色
    '41': 'background-color: #FF5555',  # Critical
    
    # 文本样式
    '0': '',  # 重置
    '1': 'font-weight: bold',  # 粗体
    '3': 'font-style: italic',  # 斜体
    '4': 'text-decoration: underline',  # 下划线
    '9': 'text-decoration: line-through',  # 删除线
}


# Abbr.: et = Extra Type
KEY_MAP = {
    "conf_version": {
        "zh": "文件版本",
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
    "config_alts_dir": {
        "zh": "自定义配置路径",
        "en": "Custom Config Directory",
        "ico": ICON.FOLDER,
        "et": "DIR",
        "caption": {
            "zh": "选择配置文件路径",
            "en": "Select config files path."
        },
        "defalut": "characters"
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
        "et": "OPTIONS"
    },
    "provider": {
        "zh": "运算设备",
        "en": "Provider",
        "ico": ICON.TRAIN,
        "et": "OPTIONS"
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
    "api_key": {
        "zh": "API 密钥",
        "en": "API Key",
        "ico": ICON.VPN,
        "et": "PWD"
    },
    "config_id": {
        "zh": "配置 ID",
        "en": "Config ID",
        "ico": ICON.FLAG,
        "et": str
    },
    "faster_first_response": {
        "zh": "快速响应",
        "en": "faster_first_response",
        "ico": ICON.SPEED_HIGH,
        "et": bool
    },
    "segment_method":   {
        "zh": "句子分割方式",
        "en": "Segment Method",
        "ico": ICON.TILES,
        "et": "OPTIONS"
    },
    "idle_timeout": {
        "zh": "空闲时间",
        "en": "Idle Timeout",
        "ico": ICON.EMBED,
    },
    "model": {
        "zh": "模型",
        "en": "Model",
        "ico": ICON.IOT,
        "et": str
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
        "et": "DIR",
        "caption": {
            "zh": "选择模型文件存放目录",
            "en": "Select a folder that stores model files."
        },
        "defalut": "models"
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
    "language": {
        "zh": "语言",
        "en": "Language",
        "ico": ICON.LANGUAGE,
        "et": "OPTIONS"
    },
    "device": {
        "zh": "设备",
        "en": "Device",
        "ico": ICON.TRAIN,
        "et": "OPTIONS"
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
        "ico": ICON.CLOUD_DOWNLOAD,
        "et": "OPTIONS"
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
        "ico": ICON.LANGUAGE,
        "et": "OPTIONS"
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
        "et": "CINT"
    },
    "rate": {
        "zh": "语速",
        "en": "Speech Rate",
        "ico": ICON.SPEED_OFF,
        "et": "CINT"
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
        "et": "CINT"
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
        "et": "CBOOL"
    },
    "reference_id": {
        "zh": "参考 ID",
        "en": "Reference ID",
        "ico": ICON.FLAG
    },
    "latency": {
        "zh": "延迟策略",
        "en": "Latency",
        "ico": ICON.DICTIONARY,
        "et": "OPTIONS"
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
    },
    "temperature": {
        "zh": "温度",
        "en": "Temperature",
        "ico": ICON.FRIGID,
        "range": (1.0, 2.0)
    },
    "download_root": {
        "zh": "模型下载路径",
        "en": "Model Download Path",
        "ico": ICON.FOLDER,
        "et": "DIR",
        "caption": {
            "zh": "选择下载路径",
            "en": "Select download path."
        },
        "defalut": "models/whisper"
    },
    "name": {
        "zh": "模型名称",
        "en": "Model Name",
        "ico": ICON.IOT
    },
    "print_realtime": {
        "zh": "实时输出",
        "en": "Print Realtime",
        "ico": ICON.MORE
    },
    "print_progress": {
        "zh": "输出进度",
        "en": "Print Progress",
        "ico": ICON.CALENDAR
    },
    "organization_id": {
        "zh": "组织 ID",
        "en": "Organization ID",
        'ico': ICON.PEOPLE,
        "et": str
    },
    "project_id": {
        "zh": "项目 ID",
        "en": "Project ID",
        'ico': ICON.FLAG,
        "et": str
    },
    "keep_alive": {
        "zh": "状态保持时间",
        "en": "Keep Alive",
        "ico": ICON.DATE_TIME,
        "range": (-1, 999999)
    },
    "unload_at_exit": {
        "zh": "退出时卸载",
        "en": "Unload at Exit",
        "ico": ICON.ERASE_TOOL,
    },
}



CARDS_MAP = {
    int: NumberCard,
    float: NumberCard,
    str: InputCard,
    bool: SwitchCard,
    "UNCHANGEABLE": DisplayCard,
    "OPTIONS": OptionsCard,
    "PWD": PasswordInputCard,
    "CBOOL": DisplayCard,
    "CINT": DisplayCard,
    "FILE": DisplayCard,
    "DIR": FolderCard,
    "URL": InputCard,
}



AVAILABLE_VALUES = {
    "llm_provider": [
        "openai_compatible_llm",
        "claude_llm",
        "llama_cpp_llm",
        "ollama_llm",
        "openai_llm",
        "gemini_llm",
        "zhipu_llm",
        "deepseek_llm",
        "groq_llm",
        "mistral_llm",
    ],
    "conversation_agent_choice": [
        "basic_memory_agent", "mem0_agent", "hume_ai_agent"
    ],
    "segment_method": [
        "regex", "pysbd"
    ],
    "asr_model": [
        "faster_whisper",
        "whisper_cpp",
        "whisper",
        "azure_asr",
        "fun_asr",
        "groq_whisper_asr",
        "sherpa_onnx_asr",
    ],
    "provider": [
        "cpu",
        "cuda"
    ],
    "device": [
        "cpu",
        "cuda",
        "auto",
        ""
    ],
    "language": [
        "zh",
        "en",
        "auto",
        "",
        "ZH",
        "EN"
    ],
    "lang": [
        "zh",
        "en",
        "auto",
        '',
        "ZH",
        'EN'
    ],
    "hub": [
        "ms",
        "hf",
    ],
    "tts_model": [
        "azure_tts",
        "bark_tts",
        "edge_tts",
        "cosyvoice_tts",
        "melo_tts",
        "piper_tts",
        "coqui_tts",
        "x_tts",
        "gpt_sovits_tts",
        "fish_api_tts",
        "sherpa_onnx_tts",
    ],
    "latency": [
        "normal",
        "balanced",
    ],
}



EXTRA_ENV_COMMANDS = {
    "fun_asr": "uv pip install funasr modelscope huggingface_hub torch torchaudio onnx onnxconverter_common",
    "fish_tts": "uv pip install fish-audio-sdk"   
}

