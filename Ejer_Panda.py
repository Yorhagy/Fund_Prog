
import pandas as pd

# %%

datos = pd.read_csv('Parks.csv')

datos.rename(index = datos['park.key'], inplace = True)
datos.drop(datos.columns[[0]], axis = 1, inplace = True)
info = datos.info()


P_10 = datos.iloc[0:10]
P_15 = datos.iloc[15,:]
P_CLEO = datos.loc['CLE04',:]
P_Mul = datos.loc[['LBV01','MIA01','PHI10','SYR03'],:]
l = len(datos)

