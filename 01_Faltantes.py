import pandas as pd
import numpy as np
import os
import chardet
os.chdir('../Datos//')
nomArch = 'Premios2020.csv' 
with open(nomArch, 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large

df= pd.read_csv(nomArch, encoding=result['encoding'])

print(df.isnull().sum())

# completa los atrib.numéricos con la media
values = {'nominations': df['nominations'].min(), 'rating': 5}
df3 = df.fillna(value=values)

#-- reemplaza todos los nan con 0
df4 = df.replace(np.nan, 0)

#crea una copia de df
df5 = pd.DataFrame(df)
modaCat = df5['genre2'].mode()

df5['genre2'] = df5['genre2'].replace([np.nan], modaCat)
print('Df5\n')
print(df5.isnull().sum())
