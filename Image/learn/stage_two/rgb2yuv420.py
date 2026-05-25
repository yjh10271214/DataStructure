import cv2
import numpy as np

IMAGE_IN_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"
IMAGE_OUT_PATH = "./output.yuv"

def rgb_to_yuv(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.14713 * r - 0.28886 * g + 0.436 * b + 128  # Added +128 to center at 128
    v = 0.615 * r - 0.51499 * g - 0.10001 * b + 128   # Added +128 to center at 128
    return y, u, v


def process_image_to_yuv420():
    bgr_frame = cv2.imread(IMAGE_IN_PATH, cv2.IMREAD_COLOR)
    if bgr_frame is None:
        print("open image error")
        exit(-1)

    img_rgb = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)

    # BGR转灰度
    img_gray = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)

    # BGR转YUV
    img_yuv = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2YUV)
    img_i420 = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2YUV_I420)
    print(f"手动生成的YUV420大小: {len(open('output.yuv', 'rb').read())} 字节")
    print(f"OpenCV生成的YUV420大小: {img_i420.size} 字节")
    # BGR转HSV
    img_hsv = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2HSV)

    # 看看每种格式的shape有什么区别
    print(f"BGR: {bgr_frame.shape}, 灰度: {img_gray.shape}, YUV: {img_yuv.shape}")

    rgb_frame = bgr_frame[:, :, ::-1]
    h, w = rgb_frame.shape[:2]
    
    # Ensure height and width are even numbers for YUV420
    h = h - h % 2
    w = w - w % 2
    rgb_frame = rgb_frame[:h, :w]
    
    # Convert RGB to YUV444 (floating point first)
    y = np.zeros((h, w), dtype=np.float32)
    u = np.zeros((h, w), dtype=np.float32)
    v = np.zeros((h, w), dtype=np.float32)
    y[:, :], u[:, :], v[:, :] = rgb_to_yuv(rgb_frame[:, :, 0], 
                                          rgb_frame[:, :, 1], 
                                          rgb_frame[:, :, 2])
    
    # Convert to uint8 after clamping
    y = np.clip(y, 0, 255).astype(np.uint8)
    u = np.clip(u, 0, 255).astype(np.uint8)
    v = np.clip(v, 0, 255).astype(np.uint8)
    
    # Downsample U and V to YUV420
    u420 = np.zeros((h//2, w//2), dtype=np.uint8)
    v420 = np.zeros((h//2, w//2), dtype=np.uint8)
    
    for i in range(0, h, 2):
        for j in range(0, w, 2):
            # Calculate average of 2x2 block
            u420[i//2, j//2] = (u[i, j].astype(np.uint16) + u[i+1, j] + u[i, j+1] + u[i+1, j+1]) // 4
            v420[i//2, j//2] = (v[i, j].astype(np.uint16) + v[i+1, j] + v[i, j+1] + v[i+1, j+1]) // 4

    # Write to file in YUV420 planar format (Y then U then V)
    with open(IMAGE_OUT_PATH, "wb") as f:
        f.write(y.tobytes())
        f.write(u420.tobytes())
        f.write(v420.tobytes())


if __name__ == "__main__":
    process_image_to_yuv420()