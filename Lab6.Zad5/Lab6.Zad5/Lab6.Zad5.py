import numpy as np

def funkcja(n):
    a = np.diag([a for a in range(n,0,-1)])
    return a

print(funkcja(6))
