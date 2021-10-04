import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df= pd.read_csv('..//Datos//Premios2020.csv', encoding='ISO-8859-1')

LD = ['NO'] * len(df)
for i in range(len(df)):
    if df['duration'][i] > 120:
        LD[i] = 'SI'
# Agregando un atributo al DataFrame
df = df.assign( largaDuracion = LD )
print('Atributo largaDuracion')
print(pd.value_counts(df['largaDuracion']))

plt.figure()
barras = pd.value_counts(df['largaDuracion'])
n = len(barras)

# Dibujamos el gráfico de barras
plt.bar(np.arange(n), barras)

plt.title('largaDuracion')     # Colocamos el título
plt.ylabel('Frecuencia') # etiqueta en el eje Y
# nombres de cada barra
plt.xticks(np.arange(n),barras.index,rotation = 0) 


