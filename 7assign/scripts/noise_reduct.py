import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
import math

def shift(img):
    M, N = img.shape
    result = np.zeros((M,N))
    for i in range(0, M):
        for j in range(0,N):
            result[i][j] = ((-1)**(i+j))*img[i][j]
    return result

# PART A
def sinusoidal_noise(x,y, A, u_o, v_o):
    return A*math.sin( (2*math.pi*u_o*x) + (2*math.pi*v_o*y) )

# PART B
img = plt.imread('../images/Fig5.26a.jpg')
M, N = img.shape
fig, ax = plt.subplots(2,2)

# add noise
output = np.zeros((M,N))
for i in range(0,M):
    for j in range(0,N):
        output[i][j] = img[i][j] + sinusoidal_noise(i,j, 100, 0.25, 0)
     
ax[0, 0].imshow(img, cmap='gray')
ax[0, 0].axis('off') 
ax[0, 0].set_title('Original')
ax[0, 1].imshow(output, cmap='gray')
ax[0, 1].set_title('Degraded')
ax[0, 1].axis('off') 

# PART C
output = shift(output)
f_img = fft.fft2(output)
f_spec = abs(f_img)

# perform log transform to scale
# c = 5
# for i in range(0,M):
#     for j in range(0,N):
#         f_spec[i][j] = math.floor(c*math.log(1+f_spec[i][j]))

a, b = f_spec.shape
ax[1, 0].imshow(f_spec, cmap='gray')
ax[1, 0].set_title('Fourier Spectrum')
ax[1, 0].axis('off') 

# PART D
# Using matplotlib plot GUI, we can see that there is a white dot at (128,192)
# But when using coordinates in arrays, we flip them (192,128). Plus we shifted
# the (0,0) to the (M/2, N/2) so since M/2= 128, N=128 (192, 128) - (128, 128)
# = (64,0)
i_0 = 64
j_0 = 0
D_o = 10

# create gaussian notch reject filter
H = np.zeros((M,N))
for i in range(0, M):
    for j in range(0, N):
        D_k = math.sqrt( ((i - (M/2) - i_0)**2) + ((j - (N/2) - j_0)**2) )
        D_nk = math.sqrt( ((i - (M/2) + i_0)**2) + ((j - (N/2) + j_0)**2) )
        H[i][j] = 1 - math.exp(-1/2*D_k*D_nk/(D_o**2) )

# apply filter to fourier transform
G = H * f_img
# apply ifft and unshift
denoised_img = shift(fft.ifft2(G).real)
ax[1, 1].imshow(denoised_img, cmap='gray')
ax[1, 1].set_title('Denoised')
ax[1, 1].axis('off') 

plt.show()