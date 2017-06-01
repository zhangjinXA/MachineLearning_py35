import pandas as pd
import datetime

class process_dateTime:
    #数据csv数据
    #时间序列源信息格式 %Y%m%d
    filepath = 'C:\\Users\\16070332\\Desktop\\'
    '''
    读取数据
    转换时间序列
    '''
    def import_data(self,name,encoding,dataFormat):
        file = self.filepath + name
        fopen = open(file, encoding=encoding)
        # 读取数据
        self.data = pd.read_csv(fopen)
        #定义时间序列
        self.data.index = pd.to_datetime( \
            self.data['statis_date'],
            format=dataFormat)
        #按时间排序数据
        self.data = self.data.sort_index()
        return self.data
    '''
    时间序列格式化输出
    '''
    def 时间序列格式化_仅保留月日(self,dateTimeArr):
        #dateTimeArr : datetime数组，一般为pandas中时间序列
        date_arr_output = pd.to_datetime(
            dateTimeArr.strftime('%m%d'),
            format='%m%d',
            errors='ignore')
        print(date_arr_output)
        return date_arr_output
    def 时间序列格式化_批量更改年月日(self,dateTimeArr,strFormat):
        #dateTimeArr : datetime数组，一般为pandas中时间序列
        #strFormat:如'2015%m%d'
        date_arr_output = pd.to_datetime(
            dateTimeArr.strftime(strFormat),
            format='%Y%m%d',
            errors='ignore')
        return date_arr_output
    '''
    时间信息转化
    '''
    def 年月日转为周几(self,dateTimeArr):
        #年月日批量转化为周几
        # dateTimeArr : datetime数组，一般为pandas中时间序列
        weekOfDay = []
        for i in dateTimeArr:
            weekday = pd.to_datetime(i).weekday()
            weekOfDay.append(str(weekday))
        return weekOfDay;