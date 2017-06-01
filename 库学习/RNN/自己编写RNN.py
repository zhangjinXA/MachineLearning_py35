import tensorflow as tf
import jieba
import sklearn.preprocessing as skpre

word = '今天天气很好,天空很蓝'
'''分词：jbl'''
jb = jieba.cut(word,cut_all=False)
jbl = list(jb)
print(jbl)
'''词转换为值：trainWordNum'''
wN = skpre.LabelEncoder()
wordNum= wN.fit(jbl)
trainWordNum = wN.transform(jbl)   #
print(wN.inverse_transform(trainWordNum))
'''tf搭建'''
#输入神经元个数：1
#隐层个数：1
#隐1层神经元个数：2
#输出神经元个数：1
train_data = tf.placeholder()
#定义隐层神经元
w_state = [[0.5,0.5],
          [0.5,0.5]]
w_input = [0.5,0.5]
bias_hidden = [0.1,0.1]
#定义全连接层神经元
w_out = [0.3,0.3]
bias_out = [0.1]
#定义输入层
inputState = tf.placeholder(shape=(2))
inputLayer = tf.placeholder(shape=(1))
#定义状态输出
state = inputState * w_state + inputLayer * w_input + bias_hidden
Y  = state * w_out + bias_out
#定义损失函数
loss = tf.reduce_sum((Y - Y_true)**2)
