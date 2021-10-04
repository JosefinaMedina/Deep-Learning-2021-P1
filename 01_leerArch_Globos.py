import pandas as pd
import numpy as np
import os

os.chdir('../Datos//')
datos = pd.read_csv('AUTOS.csv')

# dtypes visualiza los tipos de datos del DataFrame
print(datos.dtypes)
print('\n')

# -- METADATOS –
print(datos.describe())

print('\nValores del atributo COLOR')
print(datos['Color'])