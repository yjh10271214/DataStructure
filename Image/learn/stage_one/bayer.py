import cv2
import numpy as np

IMAGE_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

frame = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
if frame is None:
    print("open image error")
print(f"frame is shape: {frame.shape}")

frame = cv2.resize(frame, (256, 256))
if frame is None:
    print("open image error")
print(f"frame is shape: {frame.shape}")

frame = frame[:, :, ::-1] # Convert BGR to RGB
cv2.imwrite("1.png", frame)

# Print first 16x16 RGB pixels
# print("RGB image 16x16 pixels:")
# for i in range(16):
#     for j in range(16):
#         pixel = frame[i, j]
#         print(f"({pixel[0]:3d},{pixel[1]:3d},{pixel[2]:3d})", end=" ")
#     print()  # New line after each row
# print("\n" + "="*50 + "\n")

bayer_pattern = np.zeros((256, 256, 1), dtype=np.uint8)
# bayer pattern RGGB
for i in range(frame.shape[0]):
    for j in range(frame.shape[0]):
        if (i % 2 == 0): 
            if (j % 2 == 0): # R
                bayer_pattern[i, j] = frame[i, j, 0]
            elif (j % 2 == 1): # G
                bayer_pattern[i, j] = frame[i, j, 1]
        
        if (i % 2 == 1):
            if (j % 2 == 0): # G
                bayer_pattern[i, j] = frame[i, j, 1]
            elif (j % 2 == 1): # B
                bayer_pattern[i, j] = frame[i, j, 2]

cv2.imwrite("2.png", bayer_pattern)
# cv2.imshow("mosaic.png", bayer_pattern)

# Print first 16x16 Bayer pixels
# print("Bayer pattern 16x16 pixels:")
# for i in range(16):
#     for j in range(16):
#         pixel = bayer_pattern[i, j][0]
#         print(f"{pixel:3d}", end=" ")
#     print()  # New line after each row