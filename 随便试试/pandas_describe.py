import pandas as pd

data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

a = data.describe()

print(a)

print(a.iloc[0,:])