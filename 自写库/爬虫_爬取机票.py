#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlwt
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
time = '2017-4-5'

class fight:

    hang=1
    def getinfo(self,fromcity,tocity,time):
        print('searching %s %s to %s'%(time,fromcity[1],tocity[1]))
        url='http://m.ctrip.com/html5/flight/%s-%s-day-1.html?DDate1=%s&mkt_header=bdnm'%(fromcity[1],tocity[1],time)
        page=requests.get(url).content.decode('utf-8')
        soup=BeautifulSoup(page,'html.parser')
        flights=soup.find_all('li',{'class':'f-arrow-bottom flight-open-sm mf-main-cabin '})
        for flight in flights:
            starttime=flight.find_all('span',{'class':'f-lst-time'})[0].text
            startplace=flight.find_all('span',{'class':'f-airPort'})[0].text
            endtime=flight.find_all('span',{'class':'f-lst-time'})[1].text
            endplace=flight.find_all('span',{'class':'f-airPort'})[1].text
            price=flight.find('span',{'class':'f-lst-price-num'}).text
            name=flight.find('span',{'class':'f-lst-no f-lst-no-1'}).text
            self.sheet.write(self.hang,0,startplace+'('+str(fromcity[0])+')')
            self.sheet.write(self.hang,1,endplace+'('+str(tocity[0])+')')
            self.sheet.write(self.hang,2,starttime)
            self.sheet.write(self.hang,3,endtime)
            self.sheet.write(self.hang,4,price)
            self.sheet.write(self.hang,5,name)
            self.hang+=1
    '''
    '''
    def run(self):
        citys = []
        with open(filepath+'city.txt', 'r',encoding='utf-8')as f:
            lines = f.readlines()
            for line in lines:
                citys.append(line[:-2].split(' '))


        wbk = xlwt.Workbook(encoding='utf-8')
        self.sheet = wbk.add_sheet('sheet1')
        self.sheet.write(0, 0, '始发站')
        self.sheet.write(0, 1, '终到站')
        self.sheet.write(0, 2, '起飞时间')
        self.sheet.write(0, 3, '到达时间')
        self.sheet.write(0, 4, '价格')
        self.sheet.write(0,5, '航班代码')
        for city in citys:

            self.getinfo([u'沈阳','SHE'],city,time)
        wbk.save(filepath+'toSHE-%s.xls'%time)
        self.hang=1
        wbk = xlwt.Workbook(encoding='utf-8')
        self.sheet = wbk.add_sheet('sheet1')
        self.sheet.write(0, 0, '始发站')
        self.sheet.write(0, 1, '终到站')
        self.sheet.write(0, 2, '起飞时间')
        self.sheet.write(0, 3, '到达时间')
        self.sheet.write(0, 4, '价格')
        self.sheet.write(0,5, '航班代码')
        for city in citys:

            self.getinfo(city,[u'沈阳','SHE'],time)
        wbk.save(filepath+'fromSHE-%s.xls'%time)


# a=fight()
# a.run()
