# 作者：shu qi
# 开发时间：2022/11/22 14:17
from pyecharts import Line
line = Line("美国邮费阶梯图")
datax = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
datay = [0.32,0.32,0.32,0.32,0.33,0.33,0.34,0.37,0.37,0.37,0.37,0.39,0.41,0.42,0.44]
line.add("Price",datax,datay,is_step=False,is_label_show=True,yaxis_min=0.3,yaxis_max=0.45)
line.render()