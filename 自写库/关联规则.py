import numpy as np

def apriori(X,Y):
    x,y = X,Y
    jiheL = []
    for i in range(len(X)):
        temp = [x[i],y[i]]
        jiheL.append(temp)
    #
    num_all = len(jiheL)
    num_x = len(x)
    #
    Xdiff,Ydiff = list(set(x)),list(set(y))
    #循环执行
    关联度 = []
    for i1 in Xdiff:
        for i2 in Ydiff:
            temp = [i1,i2]
            num = 0
            for ik in jiheL:
                if temp == ik:
                    num += 1
                    num_Xi1 = np.where(x == i1)[0]
            # 关联度.append([i1,i2,num,num/num_all])
            关联度.append([i1, i2, num / num_all,num/len(num_Xi1)])
    return 关联度




