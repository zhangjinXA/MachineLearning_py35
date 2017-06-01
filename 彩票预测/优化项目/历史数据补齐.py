import requests
from bs4 import BeautifulSoup
import pandas as pd
import math
import time


class 数据爬取:

    def __init__(self):
        print('获取第一页数据...')
        url = 'http://www.bwlc.net/bulletin/prevtrax.html?page=1'
        scode = 201
        while scode != 200:
            try:
                self.session = requests.get(url, timeout=1)
                scode = self.session.status_code
            except:
                print('失败')
            if scode != 200:
                print('爬取失败，2秒后重试')
                time.sleep(2)
        #
        #获取相关信息
        page = self.session.content.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        # 获得第一页记录
        num = soup.find_all('table', class_='tb')
        num_s1 = num[0].find_all('td')
        #
        self.每页记录数 = len(num_s1) / 3
        self.最新期号 = int(num_s1[0].get_text())
        self.最新号码 = num_s1[1].get_text()
        self.最新时间 = num_s1[2].get_text()
    '''################################################################'''
    def 按条爬取(self,numRecordes):
        #
        page_index = 1 ; data = []
        page_num = math.ceil(numRecordes * 1.0 / self.每页记录数)
        #
        while page_index <= page_num:
            #
            print('*******总%d条，共%d页，当前第%d页。'%(numRecordes,page_num,page_index))
            #
            url = 'http://www.bwlc.net/bulletin/prevtrax.html?page=%d'%page_index
            scode = 201
            while scode != 200:
                try:
                    self.session = requests.get(url,timeout=1)
                    scode = self.session.status_code
                except:
                    print('失败')
                if scode != 200:
                    print('爬取失败，2秒后重试')
                    time.sleep(2)
            #
            page = self.session.content.decode('utf-8')
            soup = BeautifulSoup(page, 'html.parser')
            # 获得每页记录
            num = soup.find_all('table', class_='tb')
            num_s1 = num[0].find_all('td')


            for i in range(0,len(num_s1),3):
                i1,i2,i3 = num_s1[i],num_s1[i+1],num_s1[i+2]
                #号码去除逗号
                i2_split = i2.get_text().split(',')
                #
                temp = [i1.get_text(),i3.get_text()] + i2_split
                data.append(temp)
            #循环参数更新
            page_index += 1
            time.sleep(1.5)
        #
        datapd = pd.DataFrame(data,columns=['qi','time','i1','i2','i3','i4','i5','i6','i7','i8','i9','i0'])
        return datapd

    def 数据补齐(self,历史数据路径):

        #
        history_data = pd.read_csv(历史数据路径).sort_values(by='qi',ascending=False)
        self.历史期号 = history_data.iloc[0,1]
        #
        numRecordes = self.最新期号 - self.历史期号
        if numRecordes > 0 :
            getData = self.按条爬取(numRecordes)
            new_data = getData[getData['qi'].astype(int) > self.历史期号].sort_values(by='qi', ascending=True)
            #
            #更新文件
            ofile = open(历史数据路径, 'a')
            for i in range(len(new_data.index)):
                recordi = new_data.iloc[i, :].tolist()
                print(str(i) + ',', ','.join(recordi), file=ofile)
            ofile.close()
        else:
            new_data = -99
            print('数据无需补齐')

        return new_data

    def close(self):
        self.session.close()


# ##test
# file = '/Users/zhangxuewei/Desktop/MachineLearning_py35/'
# name = '历史开奖数据.csv'
# k = 数据爬取()
# #文件不存在时，爬取前3000条
# data = k.按条爬取(300)
# data.to_csv(file+name)
# #文件存在时，补齐最新缺失部分
# data = k.数据补齐(file+name)
# print(data)
# k.close()