import numpy as np

arr = np.arange(12)

a = arr.reshape(3,4)
b = arr.reshape(4,3)
c = arr.reshape(2,6)

for i in a.flat:
   print(i)

print("-----------------------------------------------")

for i in b.flat:
   print(i)

print("-----------------------------------------------")

for i in c.flat:
   print(i)
