


[![切换至中文](https://img.shields.io/badge/语言-中文-red.svg)](README.md)
[![Switch to English](https://img.shields.io/badge/Language-English-blue.svg)](README.en.md)
# winshot

Windows 截图库 - 基于 WinAPI 实现的高性能截图工具

## 安装

```bash
pip install git+https://github.com/E5C8F/winshot.git
```

## 快速开始

```python
from winshot import 全屏截图, 保存图片, 设置DPI感知

# 设置 DPI 感知（建议在程序启动时调用）
设置DPI感知()

# 全屏截图
图像数据 = 全屏截图()

# 保存为 BMP 文件
保存图片(图像数据, "screenshot.bmp")
```

## 功能特性

- ✅ 支持全屏截图
- ✅ 支持窗口截图（前台/后台）
- ✅ 支持 BitBlt、StretchBlt、PrintWindow 三种截图方式
- ✅ 支持截图缩放
- ✅ 返回原始 BGRA 数据，方便后续处理
- ✅ 纯 Python 实现，无需编译

## API 文档

### 设置DPI感知(PROCESS_DPI_AWARENESS=2)

设置进程 DPI 感知级别，建议在程序启动时调用。

**参数：**
- `PROCESS_DPI_AWARENESS`: 0=不感知, 1=系统 DPI 感知, 2=按监视器 DPI 感知（默认）

```python
from winshot import 设置DPI感知
设置DPI感知()  # 使用默认值 2
```

### 全屏截图()

获取全屏幕截图。

**返回：** BGRA 格式的图像数据（bytearray）

```python
from winshot import 全屏截图
图像 = 全屏截图()
print(f"图像尺寸: {图像.width}x{图像.height}")
```

### 前台窗口截图(hwnd)

获取指定窗口的前台截图。

**参数：**
- `hwnd`: 窗口句柄，默认为桌面窗口

**返回：** BGRA 格式的图像数据

```python
from winshot import 前台窗口截图
图像 = 前台窗口截图(hwnd)
```

### BitBlt截图(x1, y1, cx, cy, hwnd)

通过 BitBlt 方式进行后台截图。

**参数：**
- `x1, y1`: 源矩形左上角坐标（相对于窗口）
- `cx, cy`: 截图区域宽高
- `hwnd`: 窗口句柄，默认为桌面窗口

**返回：** BGRA 格式的图像数据

```python
from winshot import BitBlt截图
图像 = BitBlt截图(0, 0, 800, 600, hwnd)
```

### StretchBlt截图(wDest, hDest, xSrc, ySrc, wSrc, hSrc, hwnd)

通过 StretchBlt 方式进行后台截图并缩放。

**参数：**
- `wDest, hDest`: 目标宽高
- `xSrc, ySrc`: 源矩形左上角坐标
- `wSrc, hSrc`: 源矩形宽高
- `hwnd`: 窗口句柄

**返回：** BGRA 格式的图像数据

### PrintWindow截图(w, h, hwnd)

通过 PrintWindow 方式进行后台截图。

**参数：**
- `w, h`: 窗口宽高
- `hwnd`: 窗口句柄

**返回：** BGRA 格式的图像数据

### 获取窗口位置(hwnd)

获取窗口的位置坐标。

**参数：**
- `hwnd`: 窗口句柄

**返回：** `(left, top, right, bottom)` 元组

```python
from winshot import 获取窗口位置
left, top, right, bottom = 获取窗口位置(hwnd)
```

### 保存图片(位图数据, 保存路径, 宽度=None, 高度=None)

保存位图数据为 BMP 文件。

**参数：**
- `位图数据`: BGRA 格式的图像数据
- `保存路径`: 文件保存路径
- `宽度, 高度`: 可选，通过本库获取的数据会自动获取

```python
from winshot import 全屏截图, 保存图片
图像 = 全屏截图()
保存图片(图像, "output.bmp")
```

## 英文别名

所有函数都提供了英文别名：

| 中文函数名 | 英文别名 |
|-----------|---------|
| 设置DPI感知 | `set_process_dpi_awareness` |
| 全屏截图 | `full_screenshot` |
| 前台窗口截图 | `foreground_window_screenshot` |
| BitBlt截图 | `bitblt_screenshot` |
| StretchBlt截图 | `stretchblt_screenshot` |
| PrintWindow截图 | `printwindow_screenshot` |
| 获取窗口位置 | `get_window_position` |
| 保存图片 | `save_image` |

```python
# 使用英文别名
from winshot import full_screenshot, save_image, set_process_dpi_awareness

set_process_dpi_awareness()
image = full_screenshot()
save_image(image, "screenshot.bmp")
```

## 注意事项

1. **DPI 感知**：建议在程序启动时调用 `设置DPI感知()`，否则在高 DPI 显示器上可能出现截图尺寸不正确的问题。
2. **后台截图**：使用 `BitBlt截图` 或 `PrintWindow截图` 进行后台截图时，可能出现全黑或全白的情况，建议根据实际场景选择合适的方法。
3. **图像格式**：返回的数据为 BGRA 格式（4 字节/像素），可直接用于图像处理或保存为 BMP 文件。
4. **平台限制**：本库仅支持 Windows 系统。

## 许可证

GNU General Public License v3.0

## 项目链接

- [主页](https://e5c8f.github.io/winshot)
- [GitHub](https://github.com/E5C8F/winshot)
- [问题反馈](https://github.com/E5C8F/winshot/issues)
