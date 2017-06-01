import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

path = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\处理后数据\\'
name = '情感分析结果汇总.xlsx'
def cluster_data(data):
    feature = data.iloc[:, [1, 2]]
    X, Y = data.iloc[:, 1], data.iloc[:, 2]

    clf = KMeans(n_clusters=10)
    s = clf.fit(feature.values)
    feature['cluster'] = clf.labels_
    # 分类中心

    cluster_center = clf.cluster_centers_

    推荐指数array = (
                    np.sqrt(
                        (cluster_center[:, 0]) ** 2 + (cluster_center[:, 1]) ** 2
                    )
                ) / 100.

    new = np.c_[cluster_center, 推荐指数array];
    推荐指数 = pd.DataFrame(new, columns=['centerX', 'centerY', '推荐指数'])

    feature['推荐指数'] = 0.
    feature['推荐指数2'] = 0
    print(推荐指数)
    for k in range(10):
        index = np.where(feature['cluster'] == k)[0]
        feature.iloc[index, -2] = 推荐指数.iloc[k, -1]
    return feature


def process_point(path,name):
    data旅店 = pd.read_excel(path+name,0)
    data景点  = pd.read_excel(path+name,1)
    #
    # feature1 = cluster_data(data旅店)
    # feature2 = cluster_data(data景点)
    print(data景点.RANK)
    return data景点

data = process_point(path,name)
# for i in range(10):
#     X = data.iloc[np.where(data['cluster']==i)[0], 0]
#     Y = data.iloc[np.where(data['cluster']==i)[0], 1]
#     plt.plot(X,Y,'o',label=str(i))
# plt.legend()
# plt.show()




