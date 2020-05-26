import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

np.random.seed(19680801)

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


def randSym():
    tabSymbol = [".", ",", "o", "v", "^",  "<", ">"]
    tabColor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for c, m, zlow, zhigh in [( random.choice(tabColor), random.choice(tabSymbol) , - 50 , - 25 ), ( random.choice(tabColor) , random.choice(tabSymbol) , - 30 , - 5 )]:
        xs = randrange(n, 23 , 32 )
        ys = randrange(n, 0 , 100 )
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c =c, marker =m)

fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 10

randSym()
randSym()
randSym()
randSym()
randSym()

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()
