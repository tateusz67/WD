
import sys

podzielne4 = []
for x in range(4,100,4):
    podzielne4 += [x]

plik=open("zad1.txt","a+")

plik.writelines(str(podzielne4))

plik.close()
