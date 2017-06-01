import 读取西瓜数据集数据 as readcsv
import numpy as np;
import pandas as pd;
import tensorflow as tf;

#sample = readcsv.read_data('F:\\资料整理\\机器学习\\');
# sample = readcsv.read_data('/Users/zhangxuewei/Desktop/py35code/p1/data/西瓜数据集2.txt');
'''
取值
'''
# print(sample.iloc[0:5,2:3])       #数组定位  取数：0,1,2,3,4
# print(sample.loc[0:5,['根蒂']])   #标签定位  取数：0,1,2,3,4,5
# print(sample.describe());          #快速统计

'''
查找
'''
# data = pd.DataFrame(np.random.rand(20,5))
# # print(data);
# # print(data.describe())
# # print(data[data[0] > 0.5].index)
# # print(data.where(data[0] > 0.5))
'''
匹配
'''
# data2= pd.DataFrame([['a','b','c'],['list','done','fuck'],['sss','www','rrr']])
# # print(data2)
# # print(data2.isin(['list']))
'''
group_by
'''
data3 = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
                      'key2':['one', 'two', 'one', 'two', 'one'],
                      'data1':np.random.randn(5),
                      'data2':np.random.randn(5)})
# grouped_data3 = data3.groupby(data3['key1'])
# print(data3)
# print(grouped_data3)
# print(grouped_data3.mean())
# print(grouped_data3.sum())
# print(grouped_data3.count())
'''
Index
'''
#使用 DataFrame.dtypes 可以查看每列的数据类型，Pandas默认可以读出int和float64，其它的都处理为object，
# 需要转换格式的一般为日期时间。
# DataFrame.astype() 方法可对整个DataFrame或某一列进行数据格式转换，支持Python和NumPy的数据类型。
Udata = pd.DataFrame([['haha','dwads','dawsd','asd854'],[10,20,30,40]])
data2 = pd.DataFrame([['s12','d21'],[10,30]])
U=pd.merge(Udata,data2,how='inner')
print(Udata)
print(data2)
print(U)
'''
multiIndex
'''
sex = data3.index.get_level_values('sex')  ;
sex= sex.drop_duplicates();
age = data3.index.get_level_values(1)      ; #选取index内某一列值
age= age.drop_duplicates();  #去除重复值

idx = pd.IndexSlice
dataX1 = data3.loc[idx['index1里面的值','index2里面的值',:],'要展示的column']


