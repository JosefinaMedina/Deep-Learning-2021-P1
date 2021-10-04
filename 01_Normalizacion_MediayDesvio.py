import pandas as pd
import numpy as np

df= pd.read_csv('../Datos/Premios2020.csv', encoding='ISO-8859-1')

# Estandarización
media = df['Age'].mean()
desvio = df['Age'].std()
df['AgeNorm']= (df['Age']-media)/desvio

