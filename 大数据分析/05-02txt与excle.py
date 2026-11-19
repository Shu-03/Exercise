# 作者：shu qi
# 开发时间：2023/5/8 17:12

import ast
import json

import xlwt

import re
import pandas as pd

f = open("city.txt",'r',encoding='utf-8').read()
label = re.findall(r'label": "[\u4e00-\u9f5a]*',f)

print(len(label))
print (label)
value= re.findall(r'\d+',f)
print (len(value))
df1 = pd.DataFrame({'label':label,'value':value})
df1.to_excel('city_txt.xlsx')

