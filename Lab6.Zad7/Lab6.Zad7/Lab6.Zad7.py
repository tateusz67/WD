import numpy as np

def funkcja(n):
    tab = np.zeros((n,n))
    for i in range(n):
        for j in range(i):
            tab[i,j] = (2+(2*i-2*j))
        for k in range(i):
            tab[n-i-1,n-k-1] = (2+(2*i-2*k))
        tab[i,i] = 2
    
    return tab

print(funkcja(7))