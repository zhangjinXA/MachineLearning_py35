import time
import pandas as pd
import numpy as np
from 项目.彩票预测 import 爬虫_爬取本期彩票号 as getinfo
from 项目.彩票预测 import readfile,predict
#
def 计算当前是否匹配(预测开奖号码,实际开奖号码):
    pred = 预测开奖号码
    true = 实际开奖号码
    匹配 = []
    for i in range(10):
        temp_pred = pred.iloc[:,i].values
        temp_true = int(true[i])
        a = np.where(temp_pred == temp_true)[0]
        匹配.append( len(a) )

    return 匹配

file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-彩票预测\\'
name = '正序.txt'
out_txt = '预测结果.txt'
预测准确率name = '预测准确率.csv'
预测范围 = 20
预测个数 = 3
hist_data = readfile.read(file + name)
#变量初始化
before_期数 = hist_data.iloc[-1,0]
before_pred = predict.预测(file+name, 预测范围, 预测个数)
while True:
    # 获取最新数据
    info = getinfo.get_info()
    #
    if info[0] == before_期数:
        aaa = 10
        # print('数据未更新，不保存')

    else:
        '''保存数据'''
        #时间格式转换
        timeArray = time.strptime(info[2], "%Y-%m-%d %H:%M:%S")
        info[2] = time.strftime("%Y-%m-%d %H:%M",timeArray)
        #
        txt = '----'.join(i for i in info)
        #输出
        f = open(file+name,'a') #追加模式
        f.write(txt+'\n')
        f.close()
        print('新一期数据已出')
        # 读取数据
        hist_data = readfile.read(file + name)
        '''保存上次预测准确率'''
        开奖号码 = hist_data.iloc[-1,1].split(',')
        上次准确率 = 计算当前是否匹配(before_pred,开奖号码);
        outputStr = str(hist_data.iloc[-1, 0]) + ',' + ','.join(str(i) for i in 上次准确率)+'\n'

        outf2 = open(file+预测准确率name,'a')
        outf2.write(outputStr)
        outf2.close()

        '''预测'''
        pred = predict.预测(file+name, 预测范围, 预测个数)
        #计算历史准确率
        data = pd.read_csv(file+预测准确率name,encoding='GB2312')
        describe = data.describe()
        历史准确率 = describe.iloc[1,1:]
        #输出
        outf = open(file+out_txt,'a')
        print('*********本期开奖结果*****************',file=outf)
        print(hist_data.iloc[-1, :].values,file=outf)
        print('上次准确率->(0:错误，1:正确)\n', outputStr,file=outf)
        print('历史准确率->\n',历史准确率,file=outf)
        print('下期预测结果->\n',pred,file=outf)

        outf.close()
        #屏幕输出
        print('*********本期开奖结果')
        print(hist_data.iloc[-1, :].values)
        print('上次准确率->(0:错误，1:正确)\n', outputStr)
        print('历史准确率->\n', 历史准确率)
        print('下期预测结果->\n',pred)
        #判断变量 赋值
        before_pred = pred
        before_期数 = info[0]
    time.sleep(20)




