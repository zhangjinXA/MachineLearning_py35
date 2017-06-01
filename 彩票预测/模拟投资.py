import pandas as pd

from 彩票预测.优化项目.预测算法 import predict_1
from 彩票预测.当期盈亏计算 import cal_猜数字

file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
name = '历史开奖数据.csv'
data = pd.read_csv(file+name)
data.index = pd.to_datetime(data['time'])
#
下分 = 5
#读取日期跨度
day_data = data['2017/05/29'].sort_values(by='qi',ascending=False)
end,start = day_data.iloc[0,1],day_data.iloc[-1,1]
#
'''

'''
print('车道:%d,预测跨度:%d,车道1,win:%d'%(车道,预测跨度,wins))