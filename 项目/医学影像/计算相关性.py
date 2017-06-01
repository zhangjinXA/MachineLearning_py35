import numpy as np
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')


file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\插24um值矩阵.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 12,2048,2048   # nb,y,x

cor_data = np.zeros([2048,2048],dtype=np.float64)
x = np.linspace(1,7,7)
print(x)
for i1 in range(2048):
    for i2 in range(2048):
        y = data[0:7,i1,i2]
        cor = np.corrcoef(x,y,rowvar=0)
        cor_data[i1,i2] = cor[0][1]
    if i1%100 == 0 : print(i1)

outfile = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\'
cor_data.tofile(outfile+'插24um值矩阵-皮尔逊相关系数.img')