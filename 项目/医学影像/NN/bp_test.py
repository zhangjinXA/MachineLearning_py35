import 项目.医学影像.NN.bp神经 as bpnn
import numpy as np
import tensorflow as tf
bp = bpnn.bp神经网络()
#
file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\插24um值矩阵.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 12,2048,2048   # nb,y,x
data = data[0:7,:,:]

'''bp'''
for i1 in range(300,1750):
    for i2 in range(300,1750):
        X = [i1,i2,1, 2, 3, 4, 5, 6, 7]
        X = np.asarray(X,dtype=np.float64)
        Y = data[:, i1, i2]
        #
        bp.define_XY(X,Y)
        if i2 > 300 :
            bp.w1,bp.w2 = tf.Variable(w1),tf.Variable(w2)
        bp.迭代次数 = 500
        w1,w2,y_fits,loss = bp.开始训练()
