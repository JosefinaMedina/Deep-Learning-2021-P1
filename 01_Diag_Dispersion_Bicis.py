import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import chardet

os.chdir('../Datos//')
nomArch = 'SeoulBikeData.csv'
with open(nomArch, 'rb') as f:
    result = chardet.detect(f.read())  

df= pd.read_csv(nomArch, encoding=result['encoding'])

print(df.dtypes)

sns.heatmap(df[['Temperature(°C)','Rented Bike Count','Humidity(%)','Visibility (10m)']].corr(), square=True, annot=True)

plt.figure()
plt.scatter(df['Temperature(°C)'],df['Rented Bike Count'], marker='o')
plt.xlabel('Temperature(°C)')
plt.ylabel('Rented Bike Count')

plt.figure()
plt.scatter(df['Humidity(%)'],df['Visibility (10m)'], marker='o')
plt.xlabel('Humidity(%)')
plt.ylabel('Visibility (10m)')

