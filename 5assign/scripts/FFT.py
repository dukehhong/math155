import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
import math

img = plt.imread('../images/Fig5.26a.jpg')
M, N = img.shape

output = np.zeros((M, N))

# # shift image to center
for i in range(0,M):
    for j in range(0, N):
        output[i][j] = img[i][j]*((-1)**(i+j))

# take absolute value of each index
fourier_spectrum = abs(fft.fft2(output))

# perform log transform to scale
c = 5
for i in range(0,M):
    for j in range(0,N):
        output[i][j] = math.floor(c*math.log(1+fourier_spectrum[i][j]))


# visualize scaled fourier spectrum
plt.title(f'Average Intensity Value: {fourier_spectrum[math.floor(M/2)][math.floor(N/2)]/(M*N)}')
plt.imshow(output, cmap='gray')
plt.axis('off')
plt.show()

# How did we get the average intensity value?
# The average intensity value of an image can be found at the center of the fourier spectrum divided by the size of the image (M*N).
# This is because we shifted the image initially such that the average would be located in the cetner of the fourier spectrum. If we
# did not shift, then the average intensity value would be at (0,0) of the fourier spectrum. It is important to note that the average value
# is using the non-scaled version of fourier spectrum. We can check our answer by using np.mean(img) which is equal to the average we calculated
