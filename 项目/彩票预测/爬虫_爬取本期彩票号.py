#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def get_info():
    url = 'http://www.bwlc.net/bulletin/prevtrax.html?page=1'
    scode = 201
    while scode != 200:
        try:
            session = requests.get(url,timeout=3)
            scode = session.status_code
        except:
            print('失败_爬取本期彩票号...')
    if scode != 200 :
        print('爬取失败，5秒后重试')
        time.sleep(2)
    page = session.content.decode('utf-8')
    soup = BeautifulSoup(page, 'html.parser')
    # 获得每页记录数
    num = soup.find_all('table', class_='tb')
    num_s1 = num[0].find_all('td')
    #
    期数 = num_s1[0].get_text()
    本期号码 = num_s1[1].get_text()
    本期时间 = num_s1[2].get_text()

    session.close()

    return [期数,本期号码,本期时间]

# a = get_info()
