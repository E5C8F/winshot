# WinShot

> 轻量级 Windows 截图库 | 纯 Python | 零依赖

[![GitHub](https://img.shields.io/badge/GitHub-E5C8F/winshot-181717?logo=github)](https://github.com/E5C8F/winshot)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python)](https://www.python.org/)

基于 Windows API 的纯 Python 截图解决方案，支持多种截图方式、**后台截图**、DPI 感知，无需任何第三方依赖。

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| 📸 **多种截图方式** | 支持 BitBlt、StretchBlt、PrintWindow 三种截图方式 |
| 👻 **后台截图** | 支持截取被遮挡或最小化的窗口（当前主流库几乎不支持） |
| 📐 **区域截图** | 支持指定坐标和尺寸进行区域截图 |
| 🔄 **图像缩放** | StretchBlt 方式支持截图时直接缩放到指定尺寸 |
| 🖥️ **DPI 感知** | 内置 DPI 感知设置，完美适配高分辨率显示器 |
| 💾 **BMP 保存** | 支持将截图数据直接保存为 BMP 格式 |
| 🚀 **零依赖** | 仅用 Python 标准库 + ctypes，无需安装任何第三方包 |
| 🇨🇳 **中文 API** | 对中文开发者友好的函数命名 |


---

## 📦 快速开始

### 1. 下载文件

将 `截图.py` 文件放入你的项目目录中。

### 2. 导入模块

```python
import 截图  # or import winshot
```

### 3. 详细文档和介绍
[https://e5c8f.github.io/winshot/](https://e5c8f.github.io/winshot/)



