import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
'''
待设置变量
'''
reSample_rule = '30T'
file_path = 'C:\\Users\\16070332\\Desktop\\销售数据\\date_data\\'
write_path = 'C:\\Users\\16070332\Desktop\\销售数据\\date_data\\ReSample\\'
datatime = 'Sample_20160721.csv'
read_file = file_path + datatime
write_file = write_path + datatime + '_'+reSample_rule+'.csv'
'''
读取文件，并设置时间序列
'''
fopen = open(read_file,encoding='UTF-8');
data = pd.read_csv(fopen);
data.index = pd.to_datetime(data.iloc[:,0]); #设置时间序列Index
'''
重采样
'''
data2 = data.resample(reSample_rule).sum();  #按一小时间隔合计采样
data3 = data.resample(reSample_rule).count();
plt.plot(data3.index,data3['pay_amt'])
plt.show()
