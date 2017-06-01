#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

#
def get_day_info(date):
    page_index = 1
    page_num = 2
    data = []
    while page_index <= page_num:
        url = 'http://www.bwlc.net/bulletin/prevtrax.html?dates=%s&page=%d' % (date, page_index)
        page = requests.get(url,timeout=3).content.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        #获得总页数
        num_pages=soup.find_all('div',class_='fc_fanye')[0]
        num2 = num_pages.find_all('span')
        总页数 = int(num2[1].get_text()[1:-1])  #总页数
        当前页数 = int(num2[2].get_text()[1:-1])  #当前页数
        print('*******爬取日期：%s，当前：%s,%s'%(date,num2[1].get_text(),num2[2].get_text()))

        #获得每页记录数
        num=soup.find_all('table',class_='tb')
        num_s1 = num[0].find_all('td')
        for i in range(0,len(num_s1),3):
            i1,i2,i3 = num_s1[i],num_s1[i+1],num_s1[i+2]
            #号码去除逗号
            i2_split = i2.get_text().split(',')
            #
            temp = [i1.get_text(),i3.get_text()] + i2_split
            data.append(temp)
        #循环参数更新
        page_num = 总页数
        page_index += 1
    #
    datapd = pd.DataFrame(data,columns=['qi','time','i1','i2','i3','i4','i5','i6','i7','i8','i9','i0'])
    return datapd


file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
date = '2017-05-28'
name = date+'.csv'

data = get_day_info(date)
data.to_csv(file+name)



