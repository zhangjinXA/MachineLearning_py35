import re
import pandas as pd

'''去除重复值'''
def drop_sameSituation(tall):

    tall_pd = pd.DataFrame(tall)
    print(tall_pd)

    tall_pd = tall_pd.drop_duplicates()

    print(tall_pd)


    return tall_pd.values.tolist()

'''正则匹配,t1,t2必须为字符串，内数字必须为0-9之间'''
def match_num(t1,t2,t3):

    tall = []

    for i1 in t1:
        for i2 in t2:
            tall.append([int(i1),int(i2),int(t3)])

    return tall

'''
正则匹配,t1,t2必须为字符串，内数字必须为0-9之间
去除赛道和压分一样的情况
'''
def match_num_dropDuplicates(t1,t2,t3):

    tall = []

    for i1 in t1:
        for i2 in t2:
            if int(i1) != int(i2):#不相等才赋值

                tall.append([int(i1),int(i2),int(t3)])

    return tall

def sigleLine_transform(SigleLinetxt):
    txt = SigleLinetxt
    txt = txt.replace(' ', '')  # 去除空格
    splittxt = re.split('-|/', txt)
    print(splittxt)

    #判断分解长度=3
    #每块为数字
    #最后一块为数字或者数字+去重
    areDigit = []
    if len(splittxt) == 3:
        for i in splittxt:areDigit.append(i.isdigit())

        #'''125-36854/5'''
        # '''125-36854-5'''
        #'''1-5/6'''
        # '''1-5-6'''
        if areDigit == [True,True,True]:

            tall = match_num(splittxt[0],splittxt[1],splittxt[2])
            # print(tall)
            return tall
        #######################


        #'''122 - 652去重'''
        #
        if areDigit == [True,True,False]:

            num = (splittxt[2])[0:-2]
            quchong = (splittxt[2])[-2:]
            # print(quchong)

            if num.isdigit() and quchong=='去重':

                tall = match_num_dropDuplicates(splittxt[0], splittxt[1], num)

                return tall
        ###################

    return [-99]

def txt_transfom(txt):

    if '\n' not in txt:

        tall = sigleLine_transform(txt)

    else:
        mutiLineTXT = txt.split('\n')

        tall = []
        for SigleLinetxt in mutiLineTXT:
            t_sigleLine = sigleLine_transform(SigleLinetxt)

            if t_sigleLine != [-99] :
                tall += t_sigleLine

    tall_dropDuplicates = drop_sameSituation(tall)

    return tall_dropDuplicates

