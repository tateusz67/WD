import random

def generuj():
    lista1 = [random.randrange(1, 100) for i in range(20)]
    lista2 = [random.randrange(1, 100) for i in range(20)]

    listaPonizej50 = []
    listaReszta = []

    for i in range(0,19):
        if lista1[i] <= 50:
            listaPonizej50.append(lista1[i])
        else:
            listaReszta.append(lista1[i])

    for i in range(0,19):
        if lista2[i] <= 50:
            listaPonizej50.append(lista2[i])
        else:
            listaReszta.append(lista2[i])


    print(listaPonizej50)
    print(listaReszta)


generuj()





