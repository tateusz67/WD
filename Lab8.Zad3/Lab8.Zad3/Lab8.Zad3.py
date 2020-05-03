import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime

df = pd.read_csv('zamowienia.csv',sep = ';')

#podpunkt a)
#print(df['Sprzedawca'].unique())

#podpunkt b)
#print(df.nlargest(5, ['Utarg'])) 

#podpunkt c)
#print(df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))

#podpunkt d)
#print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))

#podpunkt e)
#print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg': ['sum']}).tail(1))

#podpunkt f)
#print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg': ['mean']}))









 