import pandas as pd
import numpy as np

df= pd.read_csv('..//Datos//Premios2020.csv', encoding='ISO-8859-1')

opciones = pd.value_counts(df['genre1'])
print(opciones)

# Reemplazando valores
df['genre1'] = df['genre1'].replace(['Adventure','Action', \
              'Romance', 'Thriller', 'Mystery'], 'Otra')

# revisar cómo quedó
opciones2 = pd.value_counts(df['genre1'])
print(opciones2)
