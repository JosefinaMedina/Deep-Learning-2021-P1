import pandas as pd
import numpy as np
from sklearn import preprocessing

df= pd.read_csv('../Datos/Premios2020.csv', encoding='ISO-8859-1')

# Escala los valores entre 0 y 1
min_max_scaler = preprocessing.MinMaxScaler()
df['minmaxAge'] = pd.DataFrame(min_max_scaler.fit_transform(pd.DataFrame(df['Age'])))
print(min_max_scaler.min_, min_max_scaler.data_range_)

## Estandarizacion – resta la media y divide por el desvio
standarScaler = preprocessing.StandardScaler()
standarScaler.fit(pd.DataFrame(df['Age']))
print(standarScaler.mean_, standarScaler.var_)
df['stdAge'] = pd.DataFrame(standarScaler.transform(pd.DataFrame(df['Age'])))
#

