import pandas as pd
from sklearn import preprocessing as pre
from 自写库.关联规则 import *
from 项目.关联分析与聚类.关联度输出 import *
from 自写库.数据离散化 import 离散化 as pre2

'''
Xz --> 一维list
Yz --> 一维list
#
Xz,Yz长度必须一致
#
输出文件名-->outfile+outname 
X/Y 数字化方式 --> 离散化（连续数字），标签化（字符）
X/Y离散数目 -->  仅离线化时有效
'''

def 关联输出(Xz,Yz,outfile,outname,X数字化方式,Y数字化方式,X离散数目=1,Y离散数目=1):
    '''整理输入数据'''
    if X数字化方式 =='离散化':
        leX = pre2();leX.fit(Xz,X离散数目)
    else:
        leX = pre.LabelEncoder();leX.fit(Xz)
    if Y数字化方式 =='离散化':
        leY = pre2();leY.fit(Yz,Y离散数目)
    else:
        leY = pre.LabelEncoder();leY.fit(Yz)

    X,Y = leX.transform(Xz),leY.transform(Yz)
    '''关联计算及输出'''
    #计算关联关系
    关联度 = apriori(X,Y)
    #输出
    output_Have2LabelEncoding(关联度,outfile+outname,leX,leY)



