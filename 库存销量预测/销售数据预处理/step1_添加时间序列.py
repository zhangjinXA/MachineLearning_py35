import os.path
import tkinter.filedialog

from 库存销量预测.销售数据预处理.func_单文件添加时间序列 import process_datafile;

'''
warning:原始csv数据文件必须以时间格式保存，如：20170203，无后缀
待设置变量
'''
datatime = '20160719'
file_path = 'C:\\Users\\16070332\\Desktop\\销售数据\\'
file_path = '/Users/zhangxuewei/Desktop/销售数据/'
write_path = file_path+'date_data/Sample_'
#'/Users/zhangxuewei/Desktop/codePY35/data/'
########
filename=tkinter.filedialog.askopenfilename(initialdir=file_path,
                                            #filetypes=[("all","*")],
                                            multiple = 1);
for csvfile in filename:
    datatime = os.path.basename(csvfile)
    write_file = write_path+datatime+'.csv'
    data = process_datafile(datatime,csvfile,write_file);#处理并保存数据
