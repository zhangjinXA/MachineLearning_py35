import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def 生成数组区间(data,num):
    PriceMin, PriceMax = np.min(data), np.max(data)
    diff = PriceMax - PriceMin
    gradient = diff/num
    价格区间 = []
    for i in range(num):
        价格区间.append([PriceMin + gradient*i , PriceMin + gradient*(i+1)])
    价格区间[-1][-1] = PriceMax
    价格区间np = np.asarray(价格区间)
    #
    价格区间strList = []
    for i1,i2 in 价格区间np:
        价格区间strList.append(str(i1)+' - '+str(i2))
    return [价格区间strList,价格区间np]

# filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\旅游推荐算法\\New Folder With Items\\'
# filename_linshi = filepath + 'fromSHE-2017-4-5.xls'
# data = pd.read_excel(filename_linshi,0)
# 价格 = data['价格'].values
# a = 计算价格区间(价格)
