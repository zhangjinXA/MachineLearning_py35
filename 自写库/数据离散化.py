#仅支持以为数据离散化
from sklearn.cluster import KMeans
import numpy as np
class 离散化:

    def __init__(self):

        return None

    def fit(self,X,num):
        self.kmeans = KMeans(num)
        X2 = np.asarray(X);X2.shape = len(X2),1
        #
        self.kmeans.fit(X2)
        labels = self.kmeans.labels_
        #建立范围字典
        matchValue = []
        for i in range(len(X)):
            matchValue.append([X[i],labels[i]])
        matchValue = np.asarray(matchValue)
        # print(matchValue)
        #
        self.dict = {}
        setlabel = list(set(labels))
        for i in setlabel:
            index = np.where(matchValue[:,1] == i)[0]
            max = np.max(matchValue[index,0])
            min = np.min(matchValue[index,0])
            strs  = str(min)+'-'+str(max)
            self.dict[i] = strs

        return self.dict

    def transform(self,X):
        X2 = np.asarray(X);X2.shape = len(X2), 1
        temp = self.kmeans.predict(X2)
        return temp
    def inverse_transform(self,labels):
        if type(labels) != type(list()): labels = [labels]
        temp = []
        for i in labels:
            temp.append(self.dict.get(i))
        return temp