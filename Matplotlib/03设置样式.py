# 作者：shu qi
# 开发时间：2022/9/7 16:03
#导入matplotlib模块
import matplotlib.pyplot as plt
#准备x y
x=[1,2,3,4,5]
y=[1,4,9,16,25]
#绘制折线
#linewidth属性来设置折线的宽度
plt.plot(x,y,linewidth=5)
#添加x y轴名称
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
#添加标题
plt.title("多个点绘制折线图")
#显示图
plt.show()