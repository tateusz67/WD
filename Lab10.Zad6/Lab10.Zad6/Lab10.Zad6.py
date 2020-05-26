import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,"Imiona")

#podpunkt a)
K = df[df['Plec']=='K'].agg({'Liczba':['sum']})
K = K.values.flatten()
M = df[df['Plec']=='M'].agg({'Liczba':['sum']})
M = M.values.flatten()
etykiety = ['K', 'M']
wartosci = [K[0],M[0]]

plt.subplot(2, 1, 1)
plt.bar(etykiety, wartosci)
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')


#podpunkt b) DODAĆ



#podpunkt c)
ur = df.groupby(['Rok']).agg({'Liczba': ['sum']}).values.flatten()
rok = df.Rok.unique()
etykiety2 = rok
wartosci2 = ur

plt.subplot(2, 1, 2)
plt.bar(etykiety2, wartosci2)
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')

plt.show()





