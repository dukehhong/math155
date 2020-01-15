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
    z = equalizeHisto(y)

    enhanced_img = equalizeImage(img)
    y2 = makeHisto(enhanced_img)

    ## HISTOGRAM ##
    fig, axes = plt.subplots(2)
    # plot histogram
    axes[0].set_title('Original Histogram')
    axes[0].bar(x,y)
    # plot equalized histogram
    axes[1].set_title('Enhanced Histogram')
    axes[1].bar(x,y2)

    fig.subplots_adjust(hspace=0.5)

    ## IMAGES ##
    fig2, axes2 = plt.subplots(2)
    axes2[0].set_title('Original Image')
    axes2[0].imshow(img, cmap='gray')

    axes2[1].set_title('Enhanced Image')
    axes2[1].imshow(enhanced_img, cmap='gray')

    fig2.subplots_adjust(hspace=0.5)

    fig3, axes3 = plt.subplots(1)
    axes3.set_title('Histogram-Equalization Transformation Function')
    axes3.plot(x,z*255)

    plt.show()
    



