from matplotlib import pyplot as plt
import numpy as np

# derivation of sigmoid function depending on x, k, E
def T(x, k, E):
    return 1/((1+(k/x)**E))

if __name__ == '__main__':
    x = np.arange(0.01, 1, 0.01)

    # plot T(x) with k = 0.5 and E = 5,10,15,20,25
    for i in range(5, 30, 5):
        y = np.apply_along_axis(T, 0, x, 0.5, i)
        plt.plot(x, y, label='E={}'.format(i))

    # plot T(x) as "binary"
    # note this will give an overflow error due to the value of E
    y = np.apply_along_axis(T, 0, x, 0.5, 9999999999)
    plt.plot(x, y, label='E = 9999999999 (almost "binary")')

    # add legend
    plt.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left',
            ncol=3, mode='expand', borderaxespad=0)

    plt.ylabel('Intensity value T(r)')
    plt.xlabel('Intenisty value r (Normalized [0,1])')
    plt.show()