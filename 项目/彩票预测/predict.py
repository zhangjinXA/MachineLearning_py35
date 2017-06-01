import pandas as pd
from 项目.彩票预测 import readfile
import numpy as np

def 预测(filename,预测范围,预测个数):

    data = readfile.read(filename)
    '''训练数据整理'''
    predict_data = data.iloc[-预测范围:,1].values  #选取

    predict_datalist = []                    #整理成数组
    for i in predict_data:
        temp = i.split(',')
        predict_datalist.append(temp)

    pdata = np.asarray(predict_datalist,dtype=np.int)
    # print(pdata[:,0])
    '''计算概率'''
    P_all = []
    for Ni in range(0,10,1):
        dataNi = pdata[:,Ni]  #每组数据
        lens = len(dataNi)
        P_Ni = []
        for num in range(1,11,1):
            index = np.where( dataNi == num )[0]
            lenIndex = len(index)
            p = lenIndex/lens
            P_Ni.append(p)
        P_all.append(P_Ni)
    '''整理成pandas'''
    P_pd = pd.DataFrame(P_all).T
    columns = ['area'+str(i) for i in range(1,11,1)]
    P_pd.columns = columns
    P_pd['号码'] = range(1,11,1)
    '''顺序提取每个位置的前N个值'''
    final_predict = []
    for i in range(10):
        cols = P_pd.columns
        temp = P_pd.sort_values(cols[i], ascending=True)['号码'].iloc[0:预测个数].values.tolist()
        final_predict.append(temp)
        # print(cols[i],temp)
    # print(final_predict)
    final_predict = pd.DataFrame(final_predict).T
    final_predict.columns = columns
    #
    return final_predict

def 转化为UI格式(pred):
    pred = np.asarray(pred,dtype=np.str_).T.tolist()
    UItxt = []
    for i in pred:
        temp = '\n'.join(i1 for i1 in i)
        UItxt.append(temp)
    return UItxt


# file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-彩票预测\\正序.txt'
#
# pred = 预测(file,40,3)
# UItxt = 转化为UI格式(pred)
# #
# print(pred)
# print(UItxt)
