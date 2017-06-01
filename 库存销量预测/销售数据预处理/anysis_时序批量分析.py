import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
import tkinter.filedialog
'''
待设置变量
'''
reSample_rule = '30T'
file_path = 'C:\\Users\\16070332\\Desktop\\销售数据\\date_data\\'
write_path = file_path+'all.csv'
'''
批量读取
'''
data_total = [];
filename=tkinter.filedialog.askopenfilename(initialdir=file_path,
                                            filetypes=[("csv格式","csv")],
                                            multiple = 1);
for csvfile in filename:
    file_open = open(csvfile,encoding='UTF-8');
    data = pd.read_csv(file_open);
    data.index = pd.to_datetime(data.iloc[:,0]); #设置时间序列Index
    data_total.append(data)
    del data
##
data3 = pd.concat(data_total)

#data3 = data3.sort_index()
data32 = data3.resample(reSample_rule).sum();
plt.plot(data32.index,data32['sale_cnt'])
plt.show()
