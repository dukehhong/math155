import numpy as np
from matplotlib import pyplot as plt
import math

# reduces intensity range from [0,255] to [0,val] using FLOOR
def reduceIntensity(img, val):
    # reduce to all black
    if val == 0:
        return img*0
    # out of range, return original image
    elif val > 256:
        return img
    else:
        return np.floor(img/(256/val))

# read file image into numpy array
img_orig = plt.imread('../images/Fig2.21(a).jpg', 0)

# setup figure
fig = plt.figure(figsize=(10,30))
fig.suptitle('')
plt.rcParams.update({'font.size': 7})

# reduce orig_img by powers of 2 and plot resulting images
for i in range(0,8):
    img = reduceIntensity(img_orig, 256/(2**i))
    ax = fig.add_subplot(8,2,i+1, frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.title.set_text("{} gray levels".format(int(256/(2**i))))
    ax = plt.imshow(img, cmap='gray')
    
# spacing adjustment
plt.subplots_adjust(wspace= -0.5, hspace=0.1)
plt.show()


