#print("请输入一个100~999的数字:")
x=int(input('请输入一个100~999的数字:'))
#x = input()
#int a =(x % 10)
#int b =( (x/10)%10)
#int c =(x/100)
#a=(int)(x%10)
#b=(int)(x/10)%10
#c=(int)(x/100)

if x==(x%10)**3+((int)(x/10)%10)**3+((int)(x/100))**3:
    print("是水仙花数")
else:
    print("不是水仙花数")
