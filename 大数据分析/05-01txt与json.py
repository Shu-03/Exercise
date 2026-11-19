# 作者：shu qi
# 开发时间：2023/4/25 8:56
import os
import json
#import xlwt

with open('city.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        with open('city.json','a',encoding='utf-8') as city_json:
            city_json.write(line)

'''
with open("city.txt",'r',encoding='utf-8') as f:
    with open('city.json', 'w', encoding='utf-8') as f1:
        f1.write(json.dumps(f.read()))

'''