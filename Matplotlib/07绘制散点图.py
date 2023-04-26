# 作者：shu qi
# 开发时间：2022/9/10 17:16
import matplotlib.pyplot as plt
import numpy as np
#创建x y
x=np.linspace(0,10,100)
sin_y=np.sin(x)
#plot绘制图
#plt.plot(x,sin_y,'o')
#scatter绘制图
plt.scatter(x,sin_y)
#显示图
plt.show()
"""
plot与scatter都可以绘制散点图，且plot绘制的速度优于scatter，但是scatter能绘制有差异的散点
"""

