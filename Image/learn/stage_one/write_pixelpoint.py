import numpy as np
import matplotlib.pyplot as plt
import cv2

bgr_color = (120, 85, 200)

color_block = np.zeros((100, 100, 3), dtype=np.uint8)
color_block[:, :] = bgr_color


rgb_block = cv2.cvtColor(color_block, cv2.COLOR_BGR2RGB)

plt.imshow(rgb_block)
plt.title(f"BGR: {bgr_color} | RGB: {bgr_color[::-1]}")
plt.axis("off")
plt.show()