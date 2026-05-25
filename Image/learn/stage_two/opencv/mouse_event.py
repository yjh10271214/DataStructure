import time
import cv2
import numpy as np

last_time = 0  # 初始化上次时间
def mouse_callback(event, x, y, flags, param):
    """回调函数，用来处理鼠标事件"""
    global last_time

    # 处理鼠标移动事件
    if event == cv2.EVENT_MOUSEMOVE:
        current_time = time.time()  # 获取当前时间
        # 如果距离上次事件超过3秒，则打印并更新last_time
        if current_time - last_time > 3:
            print(f"Mouse moved to ({x}, {y})")
            last_time = current_time  # 更新上次触发时间

    # 处理鼠标左键按下事件
    elif event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")

    # 处理鼠标左键释放事件
    elif event == cv2.EVENT_LBUTTONUP:
        print(f"Left button released at ({x}, {y})")

    # 处理鼠标右键按下事件
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")

    # 处理鼠标右键释放事件
    elif event == cv2.EVENT_RBUTTONUP:
        print(f"Right button released at ({x}, {y})")

    # 处理鼠标中键按下事件
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"Middle button clicked at ({x}, {y})")

    # 处理鼠标中键释放事件
    elif event == cv2.EVENT_MBUTTONUP:
        print(f"Middle button released at ({x}, {y})")

    # 处理鼠标左键双击事件
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print(f"Left button double clicked at ({x}, {y})")

    # 处理鼠标右键双击事件
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print(f"Right button double clicked at ({x}, {y})")

    # 处理鼠标中键双击事件
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print(f"Middle button double clicked at ({x}, {y})")

    # 处理鼠标滚轮事件
    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            print(f"Mouse wheel moved up at ({x}, {y})")
        else:
            print(f"Mouse wheel moved down at ({x}, {y})")

    # 处理鼠标横向滚轮事件
    elif event == cv2.EVENT_MOUSEHWHEEL:
        if flags > 0:
            print(f"Mouse horizontal wheel moved right at ({x}, {y})")
        else:
            print(f"Mouse horizontal wheel moved left at ({x}, {y})")


if __name__ == "__main__":
    image = 255 * np.ones(shape=(500, 500, 3), dtype=np.uint8)
    cv2.imshow("Mouse Event", image)

    # 设置鼠标事件回调
    cv2.setMouseCallback("Mouse Event", mouse_callback)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""##########################################################################
# 函数功能：设置鼠标事件回调函数 ———— 它允许用户为窗口设置一个回调函数，当在该窗口上触发鼠标事件时，回调函数会被调用。
# 函数说明：cv2.setMouseCallback(windowName, MouseCallback, param=None)
# 输入参数：
#         windowName：         窗口名称，指定用于设置回调的窗口。
#         MouseCallback：      鼠标响应回调函数，当鼠标事件发生时会自动调用该函数。
#         param：              传递给回调函数的额外参数，默认为 None。
##########################################################################"""


"""##########################################################################
# 函数功能：鼠标事件回调函数 ————  这是一个用户自定义的函数，用于处理鼠标事件。
# 函数说明：MouseCallback(int event, int x, int y, int flags,  *userdata)
# 输入参数：
#         event：      鼠标事件类型，表示鼠标的不同操作（如点击、移动、双击等）。常见的事件类型包括：
#                             (1) cv2.EVENT_MOUSEMOVE      = 0      鼠标移动
#                             (2) cv2.EVENT_LBUTTONDOWN    = 1      左键按下
#                             (3) cv2.EVENT_RBUTTONDOWN    = 2      右键按下
#                             (4) cv2.EVENT_MBUTTONDOWN    = 3      中键按下
#                             (5) cv2.EVENT_LBUTTONUP      = 4      左键释放
#                             (6) cv2.EVENT_RBUTTONUP      = 5      右键释放
#                             (7) cv2.EVENT_MBUTTONUP      = 6      中键释放
#                             (8) cv2.EVENT_LBUTTONDBLCLK  = 7      左键双击
#                             (9) cv2.EVENT_RBUTTONDBLCLK  = 8      右键双击
#                             (10) cv2.EVENT_MBUTTONDBLCLK = 9      中键双击
#                             (11) cv2.EVENT_MOUSEWHEEL    = 10     滚轮滑动（滚动方向：向上滚动时通常是负值，向下滚动时是正值）
#                             (12) cv2.EVENT_MOUSEHWHEEL   = 11     横向滚轮滑动（较少使用）
#         x, y：       鼠标在窗口中的位置，表示鼠标事件发生时的坐标。
#         flags：      鼠标按键和键盘修饰符，用于传递额外的信息（如 Ctrl、Shift 或 Alt）。常见的标志包括：
#                             (1) cv2.EVENT_FLAG_LBUTTON   = 1      左键按下标志。与 EVENT_LBUTTONDOWN 一起使用。
#                             (2) cv2.EVENT_FLAG_RBUTTON   = 2      右键按下标志。与 EVENT_RBUTTONDOWN 一起使用。
#                             (3) cv2.EVENT_FLAG_MBUTTON   = 4      中键按下标志。与 EVENT_MBUTTONDOWN 一起使用。
#                             (4) cv2.EVENT_FLAG_CTRLKEY   = 8      Ctrl 键按下标志
#                             (5) cv2.EVENT_FLAG_SHIFTKEY  = 16     Shift 键按下标志
#                             (6) cv2.EVENT_FLAG_ALTKEY    = 32     Alt 键按下标志
#         userdata：   可选参数，可用于传递额外的自定义数据给回调函数（例如图像对象等）。
#
# 鼠标事件组合（示例）
#     cv2.EVENT_LBUTTONDOWN + cv2.EVENT_FLAG_CTRLKEY      表示鼠标左键按下时同时按下了 Ctrl 键。
#     cv2.EVENT_LBUTTONUP + cv2.EVENT_FLAG_ALTKEY         表示鼠标左键松开时按下了 Alt 键。
##########################################################################"""
