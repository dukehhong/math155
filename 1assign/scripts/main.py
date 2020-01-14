import numpy as np
from matplotlib import pyplot as plt
import math

# given an MxN array of intensity levels, return 1x256 array where each index i indicates
# (the number of pixels with intensity value i)/(total number of pixels)
def makeHisto(img):
    M, N = img.shape
    histo = np.zeros(256)
    # for each intensity value r_k in img[i][j], increase y by 1 at index r_k
    for i in range(0, M):
        for j in range(0, N):
            histo[int(img[i][j])] += 1
    return (histo/(M*N))

# equalizes histogram
def equalizeHisto(histo):
    equalHisto = np.zeros(256)
    equalHisto[0] = y[0]
    for i in range(1,256):
        equalHisto[i] = equalHisto[i-1] + histo[i]
    return equalHisto

# performs histogram equalization on img and returns resulting image
def equalizeImage(img):
    M, N = img.shape
    product = np.zeros((M, N))
    s = equalizeHisto(makeHisto(img))
    for i in range(0, M):
        for j in range(0, N):
            product[i][j] = math.floor(s[img[i][j]] * 255)
    return product

if __name__ == '__main__':

    # reads file image into numpy array
    img = plt.imread('../images/Fig3.08(a).jpg', 0)
    M, N = img.shape

    x = list(range(0,256)) # x-axis
    y = makeHisto(img) # histogram of img
    z = equalizeHisto(y) # equalized histogram

    fig, axes = plt.subplots(2)
    axes[0].set_title('Histogram')
    axes[0].bar(x,y)

    axes[1].set_title('Equalized Histogram')
    axes[1].bar(x,z)

    fig.subplots_adjust(hspace=0.5)
    plt.show()


