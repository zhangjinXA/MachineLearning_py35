import pandas as pd
import matplotlib.pyplot as plt

file = 'C:\\Users\\Administrator\\Desktop\\DM\\'


data1 = pd.read_excel(file+'DM1.xlsx',sheetname=0,header=None)
data2 = pd.read_excel(file+'DM2.xlsx',sheetname=0,header=None)
data3 = pd.read_excel(file+'DM3.xlsx',sheetname=0,header=None)

data = pd.concat([data1,data2,data3])
data.head = ['x','y']


plt.scatter(data.iloc[:,0],data.iloc[:,1],s=1)
plt.show()

