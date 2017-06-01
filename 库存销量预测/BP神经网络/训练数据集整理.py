import pandas as pd
import numpy as np

data = pd.read_csv('C:\\Users\\16070332\\Desktop\\中间数据\\抽纸_剔除大促与异常值.csv')
data.index = pd.to_datetime(data['statis_date'])
Year = data.index.strftime('%Y').tolist()
YearMax,YearMin = max(Year),min(Year)

Xl = []
for year in range(int(YearMin),int(YearMax)+1):
    dataY = data[str(year)]
    week = dataY['WeekInYear'].drop_duplicates()
    for ii in week:
        index = np.where(dataY['WeekInYear'] == ii)[0].tolist()
        dataXY = dataY.iloc[index,1].values.tolist()
        dataXY.append(float(year))
        dataXY.append(float(ii))
        Xl.append(dataXY)
X = pd.DataFrame(Xl)
X.to_csv('C:\\Users\\16070332\\Desktop\\中间数据\\神经网络X.csv')

Y = data.resample('W').sum()
Y['WeekInYear'] = Y['WeekInYear']/7
Y = Y.dropna()
Y.to_csv('C:\\Users\\16070332\\Desktop\\中间数据\\神经网络Y.csv')