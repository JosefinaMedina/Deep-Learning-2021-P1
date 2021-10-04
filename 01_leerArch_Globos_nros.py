import pandas as pd
import numpy as np
import os

os.chdir('../Datos//')
datos = pd.read_csv('Globos_nros.csv')

# dtypes visualiza los tipos de datos del DataFrame
print(datos.dtypes)
print('\n')

# -- METADATOS –
# Si hay atrib.numéricos, muestra sólo esos
print(datos.describe())

# Sólo los atributos categóricos
print(datos.describe(include=[np.object]))

# Sólo atributos numéricos
print(datos.describe(include=[np.number]))

# Todos los atributos
print(datos.describe(include='all'))

