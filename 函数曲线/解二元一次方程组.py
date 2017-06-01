import numpy as np

a = 1
b= -1
c = np.exp(-2)
X = 0
Y = a*X**2 + b*X + c

j1 = (-b + np.sqrt( b**2 - 4*a*c )) / (2*a)
j2 = (-b - np.sqrt( b**2 - 4*a*c )) / (2*a)
print(j1,j2)