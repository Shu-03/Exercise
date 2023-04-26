# 作者：shu qi
# 开发时间：2022/9/7 16:29
#导入matplotlib模块
import matplotlib.pyplot as plt
#生成200个点
x=range(-100,100)
y=[i**2 for i in x]
#绘制图
plt.plot(x,y)
#保存图
plt.savefig("04result")#默认是png格式
plt.savefig("04result.jpg")
#显示图
plt.show()