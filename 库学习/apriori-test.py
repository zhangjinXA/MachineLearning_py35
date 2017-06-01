import 自写库.apriori_forPY3 as ap
import pandas as pd
import sklearn.preprocessing as pre
import numpy as np

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '关联规则第一类规则（与运动方式、加工材料、行为相关）用数据.xlsx'
data = pd.read_excel(file+name,0)
# dataSet = data.iloc[:,7:].values
dataSet = data.values
dataSet = np.asarray(dataSet,dtype=np.str)
#
fitData = []
for i in range(dataSet.shape[1]):fitData += dataSet[:,i].tolist()
le = pre.LabelEncoder()
le.fit(fitData)
for i in range(dataSet.shape[1]):
    temp_coder = le.transform(dataSet[:,i].tolist())
    dataSet[:, i] = temp_coder
dataSet = np.asarray(dataSet,dtype=np.int)
dataSet = dataSet.tolist()
print(dataSet)
#

# dataSet=ap.loadDataSet()
# print(type(dataSet[0][0]))
C1=ap.createC1(dataSet)
ap.le = le
L,supportData=ap.apriori(dataSet,0.1)
brl=ap.generateRules(L, supportData,0.7)


print('brl---------------------------------------------------------------')

for i1 in brl:
    temp1 = i1[:-1]
    temp10 = []
    for i2 in temp1:
        for i3 in i2:
            temp10.append( le.inverse_transform(i3))
    temp2 = i1[-1]
    tempF = [temp10,temp2]

    print(tempF)


