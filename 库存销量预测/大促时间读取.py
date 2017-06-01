import pandas as pd;

class read_promotionDate:
    filepath = 'F:\\自发项目\\2017.3.17价格销量预测\\大促时间表\\大促时间表.xlsx'
    def __init__(self):
        filepath = self.filepath
        data2015 = pd.read_excel(filepath,sheetname=0,header=0)
        data2015['活动开始日期'] = pd.to_datetime(
                                            data2015.iloc[:,1],
                                            format='%Y.%m.%d')
        data2015['活动结束日期'] = pd.to_datetime(
                                            data2015.iloc[:,2],
                                            format='%Y.%m.%d')


        data2016=pd.read_excel(filepath,sheetname=1,header=0)
        data2016 = data2016.fillna({'活动结束日期':data2016['活动开始日期']})
        data2016['活动开始日期'] = pd.to_datetime(
                                            data2016.iloc[:,1],
                                            format='%Y/%m/%d')
        data2016['活动结束日期'] = pd.to_datetime(
                                            data2016.iloc[:,2],
                                            format='%Y/%m/%d')
        self.Promotion_Date = {'date2015':data2015,'date2016':data2016}
    def 大促时间序列生成(self,date):
        活动开始日期 = date['活动开始日期'].values
        活动结束日期 = date['活动结束日期'].values

        PdateList = []
        for i in range(len(活动开始日期)):
            Prom_date_List = pd.date_range(
                                            start= 活动开始日期[i],
                                            end=活动结束日期[i],
                                            freq='1D'
                                           )
            PdateList = PdateList + Prom_date_List.tolist()
        大促时间序列 = pd.Series(data=PdateList)
        return PdateList



