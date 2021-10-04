import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
datos = pd.read_csv('../Datos/Iris.csv')
#-- todas las columnas menos la última --
#datos2 = datos.iloc[:,0:-1]

#--Matriz de correlacion --
print(datos.corr())

sns.heatmap(datos.corr(), square=True, annot=True)

plt.figure()
plt.scatter(datos['petallength'],datos['petalwidth'])
plt.ylabel('petalwidth')
plt.xlabel('petallength')




