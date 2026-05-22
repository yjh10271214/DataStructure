import cv2
import numpy as np

IMAGE_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

def rgb_to_yuv(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.147 * r - 0.289 * g + 0.436 * b + 128  # Cb
    v = 0.615 * r - 0.515 * g - 0.100 * b + 128   # Cr
    return y, u, v
    

bgr_frame = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
if bgr_frame is None:
    print("open image is error")

cv2.imwrite("./1.png", bgr_frame)

print(f"open image is shape: {bgr_frame.shape}")

yuv_frame_1 = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2YUV)
cv2.imwrite("./4.png", yuv_frame_1)

rgb_frame = bgr_frame[:, :, ::-1] #rgb
cv2.imwrite("./2.png", rgb_frame)

yuv_frame = np.empty_like(rgb_frame)
yuv_frame[:, : , 0], yuv_frame[:, :, 1], yuv_frame[:, :, 2] = rgb_to_yuv(rgb_frame[:, :, 0], rgb_frame[:, :, 1], rgb_frame[:, :, 2])

cv2.imwrite("./3.png", yuv_frame)









