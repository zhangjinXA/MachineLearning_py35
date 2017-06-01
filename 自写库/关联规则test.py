import numpy as np
import pandas as pd
from sklearn import preprocessing as pre
from 自写库.关联规则 import *

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\已完成\\2017-5-23-关联规则\\'
name = '第一类规则（与运动方式、加工材料、行为相关）用数据.xlsx'

data = pd.read_excel(file+name,0).dropna()
Xz,Yz = data['运动方式'].values.tolist(),data['加工材料'].values.tolist()
#定义X,Y（list）
le = pre.LabelEncoder();le.fit(Xz+Yz)
X,Y = le.transform(Xz),le.transform(Yz)
#计算关联关系
关联度 = apriori(X,Y)
#输出
outfile = file+'test.csv'
f = open(outfile, 'w')
print('A1,n,A2,支持度,置信度', file=f)
for temp in 关联度:
    #输出到屏幕
    print(le.inverse_transform(temp[0]),
          ',->,',
          le.inverse_transform(temp[1]),
          ',支持度：',
          temp[2],',置信度：',
          temp[3]
          )
    #输出到文本
    print(le.inverse_transform(temp[0]),
          ',->,',
          le.inverse_transform(temp[1]),
          ',',
          temp[2],',',
          temp[3],
          file = f
          )
f.close()