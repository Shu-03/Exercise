# 作者：shu qi
# 开发时间：2023/3/14 8:36

import random
def GuessSecret(maxtimes):
    guess = 0
    times = 1
    secret = random.randint(0, 100)

    print("-----------------------------------------------------------------")
    print("----                                                         ----")
    print("----                欢迎参加猜数字游戏，请开始                ----")
    print("----                                                         ----")
    print("-----------------------------------------------------------------")
    while guess != secret:
        guess = int(input("@数字区间0-100，请输入你猜的数字："))
        print("你输入的数字是：", guess)
        if guess == secret:
            print("你猜了{}次，猜对了，真厉害".format(times))
        else:
            if guess < secret:
                print("你猜的数字小于正确答案")
            else:
                print("你猜的数字大于正确答案")
        times += 1
        if(times>maxtimes):
            print("你猜的次数为{}，达到了最大次数".format(times))
            break
    print("游戏结束")

maxts=eval(input("@请输入猜数字的最大次数："))
GuessSecret(maxts)