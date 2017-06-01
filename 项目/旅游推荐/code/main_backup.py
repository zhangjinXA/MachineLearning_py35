# -*- coding: utf-8 -*-

"""
Module implementing process.
"""
import pandas as pd
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from 项目.旅游推荐.code.Ui_main import Ui_Dialog
from 项目.旅游推荐 import flight,bulit_text,下拉框选项处理
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
filename_linshi = filepath + 'fromSHE-2017-4-5.xls'; flight.filepath = filepath

path情感数据 = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\处理后数据\\情感分析结果汇总.xlsx'
data旅店 = pd.read_excel(path情感数据, 0)
data景点 = pd.read_excel(path情感数据, 1)
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
        time = self.textBrowser_2.toPlainText();self.label_info.setText('正在读取航班信息...')
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
        self.label_info.setText(str(s出发地点index))
        '''读取控件选择情况'''
        selectIndex_出发地点 = self.select_location.currentIndex()
        selectIndex_出发时间 = self.select_time.currentIndex()
        selectIndex_价格区间 = self.select_price.currentIndex()
        selectIndex_酒店指数 = self.select_Hotel.currentIndex()
        selectIndex_景点指数 = self.select_Views.currentIndex()
        '''匹配信息'''
        出发时间 = [['0:00','6:00'],['6:01','12:00'],['12:01','18:00'],['18:01','23:59']]
        select出发地点 = self.出发地点[selectIndex_出发地点]
        range_出发时间 = 出发时间[selectIndex_出发时间]
        range_价格区间 = (self.价格区间[1])[selectIndex_价格区间]
        range_酒店指数 = (Rank区间_旅店[1])[selectIndex_酒店指数]
        range_景点指数 = (Rank区间_景点[1])[selectIndex_景点指数]
        print(select出发地点,range_出发时间,range_价格区间,range_酒店指数,range_景点指数)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = process()
    dlg.show()
    sys.exit(app.exec_())
