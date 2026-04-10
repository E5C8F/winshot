
import ctypes
from ctypes import wintypes
import struct
import os

class RGBQUAD(ctypes.Structure):
    _fields_ = [
        ("rgbBlue", wintypes.BYTE),      # 蓝色的强度
        ("rgbGreen", wintypes.BYTE),     # 绿色的强度  
        ("rgbRed", wintypes.BYTE),       # 红色的强度
        ("rgbReserved", wintypes.BYTE),  # 保留成员, 必须为零
    ]


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", wintypes.DWORD),           # 结构大小
        ("biWidth", wintypes.LONG),            # 位图宽度(像素)
        ("biHeight", wintypes.LONG),           # 位图高度(像素)
        ("biPlanes", wintypes.WORD),         # 目标设备平面数, 必须为1
        ("biBitCount", wintypes.WORD),       # 每像素位数(bpp)
        ("biCompression", wintypes.DWORD),    # 压缩方式
        ("biSizeImage", wintypes.DWORD),      # 图像大小(字节)
        ("biXPelsPerMeter", wintypes.LONG),    # 水平分辨率(像素/米)
        ("biYPelsPerMeter", wintypes.LONG),    # 垂直分辨率(像素/米)
        ("biClrUsed", wintypes.DWORD),        # 实际使用的颜色索引数
        ("biClrImportant", wintypes.DWORD),   # 重要颜色索引数
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),  # 位图信息头
        ("bmiColors", RGBQUAD * 1),       # 颜色表(柔性数组, 这里定义为1个元素)
    ]
    def __init__(self):
        self.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
        self.bmiHeader.biPlanes = 1
        self.bmiHeader.biBitCount = 32
        self.bmiHeader.biCompression = 0
        self.bmiHeader.biSizeImage = 0
        self.bmiHeader.biXPelsPerMeter = 0
        self.bmiHeader.biYPelsPerMeter = 0
        self.bmiHeader.biClrUsed = 0
        self.bmiHeader.biClrImportant = 0

user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
shcore = ctypes.WinDLL('shcore', use_last_error=True)
def errcheck (result, func, args):
    错误码 = ctypes.set_last_error(0)
    if 错误码:
        # print(f'error code: {错误码}, result: {result}, func: {func}, args: {args}')
        raise ctypes.WinError(错误码, fr'result: {result}, func: {func}, args: {args}')
    return result



CreateDIBSection = gdi32.CreateDIBSection
CreateDIBSection = gdi32.CreateDIBSection
CreateDIBSection.argtypes = [
    wintypes.HDC,
    ctypes.POINTER(BITMAPINFO),
    wintypes.UINT,
    ctypes.POINTER(ctypes.c_void_p),
    wintypes.HANDLE,
    wintypes.DWORD
]
CreateDIBSection.restype = wintypes.HBITMAP
CreateDIBSection.errcheck = errcheck


GetWindowDC = user32.GetWindowDC
GetWindowDC.argtypes = [
    wintypes.HWND
]
GetWindowDC.restype = wintypes.HDC
GetWindowDC.errcheck = errcheck

CreateCompatibleDC = gdi32.CreateCompatibleDC
CreateCompatibleDC.argtypes = [
    wintypes.HDC
]
CreateCompatibleDC.restype = wintypes.HDC
CreateCompatibleDC.errcheck = errcheck

SelectObject = gdi32.SelectObject
SelectObject.argtypes = [
    wintypes.HDC,
    wintypes.HGDIOBJ
]
SelectObject.restype = wintypes.HGDIOBJ
SelectObject.errcheck = errcheck

DeleteObject = gdi32.DeleteObject
DeleteObject.argtypes = [
    wintypes.HGDIOBJ
]
DeleteObject.restype = wintypes.BOOL
DeleteObject.errcheck = errcheck

DeleteDC = gdi32.DeleteDC
DeleteDC.argtypes = [
    wintypes.HDC
]
DeleteDC.restype = wintypes.BOOL
DeleteDC.errcheck = errcheck

ReleaseDC = user32.ReleaseDC
ReleaseDC.argtypes = [
    wintypes.HWND,
    wintypes.HDC
]
ReleaseDC.restype = wintypes.INT
ReleaseDC.errcheck = errcheck

BitBlt = gdi32.BitBlt
BitBlt.argtypes = [
    wintypes.HDC,# [in] hdc 目标设备上下文的句柄。
    wintypes.INT,# [in] x 目标矩形左上角的 x 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] y 目标矩形左上角的 y 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] cx 目标矩形的宽度（以逻辑单位为单位）。
    wintypes.INT,# [in] cy 目标矩形的高度（以逻辑单位为单位）。
    wintypes.HDC,# [in] hdcSrc 源设备上下文的句柄。
    wintypes.INT,# [in] x1 源矩形左上角的 x 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] y1 源矩形左上角的 y 坐标（以逻辑单位为单位）。
    wintypes.DWORD,# [in] rop 光栅操作代码。 这些代码定义如何将源矩形的颜色数据与目标矩形的颜色数据相结合，以实现最终颜色。
]
BitBlt.restype = wintypes.BOOL
BitBlt.errcheck = errcheck

StretchBlt = gdi32.StretchBlt
StretchBlt.argtypes = [
    wintypes.HDC,# [in] hdcDest 目标设备上下文的句柄。
    wintypes.INT,# [in] xDest 目标矩形左上角的 x 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] yDest 目标矩形左上角的 y 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] wDest 目标矩形的宽度（以逻辑单元表示）。
    wintypes.INT,# [in] hDest 目标矩形的高度（以逻辑单元表示）。
    wintypes.HDC,# [in] hdcSrc 源设备上下文的句柄。
    wintypes.INT,# [in] xSrc 源矩形左上角的 x 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] ySrc 源矩形左上角的 y 坐标（以逻辑单位为单位）。
    wintypes.INT,# [in] wSrc 源矩形的宽度（以逻辑单元表示）。
    wintypes.INT,# [in] hSrc 源矩形的高度（以逻辑单元表示）。
    wintypes.DWORD,# [in] rop 光栅操作代码。 这些代码定义如何将源矩形的颜色数据与目标矩形的颜色数据相结合，以实现最终颜色。
]
StretchBlt.restype = wintypes.BOOL
StretchBlt.errcheck = errcheck

PrintWindow = user32.PrintWindow
PrintWindow.argtypes = [
    wintypes.HWND,# hwnd 要打印的窗口的句柄。
    wintypes.HDC,# hdcBlt 设备上下文的句柄。
    wintypes.UINT,# nFlags 绘图选项。
]
PrintWindow.restype = wintypes.BOOL
PrintWindow.errcheck = errcheck

GetWindowRect = user32.GetWindowRect
GetWindowRect.argtypes = [
    wintypes.HWND,
    ctypes.POINTER(wintypes.RECT)
]
GetWindowRect.restype = wintypes.BOOL
GetWindowRect.errcheck = errcheck

SetProcessDpiAwareness = shcore.SetProcessDpiAwareness
SetProcessDpiAwareness.argtypes = [
    ctypes.c_int
]
SetProcessDpiAwareness.restype = ctypes.c_long
SetProcessDpiAwareness.errcheck = errcheck


def _动态属性化(类型, **属性):
    class 动态属性化(类型):
        def __new__(cls, *args, **kwargs):
            对象 = super().__new__(cls, *args, **kwargs)
            对象.__dict__.update(属性)
            return 对象
        def __setattr__(self, name, value):
            self.__dict__[name] = value
        def __getattr__(self, name):
            return self.__dict__[name]
        def __delattr__(self, name):
            del self.__dict__[name]
    return 动态属性化

def BitBlt截图(x1, y1, cx, cy, hwnd = user32.GetDesktopWindow()):
    '''
    function: 通过 BitBlt 对 hwnd 对应 窗口进行后台截图.\n
    param x1, y1: 源矩形左上角的坐标（以逻辑单位为单位）, 即相对于窗口左上角的相对坐标.\n
    param cx, cy: 目标矩形的宽高（以逻辑单位为单位）, 即要截取的窗口区域大小.\n
    param hwnd: 窗口句柄, 默认值为桌面窗口句柄.\n
    return: 返回二进制格式的BGRA图像数据.\n
    注意事项:
    1. 建议使用前 设置DPI感知, 否则很可能出现DPI问题, 已提供 设置DPI感知 函数 方便调用.
    2. 针对后台窗口截图, 可能出现 全黑 或者 全白 等截图 问题, 建议配合 PrintWindow截图 按需交替使用.
    3. 截图的图像数据为 BGRA 格式, 即 4 个字节分别表示 BGRA 四通道颜色值.
    '''

    窗口设备上下文句柄 = GetWindowDC(hwnd)
    内存设备上下文句柄 = CreateCompatibleDC(窗口设备上下文句柄)
    _BITMAPINFO结构体 = BITMAPINFO()
    _BITMAPINFO结构体.bmiHeader.biWidth = cx
    _BITMAPINFO结构体.bmiHeader.biHeight = -cy # 负值表示自上而下更符合现代编程习惯
    像素数据指针 = wintypes.LPVOID()

    
    位图句柄 = CreateDIBSection(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)
    原对象句柄 = SelectObject(内存设备上下文句柄, 位图句柄)
    BitBlt操作结果 = BitBlt(内存设备上下文句柄, 0, 0, cx, cy, 窗口设备上下文句柄, x1, y1, 0x00CC0020)
    总字节数 = int(cx * cy * 4)
    # 图像缓冲区 = bytearray(总字节数)
    图像缓冲区 = _动态属性化(bytearray, width=cx, height=cy)(总字节数)
    ctypes.memmove((ctypes.c_ubyte * 总字节数).from_buffer(图像缓冲区), 像素数据指针.value, 总字节数)
    SelectObject(内存设备上下文句柄, 原对象句柄)
    DeleteObject(位图句柄)

    DeleteDC(内存设备上下文句柄)
    ReleaseDC(hwnd, 窗口设备上下文句柄)
    return 图像缓冲区

def StretchBlt截图(wDest: int, hDest: int, xSrc: int, ySrc: int, wSrc: int, hSrc: int, hwnd: wintypes.HWND = user32.GetDesktopWindow()) -> bytes:
    '''
    function: 通过 StretchBlt 对 hwnd 对应 窗口进行后台截图并缩放.\n
    param wDest, hDest: 目标矩形的宽高（以逻辑单位为单位）, 即要缩放后的区域大小.\n
    param xSrc, ySrc: 源矩形的坐标（以逻辑单位为单位）, 即相对于窗口左上角的相对坐标.\n
    param wSrc, hSrc: 源矩形的宽高（以逻辑单位为单位）, 即要截取的窗口区域大小.\n
    param hwnd: 窗口句柄
    return: 返回二进制格式的BGRA图像数据
    注意事项:
    1. 建议使用前 设置DPI感知, 否则很可能出现DPI问题, 已提供 设置DPI感知 函数 方便调用.
    2. 针对后台窗口截图, 可能出现 全黑 或者 全白 等截图 问题, 建议配合 PrintWindow截图 按需交替使用.
    3. 截图的图像数据为 BGRA 格式, 即 4 个字节分别表示 BGRA 四通道颜色值.
    '''
    窗口设备上下文句柄 = GetWindowDC(hwnd)
    内存设备上下文句柄 = CreateCompatibleDC(窗口设备上下文句柄)
    _BITMAPINFO结构体 = BITMAPINFO()
    _BITMAPINFO结构体.bmiHeader.biWidth = wDest
    _BITMAPINFO结构体.bmiHeader.biHeight = -hDest # 负值表示自上而下更符合现代编程习惯
    像素数据指针 = wintypes.LPVOID()

    
    位图句柄 = CreateDIBSection(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)
    原对象句柄 = SelectObject(内存设备上下文句柄, 位图句柄)
    StretchBlt操作结果 = StretchBlt(内存设备上下文句柄, 0, 0, wDest, hDest, 窗口设备上下文句柄, xSrc, ySrc, wSrc, hSrc, 0x00CC0020)
    总字节数 = int(wDest * hDest * 4)
    # 图像缓冲区 = bytearray(总字节数)
    图像缓冲区 = _动态属性化(bytearray, width=wDest, height=hDest)(总字节数)

    ctypes.memmove((ctypes.c_ubyte * 总字节数).from_buffer(图像缓冲区), 像素数据指针.value, 总字节数)
    SelectObject(内存设备上下文句柄, 原对象句柄)
    DeleteObject(位图句柄)

    DeleteDC(内存设备上下文句柄)
    ReleaseDC(hwnd, 窗口设备上下文句柄)
    return 图像缓冲区

def PrintWindow截图(w: int, h: int, hwnd: wintypes.HWND) -> bytes:
    '''
    function: 通过 PrintWindow 对 hwnd 对应 窗口进行后台截图, 建议使用前 设置DPI感知 避免DPI问题.\n
    param w, h: 目标窗口的宽高（以逻辑单位为单位）.\n
    param hwnd: 窗口句柄\n
    return: 返回二进制格式的BGRA图像数据
    注意事项:
    1. 建议使用前 设置DPI感知, 否则很可能出现DPI问题, 已提供 设置DPI感知 函数 方便调用.
    2. 针对后台窗口截图, 可能出现 全黑 或者 全白 等截图 问题, 建议配合 BitBlt截图 按需交替使用.
    3. 截图的图像数据为 BGRA 格式, 即 4 个字节分别表示 BGRA 四通道颜色值.
    '''
    窗口设备上下文句柄 = GetWindowDC(hwnd)
    内存设备上下文句柄 = CreateCompatibleDC(窗口设备上下文句柄)

    _BITMAPINFO结构体 = BITMAPINFO()
    _BITMAPINFO结构体.bmiHeader.biWidth = w
    _BITMAPINFO结构体.bmiHeader.biHeight = -h # 负值表示自上而下更符合现代编程习惯
    像素数据指针 = wintypes.LPVOID()
    位图句柄 = CreateDIBSection(内存设备上下文句柄, ctypes.byref(_BITMAPINFO结构体), 0, ctypes.byref(像素数据指针), None, 0)
    原对象句柄 = SelectObject(内存设备上下文句柄, 位图句柄)
    PrintWindow操作结果 = PrintWindow(hwnd, 内存设备上下文句柄, 0x00000002)
    总字节数 = int(w * h * 4)
    # 图像缓冲区 = bytearray(总字节数)
    图像缓冲区 = _动态属性化(bytearray, width=w, height=h)(总字节数)

    ctypes.memmove((ctypes.c_ubyte * 总字节数).from_buffer(图像缓冲区), 像素数据指针.value, 总字节数)
    SelectObject(内存设备上下文句柄, 原对象句柄)
    DeleteObject(位图句柄)

    DeleteDC(内存设备上下文句柄)
    ReleaseDC(hwnd, 窗口设备上下文句柄)
    return 图像缓冲区

def 获取窗口位置(hwnd: wintypes.HWND = user32.GetDesktopWindow()) -> tuple[int, int, int, int]:
    '''
    function: 获取窗口 left, top, right, bottom 坐标\n
    param hwnd: 窗口句柄\n
    return: 返回窗口 left(左边), top(顶边), right(右边), bottom(底边) 坐标
    '''
    窗口矩形 = wintypes.RECT()
    GetWindowRect(hwnd, ctypes.byref(窗口矩形))
    return 窗口矩形.left, 窗口矩形.top, 窗口矩形.right, 窗口矩形.bottom

def 设置DPI感知(PROCESS_DPI_AWARENESS: int = 2):
    '''
    function: 设置进程默认 DPI 感知级别, 建议在程序启动时调用并设置为 PROCESS_DPI_AWARENESS = 2, 否则大部分现代显示器无法正确进行截图或相关操作.\n
    param PROCESS_DPI_AWARENESS: 0: 不感知, 1: 系统 DPI 感知, 2: 按监视器 DPI 感知.\n
    return: 0 (S_OK) 表示设置成功，负数表示失败。
    '''
    return SetProcessDpiAwareness(PROCESS_DPI_AWARENESS)

def 前台窗口截图(hwnd: wintypes.HWND = user32.GetDesktopWindow()) -> bytes:
    '''
    function: 获取前台窗口截图.
    param hwnd: 窗口句柄, 默认值为桌面窗口句柄.
    return: 返回二进制格式的BGRA图像数据
    注意事项:
    1. 建议使用前 设置DPI感知, 否则很可能出现DPI问题, 已提供 设置DPI感知 函数 方便调用.
    2. 截图的图像数据为 BGRA 格式, 即 4 个字节分别表示 BGRA 四通道颜色值.
    3. 由于是 前台窗口截图, 如果窗口被遮挡, 则截图结果也会被遮挡.
    '''
    left, top, right, bottom = 获取窗口位置(hwnd)
    return BitBlt截图(left, top, right - left, bottom - top, hwnd)

def 全屏截图() -> bytes:
    '''
    function: 获取全屏幕截图.\n
    return: 返回二进制格式的BGRA图像数据
    注意事项:
    1. 建议使用前 设置DPI感知, 否则很可能出现DPI问题, 已提供 设置DPI感知 函数 方便调用.
    1. 截图的图像数据为 BGRA 格式, 即 4 个字节分别表示 BGRA 四通道颜色值.
    '''
    return 前台窗口截图()

def 保存图片(位图数据: bytes, 保存路径: str, *, 宽度: int = None, 高度: int = None):
    '''
    function: 保存位图数据为图片文件.\n
    param 位图数据: 二进制格式的BGRA图像数据.\n
    param 宽度 高度: 图像宽高, 如果是通过 `本库` 中的方法获取的位图数据, 则不需要设置.\n
    param 保存路径: 要存放的图片文件路径, 建议保存为 bmp 格式.\n
    '''
    if not (宽度 or 高度):
        宽度, 高度 = 位图数据.width, 位图数据.height
    # 创建BMP文件头
    文件头 = struct.pack('<2sIHHI', b'BM', 54 + len(位图数据), 0, 0, 54)
    # 创建BMP信息头
    信息头 = struct.pack('<iiiHHIIIIII', 40, 宽度, -高度, 1, 32, 0, len(位图数据), 0, 0, 0, 0)

    os.makedirs(os.path.dirname(os.path.abspath(保存路径)), exist_ok=True)
    # 写入文件(BMP要求数据从下到上存储)
    with open( fr'\\?\{os.path.abspath(保存路径)}', 'wb') as 文件:
        文件.write(文件头 + 信息头 + 位图数据)

