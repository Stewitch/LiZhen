![Banner](./assets/imgs/banner.png)
<h1 align="center">离真 - Li Zhen</h1>

---

<h3 align="center">

[![Github License](https://img.shields.io/github/license/Stewitch/LiZhen?style=for-the-badge)](./LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/Stewitch/LiZhen?include_prereleases&sort=date&display_name=tag&style=for-the-badge)](https://github.com/Stewitch/LiZhen/releases)
[![GitHub Issues](https://img.shields.io/github/issues/Stewitch/LiZhen?style=for-the-badge)](https://github.com/Stewitch/LiZhen/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Stewitch/LiZhen?style=for-the-badge)](https://github.com/Stewitch/LiZhen/pulls)
![GitHub top language](https://img.shields.io/github/languages/top/Stewitch/LiZhen?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/Stewitch/LiZhen?style=for-the-badge)](https://github.com/Stewitch/LiZhen/forks)
![GitHub Repo stars](https://img.shields.io/github/stars/Stewitch/LiZhen?style=for-the-badge)

English README | [中文 README](./README.CN.md)

</h3>

---

## ❓ What is this project

**Li Zhen** is a modern launcher designed for the [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) project. It is developed in Python, using the PySide6 UI framework and the [PySide6-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6) component library. It aims to provide services such as quick startup and visual configuration for the project. It is committed to creating a more comfortable experience for **Windows users**.

**Note: The term "project" in the following text refers to the "Open-LLM-VTuber project"**

---

## 🌟 Features

- 🖱️ **One-click startup:** Just press the button, and the launcher will automatically enter the virtual environment and start the project without the need to manually enter commands.
- ⚙️ **Visual configuration:** Tired of modifying configuration files? Confused about the relationships between different settings? The launcher separates the configurations and uses switches, drop-down boxes, and other controls to make configuration easier.
- 📄 **Automatic virtual environment configuration:** Each time the project is started, the launcher will automatically execute the uv virtual environment commands to check the environment, ensuring it always meets the project's dependency requirements.
- 📥 **Download dependencies:** The launcher can currently automatically configure the uv virtual environment tool, eliminating the need for manual download and installation.
- 📓 **Information display:** The startup page shows the currently selected character, Live2D model, ASR/LLM/TTS provider, and model information, making it convenient for users to confirm.
- 🎛️ **Project/Launcher Console:** View the runtime status of the project/launcher within the launcher and quickly export logs for easy issue submission.

---

## 🖥️ System Requirements

- Windows 10/11 22H2 or later versions
- Others are consistent with the project

---

## ℹ️ File Structure

**Note:** Based on Releases, some file structures are omitted.

**Excluding the `Open-LLM-VTuber` folder**
> - /launcher
>   - /assets
>   - /configs
>   - /interfaces
>   - /logs
>   - /open_llm_vtuber #Borrowed codes form Project
>   - /utils
> - lizhen.exe
> - updater.exe

**Including the `Open-LLM-VTuber` folder**
> - /launcher
>   - /assets
>   - /configs
>   - /interfaces
>   - /logs
>   - /open_llm_vtuber #Borrowed codes form Project
>   - /utils
> - /Open-LLM-VTuber
>   - ...
> - lizhen.exe
> - updater.exe

---

## ▶️ Quick Start

#### Release
1. **Make sure you have downloaded and extracted the project files and configured FFMpeg (NVIDIA card users also need to configure CUDA and CUDNN)**. You can refer to the [Project Documentation#Environment Preparation](https://open-llm-vtuber.github.io/docs/quick-start/#%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87).
2. Download the latest version of the launcher Release package (.zip file).
3. Extract the files to a folder at the same level as the project folder (refer to the File Structure#Including the `Open-LLM-VTuber` folder).
4. Double-click to run `lizhen.exe`.
5. When exiting for the first time, you will be asked whether to create a desktop shortcut, or you can manually create one.

#### Source
1. On the basis of step 1 in **Release**, install Python 3.12.x.
2. Clone this repository using Git:
```batch
git clone https://github.com/Stewitch/LiZhen.git
```
3. Open the repository directory that was just cloned in the File Explorer, and copy the files to the directory at the same level as the project folder (refer to File Structure#Including the `Open-LLM-VTuber` folder).
4. Install project dependencies:
```batch
pip install -r requirements.txt
rem For users in China: If the download speed is slow, you can try setting the Tsinghua source and reinstalling
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
rem After setting, run the first command again
```
5. Start `main.py`. You can run it directly by double-clicking if the Python environment is properly configured, or use the command:
```batch
python main.py
```

---

## 🫡 Credits
- **@t41372** [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)
- **@zhiyiYo** [PySide6-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Stewitch/LiZhen&type=Date)](https://star-history.com/#Stewitch/LiZhen&Date)