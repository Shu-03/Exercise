# 作者：shu qi
# 开发时间：2023/3/14 8:22

#猜数字游戏，预设数字0-9
guess=0     #输入的数字
secret=7    #预设的数字
times=1     #猜数字的次数

print("---------------欢迎参加猜数字游戏，请开始---------------")
while guess!=secret:
    guess=int(input("@数字区间0-9，请输入你猜的数字："))
    print("你输入的数字是：",guess)
    if guess==secret:
        print("你猜了{}次，猜对了，真厉害".format(times))
    else:
        if guess<secret:
            print("你猜的数字小于正确答案")
        else:
            print("你猜的数字大于正确答案")
    times+=1
print("游戏结束")