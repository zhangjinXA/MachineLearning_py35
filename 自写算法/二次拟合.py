import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
"""
定义绘图版
"""
#2d绘图
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, y,'ro');
#3d绘图
fig3d = plt.figure()
ax3d = Axes3D(fig3d)
# ax3d.plot_surface(x,x0,y)
#整体设置
plt.grid(True)  # 添加网格
plt.ion()  # interactive mode on
"""
#制造数据
"""
x = np.random.normal(0,5.0,500)
x0 = np.random.normal(0,5.0,500)
y = 4.5*x**2 + 18.9*x - 9;
y = 4.5*(x+np.random.normal(0,4,500)) + 18.9*(x0+np.random.normal(0,4,500)) - 9;
#绘图
ax3d.scatter(x,x0,y,c='r')
# plt.pause(1)
"""
#定义公式#
"""
w1 = tf.Variable(1,dtype='float64')
w2 = tf.Variable(1,dtype='float64')
theta = tf.Variable(1,dtype='float64')
y_fit = w1 * x**2 + w2*x +theta
y_fit = w1 * x + w2*x0 +theta
#定义loss
loss = tf.reduce_mean( tf.square(y_fit-y) )   # 均方差
#定义训练方法--梯度下降
opt = tf.train.GradientDescentOptimizer(0.001); #梯度下降
train = opt.minimize(loss)                     #梯度下降方法下最小化loss
#初始化，建立tf进程
init = tf.global_variables_initializer();
session = tf.Session()
session.run(init);
#递归
for xstep in range(40000):
    session.run(train)
    # print(xstep, session.run(w1), session.run(w2),session.run(theta), '**--4.5:18.9:-9')
    # plt.pause(0.0000000000000000001)
print(xstep, session.run(w1), session.run(w2), session.run(theta), '**--4.5:18.9:-9')
ax3d.scatter(x,x0,session.run(y_fit))
plt.pause(1000)
