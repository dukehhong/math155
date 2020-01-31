import numpy as np
from matplotlib import pyplot as plt
import math

def calcMask(img, m, y, x):
    w = 1/(m**2)  # average mask entry
    a = int((m-1)/2)
    y_max, x_max = img.shape
    g = 0  # filtered intensity value for [y][x]

    # iterate over each mxm index centered at [y][x]
    for i in range(-1*a, a+1):
        for j in range(-1*a, a+1):
            y_pos = y + i
            x_pos = x + j
            # check if index is within img
            if 0 <= y_pos < y_max:
                if 0 <= x_pos < x_max:
                    g += (img[y_pos][x_pos])
    return math.floor(g*w)

# apply linear filter with average mask with entries w = 1/m^2
# and returns filtered image
def applyLinearFilter(img, m):
    y_max, x_max = img.shape
    result = np.zeros(img.shape)
    for i in range(0, y_max):
        for j in range(0, x_max):
            result[i][j] = calcMask(img, m, i, j)
    return result

img = plt.imread('./images/Fig0335(a).tif', 0)

filtered_img = applyLinearFilter(img, 3)

plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(filtered_img, cmap='gray')
plt.show()