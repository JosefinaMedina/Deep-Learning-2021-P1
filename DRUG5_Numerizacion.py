import pandas as pd
import seaborn as sns

df = pd.read_csv('../Datos/Drug5.csv')
pd.plotting.scatter_matrix(df)
sns.pairplot(df)
sns.pairplot(df, hue='Drug', diag_kind='hist')

#-- cualitativos a numericos --
df2 = pd.get_dummies(df.iloc[:, 0:-1])

#-- ordinales a numericos ---
mapeo = {'Sex': {'F':1, 'M':0},
          'BP':{'HIGH':2, 'NORMAL':1, 'LOW':0},
          'Cholesterol':{'NORMAL':0, 'HIGH':1}}

df.replace(mapeo, inplace=True)
