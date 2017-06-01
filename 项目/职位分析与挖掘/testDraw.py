from 项目.职位分析与挖掘 import Draw_china_map
import numpy as np
import pandas as pd

shapefile = "E:\\PythonCode\\myPthon35_Code\\data\\CHN_adm_shp\\CHN_adm1"
dataFile = "D:\\city.csv"
#
posi = pd.read_csv(dataFile,encoding='GBK')
lat = np.array(posi["lat"])  # 获取维度之维度值
lon = np.array(posi["lon"])  # 获取经度值
pop = np.array(posi["pop"], dtype=float)  # 获取人口数，转化为numpy浮点型
Draw_china_map.draw(shapefile,lat,lon,pop,"Population Distribution in China")