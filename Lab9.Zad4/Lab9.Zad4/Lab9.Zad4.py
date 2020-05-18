
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.data', delimiter = ',')
x = iris['sepal length']
y = iris['petal length']
colors = np.random.rand(150)
plt.scatter(x,y,c = colors)
plt.show()
