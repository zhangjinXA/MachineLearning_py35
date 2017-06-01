import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
###################################################################################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.grid(True)  # 添加网格
####################################################################################
####################################################################################
lenx=output_num = 7 ; hidden_num =400 ;
学习率 = 0.07
迭代次数 = 100000
sess = tf.Session()
#
x = np.random.rand(lenx*2048);x.shape = 2048,lenx
y = 2.78 * x + 4.35
#plot
plt.plot(x[10,:],y[10,:])
plt.xlim(np.min(x[10,:]),np.max(x[10,:]))
plt.ylim(np.min(y[10,:]),np.max(y[10,:]))
plt.pause(0.1)
#
w1 = np.random.rand(lenx*hidden_num) ; w1.shape = lenx,hidden_num
w2 = np.random.rand(hidden_num*output_num) ; w2.shape = hidden_num,output_num
#
w1 = tf.Variable(w1)
w2 = tf.Variable(w2)
#
hidden_State = tf.matmul(x,w1)
y_fit = tf.matmul(hidden_State,w2)
#
print(w1)
print(w2)
print(hidden_State)
print(y_fit)
loss = tf.reduce_sum(tf.square(y-y_fit))
梯度下降 = tf.train.AdamOptimizer(learning_rate=学习率).minimize(loss)
#
sess.run(tf.global_variables_initializer())
for i in range(迭代次数):
    sess.run(梯度下降)
    if i%300 == 0:
        y_fits = sess.run(y_fit)
        ax.plot(x[10,:],y_fits[10,:] , 'ro')
        plt.title('训练次数：' + str(i) + '--误差:' + str(sess.run(loss)))
        plt.pause(0.000000000000001)
        ax.lines.pop(1)