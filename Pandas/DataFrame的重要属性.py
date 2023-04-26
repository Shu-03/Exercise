# 作者：shu qi
# 开发时间：2022/9/27 20:34
import pandas as pd
#列表方式创建DataFrame
data=[["小太阳",320.9,100],["鼠标",150.3,50],["小刀",1.5,200]]
columns=['名称','单价','数量']
df=pd.DataFrame(data=data,columns=columns)
print(df)
print("查看所有元素的值\n",df.values)
print("查看所有元素的类型\n",df.dtypes)
print("查看所有行名称（索引）\n",df.index)
print("查看所有行名称（索引）\n",list(df.index))

#行列转换
new_df=df.T
print(new_df)
pd.set_option("display.unicode.east_asian_width",True)#规整格式
print(new_df)

#查看前后N条数据
print("查看前N条数据\n",df.head(1))
print("查看后N条数据\n",df.tail(1))

#查看几行几列，shape[0]表示行，shape[1]表示列
print("行",df.shape[0],"列",df.shape[1])

print("查看索引、数据类型、内存等所有信息\n",df.info)