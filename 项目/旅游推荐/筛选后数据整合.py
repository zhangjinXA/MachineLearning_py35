import pandas as pd
from 项目.旅游推荐.bulit_text import builtLine
import datetime

def conbine(dataFly,dataHotel,dataView):
    text = ''
    for i1 in range(len(dataFly.index)):
        temp = dataFly.iloc[i1,:].values
        出发时间 = datetime.datetime.strftime(temp[2],format='%H:%M')
        落地时间 = datetime.datetime.strftime(temp[3],format='%H:%M')
        temptext = '始终：'+str(temp[0])+'-'+str(temp[1])+' -- 起落时间：'+出发时间+'-'+落地时间+' -- 价格：'+str(temp[4])+'元'
        # text = text + '<h2>' + builtLine(dataFly.iloc[i1,:]) + '</h2>'
        text = text + '<h2>' + temptext + '</h2>'
        for i2 in range(len(dataHotel.index)):
            temp = dataHotel.iloc[i2, :].values
            temptext = '<h3>'+str(temp[0])+'-------------推荐指数：'+str(temp[3]) + '</h3>'
            text = text + temptext
            # text =text+ '<h3>'+builtLine(dataHotel.iloc[i2,:]) + '</h3>'
            for i3 in range(len(dataView.index)):
                temp = dataView.iloc[i3,:].values
                temptext = '<p>' + str(temp[0]) + '   ,   推荐指数：' + str(temp[3]) + '</p>'
                text = text + temptext
                # text = text + '<p>' +builtLine(dataView.iloc[i3,:]) + '</p>'
    return text

def conbine2(dataFly, dataHotel, dataView):
    text = ''
    text += '<h2>******************航班列表******************</h2>'
    for i1 in range(len(dataFly.index)):
        temp = dataFly.iloc[i1, :].values
        出发时间 = datetime.datetime.strftime(temp[2], format='%H:%M')
        落地时间 = datetime.datetime.strftime(temp[3], format='%H:%M')
        temptext = '始终：' + str(temp[0]) + '-' + str(temp[1]) + ' -- 起落时间：' + 出发时间 + '-' + 落地时间 + ' -- 价格：' + str(
            temp[4]) + '元'
        text = text + '<h4>' + temptext + '</h4>'
    text += '<h2>******************酒店推荐******************</h2>'
    for i2 in range(len(dataHotel.index)):
        temp = dataHotel.iloc[i2, :].values
        temptext = '<h4>推荐指数：' + str(temp[3]) + ' ----'+ str(temp[0]) +'</h4>'
        text = text + temptext
    text += '<h2>******************景点推荐******************</h2>'
    for i3 in range(len(dataView.index)):
        temp = dataView.iloc[i3, :].values
        temptext = '<h4>推荐指数：' + str(temp[3]) + ' ----'+str(temp[0]) + '</h4>'
        text = text + temptext
    return text



path情感数据 = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\处理后数据\\情感分析结果汇总.xlsx'
filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
filename_linshi = filepath + 'fromSHE-2017-4-5.xls'

dataF = pd.read_excel(filename_linshi,0)
data旅店 = pd.read_excel(path情感数据, 1)
data景点 = pd.read_excel(path情感数据, 0)

dataF['起飞时间'] = pd.to_datetime(dataF['起飞时间'],format='%H:%M')
dataF['到达时间'] = pd.to_datetime(dataF['到达时间'],format='%H:%M')
tex = conbine2(dataF.iloc[:5,:],data旅店.iloc[:5,:],data景点.iloc[:5,:])
print(tex)