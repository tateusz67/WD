import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(0, 30, 0.1)
plt.plot(x, np.sin(x), label='funkcja sin(x)')
plt.plot(x, np.cos(x+math.pi/2)-2, label='funkcja cos(x)')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.legend()
plt.show()

