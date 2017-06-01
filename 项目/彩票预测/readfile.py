import pandas as pd
import matplotlib.pyplot as plt
def read(filepath):
    f = open(filepath,'r')
    lines = f.readlines()
    #数据整理
    hist_data = []
    for line in lines:
        temp = line[0:-1].split('----')
        hist_data.append(temp)
    data = pd.DataFrame(hist_data, columns=['期数', '号码', '开奖日期'])
    return data

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-彩票预测\\'
name = '正序.txt'
data = read(file+name)


data.iloc[:,1].hist()
plt.show()
print(data)

