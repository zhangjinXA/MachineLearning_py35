from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#matplotlib中文显示
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

'''
可修改区域
'''
file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '聚类分析用数据.xlsx'
numClasses = 5  #分几类
data = pd.read_excel(file+name,0)  #读取第几个表，0 = sheet1
'''
不可修改区域
'''
X = data.iloc[:,[2,3,4]]
clu = KMeans(numClasses).fit(X)
data['cluster'] = clu.labels_.tolist()
#
outfile = file+'整体聚类.csv'
data.to_csv(outfile)
ofile = open(outfile,'a')

clusterSet = list(set(clu.labels_))
print('\n聚类中心点',file=ofile)
print('cluster,x,y,z',file=ofile)
n = 0
for i in clu.cluster_centers_:
    ii = np.asarray(i,dtype=np.str)
    print(clusterSet[n] ,',', ','.join(ii.tolist()),file=ofile)
    n += 1

#
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
plt.title('all-')
for i in clusterSet:
        temp2data = data[data['cluster'] == i]
        X = temp2data['X']
        Y = temp2data['Y']
        Z = temp2data['Z']
        ax.scatter(X, Y, Z, marker='*', label='cluster ' + str(i))  # 点为红色三角形
plt.legend()
plt.show()





