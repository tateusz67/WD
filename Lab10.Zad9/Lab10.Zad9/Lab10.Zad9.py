import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('zamowienia.csv',sep = ';')
sprzedawcy = df.Sprzedawca.unique()
zamowienia = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})

wedges, texts, autotexts = plt.pie(zamowienia.values.flatten(), labels=sprzedawcy,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"),shadow=True)
plt.setp(autotexts, size=14, weight="bold")
plt.title("ilość zamówień na sprzedawcę")
plt.legend(title='Sprzedawca')
plt.show()




