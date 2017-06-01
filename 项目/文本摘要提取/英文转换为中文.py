import numpy as np
import pandas as pd
import jieba
from sklearn import preprocessing as pre


def recode_l():
    file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\已完成\\2017-5-9-基于RNN的新闻文本关键字提取\\'
    #
    Train_name = 'Charades_v1_train.csv'
    Test_name = 'Charades_v1_test.csv'

    trainX = ''
    #整理训练数据
    data = pd.read_csv(file+Train_name);
    data = data.iloc[:,[2,8]].values
    for i in range(len(data[:,1])): trainX += (data[i,1])[0:-2]+'!! '+data[i,0]+'.'
    #整理测试数据
    test_data = pd.read_csv(file+Test_name);
    test_data = test_data.iloc[:,[2,8]].values
    testY = test_data[:,0]
    testX = test_data[:,1]
    for ii in range(len(testX)):
        ichars = testX[ii]
        if ichars[-1] == '.':
            testX[ii] = ichars[0:-2]+'!!'
        else:
            testX[ii] = ichars + '!!'


    print(testX)
    #整体词
    words = trainX
    for i in testX:
        words += ' '+i
    总体词汇总 = list(jieba.cut(words))
    #编码并转换为中文格式
    le = pre.LabelEncoder()          #编码
    le.fit(总体词汇总)               #编码
    #训练数据
    trainX = list(jieba.cut(trainX))  # 分词
    trainX_code = le.transform(trainX) #编码
    #中文格式训练数据生成dataSet
    #解码需：le.inverse_transform(ord(dataSet))
    dataSet = ''
    for i2 in range(len(trainX_code)):
        if trainX[i2] != ' ':
            dataSet += chr(trainX_code[i2])
            # print(trainX_code[i2],'--',trainX[i2],'--',chr(trainX_code[i2]))
    '''训练数据转换为中文格式编码'''
    testSet = {}
    for i in range(len(testX)):
        sentence = testX[i]
        sentenceList = list(jieba.cut(sentence))
        sentenceList_code = le.transform(sentenceList)
        sentence_chinese = ''
        for i2 in range(len(sentenceList)):
            if sentence[i2] != ' ':
                sentence_chinese += chr(sentenceList_code[i2])
        testSet[i] = sentence_chinese
    # print(testSet[1])
    return [dataSet,testSet,testY,le]
    # for i in dataSet : print(le.inverse_transform(ord(i)))


