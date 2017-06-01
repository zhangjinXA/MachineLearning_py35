import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import AutoDateLocator, DateFormatter

fig = plt.figure()
ax = fig.add_subplot(111)

yearsFmt = DateFormatter('%H:%M')
autodates = AutoDateLocator()



a = pd.DataFrame()
path = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
file = path + 'toSHE-2017-4-5.xls'
data = pd.read_excel(file,0)

X1 = pd.to_datetime(data.到达时间,format="%H:%M")
X2 = pd.to_datetime(data.起飞时间,format="%H:%M")
X =X1-X2
Y = data.价格
# a.sort_values
print(X)
ax.plot(Y.sort_values(),'ro')
# ax.xaxis.set_major_locator(autodates)       #设置时间间隔
# ax.xaxis.set_major_formatter(yearsFmt)      #设置时间显示格式

plt.show()