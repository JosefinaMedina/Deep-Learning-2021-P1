import pandas as pd
import numpy as np
import os
import chardet

os.chdir('../Datos//')
nomArch = 'Drug5.csv' 

#-- detectando la codificación de caracteres usada ----
with open(nomArch, 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large


datos= pd.read_csv(nomArch, encoding=result['encoding'])

# dtypes visualiza los tipos de datos del DataFrame
print(datos.dtypes)
print('\n'*2)

# -- METADATOS –
print(datos.describe())
print('\n')
print(datos['Drug'].describe())
