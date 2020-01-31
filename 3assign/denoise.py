import numpy as np
from matplotlib import pyplot as plt
import math
import statistics
import copy

# returns median value of mxm subimage centering at (y,x)
def calcMedian(img, m, y, x):
    a = int((m-1)/2)
    y_max, x_max = img.shape

    vals = []
    # iterate over each mxm index centered at [y][x]
    for i in range(-1*a, a+1):
        for j in range(-1*a, a+1):
            y_pos = y + i
            x_pos = x + j
            # check if index is within img
            if 0 <= y_pos < y_max:
                if 0 <= x_pos < x_max:
                    vals.append(int(img[y_pos][x_pos]))
    return statistics.median(vals)

img = plt.imread('./images/Fig0335(a).tif', 0)
max_y, max_x = img.shape

# perform median filter on image
result = copy.deepcopy(img)
for i in range(3, max_y):
    for j in range(3, max_x):
        result[i][j] = calcMedian(img, 3, i, j)

# plt.imshow(img, cmap='gray')
# plt.show()
plt.imshow(result, cmap='gray')
plt.show()
