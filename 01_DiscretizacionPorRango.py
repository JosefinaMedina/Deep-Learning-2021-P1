import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df= pd.read_csv('..//Datos//Premios2020.csv', encoding='ISO-8859-1')

etiq = ["bajo","medio","alto", "muy alto"]

# Discretización por RANGO
columna = pd.cut(df["duration"],bins=len(etiq),labels=etiq)

df['duration2']= pd.Series.to_frame(columna)

barras = pd.value_counts(df['duration2'])
print(barras)

plt.figure()
N=len(barras)
plt.bar(np.arange(N), barras)  # Gráfico de barras
plt.title('duration')      # Colocamos el título
plt.ylabel('Frecuencia')
# Colocamos las etiquetas del eje x
plt.xticks(np.arange(N), barras.index)