import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
'''
定义绘图板
'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
'''
定义函数
'''
def func(p,x):  #定义函数
     return p[0]*x**2 + p[1]*x + p[2]
'''
制造数据
'''
x_data = np.random.rand(1000)   # X数据
y_data = func([3.5,4.8,9.7],x_data) + np.random.normal(0,0.1,1000) #Y+噪声数据
#绘图
ax.plot(x_data, y_data,'ro');
plt.ylim(min(y_data), max(y_data))
'''
定义公式，损失函数，回归方法
'''
#定义参数
p1 = tf.Variable(1.0);
p2 = tf.Variable(1.0);
p3 = tf.Variable(1.0);
#定义公式
y_fit = p1*x_data**2 + p2*x_data + p3;
#定义损失函数
loss = ((y_fit - y_data)**2)/len(y_data);
#定义回归方法
opt = tf.train.GradientDescentOptimizer(0.1) #定义学习率
train = opt.minimize(loss)                   #定义梯度下降最小化对象
'''
创建ts进程
'''
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
'''
开始迭代
'''
for xstep in range(800):
     sess.run(train);
     '''
     绘制迭代过程图
     '''
     print(xstep,sess.run(p1),sess.run(p3),'**--0.1--0.3')
     ax.plot(x_data, sess.run(y_fit),'bo');
     plt.pause(0.000000000001)
     ax.lines.pop(1)