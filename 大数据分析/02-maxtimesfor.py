# 作者：shu qi
# 开发时间：2023/3/14 8:47

import random

guess=0     #输入的数字
times=1     #猜数字的次数
secret=random.randint(0,100)

maxtimes=6

print("---------------欢迎参加猜数字游戏，请开始---------------")
print("本次游戏猜数字的最大次数为{}".format(maxtimes))
for i in range(maxtimes):
    guess = int(input("@数字区间0-100，请输入你猜的数字："))
    if guess==secret:
        print("你猜了{}次，猜对了，真厉害".format(times))
        break;
    else:
        if guess<secret:
            print("你猜的数字小于正确答案,你还剩{}次机会".format(maxtimes-times))
        else:
            print("你猜的数字大于正确答案,你还剩{}次机会".format(maxtimes-times))
    times+=1
print("游戏结束")