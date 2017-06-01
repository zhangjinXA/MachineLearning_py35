import numpy as np
import matplotlib.pyplot as plt


X = np.random.rand(1000)
Y = np.exp(X)
Y = (10**80)**-X

plt.plot(X,Y,'o',label='Y = 100000000000^(-X)')
plt.legend()
plt.show()