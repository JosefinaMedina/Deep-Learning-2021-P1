import pandas as pd
import numpy as np
from sklearn import preprocessing
import seaborn as sns

df = pd.read_csv('../Datos/Drug5.csv')
#-- cualitativos a numericos --
#df2 = pd.get_dummies(df.iloc[:, 0:-1])

#-- ordinales a numericos ---
mapeo = {'Sex': {'F':1, 'M':0},
          'BP':{'HIGH':2, 'NORMAL':1, 'LOW':0},
          'Cholesterol':{'NORMAL':0, 'HIGH':1}}

df.replace(mapeo, inplace=True)

entradas = np.array(df.iloc[:,0:-1])
salidas = 1*(df.Drug=="drugY")

normalizarEntrada = 1  # 1 si normaliza; 0 si no
if normalizarEntrada:
    # Escala los valores entre 0 y 1
    normalizador = preprocessing.MinMaxScaler()
    
    # Estandarizacion – resta la media y divide por el desvio
    normalizador = preprocessing.StandardScaler()
    entradas = normalizador.fit_transform(entradas)
    
    
nEj, nAtrib = entradas.shape

for e in range(5):
    for a in range(nAtrib):
        print("E(%d, %d)= %.2f " % (e, a, entradas[e,a]))
    print("\n")
    
ejemplo=np.array([[23, 1, 2, 1, .5, .67], [34,0,2,3,.66,0.22]])

e2=normalizador.transform(ejemplo)
print(e2)
    