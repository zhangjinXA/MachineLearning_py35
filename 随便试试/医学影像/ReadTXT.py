import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import leastsq;
import numpy as np
import math

'''
读取数据
'''
file = 'C:\\Users\\Administrator\\Desktop\\DM\\2890000.txt'
data = pd.read_table(file,header=None,encoding='gb2312',delim_whitespace=True,index_col=None)
x = data.iloc[:,0]
y = data.iloc[:,1]
'''
拟合设置
'''
#定义拟合函数
def func(w,x):
    y_cal = 0
    for i in range(len(w)):
        y_cal = np.exp(y_cal + w[i]*x**(len(w)-1-i))
    return y_cal
#定义损失函数
def loss(w,x,y_true):
    lossY = func(w,x)-y_true
    return lossY
#测试定义的函数正确性
# xx = np.array([1.0,2.0,3.0,4.0,5.0])
# ww = np.array([1,1,1])
# yy = func(ww,xx)
# print(yy)
#拟合
初始系数 =  [0,0,0]    #数组个数决定拟合最高次幂，比如[1,1]为线性拟合，[1,1,1]为二次多项式
para = leastsq(loss,初始系数, args=(x, y))    #拟合系数
y_fit = func(para[0], x)
###############绘图
print('拟合系数：',para[0])
x_re=[]
y_fit_re=[]
for i in range(math.floor(len(x)/10000.0)):
    x_re.append(x[i*10000])
    y_fit_re.append(y_fit[i*10000])

plt.scatter(x,y,s=0.1)
plt.plot(x_re, y_fit_re,color='red')
plt.show()