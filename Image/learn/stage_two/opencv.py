import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

src_img = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
if src_img is None:
    print("open img faild")
    exit(-1)

h, w = src_img.shape[:2]
print(f"src_imag shape: {src_img.shape}")
cv2.imwrite("./src_imag.png", src_img)

interplation_linear_img = cv2.resize(src_img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite("./interplation_linear_img.png", interplation_linear_img)
interplation_cubic_img = cv2.resize(src_img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imwrite("./interplation_cubic_img.png", interplation_cubic_img)

horizontal_flip = cv2.flip(src_img, 1)
cv2.imwrite("./horizontal_flip.png", horizontal_flip)
vertical_flip = cv2.flip(src_img, 0)
cv2.imwrite("./vertical_flip.png", vertical_flip)
both_flip = cv2.flip(src_img, -1)
cv2.imwrite("./both_flip.png", both_flip)

#旋转
M = cv2.getRotationMatrix2D((h//2, w//2), 45, 1.0)
rotated_img = cv2.warpAffine(src_img, M, (h, w))
cv2.imwrite("./rotated_img.png", rotated_img)

src_pts = np.float32([[50,50], [200,50], [50,200]])
dst_pts = np.float32([[10,100], [200,50], [100,250]])

#仿射变换
M = cv2.getAffineTransform(src_pts, dst_pts)
affined_img = cv2.warpAffine(src_img, M, (h, w))
cv2.imwrite("./affined_img.png", affined_img)

#透视变换
src_pts = np.float32([[56,65],[368,52],[28,387],[389,390]])
dst_pts = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(src_pts, dst_pts)
perspected_img = cv2.warpPerspective(src_img, M, (300,300))
cv2.imwrite("./perspected_img.png", perspected_img)

img = cv2.cvtColor(src_img, cv2.COLOR_RGB2GRAY)
# 添加椒盐噪声
def add_salt_pepper_noise(image, salt_prob, pepper_prob):
    noisy = image.copy()
    total_pixels = image.size
    
    # 添加盐噪声(白色像素)
    salt_pixels = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i-1, salt_pixels) for i in image.shape]
    noisy[salt_coords[0], salt_coords[1]] = 255
    
    # 添加胡椒噪声(黑色像素)
    pepper_pixels = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i-1, pepper_pixels) for i in image.shape]
    noisy[pepper_coords[0], pepper_coords[1]] = 0
    
    return noisy

noisy_img = add_salt_pepper_noise(img, 0.01, 0.01)

# 应用四种滤波方法
mean_filtered = cv2.blur(noisy_img, (5,5))
gaussian_filtered = cv2.GaussianBlur(noisy_img, (5,5), 0)
median_filtered = cv2.medianBlur(noisy_img.astype('float32'), 5)
bilateral_filtered = cv2.bilateralFilter(noisy_img, 9, 75, 75)

# # 显示结果
# plt.figure(figsize=(15,10))

# plt.subplot(2,3,1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.axis('off')

# plt.subplot(2,3,2), plt.imshow(noisy_img, cmap='gray')
# plt.title('Noisy Image'), plt.axis('off')

# plt.subplot(2,3,3), plt.imshow(mean_filtered, cmap='gray')
# plt.title('Mean Filter'), plt.axis('off')

# plt.subplot(2,3,4), plt.imshow(gaussian_filtered, cmap='gray')
# plt.title('Gaussian Filter'), plt.axis('off')

# plt.subplot(2,3,5), plt.imshow(median_filtered, cmap='gray')
# plt.title('Median Filter'), plt.axis('off')

# plt.subplot(2,3,6), plt.imshow(bilateral_filtered, cmap='gray')
# plt.title('Bilateral Filter'), plt.axis('off')

# plt.tight_layout()
# plt.show()

# x方向梯度(垂直边缘)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# y方向梯度(水平边缘)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# 合并梯度
sobel = np.sqrt(sobelx**2 + sobely**2)

# Laplacian算子
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

# Canny边缘检测
# 默认阈值
canny_default = cv2.Canny(img, 100, 200)
# 调整阈值后的示例
canny_adjusted = cv2.Canny(img, 50, 150)

# 可视化所有结果
plt.figure(figsize=(15, 10))

# Sobel算子结果
plt.subplot(2,3,1), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X (Vertical Edges)'), plt.axis('off')

plt.subplot(2,3,2), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y (Horizontal Edges)'), plt.axis('off')

plt.subplot(2,3,3), plt.imshow(sobel, cmap='gray')
plt.title('Sobel Combined'), plt.axis('off')

# Laplacian算子结果
plt.subplot(2,3,4), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian (Both Directions)'), plt.axis('off')

# Canny边缘检测结果
plt.subplot(2,3,5), plt.imshow(canny_default, cmap='gray')
plt.title('Canny Default (100,200)'), plt.axis('off')

plt.subplot(2,3,6), plt.imshow(canny_adjusted, cmap='gray')
plt.title('Canny Adjusted (50,150)'), plt.axis('off')

plt.tight_layout()
plt.show()




















