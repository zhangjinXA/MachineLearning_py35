import numpy as np


file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\插24um值矩阵.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 12,2048,2048   # nb,y,x

# 方差
noise1 = np.random.normal(0.0,10,[2048,2048])
noise2 = np.random.normal(0.0,10,[2048,2048])
print('111')
data[1,:,:] += np.uint16(np.round(noise1,0))
data[3,:,:] += np.uint16(np.round(noise2,0))

outfile = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\'
data.tofile(outfile+'插24um值矩阵_添加噪声.img')
