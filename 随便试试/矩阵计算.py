import numpy as np
from itertools import permutations

zuhe = list(permutations('1234'))
print(zuhe)

A = [[1.,6,8,10],
     [9.,15,7,13],
     [5,5,5,5],
     [5,5,5,5]]

B = [[1,2],
     [3,4]]

x = np.asarray(A,dtype='float')
y = np.asarray(B,dtype='float')
print(x)
print(x[1,2])
print(np.linalg.det(x))