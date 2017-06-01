import numpy as np
import pandas as pd
import jieba
from sklearn import preprocessing as pre


def 按词频排序(dataSet):
    cutData = list(jieba.cut(dataSet, cut_all=False))  #分词结果
    #
    filterData =[] #词内元素小于2的剔除
    for i in cutData:
        if len(i) >= 2 :
            filterData.append(i)
    #词向量转换
    le = pre.LabelEncoder()
    le.fit(filterData)
    coder = le.transform(filterData)
    #寻找高频词
    pdData = pd.DataFrame(filterData,columns=['word'])
    pdData['count'] = coder
    tt = pdData.groupby(by='word',axis=0).count()
    final = tt.sort('count',ascending=False)
    return final


# file = 'C:\\Users\\ZhangSSD\Desktop\\活儿\\2017-5-9-基于RNN的新闻文本关键字提取\\'
# tname = '英超-孙继海轻伤不下火线 曼城1-1惜平沃特福德.txt'
# dataSet = open(file+tname, 'r').read() #读取txt一整个文件的内容为字符串str类型
# final = 按词频排序(dataSet)
# bbb = ''.join(final.index[:5])
# print(bbb)

