import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#baca keempat data 
BCG = pd.read_csv('BCG.csv',na_values='n.a')
DPT = pd.read_csv('DPT.csv',na_values='n.a')
campak = pd.read_csv('campak.csv',na_values='n.a')
polio = pd.read_csv('polio.csv',na_values='n.a')
nama_data = ['BCG','DPT','campak','polio']

#melihat berapa data yang kosong
print(BCG.info())
print(DPT.info())
print(campak.info())
print(polio.info())

# mengubah data kosong diolah dengan metode interpolasi linear,
BCG = BCG.interpolate()
DPT = DPT.interpolate()
campak = campak.interpolate()
polio = polio.interpolate()

plt.figure('Persentasi balita terimunisasi 1995-2017', figsize =(13,9))
plt.subplot(2,2,1)
plt.bar(BCG['Tahun'],BCG['% Balita yang pernah mendapat imunisasi BCG'],color ='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,2)
plt.bar(campak['Tahun'],campak['% Balita yang pernah mendapat imunisasi Campak'],color ='green')
plt.title('Campak')
plt.xticks(campak['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,3)
plt.bar(DPT['Tahun'],DPT['% Balita yang pernah mendapat imunisasi DPT'],color ='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,4)
plt.bar(polio['Tahun'],polio['% Balita yang pernah mendapat imunisasi Polio'],color ='blue')
plt.title('Polio')
plt.xticks(polio['Tahun'],np.arange(1995,2018),rotation = 90)
plt.tight_layout()

plt.figure('Persentase balita tak terimunisasi 1995-2017', figsize =(13,9))
plt.subplot(2,2,1)
plt.bar(BCG['Tahun'],100 - BCG['% Balita yang pernah mendapat imunisasi BCG'],color ='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,2)
plt.bar(campak['Tahun'],100 - campak['% Balita yang pernah mendapat imunisasi Campak'],color ='green')
plt.title('Campak')
plt.xticks(campak['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,3)
plt.bar(DPT['Tahun'],100 - DPT['% Balita yang pernah mendapat imunisasi DPT'],color ='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,4)
plt.bar(polio['Tahun'],100 - polio['% Balita yang pernah mendapat imunisasi Polio'],color ='blue')
plt.title('Polio')
plt.xticks(polio['Tahun'],np.arange(1995,2018),rotation = 90)
plt.tight_layout()
plt.show()