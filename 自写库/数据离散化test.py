from 自写库.数据离散化 import 离散化 as pre2
import pandas as pd

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '第一类规则（与运动方式、加工材料、行为相关）用数据.xlsx'

data = pd.read_excel(file+name,0).dropna()
长度 = data['长']
#
le = pre2()
a = le.fit(长度.values,5)
b = le.transform([15.0])
c = le.inverse_transform([0])
#
print('a\n',a)
print('b\n',b)
print('c\n',c)