# 作者：shu qi
# 开发时间：2022/6/25 10:43

#转义字符的使用

print("hello\nworld")# \ + 转义功能的首字母  n-->newline
print("hello\tworld") # t-->table 水平制表符 有三个空格
print("helloooo\tworld")#四个空格
print("hello\rworld")#world 把 hello 覆盖了  r-->return 回车
print("hello\bworld")#hellworld

print("http:\\www.baidu.com")
print("http:\\\\www.baidu.com")
print("\"哇！\"，\"天气真好！\"")
#原字符r/R,使转义字符不起作用的字符
print(r"hello\nworld")