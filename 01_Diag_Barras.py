import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('../Datos//')
datos = pd.read_csv('Drug5.csv')
barras = pd.value_counts(datos['Drug'])
plt.figure()
N=len(barras)
plt.bar(np.arange(N), barras)  # Gráfico de barras
plt.title('Drug')      # Colocamos el título
plt.ylabel('Frecuencia')
# Colocamos las etiquetas del eje x
plt.xticks(np.arange(N), barras.index)


