'''
YMD年月日：'20170506'
HMS时分秒: numpy系列一维数组，int格式，如：90835（9点08分35秒）
return datetime，可被pandas.to_datetime转化的字符串数组，例：['20170506124535']
'''
def shift_time(YMD,HMS):
    dt = []
    for i in range(len(HMS)):
        # 判断位数
        HMS_i = HMS[i]
        c=0
        while HMS_i != 0:
            HMS_i = int(HMS_i / 10)
            c += 1
        if c == 0:
            HMS_str = '000000'
        elif c == 1:
            HMS_str = '00000' + str(HMS[i])
        elif c == 2:
            HMS_str = '0000' + str(HMS[i])
        elif c == 3:
            HMS_str = '000' + str(HMS[i])
        elif c == 4:
            HMS_str = '00' + str(HMS[i])
        elif c == 5:
            HMS_str = '0' + str(HMS[i])
        elif c == 6:
            HMS_str = str(HMS[i])
        else:
            print('时分秒超过6位！',HMS[i],c)
        NYRSFM_str = str.strip(YMD)+str.strip(HMS_str)
        dt.append(NYRSFM_str.strip())
    return dt;
