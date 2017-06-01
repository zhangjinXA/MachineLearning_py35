import pandas as pd;
import matplotlib.pyplot as plt
import numpy as np
from 自写算法 import 时间序列处理工具包 as timeKit

a = pd.DataFrame();
fig = plt.figure() ;
p = fig.add_subplot(1,1,1);

tKit = timeKit.process_dateTime()
tKit.filepath='F:\\资料整理\\myPthon35_Code\\data\\sal库eam存t\\'
单品销量日占比 = tKit.import_data(name='单品销量日占比.csv',encoding='utf-8',dataFormat='%Y-%m-%d')

商品编码 = 单品销量日占比.gds_cd.drop_duplicates()
for i in 商品编码 :
    data = 单品销量日占比[单品销量日占比.gds_cd == i]
    p.plot(data.index,data.iloc[:,-1])
    plt.pause(0.5)