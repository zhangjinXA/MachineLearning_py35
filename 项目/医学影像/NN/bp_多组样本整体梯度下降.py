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
#读取数据
file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\插24um值矩阵.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 12,2048,2048   # nb,y,x
data = data[:7,:,:] / 1000.
####组织成训练数据
x,y = [],[]
start = 300 ; end = 800
for i1 in range(start,end,1):
    for i2 in range(start,end,1):
        x.append([i1,i2])
        y.append(data[:,i1,i2].tolist())
x = np.asarray(x,dtype=np.float64)
y = np.asarray(y,dtype=np.float64)
print(x.shape,y.shape)
####################################################################################
lenx=2;                         #输入层个数
output_num = 7 ;                #输出层个数
hidden_num =300 ;               #隐层神经元个数
学习率 = 0.01
迭代次数 = 1000000
随机样本个数 = 500            #随机梯度下降
# test_index = 100
sess = tf.Session()
##
'''bp设置·········'''
#定义训练数据
# x_train,y_train = x[:随机样本个数,:],y[:随机样本个数,:]
x_train = tf.placeholder(dtype=tf.float64,shape=(随机样本个数,lenx))
y_train = tf.placeholder(dtype=tf.float64,shape=(随机样本个数,output_num))
#定义w
w1 = np.random.rand(lenx*hidden_num) ; w1.shape = lenx,hidden_num;w1 = tf.Variable(w1)
w2 = np.random.rand(hidden_num*output_num) ; w2.shape = hidden_num,output_num;w2 = tf.Variable(w2)
#
hidden_State = tf.matmul(x_train,w1)
y_fit = tf.matmul(hidden_State,w2)
#
print(w1);print(w2);print(hidden_State);print(y_fit)
loss = tf.reduce_sum(tf.square(y_train-y_fit))
梯度下降 = tf.train.AdamOptimizer(learning_rate=学习率).minimize(loss)
#
sess.run(tf.global_variables_initializer())
for i in range(迭代次数):
    random_index = np.random.randint(low=0, high=(end - start) ** 2, size=随机样本个数)  # 随机序列
    tempX,tempY = x[random_index,:],y[random_index,:]
    sess.run(梯度下降,feed_dict={x_train:tempX,y_train:tempY})
    if i%100 == 0:
        ax.plot(tempY[0,:])
        plt.ylim(np.min(tempY[0,:]),np.max(tempY[0,:]))
        #
        y_fits = sess.run(y_fit,feed_dict={x_train:tempX})
        ax.plot(y_fits[0,:] , 'o')
        #
        plt.title('训练次数：' + str(i) + '--误差:' + str(sess.run(loss,{x_train:tempX,y_train:tempY})))
        plt.pause(0.000000000000001)
        ax.lines.pop(1)
        ax.lines.pop(0)


#训练参数输出

w1 = sess.run(w1)
w2 = sess.run(w2)

test = [400,900]
hidden_State = np.matmul(x,w1)
y_fits = np.matmul(hidden_State,w2)

