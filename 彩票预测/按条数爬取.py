import requests
from bs4 import BeautifulSoup
import pandas as pd
import math
import time

#
def get_numRecordes_info(numRecordes):
    page_index = 1
    page_num = 2
    data = []
    while page_index <= page_num:
        url = 'http://www.bwlc.net/bulletin/prevtrax.html?page=%d'%page_index
        scode = 201
        while scode != 200:
            try:
                session = requests.get(url,timeout=3)
                scode = session.status_code
            except:
                print('失败')
            if scode != 200:
                print('爬取失败，2秒后重试')
                time.sleep(2)

        page = session.content.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        #获得总页数
        num_pages = soup.find_all('div',class_='fc_fanye')[0]
        当前爬取页信息 = num_pages.find_all('span')

        #获得每页记录数
        num=soup.find_all('table',class_='tb')
        num_s1 = num[0].find_all('td')
        每页记录数 = len(num_s1)/3

        print('*******当前：%s,%s，需要获取%d条，共计%d页，每页%d条'%(当前爬取页信息[2].get_text(),当前爬取页信息[1].get_text(),numRecordes,page_num,每页记录数))

        for i in range(0,len(num_s1),3):
            i1,i2,i3 = num_s1[i],num_s1[i+1],num_s1[i+2]
            #号码去除逗号
            i2_split = i2.get_text().split(',')
            #
            temp = [i1.get_text(),i3.get_text()] + i2_split
            data.append(temp)
        #循环参数更新
        page_num = math.ceil(numRecordes*1.0/每页记录数)
        page_index += 1
        time.sleep(1.5)
    #
    datapd = pd.DataFrame(data,columns=['qi','time','i1','i2','i3','i4','i5','i6','i7','i8','i9','i0'])
    return datapd

# data = get_day_info(61)
# print(data)