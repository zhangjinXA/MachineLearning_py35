import pandas as pd
import numpy as np



def cal_猜数字(trueNum,赔率,押注,下分):
    #押注格式转换
    for i1 in range(len(押注)):
        for i2 in range(len(押注[i1][:-1])):
            if 押注[i1][i2] == 0:
                押注[i1][i2] = 10

    #计算损失
    loss = 0
    win = 0
    for i in 押注:
        loss += (len(i)-1)*下分
        index = np.where(np.asarray(i[1:]) == trueNum[i[0]-1])[0]
        win += i[-1]*赔率*len(index)*下分
    本期赢额 = win - loss
    return 本期赢额
#
file = 'C:\\Users\\ZhangSSD\\Desktop\\预测\\'
name = '2017-05-23.csv'
预测期数= 619481
data = pd.read_csv(file + name)
trueNum = data[data['qi'] == 预测期数].iloc[0,3:].tolist()
wins = cal_猜数字(trueNum,9.85,[[1,0,5],[2,0,0,0,0]],5 )
print(wins)
