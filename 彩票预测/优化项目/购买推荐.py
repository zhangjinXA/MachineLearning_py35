import numpy as np
import pandas as pd
from 彩票预测.优化项目.历史数据补齐 import 数据爬取
from 彩票预测.优化项目.预测算法 import *

#
class 购买推荐:

    def __init__(self):
        self.file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
        self.name = '历史开奖数据.csv'
        self.跨度 = 20
        self.下分 = 5
        self.车道 = range(10)
        self.算法 = 1
        self.方差阈值 = 3.5
        self.连续个数 = 3

    def output_param(self):

        string = '跨度:%d , 下分:%d\n算法:%d , 方差阈值:%s\n车道:%s\n连续个数:%d'%(\
                    self.跨度,self.下分,self.算法,str(self.方差阈值),str(self.车道),self.连续个数)
        return string

    def update_data(self):
        #update
        getData = 数据爬取()
        getData.数据补齐(self.file+self.name)  #检查补齐历史数据
        getData.close()
        # 获取最新数据
        self.最新期数,最新号码,self.最新时间 = getData.最新期号,getData.最新号码,getData.最新时间
        self.最新号码 = np.asarray(最新号码.split(','),dtype=np.int).tolist()
        return [self.最新期数,self.最新号码,self.最新时间]

    def __pick_traindata(self,start,end):

        最新历史数据 = pd.read_csv(self.file + self.name).sort_values(by='qi',ascending=False)
        train_Data = 最新历史数据.iloc[start:end,:]
        train_Data.index = train_Data['qi']
        return train_Data
        #
    def 输出推荐结果(self,start,end):
        #
        train_data = self.__pick_traindata(start,end)
        #
        if self.算法 == 1:
            posi_num = predict_1(train_data, self.跨度)
            过滤后输出 = 格式化输出(posi_num, self.下分, self.车道)


        if self.算法 == 3:
            posi_num = predict_3(train_data, self.跨度)
            过滤后输出 = 格式化输出(posi_num, self.下分, self.车道)


        if self.算法 == 2:
            过滤后输出 = ''
            for 车道 in self.车道:
                posi_num = predict_2(train_data,self.跨度,车道,self.方差阈值)
                过滤后输出temp = 格式化输出(posi_num, self.下分, self.车道)
                过滤后输出 = 过滤后输出 + 过滤后输出temp

        if self.算法 == 4:
            posi_num = predict_4(train_data,self.连续个数)
            过滤后输出 = 格式化输出(posi_num, self.下分, self.车道)
        return 过滤后输出






