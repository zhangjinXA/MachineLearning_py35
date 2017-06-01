import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
###################################################################################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.grid(True)  # 添加网格
####################################################################################
#读取数据
file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-22-股市预测-bp\\收盘价_时序数据 -改善.xls'
data = pd.read_excel(file,0)
print(data)
####组织成训练数据
#x.shape = 样本条数，输入个数
#y.shape = 样本条数,输出个数

x = data.iloc[:,4:].values
y = data.iloc[:,3].values ; y.shape = len(y),1

print(x.shape)
print(y.shape)



####################################################################################
# 必改参数
lenx=x.shape[1];                         #输入层个数
output_num = y.shape[1] ;                #输出层个数
start,end = 0,y.shape[0] -1     #训练样本开始结束条目数
随机样本个数 = x.shape[0]            #随机梯度下降
#选改参数
hidden_num =300 ;               #隐层神经元个数
学习率 = 0.001
迭代次数 = 100000000

# test_index = 100


#
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

hidden_bias = np.zeros((1,hidden_num))
output_bias = np.zeros((1,output_num))
#
hidden_State = tf.tanh(
    tf.add(
        tf.matmul(x_train,w1) , hidden_bias
    )
)
y_fit = tf.add(tf.matmul(hidden_State,w2) , output_bias)
#
print(w1);print(w2);print(hidden_State);print(y_fit)
loss = tf.reduce_sum(tf.square(y_train-y_fit))
梯度下降 = tf.train.AdamOptimizer(learning_rate=学习率).minimize(loss)
#
sess.run(tf.global_variables_initializer())
for i in range(迭代次数):
    random_index = np.random.randint(low=0, high=(end - start), size=随机样本个数)  # 随机序列
    tempX,tempY = x[random_index,:],y[random_index,:]
    sess.run(梯度下降,feed_dict={x_train:tempX,y_train:tempY})

    if i%100 == 0:
        #plot   根据输入数据特点修改
        y_fits = sess.run(y_fit,feed_dict={x_train:tempX})
        ax.plot(tempY[:,0],'ro')
        ax.plot(y_fits[:,0] , 'b+')
        plt.ylim(np.min(y_fits[:, 0]) -1, np.max(y_fits[:,0]) + 1)
        #设置显示
        plt.title('训练次数：' + str(i) + '--误差:' + str(sess.run(loss,{x_train:tempX,y_train:tempY})))
        plt.pause(0.000000000000001)
        ax.lines.pop(1)
        ax.lines.pop(0)
        print(tempY[:10,0])
        print(y_fits[:10,0])
        print('+++++++++++++++++++++++++')

# plot   根据输入数据特点修改
y_fits = sess.run(y_fit, feed_dict={x_train: tempX})
ax.plot(tempY[:, 0], 'ro')
ax.plot(y_fits[:, 0], 'b+')
plt.ylim(np.min(y_fits[:, 0]), np.max(y_fits[:, 0]))
# 设置显示
plt.title('训练次数：' + str(i) + '--误差:' + str(sess.run(loss, {x_train: tempX, y_train: tempY})))
#训练参数输出
plt.show()
w1 = sess.run(w1)
w2 = sess.run(w2)

test = [400,900]
hidden_State = np.matmul(x,w1)
y_fits = np.matmul(hidden_State,w2)

