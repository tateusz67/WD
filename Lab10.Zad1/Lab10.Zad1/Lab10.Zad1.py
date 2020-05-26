import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,20,20)
plt.plot(x, 1/x, label='funkcja 1/x')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.legend()
plt.show()