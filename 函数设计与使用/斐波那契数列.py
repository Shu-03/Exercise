# 作者：shu qi
# 开发时间：2022/9/27 14:17
'''
def 函数名（[参数列表]）:
    注释
    函数体
'''
def fib(n):
    '''accept an integer n.
        return the numbers less than n in Fibonacci sequence'''
    a,b=1,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
print(fib(1000))