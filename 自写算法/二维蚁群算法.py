import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''载入影像数据'''
filepath = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\医学影像\\rawdata\\201705造数据\\'
file = filepath+'pppp系数矩阵.img'
data = np.fromfile(file,dtype=np.float64);
data.shape = 2,2048,2048
#
'''生成蚂蚁初始位置'''
def define_aunt(limX,limY,R):
    x0 = np.random.random_integers(R+1,limX-R-1)
    y0 = np.random.random_integers(R+1,limY-R-1)
    return [x0,y0]
'''生成搜索坐标'''
def generate_SearchPoint(R,center_point):
    x_bias, y_bias = center_point
    x,y = np.asarray(range(-R,R+1,1))+x_bias, np.asarray(range(-R,R+1,1))+y_bias
    #
    point = []
    for i1 in x:
        point.append([i1,R+y_bias]);point.append([i1,-R+y_bias])
    for i2 in y:
        point.append([R+x_bias,i2]);point.append([-R+x_bias,i2])
    point = np.asarray(point)
    return point
'''蚂蚁搜索方式定义'''
def search(startPoint,SearchPoint,data):
    sp,cp = SearchPoint,startPoint
    if (cp[0]+R < len(data[:,0])) and (cp[1]+R < len(data[0,:])):   #判断搜索点需要在图像范围内
        路径 = [cp[0],cp[1]]  #x,y
        for i in range(len(sp[:,0])):                             #每个搜索点循环
            sp_data_i = data[sp[i,0],sp[i,1]]

            if sp_data_i < data[路径[0],路径[1]]:                 #如果搜索点值大于记录值，则记录该点
                路径 = [sp[i,0],sp[i,1]]
    else:
        路径 = [cp[0], cp[1]]

    return 路径

########################################################################
'''开始搜索'''
R = 50           #搜索半径 >0
num_aunts =  10000 #蚂蚁数量
start_Points = []
final_Points = []
for i in range(num_aunts):
    startPoint = define_aunt(2048,2048,R);#定义蚂蚁初始坐标
    start_Points.append(startPoint)
    endPoint = [0,0];n=0

    while endPoint != startPoint:               # 开始点和终点不变时结束
        if n!=0:startPoint = endPoint
        SearchPoint = generate_SearchPoint(R, startPoint)
        endPoint = search(startPoint,SearchPoint,data[1,:,:])
        n += 1
    final_Points.append(endPoint)
    if i%1000 == 0 :print('蚂蚁******',i,'----',startPoint)


#保存数据
final_Points = pd.DataFrame(final_Points,columns=['X','Y']).to_csv(filepath+'蚁群搜索结果-R'+str(R)+'.csv')
start_Points = pd.DataFrame(start_Points,columns=['X','Y']).to_csv(filepath+'蚁群初始分布-R'+str(R)+'.csv')

plt.plot(final_Points['X'],final_Points['Y'],'ro')
plt.show()
