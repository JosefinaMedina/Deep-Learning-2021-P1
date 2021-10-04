import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('../Datos/Drug5_atipicos.csv')

media = datos["Age"].mean()
mediana = datos["Age"].median()
moda = datos["Age"].mode()
print("Media %.1f" % media)
print("Mediana: %.1f \nModa: %.1f" % (mediana,moda))

maximo = datos['Age'].max()
minimo = datos['Age'].min()
varianza = datos['Age'].var()
desvio = datos['Age'].std()
print('Maximo %.1f - Minimo: %.1f ' % (maximo, minimo))
print('Var %.1f - STD: %.1f ' % (varianza, desvio))

 #--- cuartiles --- 
Q = datos["Age"].quantile([0.25, 0.5, 0.75]).values
print("Q1 =%.2f   Q2=%.2f   Q3=%.2f" % (Q[0], Q[1], Q[2]))
RIC=Q[2]-Q[0]
print("RCI = %.2f" % RIC)

plt.figure()
datos.boxplot(column=['Age'], vert=False, grid=False) #gráfico del diagrama de caja

