import numpy as np
import matplotlib.pyplot as plt

# 定义两个向量
v = np.array([3, 1])
w = np.array([1, 2])

# 向量加法
print(f"v + w = {v + w}")

# 向量点积
print(f"v · w = {np.dot(v, w)}")

# 可视化向量
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
plt.quiver(0, 0, v[0]+w[0], v[1]+w[1], angles='xy', scale_units='xy', scale=1, color='g', label='v+w')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.legend()
plt.show()