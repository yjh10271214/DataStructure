import cv2
import numpy as np


IMAGE_IN_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

# def on_trackbar(val):
#     """回调函数，用来处理滑动条变化事件"""
#     current_value = cv2.getTrackbarPos("Brightness", "Trackbar Example")  # 获取当前滑动条的值
#     print(f"当前滑动条值：{current_value}")


# if __name__ == '__main__':
#     image = np.zeros((200, 400, 3), dtype=np.uint8)
#     cv2.imshow("Trackbar Example", image)  # 创建窗口

#     cv2.createTrackbar("Brightness", "Trackbar Example", 0, 255, on_trackbar)  # 创建滑动条
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

image = cv2.imread(IMAGE_IN_PATH)
cv2.imshow('image', image)  # 创建窗口
cv2.createTrackbar('threshold', 'image', 0, 255, lambda x: None)  # 创建阈值滑动条
while True:
    threshold_value = cv2.getTrackbarPos('threshold', 'image')  # 获取滑动条的阈值
    threshold_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)[1]  # 阈值图像
    cv2.imshow('image', threshold_image)
    if cv2.waitKey(1) == 27:  # Esc退出
        break
cv2.destroyAllWindows()

"""#########################################################################
# 功能说明：创建一个滑动条控件，放置在指定的窗口中，并绑定一个回调函数。———— 当滑动条的值变化时，回调函数会被触发。
# 函数说明: cv2.createTrackbar(Track_name, img, min, max, TrackbarCallback)
# 输入参数：
#         Track_name：		滑动条的名称，必须是一个字符串
#         img：				滑动条所在的窗口或画布
#         min：				滑动条的最小值
#         max：				滑动条的最大值
#         TrackbarCallback：当滑动条值变化时，被调用的回调函数。此函数必须接受一个参数，表示滑动条当前的值。
#########################################################################"""

"""#########################################################################
# 功能说明：获取滑动条的值
# 函数说明：value = cv2.getTrackbarPos(Track_name, img)
# 输入参数：
#         Track_name：		滑动条的名称
#         img：				滑动条所在的窗口或画布
# 输出参数：
#         当前滑动条所在位置的数值（整数）
#########################################################################"""
