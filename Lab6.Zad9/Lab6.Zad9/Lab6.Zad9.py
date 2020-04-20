import numpy as np

def fibb(n):
    wynik = [1, 1]
    for i in range(n-2):
        wynik.append(wynik[i] + wynik[(i + 1)])

    return wynik

fibo = np.array(fibb(25))

print(fibo.reshape(5,5))