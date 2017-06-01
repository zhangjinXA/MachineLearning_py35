import pandas as pd;
import numpy as np;
import scipy as sc;
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from 西瓜数据处理 import 西瓜数据读取与清洗
import numpy as np
#
'''决策树判断函数'''
def f(y):
    #
    def 信息熵(p): return p * np.log(p) / np.log(2)  # 信息熵
    #
    len_y = float(len(y))                           #样本总数
    K = np.unique(y,return_index=False)            #样本总类
    result = 0.0

    for i in K:
        Index_Ki = np.where(y==i)[0]
        Pk =  float(len(Index_Ki))/len_y
        result = result + 信息熵(Pk)
    result =  - result
    #定义结果为信息熵
    # print(len_y,float(len(Index_true_value)),p_true)
    return result
#
a = pd.Series()
file = 'E:\\PythonCode\\myPthon35_Code\\data\\西瓜数据集2.txt'
data = 西瓜数据读取与清洗.read_XiGua(file)
'''标签数字化'''
lb = preprocessing.LabelBinarizer()
lb.fit(data['好瓜'])
data['isGood'] = lb.transform(data['好瓜'])
Y = data['isGood'].values
Ent_All = f(data['isGood'].values)               #整体信息熵
'''子类信息熵计算'''
data_values = data.values
colums = data.columns
#
for i in range(len(colums)):  #属性column[i]
    dataI = data_values[:, i]
    numK = np.unique(dataI)
    Ent_Da = 0.0
    for i2 in numK:   #属性i中的属性值i2
        index = np.where(dataI == i2)[0]
        isGood_i2 = Y[index]
        Ent_Da = Ent_Da + (len(isGood_i2)/len(dataI)) * f(isGood_i2)
    GainEnt_II2 = Ent_All - Ent_Da
    print(colums[i],GainEnt_II2,Ent_All)



