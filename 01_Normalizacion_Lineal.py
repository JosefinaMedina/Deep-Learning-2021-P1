import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('../Datos/Premios2020.csv', encoding='ISO-8859-1')

# Escala los valores entre 0 y 1
mini = df['Age'].min()
maxi = df['Age'].max()
df['AgeLineal']= (df['Age']-mini)/(maxi-mini)

# plt.figure()
# df.Age.hist()
# plt.figure()
# df.AgeLineal.hist()

#-- tipificacion --
media = df['Age'].mean()
desvio = df['Age'].std()
df['AgeNorm']= (df['Age']-media)/desvio
# plt.figure()
# df.AgeTipificada.hist()

plt.figure()
df[['Age','AgeLineal','AgeNorm']].hist()
