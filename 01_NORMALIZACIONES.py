import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#df= pd.read_csv('../Datos/Adult_data.csv')
df= pd.read_csv('../Datos/iris.csv')
df2 = df.select_dtypes(include = ["int64", "float64"])
df2.hist()

df3 = (df2-df2.min())/(df2.max()-df2.min())
df3.hist()

df4 = (df2-df2.mean())/df2.std()
df4.hist()


