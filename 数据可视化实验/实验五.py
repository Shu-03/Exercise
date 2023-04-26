# 作者：shu qi
# 开发时间：2022/11/24 17:07
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
crime=pd.read_csv("crimeRatesByState2005.csv")
crime2=crime[crime.state != "Uninted States"]
crime2=crime2[crime2.state !="District of Columbia"]
g=sns.jointplot(x='murder',y='burglary',data=crime2,kind="reg",height=5,ratio=3 ,color="g")
plt.show()
#plt.savefig("实验五散、密、直一体图.png")

from pyecharts import EffectScatter
es =EffectScatter("动态散点图示例")
es.add("arrow_sample",crime2['murder'],crime2['burglary'],symbol="arrow")
es.render()

#矩阵图
crime2=crime2.drop(['state'],axis=1)
crime2=crime2.drop(['population'],axis=1)
g=sns.pairplot(crime2)
plt.show()
#plt.savefig("实验五矩阵图.png")