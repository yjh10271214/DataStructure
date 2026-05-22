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

frame = frame[:, :, ::-1]  # Convert BGR to RGB
cv2.imwrite("1.png", frame)

bayer_pattern = np.zeros((256, 256, 1), dtype=np.uint8)
# bayer pattern RGGB
for i in range(frame.shape[0]):
    for j in range(frame.shape[1]):  # 这里修复：原来是 frame.shape[0]
        if (i % 2 == 0):
            if (j % 2 == 0):  # R
                bayer_pattern[i, j, 0] = frame[i, j, 0]
            elif (j % 2 == 1):  # G
                bayer_pattern[i, j, 0] = frame[i, j, 1]

        if (i % 2 == 1):
            if (j % 2 == 0):  # G
                bayer_pattern[i, j, 0] = frame[i, j, 1]
            elif (j % 2 == 1):  # B
                bayer_pattern[i, j, 0] = frame[i, j, 2]

cv2.imwrite("2.png", bayer_pattern)

rgb_image = np.zeros((256, 256, 3), dtype=np.uint8)
for i in range(bayer_pattern.shape[0]):
    for j in range(bayer_pattern.shape[1]):
        if (i % 2 == 0):
            if (j % 2 == 0):  # R
                rgb_image[i, j, 0] = bayer_pattern[i, j, 0]  # r
                if i == 0 and j == 0:  # 左上角元素
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j+1, 0]) + int(bayer_pattern[i+1, j, 0])) // 2  # g
                    rgb_image[i, j, 2] = bayer_pattern[i+1, j+1, 0]  # b
                elif i == 0:
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # g
                    rgb_image[i, j, 2] = (int(bayer_pattern[i+1, j-1, 0]) + int(bayer_pattern[i+1, j+1, 0])) // 2  # b
                elif j == 0:
                    rgb_image[i, j, 1] = (int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # g
                    rgb_image[i, j, 2] = (int(bayer_pattern[i-1, j+1, 0]) + int(bayer_pattern[i+1, j+1, 0])) // 2  # b
                else:
                    rgb_image[i, j, 1] = (int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i+1, j, 0]) + int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 4  # g
                    rgb_image[i, j, 2] = (int(bayer_pattern[i-1, j-1, 0]) + int(bayer_pattern[i-1, j+1, 0]) + int(bayer_pattern[i+1, j-1, 0]) + int(bayer_pattern[i+1, j+1, 0])) // 4  # b

            elif (j % 2 == 1):  # G
                rgb_image[i, j, 1] = bayer_pattern[i, j, 0]  # g
                if i == 0 and j == 255:  # 右上角
                    rgb_image[i, j, 0] = bayer_pattern[i, j-1, 0]  # r
                    rgb_image[i, j, 2] = bayer_pattern[i+1, j, 0]  # b
                elif i == 0:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # r
                    rgb_image[i, j, 2] = bayer_pattern[i+1, j, 0]  # b
                elif j == 255:
                    rgb_image[i, j, 0] = bayer_pattern[i, j-1, 0]  # r
                    rgb_image[i, j, 2] = (int(bayer_pattern[i+1, j, 0]) + int(bayer_pattern[i-1, j, 0])) // 2  # b
                else:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # r
                    rgb_image[i, j, 2] = (int(bayer_pattern[i+1, j, 0]) + int(bayer_pattern[i-1, j, 0])) // 2  # b

        if (i % 2 == 1):
            if (j % 2 == 0):  # G
                rgb_image[i, j, 1] = bayer_pattern[i, j, 0]  # g
                if i == 255 and j == 0:  # 左下角
                    rgb_image[i, j, 0] = bayer_pattern[i-1, j, 0]  # r
                    rgb_image[i, j, 2] = bayer_pattern[i, j+1, 0]  # b
                elif j == 0:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i+1, j, 0])) // 2  # r
                    rgb_image[i, j, 2] = bayer_pattern[i, j+1, 0]  # b
                elif i == 255:
                    rgb_image[i, j, 0] = bayer_pattern[i-1, j, 0]  # r
                    rgb_image[i, j, 2] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # b
                else:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i+1, j, 0])) // 2  # r
                    rgb_image[i, j, 2] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0])) // 2  # b

            elif (j % 2 == 1):  # B
                rgb_image[i, j, 2] = bayer_pattern[i, j, 0]  # b
                if i == 255 and j == 255:
                    rgb_image[i, j, 0] = bayer_pattern[i-1, j-1, 0]  # r
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i-1, j, 0])) // 2  # g
                elif j == 255:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i-1, j-1, 0]) + int(bayer_pattern[i+1, j-1, 0])) // 2  # r
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i+1, j, 0])) // 3  # g
                elif i == 255:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i-1, j-1, 0]) + int(bayer_pattern[i-1, j+1, 0])) // 2  # r
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0]) + int(bayer_pattern[i-1, j, 0])) // 3  # g
                else:
                    rgb_image[i, j, 0] = (int(bayer_pattern[i-1, j-1, 0]) + int(bayer_pattern[i-1, j+1, 0]) + int(bayer_pattern[i+1, j-1, 0]) + int(bayer_pattern[i+1, j+1, 0])) // 4  # r
                    rgb_image[i, j, 1] = (int(bayer_pattern[i, j-1, 0]) + int(bayer_pattern[i, j+1, 0]) + int(bayer_pattern[i-1, j, 0]) + int(bayer_pattern[i+1, j, 0])) // 4  # g

cv2.imwrite("3.png", rgb_image)

//1.yuv格式,可以按比例来储存，按需选择格式，将人眼最敏感的y分量无损保留下来，uv就是按需来，batyer pattern的格式也是有两个g也是因为人眼最敏感
//2.opencv里面用的是bgr格式记得转换[start:end:step] [::-1]倒序读取
//3.sensor上接收到的数据是一个像素只有一个颜色通过滤光片，RGGB，BGGR，GRBG， GBRG，得到的元数据是带mosiac的，所以需要demosiac,
raw8,raw10,raw12:元数据的存储大小，8就是一个像素8bit也就是一字节，10就是10bit但是是两个字节6bit不使用，12类似
