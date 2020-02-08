import numpy as np
from matplotlib import pyplot as plt
import math


def reScale(img):
    M, N = img.shape
    fmax = img.max()
    fmin = img.min()

    slope = 255/(fmax - fmin)
    temp = np.zeros((M, N))

    for j in range(0, M):
        for i in range(0, N):
            temp[j][i] = math.floor(slope*(img[j][i] - fmin))
    return temp


img = plt.imread('../images/Fig5.26a.jpg')
M, N = img.shape
output = np.zeros((M, N))

xsobel = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

ysobel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

for j in range(1, M-1):
    for i in range(1, N-1):
        temp = img[j-1: j+2, i-1: i+2]
        fx = np.multiply(temp, xsobel)
        fy = np.multiply(temp, ysobel)
        output[j][i] = abs(np.sum(fx)) + abs(np.sum(fy))

output = reScale(output)

fig, axes = plt.subplots(1, 2)

axes[0].axis('off')
axes[1].axis('off')
axes[0].set_title('Original')
axes[0].imshow(img, cmap='gray')
axes[1].set_title('Sobel Filtered')
axes[1].imshow(output, cmap='gray')

plt.show()
