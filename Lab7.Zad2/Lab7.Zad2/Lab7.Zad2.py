import numpy as np

a = np.arange(9).reshape(3,3)
b = np.arange(12).reshape(3,4)

print("Najnizsza wartosc dla rzedu macierzy a:",a.min(axis=1))

print("Najnizsza wartosc dla kolumn macierzy a:",a.min(axis=0))

print("Najnizsza wartosc dla rzedu macierzy b:",b.min(axis=1))

print("Najnizsza wartosc dla kolumn macierzy b:",b.min(axis=0))
