import pandas as pd
import numpy as np


file = "C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\插值之后数据\\6mu测量点插值1700.csv"
out_file = "C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\插值之后数据\\ShuiPing.img"
print('1')
data = pd.read_csv(file)
print('2')
data_value = data.values
print(type(data_value[0,0]))


a= np.zeros(100)
data_value.tofile(out_file)

