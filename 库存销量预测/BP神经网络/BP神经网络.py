import tensorflow as tf
import pandas as pd
import numpy as np

#训练数据集整理
Xt = pd.read_csv('C:\\Users\\16070332\\Desktop\\中间数据\\神经网络X.csv')
Yt = pd.read_csv('C:\\Users\\16070332\\Desktop\\中间数据\\神经网络Y.csv')
X = Xt.iloc[:, 0:3].values.astype('float32')
Y = np.asarray(Yt.iloc[:, 1]).astype('float32')
#定义系数（输入3，一隐层，隐层神经元7个）
w1 = tf.Variable(tf.random_normal([3,7],stddev=2))
w2 = tf.Variable(tf.random_normal([7,1],stddev=2))
#定义输入特征
x = tf.constant(X)
y_ = tf.constant(Y)
#获得前馈输出
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)
#定义损失函数和反向传播算法
c1 = y_ * tf.log(tf.clip_by_value(y,1e-10,1.0))
cross_entropy = -tf.reduce_sum(c1)
# cross_entropy = y_ - y

train_step = tf.train.GradientDescentOptimizer(learning_rate=1e-14).minimize(cross_entropy)

#定义训练数据batch的大小
sess = tf.Session()
sess.run(tf.global_variables_initializer())

yy = sess.run(y)
yy_ = sess.run(y_)
print(yy_,yy,'************')
#设定训练轮数
steps = 70
for i in range(steps):
    #训练
    sess.run(train_step)
    if i%10 == 0:
        total_cross_entropy = sess.run(cross_entropy)
        print(i,'-----轮-----',total_cross_entropy)
#运行
w11 = sess.run(w1)
w22 = sess.run(w2)
for i in range(len(Y)):
     x1 = X[i]
     a1 = np.matmul(x1,w11)
     y1 = np.matmul(a1,w22)
     Yi = Y[i]
     # print(Y[i],'预测值:',y1,'-',Yi,' = ',y1-Yi )
sess.close()




