import pandas as pd;
import matplotlib.pyplot as plt
import numpy as np
from 自写算法 import 时间序列处理工具包 as timeKit
'''
处理数据
'''
dt_kit = timeKit.process_dateTime('R9001849_20150101');#dt_kit.filepath = 'C:\\Users\\16070332\\Desktop\\'
data = dt_kit.import_data('utf-8')  #statis_date column存在
print(data)

#step1--> groupby
data1 = data.groupby(['statis_date','fhdd']).sum()
data1 = data.groupby(['statis_date']).sum()
data1['statis_date'] = data1.index
#step2--> 重采样  与step1作用类似
data2 = data.resample('D').sum()
'''
年度频率
'''
# data2015 = data2['2017-01-01':]                       #2015年数据处理
# time2015 = dt_kit.时间序列格式化_批量更改年月日(data2015.index,'2015%m%d')
# data2016 = data2['2016-01-01':'2016-12-31'].dropna() #2016年数据处理
# time2016 = dt_kit.时间序列格式化_批量更改年月日(data2016.index,'2015%m%d')
# # 绘图
# plt.plot(time2015,data2015['_c2'])
# plt.plot(time2016,data2016['_c2'] )
# plt.ylim(0,500)
# plt.show()
'''
月度频率
'''
for days in [9,10,11]:
    day = days+1;
    Ym = '2016-'+str(day)
    data2017X = data2[str(Ym)]
    time2017X = dt_kit.时间序列格式化_批量更改年月日(data2017X.index,'201501%d')
    # 绘图
    plt.plot(time2017X,data2017X['_c3'] )
plt.ylim(0,500)
plt.show()

'''
按周频率显示
'''
# weekofday = dt_kit.年月日转为周几(data2.index)
# data2015.loc['weekofday'] = pd.DataFrame(weekofday)
# for i in range(10):
#     print(weekofday[0+7*i:7+7*i],'************')
#     plt.plot(weekofday[0+7*i:7+7*i],data2.iloc[0+7*i:7+7*i,1])
# plt.xlim(-1,7)
# plt.show()