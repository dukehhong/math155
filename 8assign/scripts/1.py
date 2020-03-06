import numpy as np
import matplotlib.pyplot as plt
import math
import skimage
import skimage.metrics

def ari_filter(img):
    M, N = img.shape
    res = np.zeros((M, N))
    mask = np.array([
        [1/9,1/9,1/9],
        [1/9,1/9,1/9],
        [1/9,1/9,1/9]
        ])

    for i in range(1, M - 1):
        for j in range (1, N - 1):
            res[i][j] = (img[i-1:i+2, j-1:j+2] * mask).sum()
    return res

def rescale(img):
    maxv = np.max(img)
    minv = np.min(img)
    M, N = img.shape
    img2 = np.zeros(img.shape)
    slope = 255/(maxv- minv)
    for i in range(0, M):
        for j in range(0, N):
            img2[i][j] = math.floor( slope*(img[i][j] - minv) )
    return img2

def geo(mat):
    m,n = mat.shape
    product = 1
    for i in range(0, m):
        for j in range(0,n):
            product = product * (mat[i][j])
    return product

def geo_filter(img):
    M, N = img.shape
    res = np.zeros((M,N))
    for i in range(1, M-1):
        for j in range(1, N-1):
            temp = img[i-1:i+2, j-1:j+2]
            res[i][j] = geo(temp)**(1/9)
    return res

def SNR(img, dimg):
    a = dimg**2
    b = (img-dimg)**2
    return 10*math.log10(a.sum() / b.sum())

o_img = plt.imread('../images/Fig5.07(a).jpg')

n_img = skimage.util.random_noise(o_img, mode='gaussian', mean=0, var=.01)
n_img = rescale(n_img)

ari_img = ari_filter(n_img)
geo_img = geo_filter(n_img)

ari_img = rescale(ari_img)
geo_img = rescale(geo_img)

SNR_noi = SNR(o_img, n_img)
SNR_ari = SNR(o_img, ari_img)
SNR_geo = SNR(o_img, geo_img)

fig, ax = plt.subplots(2,2)
ax[0,0].imshow(o_img, cmap="gray")
ax[0,0].set_title("Original")
ax[0,1].imshow(n_img, cmap="gray")
ax[0,1].set_title(f'Noised SNR: {SNR_noi}')
ax[1,0].imshow(ari_img, cmap="gray")
ax[1,0].set_title(f'Arithmetic SNR: {SNR_ari}')
ax[1,1].imshow(geo_img, cmap="gray")
ax[1,1].set_title(f'Geometric SNR: {SNR_geo}')
plt.show()