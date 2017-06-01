import pandas as pd;
import matplotlib.pyplot as plt
import numpy as np
from 库存销量预测 import 大促时间读取 as readProm
from 自写算法 import 时间序列处理工具包 as timeKit

a = pd.DataFrame();
fig = plt.figure();

p1 = fig.add_subplot(211);
p2 = fig.add_subplot(212);
# p3 = fig.add_subplot(313);
'''
数据清洗
1、去除大促时间段数据
2、按天汇总
3、添加周几信息column：WeekOfDay(周几),WeekInYear(第几周)
4、只保留：时间，销量，周
数据：data = 数据清洗().按天重采样_加周()
'''
class 数据清洗:
    def 按天重采样_加周(self):
        #读取数据
        tKit = timeKit.process_dateTime()
        tKit.filepath='F:\\资料整理\\myPthon35_Code\\data\\sal库eam存t\\'
        data抽纸商品组销售数据 = tKit.import_data(name='R9001849_2015_201704(抽纸)',encoding='utf-8',dataFormat='%Y%m%d')
        #读取大促时间
        Obj_读取大促时间 = readProm.read_promotionDate()
        PromDate = Obj_读取大促时间.Promotion_Date;
        Prom_Date2015 = PromDate['date2015'];
        大促时间序列表2015年 = Obj_读取大促时间.大促时间序列生成(PromDate['date2015']);
        大促时间序列表2016年 = Obj_读取大促时间.大促时间序列生成(PromDate['date2016']);
        #丢弃大促时间
        data抽纸销量_去大促 = data抽纸商品组销售数据.drop(大促时间序列表2015年+大促时间序列表2016年)
        #重采样
        data抽纸销量_去大促_按天重采样 = data抽纸销量_去大促.resample('1D').sum();
        #周信息添加
        weekOfDay = []
        weekInYear = []
        for i in data抽纸销量_去大促_按天重采样.index:
            weekday = i.weekday()
            weekOfDay.append(int(weekday))
            weekYear = i.strftime('%W')
            weekInYear.append(int(weekYear))
        weekOfDay_pd = pd.DataFrame(weekOfDay,index=data抽纸销量_去大促_按天重采样.index,columns=['WeekOfDay'])
        weekInYear_pd = pd.DataFrame(weekInYear,index=data抽纸销量_去大促_按天重采样.index,columns=['WeekInYear'])
        data抽纸销量_去大促_按天重采样_加周 = pd.merge(data抽纸销量_去大促_按天重采样,weekOfDay_pd,right_index=True,left_index=True)
        self.data抽纸销量_去大促_按天重采样_加周_加第几周 = pd.merge(data抽纸销量_去大促_按天重采样_加周,weekInYear_pd,right_index=True,left_index=True)
        self.data抽纸销量_去大促_按天重采样_加周_清洗 =  self.data抽纸销量_去大促_按天重采样_加周_加第几周.drop(['statis_date','gds_cd'],axis=1)#'statis_date','gds_cd'
        return self.data抽纸销量_去大促_按天重采样_加周_清洗
'''
无数据日期所在周数据剔除
'''
class 不完整周剔除:
    def 剔除(self,data):
        data['_c3'] = data['_c3'].fillna(value=-9999999)
        maxWeek = np.max(data.iloc[:,-1])
        Year = data.index.strftime('%Y').tolist()
        maxYear,minYear = max(Year),min(Year)
        Xrange = range(int(minYear),int(maxYear)+1,1)
        #
        # print(data)
        data_drop = []
        for year in Xrange:
            data_year = data[str(year)]
            if data_year.iloc[-1,1] != 6:
                index_年末 = np.where(data_year.iloc[:,2] == data_year.iloc[-1,2])
                data_year= data_year.drop(data_year.index[index_年末[0]],axis=0)
            if data_year.iloc[0,1] != 0:
                index_年初 = np.where(data_year.iloc[:,2] == data_year.iloc[0,2])
                data_year = data_year.drop(data_year.index[index_年初[0]],axis=0)
            #对一年数据进行剔除不完整周
            NaIndex = np.where(data_year.iloc[:,0] == -9999999)
            NaWeek = data_year.iloc[NaIndex[0],2].drop_duplicates()
            NaWeekIndex = np.where(data_year.iloc[:,2].isin(NaWeek.values))
            data_drop.append(data_year.drop(data_year.index[NaWeekIndex[0]],axis=0))
        self.剔除周数据 = pd.concat(data_drop)
        return self.剔除周数据

'''
异常数据获取
'''
class 异常销量获取:
    def 剔除(self,data,percent):
        #异常值
        saleAmt_sort = data.sort_values(by='_c3',ascending=False)
        num = saleAmt_sort['_c3'].count()
        #阈值位置
        index_Max = round(num * percent).astype(int)
        #销量大于阈值的index
        threshold_Max = saleAmt_sort.iloc[index_Max, 0]
        th_Index_Max = np.where(data.iloc[:,0] >= threshold_Max)
        th_Index_Max_s = th_Index_Max[0] - 1
        #丢弃
        data.iloc[th_Index_Max_s.tolist(),0] = None
        return data
'''
数据分析
'''
data = 数据清洗().按天重采样_加周()
data_异常剔除 = 异常销量获取().剔除(data.copy(deep=True),0.1)
data_f = 不完整周剔除().剔除(data_异常剔除).dropna()
dataW = data_f.resample('W').sum().dropna()
dataW['WeekInYear'] = np.round(dataW['WeekInYear'].values/7)
data_f.to_csv('C:\\Users\\16070332\\Desktop\\中间数据\\抽纸_剔除大促与异常值.csv')
data_Diff = data_f.diff(1)
#提取
data2015f,data2016f = data_f['2015'],data_f['2016']
data2015W,data2016W = dataW['2015'],dataW['2016']
diff2015,diff2016 = data_Diff['2015'],data_Diff['2016']

p2.plot(pd.to_datetime(data2015f.index.strftime('%m-%d'),format='%m-%d'),data2015f.iloc[:,0],marker='o')
p2.plot(pd.to_datetime(data2016f.index.strftime('%m-%d'),format='%m-%d'),data2016f.iloc[:,0],marker='o')
#
p1.plot(pd.to_datetime(data2015W.index.strftime('%m-%d'),format='%m-%d'),data2015W.iloc[:,0],marker='o')
p1.plot(pd.to_datetime(data2016W.index.strftime('%m-%d'),format='%m-%d'),data2016W.iloc[:,0],marker='o')
#
# p1.plot(pd.to_datetime(diff2015.index.strftime('%m-%d'),format='%m-%d'),diff2015.iloc[:,0],color='red')
# p1.plot(pd.to_datetime(diff2016.index.strftime('%m-%d'),format='%m-%d'),diff2016.iloc[:,0],color='blue')
#
plt.show()
# print(data2015W.dropna().mean())
# print(data2016W.dropna().mean())

class 按周绘图:
    def 绘图(self,data,Year,p,ranges):
        X = data[Year].iloc[:,-2]
        Y = data[Year].iloc[:,0]
        周一日期 = X.index[X==0]
        周日日期 = X.index[X==6]
        Y.fillna(value=0)
        # for i in range(len(周一日期)):
        for i in ranges:
            Yi = Y[周一日期[i]:周日日期[i]]
            Xi = X[周一日期[i]:周日日期[i]]
            p.plot(Xi,Yi,label=周一日期[i].strftime('%m.%d'),marker='.')

# p = [p1,p2]
# nnn1 = 按周绘图().绘图(data=data_f,Year='2015',p=p[0],ranges=[5,6,7,8,9])
# nnn2 = 按周绘图().绘图(data=data_f,Year='2016',p=p[1],ranges=[5,6,7,8,9])
# plt.show()
