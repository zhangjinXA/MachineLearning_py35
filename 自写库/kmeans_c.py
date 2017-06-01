from sklearn.cluster import KMeans
import sklearn.preprocessing as pre
from sklearn.externals import joblib
import pandas as pd

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-30-聚类-学生\\'
name = 'data.csv'  #输入文件名
outname = 'cluster_data.csv' #输出文件名
num_classes = 5 #分几类
data = pd.read_csv(file+name)
#数据预处理
le = pre.LabelEncoder()
le.fit(data.iloc[:,0].values)
sex = le.transform(data.iloc[:,0].values)

data.iloc[:,0] = sex * 0.2 #性别归一化
data.iloc[:,-1] = data.iloc[:,-1] * 0.05  #年龄归一化
#kmeans聚类
km = KMeans(num_classes)
km.fit(data.values)

#
data['classes'] = km.labels_.tolist()
data.to_csv(file+outname)
print(data)
#
#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
for i in range(5,30,1):
     clf = KMeans(n_clusters=i)
     s = clf.fit(data.values)
     print(i , clf.inertia_)

'''模型的保存与载入方法'''
#保存模型
joblib.dump(km , 'd:/km.pkl')
#载入保存的模型
clf = joblib.load('d:/km.pkl')
