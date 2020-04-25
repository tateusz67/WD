import numpy as np

b = np.arange(81)

print(b.reshape(9,9))

print(b.reshape(81,1))

print(b.reshape(1,81))

#mamy w tym przypadku tylko takie możliwości bo iloczyn rzędów i kolumn musi być równy rozmiarowi macierzy
