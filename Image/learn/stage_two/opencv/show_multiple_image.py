import numpy as np
import cv2  # opencv读取图像默认为BGR
import matplotlib.pyplot as plt  # matplotlib显示图像默认为RGB

IMAGE_IN_PATH = "/media/yjh/_dde_home/yjh/上传/260521/1.png"

# image = cv2.imread(IMAGE_IN_PATH)
# image = image[:, :, ::-1]
# res_horizontal = np.hstack((image, image))  # 水平方向堆叠图像
# res_vertical = np.vstack((image, image))  # 竖直方向堆叠图像

# plt.subplot(1, 3, 1), plt.imshow(image), plt.title('image'), plt.axis('off')
# plt.subplot(1, 3, 2), plt.imshow(res_horizontal), plt.title('res_horizontal'), plt.axis('off')
# plt.subplot(1, 3, 3), plt.imshow(res_vertical), plt.title('res_vertical'), plt.axis('off')
# plt.show()

# gray_image = cv2.imread(IMAGE_IN_PATH, cv2.IMREAD_GRAYSCALE)

# plt.subplot(2, 3, 1), plt.imshow(image), plt.title("plt.imshow(image)"), plt.axis('off')
# plt.subplot(2, 3, 2), plt.imshow(image, cmap='gray'),   plt.title("plt.imshow(image, camp='gray')"),            plt.axis('off')
# plt.subplot(2, 3, 3), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title("plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))"), plt.axis('off')

# plt.subplot(2, 3, 4), plt.imshow(gray_image), plt.title("plt.imshow(gray_image)"),                plt.axis('off')
# plt.subplot(2, 3, 5), plt.imshow(gray_image, cmap='gray'), plt.title("plt.imshow(gray_image, cmap='gray')"),   plt.axis('off')
# plt.subplot(2, 3, 6), plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB)), plt.title("plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))"), plt.axis('off')
# plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示

# === 生成模拟数据 ===
num_images = 10

# 示例 1：线性增长
linear_means = np.linspace(50, 100, num_images)  # 线性增长均值

# 示例 2：非线性增长（指数）
nonlinear_means = 50 + np.cumsum(np.random.rand(num_images) * 5)  # 随机累积，非线性

# === 绘图函数 ===
def plot_means(means, title="图像均值变化图"):
    plt.figure(figsize=(8,5))
    plt.plot(means, 'o-', label='均值')
    plt.xlabel("图像序号")
    plt.ylabel("图像均值")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# === 绘制线性示例 ===
plot_means(linear_means, title="模拟线性均值变化")

# === 绘制非线性示例 ===
plot_means(nonlinear_means, title="模拟非线性均值变化")

# 常用于数据拼接和组合
"""#############################################################################################
# 函数功能：沿水平方向将数组进行堆叠。
# 函数说明：np.hstack(tup)
# 参数说明：
#         tup：一个包含要堆叠的数组的元组或列表。所有输入数组必须具有相同的形状，除了要堆叠的轴（即列数可以不同）。
# 返回值：
#         返回一个新的数组，包含输入数组在水平方向上堆叠的结果。
#############################################################################################"""

"""#############################################################################################
# 函数功能：沿垂直方向将数组进行堆叠。
# 函数说明：np.vstack(tup)
# 参数说明：
#         tup：一个包含要堆叠的数组的元组或列表。所有输入数组必须具有相同的形状，除了要堆叠的轴（即行数可以不同）。
# 返回值：
#         返回一个新的数组，包含输入数组在垂直方向上堆叠的结果。
#############################################################################################"""
"""#############################################################################################
# 函数功能：用于显示图像或矩阵数据，并自动将其展示在一个窗口中。
# 函数说明：plt.imshow(image, cmap=None, norm=None, interpolation=None, origin=None, extent=None, filternorm=True, filterrad=4.0, resample=None, url=None, **kwargs)
# 参数说明：
#         image：要显示的图像或矩阵数据，通常是二维或三维数组。对于彩色图像，通常是一个三维数组（高度 x 宽度 x 通道）。
#         cmap：用于映射图像颜色的颜色图（colormap），可以为字符串类型的预定义颜色映射名称，如 "gray", "hot", "viridis" 等。
#               如果为 None，默认使用数据类型决定颜色映射。
#         norm：用于归一化图像数据的方式，通常为 `matplotlib.colors.Normalize` 类型。用于控制图像色阶的显示。
#         interpolation：插值方法，用于图像缩放的插值方式，常见的有：
#             - 'nearest'：最近邻插值
#             - 'bilinear'：双线性插值
#             - 'bicubic'：双三次插值
#             - 'spline36'：三次样条插值
#             - 'hanning'、'hamming'、'hermite' 等其他方法
#         origin：设置显示图像时的原点位置。常用值包括：
#             - 'upper'：图像从上方开始显示
#             - 'lower'：图像从下方开始显示
#         extent：设置图像显示区域的范围，四个数值：`[xmin, xmax, ymin, ymax]`，用于图像显示时的坐标轴限制。
#         filternorm：布尔值，指定是否对图像进行归一化处理。
#         filterrad：浮动值，控制滤波器的半径。
#         resample：布尔值，指定是否启用图像重采样。
#         url：设置图像链接，适用于使用网络图像的情况。
#         **kwargs：其他 `imshow` 支持的参数，例如 `alpha`、`aspect` 等。
# 返回值：
#         返回一个包含图像对象的句柄（`AxesImage`），可以进一步修改图像显示的属性。
#############################################################################################"""