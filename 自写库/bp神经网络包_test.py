from 自写库 import bp神经网络包 as bpcnn
import numpy as np
#
x = np.random.rand(10*30)
x.shape = 10,30

y = np.random.rand(10)


#
a = bpcnn.bp神经网络()
a.define_XY(x,y)  # -99代表使用测试数据
a.迭代次数 = 20000
a.学习率 = 0.000000000001
a.开始训练()

outfile = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-15医学影像\\论文\\数据\\'
outname = '迭代次数与损失值图.xlsx'
a.save_param(outfile,outname)