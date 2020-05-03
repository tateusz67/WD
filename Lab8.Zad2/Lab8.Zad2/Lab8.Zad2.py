import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,"Imiona")

#podpunkt a)
#print(df[df['Liczba']>1000])

#podpunkt b)
#print(df[df['Imie']=="MATEUSZ"])

#podpunkt c)
#print(df.agg({'Liczba':['sum']}))

#podpunkt d)
#print(df[df['Rok']<2006].agg({'Liczba':['sum']}))

#podpunkt e)
#print(df[df['Plec']=='M'].agg({'Liczba':['sum']}))
#print(df[df['Plec']=='K'].agg({'Liczba':['sum']}))

#podpunkt f)
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))

#podpunkt g)
#print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[[0,1]])