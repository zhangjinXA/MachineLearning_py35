import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn

lstm_hidden_size  = 2
lstm = rnn.BasicLSTMCell(lstm_hidden_size)

#初始化函数
batch_size = []
lstm.zero_state(batch_size,tf.float32)

#损失函数
loss = 0
#最大序列长度
num_steps  = 20
#
for i in range(num_steps):
    if i>0 : tf.get_variable_scope().reuse_variables() #????????????
    lstm_output,state = lstm(current_input,state)

    final_output = fully_connect(lstm_output)
    loss += calc_loss(final_output,expected_output)