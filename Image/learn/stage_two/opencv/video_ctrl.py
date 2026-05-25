"""
（1）点击空格键暂停视频播放，再次点击空格键继续播放。
（2）按 Esc 键退出程序
"""
import cv2

# （1）读取视频
video_path = r"D:\opencv-master\opencv-master\samples\data\vtest.avi"
cap = cv2.VideoCapture(video_path)  # 初始化视频捕捉对象

# （2）检查视频是否可以打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# （3）获取视频属性
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频宽度
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频高度
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 总帧数
fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 指定视频编码格式

# （4）初始化 VideoWriter
output_path = "./output_video.avi"  # 保存路径
isColor = True  # 保存图像为灰度图还是彩色图
out = cv2.VideoWriter(filename=output_path, fourcc=fourcc, fps=fps, frameSize=(frame_width, frame_height), isColor=isColor)

# （5）读取帧 + 保存帧 + 显示帧
paused = False  # 控制是否暂停播放
while True:
    if not paused:  # 只有在没有暂停时，才读取和显示新的一帧
        ret, frame = cap.read()  # 读取帧
        if not ret:
            print("Error: Failed to read frame or video end reached.")
            break
        out.write(frame)  # 保存帧
        cv2.imshow('Video', frame)  # 显示帧
        ## 为什么会产生视频效果? ———— 循环读取每一帧，并将其固定显示在同一个窗口上，则后一帧会覆盖前一帧，就产生了视频效果。

    key = cv2.waitKey(100) & 0xFF  # 获取按键（控制速度）
    if key == 27:  # 按Esc键退出
        break
    elif key == 32:  # 按空格键暂停/继续
        paused = not paused  # 切换暂停状态

# （6）释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

"""#############################################################################################
# 函数功能：用于打开视频文件、摄像头或其他视频设备，并从中读取视频帧。
# 函数说明：cap = cv2.VideoCapture([filename or device index])
# 参数说明：
#         filename or device index：输入的视频文件路径或视频设备索引。
#             - 如果是文件路径，指定要打开的影片文件（如 'video.mp4'）。
#             - 如果是设备索引，指定打开的摄像头，通常索引为 0 表示默认摄像头，1 表示第二个摄像头，以此类推。
#             - 如果设备不可用或路径无效，函数返回失败。
# 返回值：
#         如果打开成功，返回一个 `cv2.VideoCapture` 对象，用于读取视频帧。如果失败，则返回空对象。
# 常用方法：
#         1. `cap.read()`：从视频流中读取一帧图像，返回两个值，布尔值和帧图像。如果成功读取，布尔值为 True，帧图像为读取的图像矩阵。
#         2. `cap.isOpened()`：检查视频文件或设备是否成功打开。
#         3. `cap.get(propId)`：获取视频文件的属性，例如帧宽度、高度、帧率等。
#         4. `cap.set(propId, value)`：设置视频文件的属性，如设置帧的宽度和高度等。
#         5. `cap.release()` 释放资源。
#############################################################################################"""


"""#############################################################################################
# 函数功能：用于指定视频编解码器的四字符代码（FourCC），FourCC 是一个 4 字节的代码。常用于定义视频保存时的编码格式，例如 AVI、MP4 等。
# 函数说明：fourcc = cv2.VideoWriter_fourcc(c1, c2, c3, c4)
# 参数说明：
#         c1, c2, c3, c4：构成 FourCC 编解码器标识符的四个字符。常见的 FourCC 值：
#             - 'XVID': OpenDivX 编解码器     文件扩展名：.avi            适用于需要良好兼容性并且对压缩效率要求不高的场景。
#             - 'DIVX': DivX 编解码器         文件扩展名：.avi            适用于需要中等压缩质量和高质量视频的应用。支持逐渐下降
#             - 'MJPG': Motion JPEG 编解码器  文件扩展名：.avi 或.mp4     适用于需要快速编码且每帧独立，但输出视频文件较大，缺乏帧间压缩。
#             - 'MP4V': MPEG-4 编解码器       文件扩展名：.mp4            适用于需要中等压缩效果和较好兼容性的应用，尤其是在较老的设备上使用。
#             - 'H264': 高级视频编码标准        文件扩展名：.mp4            适用于需要高压缩效率、文件较小且质量较高的场景。H264 是最常用的现代视频编码标准。
# 返回值：
#         返回一个整数，表示对应的 FourCC 编解码器标识符。
#############################################################################################"""

"""#############################################################################################
# 函数功能：用于创建一个视频写入对象，方便将帧数据保存为视频文件。
# 函数说明：out = cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=True)
# 参数说明：
#         filename：字符串，保存视频的文件名及路径。例如 'output.avi'。
#         fourcc：编码器的四字符代码，使用 `cv2.VideoWriter_fourcc()` 创建。
#         fps：每秒帧数（帧率），指定视频播放的帧速率。
#         frameSize：元组，表示视频帧的宽度和高度，例如 (640, 480)。
#         isColor：布尔值，是否保存为彩色视频。默认值为 True（彩色），若为 False，则保存为灰度视频。
# 返回值：
#         返回一个 cv2.VideoWriter 对象，用于向视频文件写入帧。
# 使用步骤：
#         1. 使用 `fourcc = cv2.VideoWriter_fourcc()` 创建编码器标识符。
#         2. 调用 `out = cv2.VideoWriter` 创建视频写入对象。
#         3. 使用 `out.write(frame)` 方法将帧写入视频。
#         4. 调用 `out.release()` 释放资源。
#############################################################################################"""
