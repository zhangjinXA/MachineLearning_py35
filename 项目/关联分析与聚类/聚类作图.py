import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#matplotlib中文显示
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题


file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '聚类1.csv'

data = pd.read_csv(file+name,encoding='GB2312')
地层 = list(set(data['地层'].values.tolist()))

for i in 地层:
    #
    fig = plt.figure()
    ax = fig.add_subplot(111,projection = '3d')
    plt.title('地层-'+str(i))
    #
    tempdata = data[data['地层'] == i]
    clusters = list(set(tempdata['cluster'].values.tolist()))
    for ii in clusters:
        temp2data = tempdata[tempdata['cluster'] == ii]
        X = temp2data['X']
        Y = temp2data['Y']
        Z = temp2data['Z']
        # ax.plot(X,Y,'*',label='类别'+str(ii))
        ax.scatter(X, Y, Z, marker='*',label='类别'+str(ii))  # 点为红色三角形
    plt.legend()
    plt.show()

