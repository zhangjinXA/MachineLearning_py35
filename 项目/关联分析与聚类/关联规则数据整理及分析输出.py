from 项目.关联分析与聚类.关联分析 import *
import pandas as pd

#读取数据
file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\2017-5-23-关联规则\\'
name = '第一类规则（与运动方式、加工材料、行为相关）用数据.xlsx'
Excel数据 = pd.read_excel(file+name,0).dropna()  #去除空值
#选取输入数据
Xz =  Excel数据['长']
Yz =  Excel数据['加工材料']
#计算
关联输出(\
     Xz = Xz.values.tolist(),
     Yz = Yz.values.tolist(),
     outfile=file,
     outname='test.csv',
     X数字化方式='离散化',
     Y数字化方式='转码',
     X离散数目=5,
     Y离散数目=0)

'''
X/Y 数字化方式 --> 离散化（连续数字），标签化（字符）
X/Y离散数目 -->  仅离线化时有效
'''
