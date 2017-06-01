import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
###################################################################################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ax.axis("equal")  # 设置图像显示的时候XY轴比例
plt.grid(True)  # 添加网格
####################################################################################3
#
class bp神经网络:
    #
    __sess = tf.Session()
    # 输入神经元个数, 输出神经元个数 = 150, 150
    隐层神经元数 = 2
    学习率 = 0.0004
    迭代次数 = 5000
    # define input data
    '''仅接受一维numpy数组'''
    def define_XY(self,input_data, y_true):
        if (len(input_data) == 1) or (len(y_true) == 1):
            x0 = np.linspace(-20, 20, 150);
            y =  4.3 * x0 ** 3 + 7.5* x0**2 + 9.7
            y += np.random.rand(150)
        else:
            x0 = input_data
            y = y_true
        #
        self.输入神经元个数 = len(x0)
        self.输出神经元个数 = len(y)
        x = x0.copy(); x.shape = 1, self.输入神经元个数
        ###
        self.__x0,self.__x,self.y = x0,x,y
        self.__param_for_bp()
        # plot
        # plt.xlim(np.min(x0), np.max(x0))
        # plt.ylim(np.min(y), np.max(y) + np.min(y) / 5)
        # ax.plot(x0, y, marker='o')
        # plt.pause(0.1)
    #定义w1,w2
    def __param_for_bp(self):
        w1_np = np.random.rand(self.输入神经元个数 * self.隐层神经元数) ; w1_np.shape = self.输入神经元个数, self.隐层神经元数
        w2_np = np.random.rand(self.隐层神经元数 * self.输出神经元个数) ; w2_np.shape = self.隐层神经元数, self.输出神经元个数
        self.__w1 = tf.Variable(w1_np) #隐层系数
        self.__w2 = tf.Variable(w2_np)  #输出层系数
        #
        self.__hy = tf.matmul(self.__x,self.__w1)  #hidden_layer 值
        self.y_fit = tf.matmul(self.__hy,self.__w2)  # 输出值
        #损失函数
        self.loss = tf.reduce_sum(
                     tf.square(self.y - self.y_fit))
        self.__梯度下降 = tf.train.AdamOptimizer(learning_rate=self.学习率).minimize(self.loss)
    #
    def 开始训练(self):
        sess,y_fit,loss,梯度下降 = self.__sess,self.y_fit,self.loss,self.__梯度下降
        sess.run(tf.global_variables_initializer())
        #
        losses = []
        for i in range(self.迭代次数):
            sess.run(梯度下降)
            #输出
            if i%100==0 :
                y_fits = sess.run(y_fit)
                ax.plot(self.__x0,y_fits[0,:] ,'ro')
                plt.title('训练次数：'+str(i/100)+'--误差:'+str(sess.run(loss)))
                plt.pause(0.000000000000001)
                ax.lines.pop(1)
                tempsssssssssss = [sess.run(loss),i]
                print('*********', tempsssssssssss)
                losses.append(tempsssssssssss)

        self.losses = pd.DataFrame(losses,columns=['loss','迭代次数'])

    def save_param(self,outfile,outname):
        outfilename = outfile + outname
        self.losses.to_excel(outfilename,sheet_name='Sheet1')
