import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
from JD_pre.读取数据 import read_jdata;

dc = read_jdata()
# dc.read_raw_data();
# data0,Udata = dc.data0,dc.Udata;
# #表关联
# UD = pd.merge(data0,Udata,on='user_id',how='inner')
# #groupby
# dataX = UD.groupby(['sex','age','type']).count()
# dataX.to_excel(dc.filepath+'hahaha.xlsx','sheet1')


fopen = dc.filepath+'hahaha.xlsx'
dataX = pd.read_excel(fopen, sheetname=0,header=0,index_col=[0,1,2])

#############
def 年龄性别_下单概率_test(dataX):
    idx = pd.IndexSlice
    sex = dataX.index.get_level_values('sex')  ; sex= sex.drop_duplicates();
    age = dataX.index.get_level_values(1)      ; age= age.drop_duplicates(); #去除重复值

    list_P = [['sex','age','type','value']]

    for i1 in sex:
        for i2 in age:
            dataX1 = dataX.loc[idx[i1,i2,:],'sku_id']
            for i in range(dataX1.shape[0]):
                是否存在下单 = dataX1.index.get_level_values('type') == 4
                if 是否存在下单.sum() == 1:
                    cc = dataX1.iloc[np.where(是否存在下单 == 1)]
                    list_P.append(\
                        np.asarray(dataX1.index[i]).tolist() + \
                        (cc / dataX1.iloc[i]).values.tolist()
                    )
                else:
                    list_P.append( \
                        np.asarray(dataX1.index[i]).tolist() + [-99]
                        )
    wrData = pd.DataFrame(list_P)
    wrData.to_csv(dc.filepath+'test.csv')
##############
def 下单概率(dataX):

    dataX['type'] = dataX.index.get_level_values('type')
    dataX['age'] = dataX.index.get_level_values('age')
    dataX['sex'] = dataX.index.get_level_values('sex')
    dataX1 = dataX.groupby(by='type').sum()
    dataX2 = dataX.groupby(by='age').sum()
    dataX3 = dataX.groupby(by='sex').sum()
    dataX1.to_excel(dc.filepath+'类型取值type.xlsx','sheet0')
    dataX2.to_excel(dc.filepath + '类型取值age.xlsx', 'sheet0')
    dataX3.to_excel(dc.filepath + '类型取值sex.xlsx', 'sheet0')
    return 0
下单概率(dataX);
# del dc,data0,dataX,Udata
