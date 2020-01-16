from matplotlib import pyplot as plt
import numpy as np


def T(x, k, E):
    return 1/((1+(k/x)**E))


x = np.arange(0.01,1,0.01)


for i in range(5,30, 5):
    y = np.apply_along_axis(T, 0, x, 0.5, i)
    plt.plot(x,y, label='E={}'.format(i))

y = np.apply_along_axis(T, 0, x, 0.5, 9999999999)
plt.plot(x,y, label='E = very large number (Binary)')

plt.legend(bbox_to_anchor=(0,1,1,1), loc='lower left', ncol=3, mode='expand', borderaxespad=0)

plt.ylabel('Intensity value T(r)')
plt.xlabel('Intenisty value r (Normalized [0,1])')
plt.show()
