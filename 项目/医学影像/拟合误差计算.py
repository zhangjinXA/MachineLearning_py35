import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#读取数据
file =  'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-15医学影像\\rawdata\\201705造数据\\插24um值矩阵.img'
data = np.fromfile(file,dtype=np.uint16);
data.shape = 12,2048,2048   # nb,y,x
data = data[0:7,:,:]
print(len(data[:,0,0]))
#
x = [1,2,3,4,5,6,7]
# y = data[:,1024,1024]

xpoint = [1416,1054,1653]
ypoint = [1429,987,396]
#
pdtemp = []
for i in range(len(xpoint)):
    xi,yi = xpoint[i],ypoint[i]
    y = data[:,xi,yi]
    fit = np.polyfit(x,y,deg=1);fit_p = np.poly1d(fit);y_fit = fit_p(x)
    name = str(xi)+','+str(yi)
    pdtemp.append(y.tolist())
    pdtemp.append(np.int32(y_fit).tolist())
# print(pdtemp[0:3])
pddddd = pd.DataFrame(pdtemp)
print(pddddd)
pddddd.to_excel( 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-15医学影像\\rawdata\\201705造数据\\拟合样本.xlsx')


# loss = np.sum(np.sqrt((y - y_fit)**2))
# print(loss)
# plt.plot(x,y)
# plt.plot(x,y_fit)
# plt.show()

