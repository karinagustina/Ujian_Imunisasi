#Ujian_Imunisasi

import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

# FIGURE 1

plt.figure('Figure 1: Persentasi balita terimunisasi 1995-2017')

df=pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi BCG'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = df['% Balita yang pernah mendapat imunisasi BCG']
plt.subplot(2,2,1, title = 'BCG')
plt.bar(x,y, color = 'red')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi Campak'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = df['% Balita yang pernah mendapat imunisasi Campak']
plt.subplot(2,2,2, title = 'Campak')
plt.bar(x,y, color = 'green')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi DPT'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = df['% Balita yang pernah mendapat imunisasi DPT']
plt.subplot(2,2,3, title = 'DPT')
plt.bar(x,y, color = 'yellow')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi Polio'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = df['% Balita yang pernah mendapat imunisasi Polio']
plt.subplot(2,2,4, title = 'Polio')
plt.bar(x,y, color = 'blue')
plt.xticks(rotation = 90)


# FIGURE 2

plt.figure('Figure 2: Persentase balita tak terimunisasi 1995-2017 ')

df=pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi BCG'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = 100 - df['% Balita yang pernah mendapat imunisasi BCG']
plt.subplot(2,2,1, title = 'BCG')
plt.bar(x,y, color = 'red')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi Campak'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = 100 - df['% Balita yang pernah mendapat imunisasi Campak']
plt.subplot(2,2,2, title = 'Campak')
plt.bar(x,y, color = 'green')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi DPT'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = 100 - df['% Balita yang pernah mendapat imunisasi DPT']
plt.subplot(2,2,3, title = 'DPT')
plt.bar(x,y, color = 'yellow')
plt.xticks(rotation = 90)

df=pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv', header=0,
   names=['Tahun','% Balita yang pernah mendapat imunisasi Polio'],
   na_values=['-','n.a'])

df=df.interpolate()

x = df['Tahun']
y = 100 - df['% Balita yang pernah mendapat imunisasi Polio']
plt.subplot(2,2,4, title = 'Polio')
plt.bar(x,y, color = 'blue')
plt.xticks(rotation = 90)


plt.show()
