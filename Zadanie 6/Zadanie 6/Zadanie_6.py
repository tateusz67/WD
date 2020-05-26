import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 6567345 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax1 = fig.add_subplot( 1 , 2 , 1 , projection = '3d' )
ax2 = fig.add_subplot( 1 , 2 , 2 , projection = '3d' )
n = 20

for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax1.scatter(xs, ys, zs, c =c, marker =m)

ax1.set_xlabel( 'X Label' )
ax1.set_ylabel( 'Y Label' )
ax1.set_zlabel( 'Z Label' )

z2 = np.linspace(0 , np.pi * np.pi, 15)
x2 = np.sin(z2)
y2 = 2 * np.cos(z2)
ax2.plot(x2, y2, z2, label = 'Wykres liniowy' )
ax2.legend()

ax2.set_xlabel( 'X Label' )
ax2.set_ylabel( 'Y Label' )
ax2.set_zlabel( 'Z Label' )
plt.show()