# 作者：shu qi
# 开发时间：2022/9/27 20:58
import pandas as pd
data=[["小太阳",320.9,100],["鼠标",150.3,50],["小刀",1.5,200]]
columns=['名称','单价','数量']
df=pd.DataFrame(data=data,columns=columns)

#describe()函数
print(df.describe())
'''
   单价          数量
count    3.000000    3.000000
mean   157.566667  116.666667
std    159.823945   76.376262
min      1.500000   50.000000
25%     75.900000   75.000000
50%    150.300000  100.000000
75%    235.600000  150.000000
max    320.900000  200.000000

'''
#count() 返回非空值的个数
print(df.count())

#sum()
print(df.sum())
'''
名称    小太阳鼠标小刀
单价      472.7
数量        350
dtype: object
'''

#max() 获得每列最大值
print(df.max())
'''
名称       鼠标
单价    320.9
数量      200
dtype: object
'''