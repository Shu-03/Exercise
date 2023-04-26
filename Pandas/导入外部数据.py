# 作者：shu qi
# 开发时间：2022/9/27 21:07
#导入包
import pandas as pd
#导入excel文件
#df=pd.read_excel(r"D:\TableauDataset\2014年各省市售电量.xlsx")
#print(df)

#导入多列数据  usecols=[]
pd.set_option("display.unicode.east_asian_width",True)
df=pd.read_excel(r"D:\TableauDataset\2014年各省市售电量.xlsx",usecols=['省市','用电类别','当期值'])
print(df)

