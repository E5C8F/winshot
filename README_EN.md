
[![切换至中文](https://img.shields.io/badge/语言-中文-red.svg)](README.md)
[![Switch to English](https://img.shields.io/badge/Language-English-blue.svg)](README.en.md)

# winshot

**High-performance screenshot library for Windows based on WinAPI**

## Installation

```bash
pip install git+https://github.com/E5C8F/winshot.git
```
or
```
pip install winshot
```

## Quick Start

```python
from winshot import full_screenshot, save_image, set_process_dpi_awareness

# Set DPI awareness (recommended at program startup)
set_process_dpi_awareness()

# Full screen screenshot
image_data = full_screenshot()

# Save as BMP file
save_image(image_data, "screenshot.bmp")
```

## Features

- ✅ Full screen screenshot support
- ✅ Window screenshot support (foreground/background)
- ✅ Three screenshot methods: BitBlt, StretchBlt, PrintWindow
- ✅ Screenshot scaling support
- ✅ Raw BGRA data returned for easy processing
- ✅ Pure Python implementation, no compilation required

## API Documentation

### set_process_dpi_awareness(PROCESS_DPI_AWARENESS=2)

Set process DPI awareness level. Recommended to call at program startup.

**Parameters:**
- `PROCESS_DPI_AWARENESS`: 0=unaware, 1=system DPI aware, 2=per-monitor DPI aware (default)

```python
from winshot import set_process_dpi_awareness
set_process_dpi_awareness()  # Uses default value 2
```

### full_screenshot()

Capture full screen screenshot.

**Returns:** BGRA format image data (bytearray)

```python
from winshot import full_screenshot
image = full_screenshot()
print(f"Image size: {image.width}x{image.height}")
```

### foreground_window_screenshot(hwnd)

Capture foreground screenshot of specified window.

**Parameters:**
- `hwnd`: Window handle, defaults to desktop window

**Returns:** BGRA format image data

```python
from winshot import foreground_window_screenshot
image = foreground_window_screenshot(hwnd)
```

### bitblt_screenshot(x1, y1, cx, cy, hwnd)

Background screenshot using BitBlt method.

**Parameters:**
- `x1, y1`: Source rectangle top-left coordinates (relative to window)
- `cx, cy`: Screenshot area width and height
- `hwnd`: Window handle, defaults to desktop window

**Returns:** BGRA format image data

```python
from winshot import bitblt_screenshot
image = bitblt_screenshot(0, 0, 800, 600, hwnd)
```

### stretchblt_screenshot(wDest, hDest, xSrc, ySrc, wSrc, hSrc, hwnd)

Background screenshot with scaling using StretchBlt method.

**Parameters:**
- `wDest, hDest`: Destination width and height
- `xSrc, ySrc`: Source rectangle top-left coordinates
- `wSrc, hSrc`: Source rectangle width and height
- `hwnd`: Window handle

**Returns:** BGRA format image data

### printwindow_screenshot(w, h, hwnd)

Background screenshot using PrintWindow method.

**Parameters:**
- `w, h`: Window width and height
- `hwnd`: Window handle

**Returns:** BGRA format image data

### get_window_position(hwnd)

Get window position coordinates.

**Parameters:**
- `hwnd`: Window handle

**Returns:** `(left, top, right, bottom)` tuple

```python
from winshot import get_window_position
left, top, right, bottom = get_window_position(hwnd)
```

### save_image(bitmap_data, save_path, width=None, height=None)

Save bitmap data as BMP file.

**Parameters:**
- `bitmap_data`: BGRA format image data
- `save_path`: File save path
- `width, height`: Optional, automatically obtained from data captured by this library

```python
from winshot import full_screenshot, save_image
image = full_screenshot()
save_image(image, "output.bmp")
```

## Chinese Function Aliases

All functions also have Chinese aliases:

| English Function | Chinese Alias |
|-----------------|---------------|
| `set_process_dpi_awareness` | `设置DPI感知` |
| `full_screenshot` | `全屏截图` |
| `foreground_window_screenshot` | `前台窗口截图` |
| `bitblt_screenshot` | `BitBlt截图` |
| `stretchblt_screenshot` | `StretchBlt截图` |
| `printwindow_screenshot` | `PrintWindow截图` |
| `get_window_position` | `获取窗口位置` |
| `save_image` | `保存图片` |

```python
# Using Chinese aliases
from winshot import 全屏截图, 保存图片, 设置DPI感知

设置DPI感知()
image = 全屏截图()
保存图片(image, "screenshot.bmp")
```

## Notes

1. **DPI Awareness**: Recommended to call `set_process_dpi_awareness()` at program startup, otherwise screenshot dimensions may be incorrect on high DPI displays.
2. **Background Screenshot**: Using `bitblt_screenshot` or `printwindow_screenshot` for background capture may result in fully black or white images. Choose the appropriate method based on your use case.
3. **Image Format**: Returned data is in BGRA format (4 bytes/pixel), ready for image processing or BMP file saving.
4. **Platform Limitation**: This library only supports Windows systems.

## License

GNU General Public License v3.0

## Project Links

- [Homepage](https://e5c8f.github.io/winshot)
- [GitHub](https://github.com/E5C8F/winshot)
- [Issue Tracker](https://github.com/E5C8F/winshot/issues)
- [pypi](https://pypi.org/project/winshot)

