import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#author QQ 307080785
'''
读取数据
'''
a = pd.DataFrame([0])
file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\20170422\\vg_sales.xlsx'
data = pd.read_excel(file,sheetname=0,header=0)
'''
任务1
1.	Find top 10 publisher of sum of Global_Sales , NA_sales, JP_Sales
'''
data01 = data.iloc[:,5:].groupby(by='Publisher',axis=0,as_index=False,sort=True).sum()
#top10 :NA_Sales
top10_NA_Sales = data01.sort('NA_Sales',ascending=False).iloc[0:10,:]
print('*********任务一 --> NA地区top10   ****************')
print(top10_NA_Sales[['Publisher','NA_Sales']])
#top10 :Global_Sales
top10_Global_Sales = data01.sort('Global_Sales',ascending=False).iloc[0:10,:]
print('*********任务一 --> 全球top10   ****************')
print(top10_Global_Sales[['Publisher','Global_Sales']])
#top10 :JP_Sales
top10_JP_Sales = data01.sort('JP_Sales',ascending=False).iloc[0:10,:]
print('*********任务一 --> 日本top10   ****************')
print(top10_JP_Sales[['Publisher','JP_Sales']])

'''
任务2
find best game for those top 10 publish,based on global_sales.
'''
data02 = data.sort(['Publisher','Global_Sales'],ascending=False)
#过滤数据
publisher_top10_globalsale = top10_Global_Sales['Publisher']
index = data02['Publisher'].isin(publisher_top10_globalsale)
indexnum = np.where(index == True)
filter_data02 = data02.iloc[indexnum[0],:]
#提取数据
filter_data02['去重']=filter_data02['Publisher'].duplicated()
final_data = filter_data02.loc[filter_data02['去重'] == False]  #最终结果

print('*********任务二 --> 全球销量top10游戏名   ****************')
print(final_data)
'''
任务3
find sum of NA_Sales (JP_Sales) Condition vs. Genre
'''
data03 = data[['Genre','NA_Sales','JP_Sales']].groupby(by='Genre').sum()
#绘图
bar_width = 0.35
opacity = 0.4
index = np.arange(len(data03.index))
rects1 = plt.bar(index, data03['NA_Sales'], bar_width,alpha=opacity, color='b',label='NA_Sales')
rects2 = plt.bar(index+bar_width, data03['JP_Sales'], bar_width,alpha=opacity,color='r',label='JP_Sales')
#设置标注
plt.title('NA vs. JP sales')
plt.xticks(index + bar_width, data03.index)
plt.legend()
plt.show()
'''
任务4
plot trend of NA sales, JP sales, and global sales by year
'''
data04 = data.groupby(by='Year').sum()
#绘图
plt.plot(data04.index,data04['NA_Sales'],label='NA_Sales')
plt.plot(data04.index,data04['JP_Sales'],label='JP_Sales')
plt.plot(data04.index,data04['Global_Sales'],label='Global_Sales')
plt.legend()
plt.show()
'''
任务5
For top 1 popular game type, Action Game. Lets see the trend of sale of action game by year.
'''

data05 = data.loc[data['Genre'] == 'Action']
data05 = data05.groupby(by='Year').sum()
X = data05.index
Y = data05['NA_Sales']
#绘图
plt.plot(X,Y,label='Action--NA_Sales--trend')
plt.title('Action--NA_Sales--trend')
plt.legend()
plt.show()

'''
任务6
For top 1 popular game type in Japan, Role-playing. Lets see the trend of sale of action game by year
'''
data06 = data.loc[data['Genre'] == 'Role-Playing']
data06 = data06.groupby(by='Year').sum()
X = data06.index
Y = data06['JP_Sales']
#绘图
plt.plot(X,Y,label='Role-Playing--JP_Sales--trend')
plt.title('Role-Playing--JP_Sales--trend')
plt.legend()
plt.show()

'''
任务7
find for each year, which genre has highest NA sales, and Japan sales? 
可以用图表现出来吗? 按照年份找出每年北美销量最好的游戏类型和日本销量最好的游戏类型
'''
data07=data.loc[:,['Year','Genre','NA_Sales','JP_Sales']].groupby(by=['Year','Genre']).sum()

sales_NA = data07['NA_Sales']
sales_JP = data07['JP_Sales']


sales_NA.unstack().plot(kind='bar',stacked=True,color=['r','g','b','black','yellow','gray'])
plt.title('NA-sales bar')
plt.show()
sales_JP.unstack().plot(kind='bar',stacked=True,color=['r','g','b','black','yellow','gray'])
plt.title('JP-sales bar')
plt.show()