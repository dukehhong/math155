import numpy as np
import matplotlib.pyplot as plt
import math

def contraharmonic(img, order):
    M, N = img.shape
    res = np.zeros((M,N))
    
    for i in range(1,M-1):
        for j in range(1,N-1):
            arr = img[i-1:i+2, j-1:j+2]
            temp = np.where(arr==0, 1e-8, arr)
            
            s1 = (float)(( temp**(order + 1) ).sum())
            s2 = (float)(( temp**(order) ).sum())

            res[i][j] = math.floor(s1/s2)
    return res

imga = plt.imread('../images/Fig5.08(a).jpg')
imgb = plt.imread('../images/Fig5.08(b).jpg')
n_img = plt.imread('../images/Fig5.07(b).jpg')

C1_img = contraharmonic(imga,1.5)
C2_img = contraharmonic(imgb, -1.5)

fig, ax = plt.subplots(1,4)
ax[0].set_title('Fig5.08(a)')
ax[0].imshow(imga, cmap="gray" )
ax[1].set_title('Order 1.5')
ax[1].imshow(C1_img, cmap="gray")
ax[2].set_title('Fig5.08(b)')
ax[2].imshow(imgb, cmap="gray")
ax[3].set_title('Order -1.5')
ax[3].imshow(C2_img, cmap="gray")
plt.show()