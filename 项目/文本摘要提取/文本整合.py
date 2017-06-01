import pandas as pd
import jieba
file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\已完成\\2017-5-9-基于RNN的新闻文本关键字提取\\'
name = 'Charades_v1_train.csv'
Test_name = 'Charades_v1_test.csv'
#训练数据
test_data = pd.read_csv(file+Test_name);data = test_data.iloc[:,[2,8]].values
Y = data[:,0]
testX = data[:,1]
print(Y)
print(testX)

data = pd.read_csv(file+name);data = data.iloc[:,[2,8]].values
train_data = ''
for i in range(len(data[:,1])): train_data += (data[i,1])[0:-2]+' '+data[i,0]+'.'

aaa = jieba.cut('i love you')
print('.'.join(aaa))
