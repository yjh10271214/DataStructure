import cv2

IMAGE_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

frame = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
if frame is None:
    print("open color[" + IMAGE_PATH + "] fail...")
    exit(-1)

print(f"color image shape: {frame.shape}")


gray_frame = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
if gray_frame is None:
    print("open grayscale[" + IMAGE_PATH + "] fail...")
    exit(-1)

print(f"gray image shape: {gray_frame.shape}")









