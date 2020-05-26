import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random as rd

def randomStyle():
    color = ['red','green','orange','cyan','blue']
    edge = ['red','green','orange','cyan','blue']

    _x = np.arange( 4 )
    _y = np.arange( 5 )
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade = True, color = rd.choice(color), edgecolor = rd.choice(edge), linewidth = rd.randrange(1,10))
    ax1.set_title('Wykres')


fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 121 , projection = '3d' )

randomStyle()


plt.show()
