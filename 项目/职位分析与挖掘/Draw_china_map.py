import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
matplotlib.rcParams['toolbar'] = 'None'

ax = plt.figure().add_subplot(111)
def draw(shapefile,city,lat,lon,pop,title):

    size=(pop/np.max(pop))*100    # 绘制散点图时图形的大小，如果之前pop不转换为浮点型会没有大小不一的效果
    transparent = np.asarray(pop)/np.max(pop)  #透明度

    map = Basemap(projection='stere',
                  lat_0=35, lon_0=110,
                  llcrnrlon=82.33,
                  llcrnrlat=3.01,
                  urcrnrlon=138.16,
                  urcrnrlat=53.123,resolution='l',area_thresh=10000,rsphere=6371200.)

    map.drawcoastlines()
    map.drawcountries()
    map.drawcounties()
    map.readshapefile(shapefile,'states',drawbounds=True)
    map.drawmapboundary()

    parallels = np.arange(0.,90,10.)
    map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线

    meridians = np.arange(80.,140.,10.)
    map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线

    x,y = map(lon,lat)
    for i in range(len(x)):
        map.scatter([x[i]],[y[i]],s=size[i],alpha=transparent[i],color='red',label=city[i])
    plt.title(title)
    plt.legend()
    plt.show()