import pandas as pd
import tensorflow as tf
from tensorflow.contrib.rnn import BasicRNNCell,MultiRNNCell
import numpy as np


file = 'C:\\Users\\30708\\Desktop\\预测\\'
name = '历史开奖数据.csv'
rnn_size = 250
#
data = pd.read_csv(file+name).sort_values(by='qi',ascending=True)
y_all = data.iloc[:,3:13].values
#
input_and_output = y_all
#
cell = BasicRNNCell(num_units=rnn_size,state_is_tuple=True)
initial_state = cell.zero_state(batch_size=100,dtype=tf.float32)

softmax_w = tf.get_variable("softmax_w", [rnn_size, 11])
softmax_b = tf.get_variable("softmax_b", [11])

embedding = tf.get_variable("embedding", [11, rnn_size])

inputs = tf.nn.embedding_lookup(embedding, input_data)

outputs, last_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state, scope='rnnlm')
output = tf.reshape(outputs,[-1, rnn_size])

logits = tf.matmul(output, softmax_w) + softmax_b
probs = tf.nn.softmax(logits)