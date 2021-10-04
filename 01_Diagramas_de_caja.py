import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('../Datos//')
datos = pd.read_csv('Drug5_atipicos.csv')
plt.figure()
datos.boxplot()
plt.figure()
datos.boxplot(column=['Na', 'K'], grid=False, vert=False)

