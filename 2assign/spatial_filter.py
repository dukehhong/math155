import numpy as np
from matplotlib import pyplot as plt
import os.path
import math

# calculates mxm linear filter at position [y][x]
def calcMask(img, m, y, x):
    w = 1/(m**2) # average mask entry
    a = int((m-1)/2) 
    y_max, x_max = img.shape
    g = 0 # filtered intensity value for [y][x]

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

# load image
image_folder = os.path.join("./", "images")
img_path = os.path.join(image_folder, 'Fig0333(a).tif')
img = plt.imread(img_path, 0)

# plot m = 3, 9, 15
img_3 = applyLinearFilter(img, 3)
img_9 = applyLinearFilter(img, 9)
img_15 = applyLinearFilter(img, 15)
plt.imshow(img_3, cmap='gray')
plt.show()
plt.imshow(img_9, cmap='gray')
plt.show()
plt.imshow(img_15, cmap='gray')
plt.show()
