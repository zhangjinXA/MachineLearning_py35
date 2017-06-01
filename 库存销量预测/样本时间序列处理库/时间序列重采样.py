import pandas as pd;
import matplotlib.pyplot as plt

# file = 'F:\\自发项目\\2017.3.17价格销量预测\\sample20160719.csv';
file = '/Users/zhangxuewei/Desktop/py35code/p1/data/sample20160720.csv'
fopen = open(file,encoding='UTF-8');
data = pd.read_csv(fopen);
data.index = pd.to_datetime(data.iloc[:,0]); #设置时间序列Index

data2 = data.resample('1H').sum()
print(data2);
plt.plot(data2.iloc[:,2]);
plt.show();