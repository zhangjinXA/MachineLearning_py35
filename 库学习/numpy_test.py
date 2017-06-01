import numpy as np
import pandas as pd

data = np.linspace(1,100,100,dtype='int')
dataPd = pd.DataFrame(data)
# print(dataPd)
index = np.where(dataPd.isin([1,2,3,4]))
print(index[0])

dataPd_drop = dataPd.drop([0,1,2,3,4],axis=0)
print(dataPd_drop)
