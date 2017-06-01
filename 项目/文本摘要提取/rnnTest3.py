# -*- coding: utf-8 -*-  
""" 
Created on zxw 08 17:36:23 2017
@author: sunshininwater 
"""
import numpy as np
import pandas as pd
import jieba
from sklearn import preprocessing as pre
from 项目.文本摘要提取 import 英文转换为中文
#import codecs

dataSet,testSet,testY,le = 英文转换为中文.recode_l()
print(testSet[1])
'''
dateSet
'''
# dataSet = open(file+tname, 'r').read() #读取txt一整个文件的内容为字符串str类型
# print(dataSet)

#
charSet = list(set(dataSet))#去除重复的字符
#打印源文件中包含的字符个数、去重后字符个数  
dataSet_size, vocab_size = len(dataSet), len(charSet)  
print('dataSet has %d characters, %d unique.' % (dataSet_size, vocab_size)  )
#创建字符的索引表
# dataSet2 = dataSet
# for i in range(len(testSet)):
#     dataSet2 += testSet[i]
# charSet2 = list(set(dataSet2))#去除重复的字符
char_to_ix = { ch:i for i,ch in enumerate(charSet) }
ix_to_char = { i:ch for i,ch in enumerate(charSet) }
print( char_to_ix )
hiddenSize = 100 # 隐藏层神经元个数  
seq_length = 20 #  
learning_rate = 1e-1#学习率  
  
#网络模型  
Input_Hidden = np.random.randn(hiddenSize, vocab_size)*0.01 # 输入层到隐藏层  
Hidden_Hidden = np.random.randn(hiddenSize, hiddenSize)*0.01 # 隐藏层与隐藏层  
Hidden_Output = np.random.randn(vocab_size, hiddenSize)*0.01 # 隐藏层到输出层，输出层预测的是每个字符的概率  
Hidden_Bias = np.zeros((hiddenSize, 1)) #隐藏层偏置项  
Output_Bias = np.zeros((vocab_size, 1)) #输出层偏置项  


#inputs  t时刻序列，也就是相当于输入  
#targets t+1时刻序列，也就是相当于输出  
#hprev t-1时刻的隐藏层神经元激活值  
def lossFun(inputs, targets, hprev):  
    xs, hs, ys, ps = {}, {}, {}, {}  
    hs[-1] = np.copy(hprev)  
    loss = 0  
    #前向传导  
    for t in range(len(inputs)):
            xs[t] = np.zeros((vocab_size,1)) #把输入编码成0、1格式，在input中，为0代表此字符未激活  
            xs[t][inputs[t]] = 1  
            hs[t] = np.tanh(np.dot(Input_Hidden, xs[t]) + np.dot(Hidden_Hidden, hs[t-1]) + Hidden_Bias) # RNN的隐藏层神经元激活值计算  矩阵内积
            ys[t] = np.dot(Hidden_Output, hs[t]) + Output_Bias # RNN的输出  
            ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) # 概率归一化  
            loss += -np.log(ps[t][targets[t],0]) # softmax 损失函数  
    #反向传播  
    dInput_Hidden, dHidden_Hidden, dHidden_Output = np.zeros_like(Input_Hidden), np.zeros_like(Hidden_Hidden), np.zeros_like(Hidden_Output)  
    dHidden_Bias, dOutput_Bias = np.zeros_like(Hidden_Bias), np.zeros_like(Output_Bias)  
    dhnext = np.zeros_like(hs[0])  
    for t in reversed(range(len(inputs))):
        dy = np.copy(ps[t])  
        dy[targets[t]] -= 1 # backprop into y  
        dHidden_Output += np.dot(dy, hs[t].T)  
        dOutput_Bias += dy  
        dh = np.dot(Hidden_Output.T, dy) + dhnext # backprop into h  
        dhraw = (1 - hs[t] * hs[t]) * dh # backprop through tanh nonlinearity  
        dHidden_Bias += dhraw  
        dInput_Hidden += np.dot(dhraw, xs[t].T)  
        dHidden_Hidden += np.dot(dhraw, hs[t-1].T)  
        dhnext = np.dot(Hidden_Hidden.T, dhraw)  
        for dparam in [dInput_Hidden, dHidden_Hidden, dHidden_Output, dHidden_Bias, dOutput_Bias]:  
            np.clip(dparam, -5, 5, out=dparam) # clip to mitigate exploding gradients  
    return loss, dInput_Hidden, dHidden_Hidden, dHidden_Output, dHidden_Bias, dOutput_Bias, hs[len(inputs)-1]  


#预测函数，用于验证，给定seed_ix为t=0时刻的字符索引，生成预测后面的n个字符  
def sample(h, seed_ix, n):  
  
    x = np.zeros((vocab_size, 1))  
    x[seed_ix] = 1  
    ixes = []  
    for t in range(n):
        h = np.tanh(np.dot(Input_Hidden, x) + np.dot(Hidden_Hidden, h) + Hidden_Bias)#h是递归更新的  
        y = np.dot(Hidden_Output, h) + Output_Bias  
        p = np.exp(y) / np.sum(np.exp(y))  
        ix = np.random.choice(range(vocab_size), p=p.ravel())#根据概率大小挑选  
        x = np.zeros((vocab_size, 1))#更新输入向量  
        x[ix] = 1  
        ixes.append(ix)#保存序列索引  
    return ixes  
  
n, p = 0, 0  
mInput_Hidden, mHidden_Hidden, mHidden_Output = np.zeros_like(Input_Hidden), np.zeros_like(Hidden_Hidden), np.zeros_like(Hidden_Output)  
mHidden_Bias, mOutput_Bias = np.zeros_like(Hidden_Bias), np.zeros_like(Output_Bias) # memory variables for Adagrad  
smooth_loss = -np.log(1.0/vocab_size)*seq_length # loss at iteration 0  
  
while n<20000:
#n表示迭代网络迭代训练次数。当输入是t=0时刻时，它前一时刻的隐藏层神经元的激活值我们设置为0  
    if p+seq_length+1 >= len(dataSet) or n == 0:   
        hprev = np.zeros((hiddenSize,1)) #   
        p = 0 # go from start of dataSet  
    #输入与输出  
    inputs = [char_to_ix[ch] for ch in dataSet[p:p+seq_length]]  
    targets = [char_to_ix[ch] for ch in dataSet[p+1:p+seq_length+1]]

    if n==0:
        print( "the first inputs:")
        print (inputs)
        print (targets)
        print (dataSet[p:p+seq_length])
        print (dataSet[p+1:p+seq_length+1])
    if n==1:
        print ("the second inputs:")
        print (inputs)
        print (targets   )
        print (dataSet[p:p+seq_length])
        print (dataSet[p+1:p+seq_length+1])

    #当迭代了1000次，  
    if n % 1000 == 0:  
        sample_ix = sample(hprev, inputs[0], 50)
        txt = ''.join(ix_to_char[ix] for ix in sample_ix)

        txt2 = ''
        for i10 in txt : txt2 += le.inverse_transform(ord(i10))
        print( '----\n %s \n----' % (txt2, ))
         
    # RNN前向传导与反向传播，获取梯度值  
    loss, dInput_Hidden, dHidden_Hidden, dHidden_Output, dHidden_Bias, dOutput_Bias, hprev = lossFun(inputs, targets, hprev)  
    smooth_loss = smooth_loss * 0.999 + loss * 0.001  
    if n % 100 == 0: 
        print ('iter %d, loss: %f' % (n, smooth_loss)) # print progress
      
    
    # 采用Adagrad自适应梯度下降法
    for param, dparam, mem in zip([Input_Hidden, Hidden_Hidden, Hidden_Output, Hidden_Bias, Output_Bias],   
                                [dInput_Hidden, dHidden_Hidden, dHidden_Output, dHidden_Bias, dOutput_Bias],   
                                [mInput_Hidden, mHidden_Hidden, mHidden_Output, mHidden_Bias, mOutput_Bias]):  
        mem += dparam * dparam  
        param += -learning_rate * dparam / np.sqrt(mem + 1e-8) #自适应梯度下降公式  
    p += seq_length #批量训练  
    #p +=1
    n += 1 #记录迭代次数


'''
RNN到此结束,测试数据验证
'''
for i0 in range(len(testSet)):
    #输入数据格式转换
    inputs = []
    for ch in testSet[i0]:
        num = char_to_ix.get(ch,-99)
        if num != -99:
            inputs.append(num)
    #使用模型预测
    sample_ix = sample(hprev, inputs, 1)
    #模型输出格式转换
    txt = ''
    for ix in sample_ix:
        num = ix_to_char.get(ix,-99)
        if num != -99:
            txt += num
    txt2 = ''
    for i10 in txt: txt2 += le.inverse_transform(ord(i10))
    print( '----\n 预测：%s ---实际：%s \n----' % (txt2, testY[i0]))
    #预测文本分词






