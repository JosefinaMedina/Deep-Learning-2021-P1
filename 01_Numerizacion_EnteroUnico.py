import pandas as pd
import numpy as np

df= pd.read_csv('../Datos/Premios2020.csv',encoding='ISO-8859-1')

# print(df.isnull().sum())
# moda = df.release.mode()
# valores = {'release': moda[0]}
# df.fillna(value=valores, inplace=True)

moda = df['release'].mode()
df['release'] = df['release'].replace([np.nan], moda)

print(pd.value_counts(df['release']))

mapeo = {"release": {"January":1, "February":2, "March":3,
                      "April":4, "May":5, "June":6,
                      "July":7, "August":8, "September":9,
                      "October":10, "November":11, "December":12}}

df.replace(mapeo, inplace=True)
print(df['release'].describe())