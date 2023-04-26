# 作者：shu qi
# 开发时间：2022/9/27 14:34
#默认值参数
def say(message,times=1):
    print((message+' ')*times)

print(say.__defaults__)         #(1,)
print(say("hello"))            #hello
print(say('hello',3))           #hello hello hello
print(say('hi',7))             #hi hi hi hi hi hi hi