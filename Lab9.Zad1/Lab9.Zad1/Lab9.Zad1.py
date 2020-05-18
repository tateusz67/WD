import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,"Imiona")

dane = df.groupby(['Rok']).agg({'Liczba':['sum']})


wykres = dane.plot()
wykres.set_xlabel('Rok')
wykres.set_ylabel('Liczba urodzen')
wykres.legend()
plt.title('Liczba urodzeń w latach')

plt.show()
