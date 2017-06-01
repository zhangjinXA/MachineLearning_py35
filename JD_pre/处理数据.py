import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
from JD_pre.读取数据 import read_jdata;

dc = read_jdata();
data0 = dc.data0;
Udata = dc.Udata;


data_pay = data0[data0['type'] == 4 ]         #只看付款数据
data_gb_user = data_pay.groupby('user_id')    #按会员编号汇总
data_gb_user_paynum = data_gb_user.count()    #计数汇总
#表关联
data_gb_user_paynum['user_id'] = data_gb_user_paynum.index
Uinfo = pd.merge(data_gb_user_paynum,Udata,how='inner',on='user_id')
#统计汇总
Uinfo_sumage_l = Uinfo.groupby('age')
Uinfo_sumage = Uinfo_sumage_l.sum()
Uinfo_sumage['age'] = Uinfo_sumage.index

plt.plot(range(len(Uinfo_sumage['type'])),Uinfo_sumage['type'])
plt.show()

Uinfo_sumsex = Uinfo.groupby('sex')
print(Uinfo_sumsex.sum())
print(data0)