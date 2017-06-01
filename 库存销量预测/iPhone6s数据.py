import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('F:\\资料整理\\myPthon35_Code\\data\\sal库eam存t\\iphone6s')
data.index = pd.to_datetime(data['statis_date'],format='%Y%m%d')

data2 = data.resample('W').sum()

data2016 = data2['2016']
data2017 = data2['2017']
plt.plot(data2016.index,data2016['_c2'],marker='o')
plt.plot(data2017.index,data2017['_c2'],marker='o')
plt.show()
