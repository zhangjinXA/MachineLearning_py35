import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from 项目.职位分析与挖掘 import Draw_china_map
import jieba
from pylab import mpl
from wordcloud import WordCloud
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
'''需用户自行修改的参数'''
shapefile = "E:\\PythonCode\\myPthon35_Code\\data\\CHN_adm_shp\\CHN_adm1"  #中国地理边界文件
dataFile = "D:\\city.csv"                                                       #中国城市经纬度文件
font_path = 'C:\\Windows\\fonts\\msyh.ttc'                                    #微软雅黑字体文件
file = 'C:\\Users\\ZhangSSD\\Desktop\\活儿\\职位信息分析与挖掘\\职位信息采集4.22（3）.xlsx' #待处理数据文件
'''读取数据'''
data = pd.read_excel(file,0)
'''
数据清洗
'''
#工作地点分离
area = data['工作地点'].str.split('-')
city = []
for i in area:
    city.append(i[0])
data['city'] = city
#月薪数值化
salary = data['职位月薪'].str.replace('元/月','-')
salary = salary.str.replace('面议','0-0-')
s2 = salary.str.split('-')
salary_value = [] #数值化结果（均值）
for i in s2:
    salary_value_i = (float(i[0])+float(i[1]))/2
    salary_value = salary_value+[salary_value_i]
data['月薪数值化'] = salary_value
#工作经验数值化
工作经验 = data.工作经验
dict工作经验 = {'无经验':0,
         '不限':1,
         '1年以下':2,
         '1-3年':3,
         '3-5年':4,
         '5-10年':5,
         '10年以上':6}
value工作经验 = []
for i in 工作经验:value工作经验.append(dict工作经验[i])
data['工作经验数值化'] = value工作经验
#学历数值化
最低学历 = data.最低学历
dict最低学历 = {'不限':0,
                '高中':1,
                '中专':2,
                '大专':3,
                '本科':4,
                '硕士':5}
value最低学历 = []
for i in 最低学历:value最低学历.append(dict最低学历[i])
data['最低学历数值化'] = value最低学历
'''
要求一、 按照“职位类别”统计每个类别的岗位都有多少个? （要有图）
'''
JobClass = data['职位类别']
result1 = data.groupby(by='职位类别',as_index=True).count().iloc[:,0]
result1 = result1.sort_values(ascending=False)
#绘图
result1.plot(kind='bar')
plt.tight_layout()
plt.show()
'''
要求二、 每个职位类别要求的最低学历是如何？（高中、中专、大专、本科、不限的比例各是多少，用图表示）
'''
Job_Xueli = data.groupby(by=['职位类别','最低学历'],as_index=True).count().iloc[:,0]
#计算比例
result2 = pd.Series(index=Job_Xueli.index,dtype='float')
num_Job = len(result1.index)
for i in range(num_Job):
    Job_name_i = result1.index[i]
    p_i = Job_Xueli[Job_name_i]/result1.values[i]
    result2[Job_name_i] = p_i
#绘图
result2.unstack().plot(kind='bar',stacked=True,color=['r','g','b','black','yellow','gray'])
plt.tight_layout()
plt.show()
'''
要求三、 每个职位类要求的工作经验是多少年？(1年一下，3-5年...等的比例各是多少，用图表示)
'''
Job_Year = data.groupby(by=['职位类别','工作经验'],as_index=True).count().iloc[:,0]
#计算比例
result3 = pd.Series(index=Job_Year.index,dtype='float')
num_Job = len(result1.index)
for i in range(num_Job):
    Job_name_i = result1.index[i]
    p_i = Job_Year[Job_name_i]/result1.values[i]
    result3[Job_name_i] = p_i
#绘图
result3.unstack().plot(kind='bar',stacked=True,color=['r','g','b','black','yellow','gray'])
plt.tight_layout()
plt.show()
'''
要求四、 统计出需求前20的工作地点
'''
location = data.groupby(by='city').count().iloc[:,0]
result4 = location.sort_values(ascending=False)[:21]
#输出结果与绘图
print('需求4***************',result4)
#
posi = pd.read_csv(dataFile,encoding='GBK')
lat = np.array(posi["lat"])  # 获取维度之维度值
lon = np.array(posi["lon"])  # 获取经度值
pop = np.array(posi["pop"], dtype=float)  # 获取散点尺寸
Draw_china_map.draw(shapefile,result4.index,lat,lon,pop,"工作地点分布及大小")

'''
要求五、 统计每一类职位的工作职责是什么?(画出词云)
'''
#岗位处理
job_class = data['职位类别']
jobs = job_class.drop_duplicates()
#
jobs_need = data[['职位类别','岗位要求']]
for i in jobs:
    job_need = jobs_need.loc[jobs_need['职位类别'] == i]['岗位要求']
    #分词
    seg_list = [" ".join(jieba.cut(i,cut_all=False)) for i in job_need]
    lists = ' '.join(seg_list) #分词后的所有词
    lists = lists.replace('任职','')
    lists = lists.replace('要求','')
    #绘图
    wordcloud = WordCloud(font_path=font_path, background_color="black")
    wordcloud.generate(lists)
    plt.imshow(wordcloud)
    plt.title(i)
    plt.axis("off")
    plt.show()
# '''
# 要求六、 统计每一类职位的要求是什么?(画出词云)
# '''
#岗位处理
job_class = data['职位类别']
jobs = job_class.drop_duplicates()
#
jobs_need = data[['职位类别','岗位职责']]
for i in jobs:
    job_duty = jobs_need.loc[jobs_need['职位类别'] == i]['岗位职责']
    #分词
    seg_list = [" ".join(jieba.cut(i,cut_all=False)) for i in job_duty]
    lists = ' '.join(seg_list) #分词后的所有词
    lists = lists.replace('岗位','')
    lists = lists.replace('职责','')
    #绘图
    wordcloud = WordCloud(font_path=font_path, background_color="black")
    wordcloud.generate(lists)
    plt.imshow(wordcloud)
    plt.title(i)
    plt.axis("off")
    plt.show()

'''
要求七、 取需求最高的3类职位   判定月薪、工作经验、学历之间的关系。（有图）
'''
data7 = data[['职位类别','月薪数值化','工作经验数值化','最低学历数值化']] ; #data7 = data7.set_index('职位类别')
#
ax = plt.figure().add_subplot(111,projection='3d')
ax.set_xlabel(dict工作经验);ax.set_ylabel('月薪');ax.set_zlabel(dict最低学历)
#
Job_top3 = result1.index[0:3].tolist()
for i in Job_top3:
    result7_i = data7.loc[data7['职位类别'] == i]
    result7_i = result7_i.groupby(by=['工作经验数值化','最低学历数值化'],as_index=False).mean()
    print(result7_i)
    Z,X,Y = result7_i['月薪数值化'],result7_i['工作经验数值化'],result7_i['最低学历数值化']
    ax.plot(X, Y, Z, marker='^',label=i)
plt.title('月薪、工作经验、学历之间')
plt.legend()
plt.show()

'''
要求八、 工作经验：不限或者无经验的，工作地点与职位月薪的关系
'''
data8 = data.iloc[ np.where(data['工作经验数值化'] <= 1)[0].tolist() , : ]
data8 = data8[['工作经验','工作经验数值化','工作地点','city','月薪数值化']]
#绘图--工作地点与月薪
data81 = data8[['city','月薪数值化']]
data81=data81.groupby(by='city').mean()
data81 = data81.sort_values(by='月薪数值化')
data81.plot(kind='bar')
plt.tight_layout()
plt.show()