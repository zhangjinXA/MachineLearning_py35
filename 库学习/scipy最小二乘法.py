from scipy.optimize import leastsq;
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.tensorboard as ts
'''
定义绘图板
'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
'''
定义函数
'''
def func(p,x):  #定义函数
     k1,k2,b=p
     return k1*x**2 + k2*x + b
def loss(p,x,y):
    return func(p,x)-y #x、y都是列表，故返回值也是个列表
'''
制造数据
'''
x_data = np.random.rand(1000)   # X数据
y_data = func([3.5,4.8,9.7],x_data) + np.random.normal(0,0.1,1000) #Y+噪声数据
'''
最小二乘法
'''
para = leastsq(loss,[0,0,0],args=(x_data,y_data))
y_fit = func(para[0],x_data)
###############绘图
ax.plot(x_data,y_data,'ro')
ax.plot(x_data,y_fit,'bo')
plt.show();

