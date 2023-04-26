# 作者：shu qi
# 开发时间：2022/9/29 9:29


import io
import pandas as pd

t="""index,a,b
hi,hello,pandas"""
#当index_col为None(即默认)
pd.set_option("display.unicode.east_asian_width",True)
df1=pd.read_csv(io.StringIO(t))
print(df1)
""" index      a       b
0    hi  hello  pandas"""
#df1.to_csv("D:\\df1.csv")
#当index_col=0
df2=pd.read_csv(io.StringIO(t),index_col=0)
print(df2)
"""  
         a       b
index               
hi     hello  pandas"""
#df2.to_csv("D:\\df2.csv")

#当index_dol=False时，主要用于格式错误的文件中，比如文件每行末尾有分隔符，可用False
#强制不使用第一列作为索引，同时丢弃最后一列

p="""index,a,b
hi,hello,pandas,"""
df_None=pd.read_csv(io.StringIO(p))
print(df_None)
"""
    index       a   b
hi  hello  pandas NaN
"""
df_0=pd.read_csv(io.StringIO(p),index_col=0)
print(df_0)
"""
    index       a   b
hi  hello  pandas NaN
"""
df_False=pd.read_csv(io.StringIO(p),index_col=False)
print(df_False)
"""
  index      a       b
0    hi  hello  pandas
"""