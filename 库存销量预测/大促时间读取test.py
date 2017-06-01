from 库存销量预测 import 大促时间读取

readObj = 大促时间读取.read_promotionDate()
date = readObj.Promotion_Date
date2015 = date['date2015']
大促时间序列 = readObj.大促时间序列生成(date2015)
print(大促时间序列)