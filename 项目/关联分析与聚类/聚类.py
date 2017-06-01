from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def cluster(data,numofCluster):
    # kmeans聚类
    km = KMeans(5)
    km.fit(data)
    # 保存模型
    labels = km.labels_

    return labels

def genrate_cluster(data,numofCluster):
    data['cluster'] = 0
    地层 = np.unique(data.地层.values)
    for cengshu in 地层:
        tempData = data[data.地层 == cengshu]
        index = tempData.index
        # print(data[data.index.isin(index)])
        X = tempData.iloc[:,[2,3,4]]
        if len(X.index) >= numofCluster+2 :
            tap = cluster(X,numofCluster)
        else:
            tap = np.zeros(len(X.index),dtype=np.int)
        clu = pd.Series(tap,index=X.index.values,name=cluster)
        data.iloc[X.index.values,-1] = tap
    return data


file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '聚类分析用数据.xlsx'

data1 = pd.read_excel(file+name,0)
data2 = pd.read_excel(file+name,1)
#
data1 = genrate_cluster(data1,3)
data1.to_csv(file+'聚类1.csv')
print(data1)
#
data2 = genrate_cluster(data2,3)
print(data2)
