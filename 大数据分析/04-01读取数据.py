import csv

filename = r'C:/Users/Shu/Documents/大学/大数据分析/2009106042/学生信息表.csv'
'''
with open(filename) as f:
    reader = csv.reader(f)
    header  = next(reader)
    for item in reader:
        print(item)


with open(filename,'a') as f:
    writer = csv.writer(f)
    writer.writerow(['2009105070', '赵四', '女', '20数据2'])

with open(filename) as f:
    reader = csv.reader(f)
    header  = next(reader)
    for item in reader:
        print(item)
'''
import json
filename = r'C:/Users/Shu/Documents/大学/大数据分析/2009106042/学生信息表.csv'
ls = []
with open(filename)as f:
    for line in f:
        line = line.replace("\n","")
        ls.append(line.split(","))

fw = open(r'C:/Users/Shu/Documents/大学/大数据分析/2009106042/学生信息表.json','w',encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))

a=json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
fw.write(a)
fw.close()