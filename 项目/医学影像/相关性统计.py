import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']


file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\'
name = '插24um值矩阵-皮尔逊相关系数.img'
data = np.fromfile(file+name,dtype=np.float64);
data.shape = 2048,2048   # nb,y,x

##
data = data[300:1750,300:1750]
data.tofile(file+'linshi.dat')
data = np.fromfile(file+'linshi.dat',dtype=np.float64)
#
a = [np.min(data),np.max(data),np.mean(data),np.median(data),np.var(data)]
print(a)

# plt.plot(np.sort(data))
plt.hist(data,500)                         ##相关系数直方图
plt.xlabel('相关系数')
plt.ylabel('数量(个)')
plt.show()

dataPd = pd.Series(data,name='相关系数')
dataPd.to_csv(path=file+'相关系数.csv')