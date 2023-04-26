# 作者：shu qi
# 开发时间：2022/10/19 15:16
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('python_xs2018.xls')
print(df)
#箱式图
fig = plt.figure()  #创建一个绘图对象
ax = fig.add_subplot(1,1,1)  #将画布分成1行1列，并在第一块中画图
ax.boxplot(df['Sales'])  #按“Sale”字段画箱式图
plt.savefig('实验二箱式图.png')
plt.show() #显示图像
#import seaborn as sns  #导入seaborn，别名为sns

#小提琴图
sns.violinplot(x=df['Age'],y=df['Sex'])    #分以“Age” 、“Sex”字段字段为横、纵坐标，画小提琴图
sns.despine()    #去除上侧和右侧轴线
plt.savefig('实验二小提琴图(无上侧和右侧轴线).png')
plt.show()    #显示图像
#sns.violinplot(df['Age'],df['Sex'])    #分以“Age” 、“Sex”字段字段为横、纵坐标，画小提琴图
#sns.despine()    #去除上侧和右侧轴线
#plt.savefig('实验二小提琴图.png')
#plt.show()    #显示图像

#散点图
fig = plt.figure()  #创建一个绘图对象
ax = fig.add_subplot(1,1,1)    #设置画布
x=df['ID']     #取ID字段中的值
y=df['Income']    #取Income字段中的值
z=df['Sales']     #取Income字段中的值
ax.scatter(x,y,c='r',marker='s',s=60)  #分以“ID” 、“Income”字段为横、纵坐标，画红色方形60大小的散点图
ax.scatter(x,z,c='g',marker='o',s=60)  #分以“ID” 、“Sale”字段为横、纵坐标，画绿色圆形60大小的散点图
plt.savefig('实验二散点图.png')
plt.show()    #显示图像

#饼图
var = df.groupby(['Sex']).sum().stack()  #把数据按“sex”值分组，对其他字段值汇总，行变成列
t=var.unstack()    #再将var中的列变成行
type(t)    #返回t的数据类型
x = t ['Sales']    #取“Sale”字段的值给x
label1 = t.index   #t中索引值给label1
plt.axis('equal') #使 x轴和y轴的单位长度相同
plt.pie(x,labels=label1,autopct='%1.1f%%')#按比例画出饼图，并在外侧标注索引值，并用format格式输入百分比
plt.savefig('实验二饼图.png')
plt.show()    #显示图像

#气泡图
fig = plt.figure()  #创建一个绘图对象
bu = fig.add_subplot(1,1,1)    #设置画布
bu.scatter(df['Age'],df['Sales'],s=df['Income'])    #分以“Age” 、“Sale”字段为横、纵坐标，“Income”值为气泡大小画气泡图
plt.savefig('实验二气泡图.png')
plt.show()