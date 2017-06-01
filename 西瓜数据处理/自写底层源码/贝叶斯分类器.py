from 西瓜数据处理.西瓜数据读取与清洗 import read_XiGua
import pandas as pd
import numpy as np

a = pd.Series()
data = read_XiGua('E:\\PythonCode\\myPthon35_Code\\data\\西瓜数据集2.txt')
#提取每维度的维度值
a = []
for i in range(len(data.columns)-3):
    x = data.iloc[:,i].drop_duplicates()
    x.index = np.linspace(0,len(x.index)-1,len(x.index),dtype='int')
    a.append(x)
data_attri = pd.concat(a,axis=1)  #每个维度的维度值
print(data_attri)