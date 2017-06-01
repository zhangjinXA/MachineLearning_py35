import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

#
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ax.axis("equal")  # 设置图像显示的时候XY轴比例
plt.grid(True)  # 添加网格
#
input_num,output_num = 150,150
隐层神经元数 = 100
#
x0  = np.linspace(-20,20,input_num);

y = 2.7*x0**2 + 4.3*x0 +9.7*x0**3+ 4.3 + 9.7*x0**4
# y = np.sin(x0)
# y = np.random.rand(output_num)
x= x0.copy();x.shape = 1,input_num


plt.xlim(np.min(x0),np.max(x0))
plt.ylim(np.min(y),np.max(y) + np.min(y)/5)
ax.plot(x0,y,marker='o')
plt.pause(0.1)
#
'''CNN'''

h1w1 = np.random.rand(input_num*隐层神经元数) ; h1w1.shape = input_num,隐层神经元数
ow2 = np.random.rand(隐层神经元数*output_num) ; ow2.shape = 隐层神经元数,output_num
#
w1 = tf.Variable(h1w1) #隐层系数
w2 = tf.Variable(ow2)  #输出层系数
#
hy = tf.matmul(x,w1)  #hidden_layer 值
y_fit = tf.matmul(hy,w2)  # 输出值
#
loss = tf.reduce_sum(
             tf.square(y - y_fit))
#
lr = 0.001
梯度下降 = tf.train.AdamOptimizer(learning_rate=lr).minimize(loss)
#
sess = tf.Session()
sess.run(tf.global_variables_initializer())

print(sess.run(y_fit))
print(sess.run(loss))
#设定训练轮数
steps = 500000
for i in range(steps):
    sess.run(梯度下降)

    if i%100==0 :
        y_fits = sess.run(y_fit)
        ax.plot(x0,y_fits[0,:] ,'ro')
        plt.title('训练次数：'+str(i)+'--误差:'+str(sess.run(loss)))
        plt.pause(0.000000000000001)
        ax.lines.pop(1)
