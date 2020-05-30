import random
import statistics as st

listaWej = [random.randrange(1, 30) for i in range(20)]

lista1 = [i for i in listaWej if i >= st.mean(listaWej)]
lista2 = [i for i in listaWej if i < st.mean(listaWej)]
print(listaWej)
print(int(st.mean(listaWej)))
print(lista1)
print(lista2)

