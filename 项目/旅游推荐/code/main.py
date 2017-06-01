# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from 项目.旅游推荐.code.Ui_main import Ui_Dialog
from 项目.旅游推荐 import flight,bulit_text,下拉框选项处理,筛选后数据整合
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
filename_linshi = filepath + 'fromSHE-2017-4-5.xls'; flight.filepath = filepath

path情感数据 = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\处理后数据\\情感分析结果汇总.xlsx'
data旅店 = pd.read_excel(path情感数据, 1)
data景点 = pd.read_excel(path情感数据, 0)
Rank区间_旅店 = 下拉框选项处理.生成数组区间(data旅店['RANK'],10)
Rank区间_景点 = 下拉框选项处理.生成数组区间(data景点['RANK'],10)


class process(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(process, self).__init__(parent)
        self.setupUi(self)

    '''查询航班'''
    @pyqtSlot()
    def on_pushButton_clicked(self):
        #获取输入时间,爬虫航班数据
        time = self.textBrowser_2.toPlainText();
        self.label_info.setText('正在爬取航班信息...')
        if time == '2017-4-5':
            data = pd.read_excel(filename_linshi,0)
            self.label_info.setText('读取缺省信息完成')
        else:
            #爬虫航班信息
            flight.time = time
            flight.info_label = self.label_info
            a = flight.fight()
            a.run()
            #读取爬虫后的航班信息
            data = pd.read_excel(filepath + 'fromSHE-%s.xls'%time,0)
            self.label_info.setText('读取完成')
        #航班数据处理
        data['起飞时间'] = pd.to_datetime(data['起飞时间'], format = '%H:%M')
        data['到达时间'] = pd.to_datetime(data['到达时间'], format = '%H:%M')
        self.data航班 = data
        self.出发地点 = data['始发站'].drop_duplicates().values.tolist()
        #计算价格区间
        self.价格 = data['价格'].values
        self.价格区间 = 下拉框选项处理.生成数组区间(self.价格,10)

        #设置展示
        text = bulit_text.bulitText(data)
        self.textBrowser.setText(text)
        #传入控件值：出发地点，价格区间，酒店指数，景点指数
        self.select_location.clear()
        self.select_location.addItems(['选择出发地点']+self.出发地点)
        self.select_price.clear()
        self.select_price.addItems(['选择价格区间']+self.价格区间[0])
        #设置控件激活
        self.select_Hotel.setEnabled(True);self.select_location.setEnabled(True)
        self.select_price.setEnabled(True);self.select_time.setEnabled(True)
        self.select_Views.setEnabled(True);self.pushButton_2.setEnabled(True)

        #

    def on_pushButton_2_clicked(self):
        s出发地点index = self.select_location.currentIndex()
        self.label_info.setText('finish')
        '''读取控件选择情况'''
        selectIndex_出发地点 = self.select_location.currentIndex() -1
        selectIndex_出发时间 = self.select_time.currentIndex() -1
        selectIndex_价格区间 = self.select_price.currentIndex() -1
        selectIndex_酒店指数 = self.select_Hotel.currentIndex() -1
        selectIndex_景点指数 = self.select_Views.currentIndex() -1
        '''匹配信息'''
        出发时间 = [['0:00','6:00'],['6:01','12:00'],['12:01','18:00'],['18:01','23:59']]
        select出发地点 = self.出发地点[selectIndex_出发地点]
        range_出发时间 = 出发时间[selectIndex_出发时间]
        range_价格区间 = (self.价格区间[1])[selectIndex_价格区间]
        range_酒店指数 = (Rank区间_旅店[1])[selectIndex_酒店指数]
        range_景点指数 = (Rank区间_景点[1])[selectIndex_景点指数]
        # print(select出发地点,range_出发时间,range_价格区间,range_酒店指数,range_景点指数)
        '''筛选航班数据'''
        #航班数据过滤
        data0 = self.data航班
        #出发地点
        if selectIndex_出发地点 != -1:
            index0 = np.where(data0.iloc[:,0] == select出发地点)
            data01 = data0.iloc[index0[0],:]
        else:
            index0 = data0.index
            data01 = data0
        #出发时间
        if selectIndex_出发时间 != -1:
            timeStart = pd.to_datetime(range_出发时间[0],format='%H:%M')
            timeEnd = pd.to_datetime(range_出发时间[1], format='%H:%M')
            index11 = data01.iloc[:,2] >= timeStart
            index12 = data01.iloc[:,2] <= timeEnd
            index1 = np.where(index12 * index11 == True)   #检查是否为空
            data02 = data01.iloc[index1[0],:]
        else:
            index1 = data01.index
            data02 = data01
        #机票价格
        if selectIndex_价格区间 != -1:
            priceStart = range_价格区间[0]
            priceEnd = range_价格区间[1]
            juge = ( data02.iloc[:,4] >= priceStart ) & ( data02.iloc[:,4] <= priceEnd )
            index2 = np.where(juge == True)[0]
            data03 = data02.iloc[index2,:]
        else:
            data03 = data02
        '''
       筛选酒店/景点数据
       最终数据data03 ，data_过滤后酒店，data_过滤后景点
       '''
        if selectIndex_酒店指数 != -1:
            酒店指数start = range_酒店指数[0]
            酒店指数end = range_酒店指数[1]
            juge = ( data旅店.iloc[:,3] >= 酒店指数start ) & ( data旅店.iloc[:,3] <= 酒店指数end )
            index = np.where(juge == True)[0]
            data_过滤后酒店 = data旅店.iloc[index,:]
        else:
            data_过滤后酒店 = data旅店
        ##
        if selectIndex_景点指数 != -1:
            景点指数start = range_景点指数[0]
            景点指数end = range_景点指数[1]
            juge = ( data景点.iloc[:,3] >= 景点指数start ) & ( data景点.iloc[:,3] <= 景点指数end )
            index = np.where(juge == True)[0]
            data_过滤后景点 = data景点.iloc[index,:]
        else:
            data_过滤后景点 = data景点

        '''
       筛选后数据整合，展示
       '''
        showText = 筛选后数据整合.conbine2(data03,data_过滤后酒店,data_过滤后景点)
        self.textBrowser.setText(showText)



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = process()
    dlg.show()
    sys.exit(app.exec_())
