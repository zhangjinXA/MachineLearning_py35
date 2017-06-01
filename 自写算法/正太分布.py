import pandas as pd;
import numpy as np;
import tkinter.filedialog;
import matplotlib as mplt;

'''
批量读取
'''
file_path = '/Users/zhangxuewei/Desktop/销售数据/date_data/'
write_path = file_path+'date_data/reSample_'
reSample_rule = '1H'

data_total = []
filename = tkinter.filedialog.askopenfilename(initialdir=file_path,
                                              #filetypes=[("csv格式","csv")],
                                              multiple = 1);
for csvfile in filename:
    file_open = open(csvfile,encoding='UTF-8');
    data = pd.read_csv(file_open);
    data.index = pd.to_datetime(data.iloc[:,0]); #设置时间序列Index
    data_total.append(data)
    del data
##
data1 = pd.concat(data_total);
data12 = data1.resample(reSample_rule).sum();
print(data12)
mplt.plot(data12.index,data12['sale_cnt'])
# plt.show();

#
