import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,"Imiona")

dane = df.groupby(['Plec']).agg({'Liczba':['sum']})

wykres = dane.plot.bar()
wykres.set_xlabel('Plec')
wykres.set_ylabel('Mln')
wykres.legend()
plt.title('Liczba urodzeń podzial na plec')

plt.show()


