import numpy as np
import pandas as pd

def predict_1(need_Data,跨度):
    need_Data = need_Data.sort_values(by='qi', ascending=False)

    '''预测数据****************************************'''
    #
    numSet = set(range(1, 11))
    poistion = range(3, 13)
    位置及数字 = []

    for posi in poistion:
        tempdatai = need_Data.iloc[:跨度, posi].tolist()
        未出现数字 = list(numSet - set(tempdatai))
        当前位置 = posi - 2
        if len(未出现数字) > 0:
            #将10转化为0
            if 当前位置 == 10 :
                当前位置 = 0
            for ii in range(len(未出现数字)):
                if 未出现数字[ii] == 10 : 未出现数字[ii] = 0
            #
            位置及数字.append([当前位置] + 未出现数字)
    return 位置及数字

def predict_2(train_data,跨度,车道,方差阈值):

    ''' 
    车道从1开始,0、10代表10
    '''
    if 车道 == 0 :
        车道对应数据表位置 = 12
    else:
        车道对应数据表位置 = 车道 + 2
    if 车道 == 10: 车道 = 0

    #########################################


    train_data = train_data.sort_values(by='qi', ascending=False)

    freq_dataI = train_data.iloc[:跨度, :]

    '''预测数据****************************************'''
    #
    num_Freq = freq_dataI.groupby(by='i%d'%(车道)).count().sort_values(by='qi',ascending=False)
    sortCount = num_Freq.iloc[:,0]
    # print(sortCount)
    # print(num_Freq.describe())


    std = num_Freq.describe().iloc[2,0]
    if std > 方差阈值:
        阈值 = num_Freq.describe().iloc[5,0]   # 50%
    else:
        阈值 = num_Freq.describe().iloc[4, 0]  #25%
    预测数字 = sortCount.where(sortCount < 阈值).dropna().index.tolist()

    if std > 方差阈值 : 预测数字 = []
    # 最佳数字 = sortCount.index[-1]

    # print(sortCount)
    print(std)
    # print('最佳数字%d'%最佳数字)

    # print(位置及数字)


    # 将10转化为0
    for ii in range(len(预测数字)):
            if 预测数字[ii] == 10 : 预测数字[ii] = 0
        #
    位置及数字 = [车道]+预测数字
    return [位置及数字]

'''查找三个以上跨度内不出现的数字及车道'''
def predict_3(need_Data,跨度):
    predNum = predict_1(need_Data,跨度)
    #
    output = []
    for i in predNum:
        if len(i) >= 4:
            output.append(i)
    return output

def predict_4(train_data,连续个数):
    train_data = train_data.sort_values(by='qi', ascending=False)

    output_posi_num = []
    for 车道 in range(3,13):
        data = train_data.iloc[:连续个数+1,车道].tolist()
        #
        panduan = 1
        for i in range(连续个数-1):
            if data[i] == data[i+1]:
                panduan = panduan*1
            else:
                panduan = 0
        #
        if panduan == 1 :
            exclude_num = set( [data[0],data[-1]]  )
            pred_num = list(set(range(1,11,1)) - exclude_num)
            pred_num = [车道-2] + pred_num
            #
            for i in range(len(pred_num)):
                if pred_num[i] == 10 :pred_num[i] = 0

            output_posi_num.append(pred_num)
    return output_posi_num



def 格式化输出(位置及数字,下分,车道s):
    所有预测输出 = []   #所有车道的输出list
    for i in 位置及数字:
        i = np.asarray(i,dtype=np.str).tolist()
        tempi = ''
        for i2 in i[1:]:
            tempi += i[0]+'/'+str(i2)+'/'+str(下分)+'\n'
        所有预测输出.append(tempi)
    #按车道过滤
    过滤后输出 = ''
    for 过滤车道 in 车道s:
        for 预测车道 in range(len(位置及数字)):
            if 过滤车道 == 位置及数字[预测车道][0]:
                过滤后输出 += 所有预测输出[预测车道]
    return 过滤后输出



# file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
# name = '历史开奖数据.csv'
# 预测位置 = 201
# 跨度 = 14
#
# train_data = pd.read_csv(file+name).sort_values(by='qi',ascending=False).iloc[预测位置:]
# #
# 预测位置及号码 = predict_4(train_data,2)
# i = 格式化输出(预测位置及号码,5,range(10))
# #
# print(i)
# print(预测位置及号码)




