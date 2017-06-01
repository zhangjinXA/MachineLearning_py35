import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
################################################################################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ax.axis("equal")  # 设置图像显示的时候XY轴比例
plt.grid(True)  # 添加网格
################################################################################
