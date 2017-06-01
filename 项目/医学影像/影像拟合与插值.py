import numpy as np
import matplotlib.pyplot as plt
# from tensorflow.examples.tutorials.mnist import input_data
#读取数据
file = 'C:\\Users\\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\4号-RAW影像\\all——除了24.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 10,2048,2048   # nb,y,x
dataX = [1,3,5,6,7,8,9,10,11,12]
rg = 5 # 取值上限

#定义输出
pppp系数矩阵 = np.zeros([2,2048,2048],dtype=np.float64) #bsq b,y,x
data插24um值矩阵 = np.zeros([12,2048,2048],dtype=np.uint16)
data24um值 = np.zeros([2,2048,2048],dtype=np.uint16)
#
data插24um值矩阵[0,:,:]=data[0,:,:]   #1mu赋值
data插24um值矩阵[2,:,:]=data[1,:,:]   #3mu赋值
data插24um值矩阵[4:,:,:] = data[2:,:,:] #5mu以后赋值
#
for i1 in range(2048):
    for i2 in range(2048):
        x = dataX[:rg];y = data[:rg,i1,i2]
        fit = np.polyfit(x,y,1)  #拟合
        fit_p = np.poly1d(fit)   #提取拟合公式

        data24um值[0,i1,i2],data24um值[1,i1,i2] = np.uint(fit_p(2)),np.uint(fit_p(4))
        pppp系数矩阵[:,i1,i2] = fit
        if (i1%100==0) & (i2%1000 == 0) :
            print('X,Y-',i1,i2,'--系数矩阵：',pppp系数矩阵[:,i1,i2],'实际系数:',fit)

data插24um值矩阵[1,:,:] = data24um值[0,:,:]
data插24um值矩阵[3,:,:] = data24um值[1,:,:]


outfile = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\'
data插24um值矩阵.tofile(outfile+'插24um值矩阵2.img')
pppp系数矩阵.tofile(outfile+'pppp系数矩阵2.img')

