import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('../Datos//')
datos = pd.read_csv('Drug5.csv')

plt.figure()
barras = pd.value_counts(datos['Drug'])
plt.pie(barras,labels=barras.index, autopct="%0.1f %%")
plt.title('Drug')


