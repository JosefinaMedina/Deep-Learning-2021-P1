import pandas as pd
import numpy as np
df= pd.read_csv('../Datos/Premios2020.csv', encoding='ISO-8859-1')

# atributo sexo con codificación binaria
NuevasColumnas = pd.get_dummies(df['Sex'], prefix= 'Sex')

# Agregamos las nuevas columnas al DataFrame
df = pd.concat([NuevasColumnas, df], axis=1)

# Borramos la columna original y 1 de las nuevas
df.drop(['Sex', 'Sex_M'],axis=1, inplace=True)
