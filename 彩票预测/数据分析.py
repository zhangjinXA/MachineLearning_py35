import pandas as pd
import numpy as np
from 彩票预测.爬取单日 import get_day_info as get_info

class 投资basedOnInterval:

    def 分析数字interval(self,data,分析位置,分析号码,分析时间):
        #
        data.index = pd.to_datetime(data['time'])
        #筛选指定时间
        adata = data[分析时间]
        adata = adata.sort_index(ascending=True)
        #筛选指定位置指定号码
        xdata = adata[adata['i'+str(分析位置)] == 分析号码]
        #差分
        self.间隔 = xdata['qi'].diff().dropna().tolist()
        return self.间隔
    def 计算收益(self,赔率,投资间隔,分析时间,data):
        self.temp0 = []
        for 位置 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            for 号码 in range(1, 11):
                diff = np.sort(self.分析数字interval(data,位置,号码,分析时间))
                self.temp0 += diff[np.where(diff > 投资间隔)[0]].tolist()
        temp = np.sort(self.temp0)
        total_win = 赔率 * len(temp) - len(temp)
        total_loss = np.sum(temp - 投资间隔-1)
        最终获利 = total_win - total_loss
        #
        最大损失本金 = self.__计算最大损失本金(赔率,投资间隔)
        #
        return [最终获利,最大损失本金]

    def __计算最大损失本金(self,赔率,投资间隔):
        temp = self.temp0
        temp_loss = 0
        max_loss = 0
        for i in temp:
            loss = (i - 投资间隔)-赔率
            temp_loss += loss
            if temp_loss > max_loss:
                max_loss = temp_loss

        return max_loss




file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
date = '2017-05-26'
name = date+'.csv'
# data = get_info(date)
# data.to_csv(file+date+'.csv')
#
data = pd.read_csv(file+name)
#
tt = 投资basedOnInterval()
win,maxLoss = tt.计算收益(9.85,1,date,data)
print('投资收益->1:%f，投资期间最大亏损->1:%f'%(win,maxLoss))
#收益计算
