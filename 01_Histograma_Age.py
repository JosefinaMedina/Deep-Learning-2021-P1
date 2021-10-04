import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('../Datos/')
datos = pd.read_csv('Drug5_atipicos.csv')
plt.figure()
plt.hist(datos['Age'], bins = 10, edgecolor = 'black', \
         linewidth=1)
plt.xlabel('AGE')
plt.ylabel('Frecuencia')

