# 作者：shu qi
# 开发时间：2022/11/22 14:32

import csv
import matplotlib.pyplot as plt
filename = "(ch-3.2.2)world-population.csv"
datax = []
datay = []

'''with open() as f: 用法
        with open(r'filename.txt') as f:
            for l in f :
                l=json.loads(l)#文件的读操作
        with open('hello.txt','w') as f:
            f.write('hello world') #文件的写操作
r:只读方式打开文本，rb:以二进制格式打开一个文件用于只读，r+:打开一个文件用于读写，文件指针放在文件的开头，
rb+:二进制，读写，指针在开头，w:打开写入文件，会覆盖，无则创建，wb:二进制，写入，覆盖，,无则创建w+:用于读写，覆盖，
无则创建，wb+:二进制，读写，覆盖，无则创建，a:打开一个文件用于追加写入，有内容指针在文尾，无则创建，ab:二进制，追加写入，
指针在尾，无则创建，a+:追加读写，有内容指针在文尾，无则创建，ab+:二进制，追加读写，指针在尾，无则创建。'''
with open(filename) as f:
    reader =csv.reader(f)
    print(reader)   #结果：<_csv.reader object at 0x00000228263725E0>
    #reader 中存放的是列表类型数据，可以理解为列表嵌套列表的对象
    for datarow in reader: #将每个列表取出，也就是取出每行数据 datarow=['Year','population']
        #print(datarow)

        if reader.line_num !=1:  #跳过第一行属性名
            print(reader.line_num,datarow)  #reader.line_num：行号
            #datarow = list(map(int, datarow)) #将表格内的str类型转换为int类型
            datax.append(int(datarow[0]))
            datay.append(int(datarow[1]))
            #print(type(datarow[1]))

plt.plot(datax,datay)
plt.show()