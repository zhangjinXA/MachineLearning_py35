import pandas as pd
from sklearn import preprocessing as pre
from sklearn.cluster import KMeans
import numpy as np


file ='C:\\Users\\30708\\Desktop\\活儿\\2017-6-3 聚类\\'
name = 'qq_格式转换.xlsx'
n_clusters = 5  #分类数目


'''读取数据'''
data = pd.read_excel(file+name,0)
host = data.iloc[:,3].tolist()
# label = data.iloc[:,4]


'''
分词
去掉.com等后缀
按域名规则排序
'''
host_list = []   #分词，整理后的数据
for i in host:
    temp = i.split('.')
    last = temp[-1].split('\\')
    # print(last[0],last[0].isdigit())
    #如果不是数字就翻转
    if not last[0].isdigit():
        temp = temp[0:-1]
        temp.reverse()
        # print(temp)
    else:
        temp = temp[0:-1] + [last[0]]
        print(temp)
    #
    host_list.append(temp)
print(host_list)


'''
enconding
转为词向量
'''
dims1_hosts = []
for i1 in host_list:
    for i2 in i1:
        dims1_hosts.append(i2)
# print(dims1_hosts)
le = pre.LabelEncoder()
le.fit(dims1_hosts)
#转为词向量
host_list_vector = host_list
for i1 in range(len(host_list)):
    for i2 in range(len(host_list[i1])):
        # print(le.transform(   [(host_list[i1])[i2]]   ))
        (host_list_vector[i1])[i2] = le.transform(   [(host_list[i1])[i2]]   )[0]

# print(host_list_vector)


'''
词向量特征提取
按权重累加
'''
host_feature = []
for i1 in host_list_vector:
    featureI = 0
    for i2 in range(len(i1)):
        featureI += i1[i2]*(10**(3-i2*2))*0.1
    host_feature.append(featureI)
    # print(i1,featureI)
print(host_feature)


'''
kmeans聚类
'''
host_feature = np.asarray(host_feature)
host_feature.shape = len(host_feature),1
km = KMeans(n_clusters)
km.fit(host_feature)
print(km.labels_)


'''
输出聚类信息
'''
data['cluster'] = km.labels_
print(data)
data.to_csv(file+'cluster_'+name+'.csv')
