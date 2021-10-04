import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('../Datos//')
datos = pd.read_csv('Drug5.csv')

plt.figure()
plt.scatter(datos['K'],datos['Na'], marker='*')
plt.ylabel('Na')
plt.xlabel('K')

conDrugY = datos.query("Drug== 'drugY'")
otraDroga = datos.query("Drug != 'drugY'")

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.6, 0.8])

p1 = plt.scatter(conDrugY['K'], conDrugY['Na'],  marker='^', label='DrugY')
p2 = plt.scatter(otraDroga['K'], otraDroga['Na'],  marker='o', label='Otra')
plt.legend(handles=[p1, p2], bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylabel('Na')
plt.xlabel('K') 



