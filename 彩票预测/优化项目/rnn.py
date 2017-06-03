import pandas as pd
import tensorflow as tf
from 自写库 import bp神经网络包 as bpcnn
import numpy as np

file = 'C:\\Users\\30708\\Desktop\\预测\\'
name = '历史开奖数据.csv'

data = pd.read_csv(file+name).sort_values(by='qi',ascending=True)
y_all = data.iloc[:,3:13].values
y = y_all[:,0]
#
x  = np.asarray(list(range(len(y))))
#


