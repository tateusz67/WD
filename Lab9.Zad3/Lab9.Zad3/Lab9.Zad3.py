import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,"Imiona")

dane = df.groupby(['Plec']).agg({'Liczba': ['sum']})
#dodać tu jeszcze warunek że rok > 2011

wykres = dane.plot.pie(subplots=True, autopct='%.2f % %', fontsize=20, figsize=(6, 6))
plt.title('Procent urodzeń podzial na plec w ostatnich 5 latach')

plt.show()


