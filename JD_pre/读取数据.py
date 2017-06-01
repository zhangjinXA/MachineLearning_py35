import pandas as pd;
import tkinter.filedialog

class read_jdata:

    def __init__(self):
        self.filepath = 'F:\\京东算法大赛数据\\';

    def read_raw_data(self):
        filename = ['F:/京东算法大赛数据/JData_Action_201602.csv',
                    'F:/京东算法大赛数据/JData_Action_201603.csv',
                    'F:/京东算法大赛数据/JData_Action_201603_extra.csv',
                    'F:/京东算法大赛数据/JData_Action_201604.csv',
                    'F:/京东算法大赛数据/JData_Comment(修正版).csv',
                    'F:/京东算法大赛数据/JData_Product.csv',
                    'F:/京东算法大赛数据/JData_User.csv']
        fopen0 = open(filename[0], encoding='utf-8')
        fopen4 = open(filename[4], encoding='utf-8')
        fopen5 = open(filename[5], encoding='utf-8')
        fopen6 = open(filename[6])
        '''
        数据读取
        '''
        self.data0 = pd.read_csv(fopen0, index_col='time')
        # 商品评价表，sku_id,评论数量分段(comment_num)，坏评数量(has_bad_comment)，差评比例(bad_comment_rate)
        self.Cdata = pd.read_csv(fopen4)
        # 商品信息表，sku_id，属性(attr1)1,2,3，品类(cate)，品牌(brand)
        self.Pdata = pd.read_csv(fopen5)
        # 会员信息表，user_id，年龄段(age)，性别(sex)，等级(user_lv_cd)，注册时间(user_reg_dt)
        self.Udata = pd.read_csv(fopen6)

    def read_csv(self,filepath):
        fopen = open(filepath)
        data = pd.read_csv(fopen)
        return data

    def read_excel(self,filepath):
        fopen = open(filepath)
        data = pd.read_excel(fopen,sheetname=0)
        return data





