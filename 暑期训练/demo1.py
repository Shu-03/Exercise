# 作者：shu qi
# 开发时间：2022/6/25 10:21

#print()函数的应用

#输出数字
print(790)
print(64.73)

#输出字符串
print('helloworld')
print("helloworld")
print('''helloworld''')

#输出带有运算符的表达式（表达式=操作数+运算符）
print(5+3)
print(6*3)

#结果输出在文件中
#'a+':没有文件创建文件，有文件在文件内容后面追加
fp=open('D:/PythonDemo/Exercise/暑期训练/demo1text.txt','a+')
print("helloworld",file=fp)
fp.close()


#输出在同一行
print('你好','世界',)