import numpy as np
from matplotlib import pyplot as plt
import math

def reScale(img):
    M, N = img.shape
    fmax = img.max()
    fmin = img.min()

    slope = 255/(fmax - fmin)
    temp = np.zeros((M,N))

    for j in range(0, M):
        for i in range(0, N):
            temp[j][i] = math.floor(slope*(img[j][i] - fmin))
    return temp

img = plt.imread('../images/Fig3.40(a).jpg')

M, N = img.shape
output = np.zeros((M,N))

kernel = np.array([
    [0,1,0],
    [1,-5,1],
    [0,1,0]
])

for j in range(1, M-1):
    for i in range(1, N-1):
        lap = np.multiply(img[j-1: j+2, i-1: i+2], kernel)
        lap_sum = np.sum(lap)
        output[j][i] = img[j][i] - lap_sum

output = reScale(output)

fig, axes = plt.subplots(1,2)
axes[0].axis('off')
axes[1].axis('off')
axes[0].set_title('Original')
axes[0].imshow(img, cmap='gray')
axes[1].set_title('Laplacian Filtered')
axes[1].imshow(output, cmap='gray')

plt.show()
