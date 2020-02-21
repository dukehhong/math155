import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt 
import math

def shift(img):
    M, N = img.shape
    result = np.zeros((M,N))
    for i in range(0, M):
        for j in range(0,N):
            result[i][j] = ((-1)**(i+j))*img[i][j]
    return result

def lowtransform(u,v, D_0, M, N):
    D = math.sqrt( (((M/2) - u)**2) + (((N/2) - v)**2) )
    return math.exp(-(D**2)/(2*(D_0**2)))

def hightransform(u,v,D_0, M, N):
    D = math.sqrt( (((M/2) - u)**2) + (((N/2) - v)**2) )
    return 1 - math.exp(-(D**2)/(2*(D_0**2)))
    
img = plt.imread('../images/Fig4.45(a).jpg')
M, N = img.shape

low_result = shift(img)
high_result = shift(img)

low_result = fft.fft2(low_result)
high_result = fft.fft2(high_result)

low_filter = np.zeros((M,N))
high_filter = np.zeros((M,N))

for i in range(0,M):
    for j in range(0,N):
        low_filter[i][j] = lowtransform(i,j,25, M, N)
        high_filter[i][j] = hightransform(i,j,25, M, N)

low_result = np.multiply(low_result, low_filter)
high_result = np.multiply(high_result, high_filter)

low_result = fft.ifft2(low_result)
low_result = shift(low_result.real)
high_result = fft.ifft2(high_result)
high_result = shift(high_result.real)

fig, axes = plt.subplots(1,3)
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')
axes[1].imshow(low_result, cmap='gray')
axes[1].set_title('Gaussian Lowpass Filter')
axes[1].axis('off')
axes[2].imshow(high_result, cmap='gray')
axes[2].set_title('Gaussian Highpass Filter')
axes[2].axis('off')
plt.show()