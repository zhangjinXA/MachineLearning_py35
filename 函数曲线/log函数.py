import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

def 信息熵(X):
    Y = -X * (np.log(X)/np.log(2))
    return Y


X = np.random.rand(200)
Y = 信息熵(X)
print(np.exp(-1))
plt.plot(X,Y,'ro')
plt.plot(np.exp(-1),信息熵(np.exp(-1)),'bo')
plt.show()
