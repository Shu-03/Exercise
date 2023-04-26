# 作者：shu qi
# 开发时间：2022/10/19 17:01
from pyecharts import Polar
# from matplotlib.pyplot import polar
from pyecharts import Bar, Scatter3D
from pyecharts import Page
import csv
page = Page()
polar1 = Polar("极坐标系-堆叠柱状图示例1",width=1200,height=600)
filename="hot-dog-places.csv"
datax = []
datay = []
with open(filename)as f:
    reader = csv.reader(f)
    for datarow in reader:
        datax.append(datarow)

radius= datax[0]
y1=datax[1]
y2=datax[2]
y3=datax[3]
#print (y1)
polar1.add("A",y1,radius_data=radius,type='barRadius' ,is_stack=True)
polar1.add("B",y2,radius_data=radius,type='barRadius',is_stack=True)
polar1.add("C",y3,radius_data=radius,type='barRadius', is_stack=True)
polar1.render()
#polar.show_config()
page.add(polar1)


polar2 =Polar(" 极坐标系-堆叠柱状图示例2",width=1200,height=600)
polar2.add("A",y1, radius_dataF=radius,type='barAngle',is_stack=True)
polar2.add("B",y2,radius_data=radius,type='barAngle',is_stack=True)
polar2.add("C",y3, radius_data=radius, type='barAngle' , is_stack=True)
#polar.show_config()
page.add(polar2)
page.render()