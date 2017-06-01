'''
0、读取csv
1、选取数据
2、index操作：选取，更换，提升为column，命名
3、数据筛选：根据column筛选，根据index筛选，按时间区间筛选
4、时间：格式转换，重采样
5、
'''
import pandas as pd;
import numpy as np;

'''
0-------读取csv
'''
file = 'F:\\资料整理\\myPthon35_Code\\data\\sal库eam存t\\20150101_R'
data = pd.read_csv(file,encoding='GBK')
# print(data)
'''
1-------选取数据
'''
# 按序列提取/赋值
data.iloc[0:3, 2]  = [11,22,33]  # row:[0,1,2] , column:[2](gds_cd)
# 按column名提取/赋值 整条数据
data[['gds_cd', 'sale_amt_sum']]
#按column名提取/赋值 部分数据
data.loc[ 0:3, ['gds_cd', 'sale_amt_sum'] ] # row:[0,1,2]
'''
2-------数据拼接
'''
# 首尾拼接
data1,data2 = pd.DataFrame(data=[1,2,3,4,5]),pd.DataFrame(data=[6,7,8,9,10])
dataMerge = pd.concat([data1,data2]);#print(dataMerge)
'''
3---------数据更改
'''
values = data.values
values[[0,1,2,3], 1] = 19990101
data2 = pd.DataFrame(data=values,columns=data.columns,index=data.index)

data2.iloc[[0, 1, 2, 3], 1] = 100000101
print(data2)
'''
2-------index操作
'''
#指定index
data.index = data['statis_date'];#print(data.index);
#index还原为column
'''
4-------时间序列操作
'''
#时间格式转换
data.index = pd.to_datetime(data.index,format='%Y%m%d')
#生成时间序列
date = pd.date_range('2015-01-01','2015-01-30',freq='1D');
# for i in date : print(i);
#按时间选取数据
data2015 = data['2015'];#print(data2015);     #选取2015年整年数据
#按时间丢弃数据
data2015_filter = data2015.drop(date);#print(data2015_filter)


