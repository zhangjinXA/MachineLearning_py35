#encoding:utf-8
#sklearn 决策树只能二分类
#
import 西瓜数据处理.西瓜数据读取与清洗 as readers
import numpy as np;
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.externals.six import StringIO # 读写
import pydotplus
import sys

'''数据读取'''
data2 = readers.read_XiGua('E:\\PythonCode\\myPthon35_Code\\data\\西瓜数据集2.txt')
data = data2.copy(deep=True)
'''标签数值化'''
#X标签数值化
le = preprocessing.LabelEncoder()
for i in [0,1,2,3,4,5]:
    le.fit(data.iloc[:,i])
    data.iloc[:,i] = le.transform(data.iloc[:,i])
#Y结果二值化
le2 = preprocessing.LabelBinarizer()
le2.fit(data.iloc[:,8])
data.iloc[:,8] = le2.transform(data.iloc[:,8])
#
data.to_csv('C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\xigua2.csv')
'''决策树'''
x,y = data.iloc[:,0:6].values,data.iloc[:,-1].values
''''' 拆分训练数据与测试数据 '''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
''''' 使用信息熵作为划分标准，对决策树进行训练 '''
# clf = tree.DecisionTreeClassifier(criterion='entropy',max_features=1.0)
clf = tree.DecisionTreeClassifier(criterion='gini',min_samples_split=4)
clf.fit(x, y)
# clf.fit(x_train, y_train)
''' 把决策树结构写入文件 '''
file = StringIO()
tree.export_graphviz(clf, out_file=file,\
                     feature_names=['色泽','GenDi','QiaoSheng','纹理','QiBu','ChuGan'], \
                     special_characters=True)
graph = pydotplus.graph_from_dot_data(file.getvalue())
print(file.getvalue())
graph.write_png("C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\iris.png")
''' 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大 '''
print(clf.feature_importances_)
'''测试结果的打印'''
answer = clf.predict(x_train)
print(np.mean( answer == y_train))
'''准确率与召回率'''
precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
answer = clf.predict_proba(x)[:,1]
print(classification_report(y, answer))#, target_names = ['thin', 'fat']
