# 作者：shu qi
# 开发时间：2022/9/11 10:37
import matplotlib.pyplot as plt
import numpy as np
#创建x y
np.random.seed(0)
x=np.random.rand(100)#100个0.0到1.0之间点
y=np.random.rand(100)
#10种大小
#ValueError: s must be a scalar, or float array-like with the same size as x and y
#10种大小报错,大小种类得与x y相同
size=np.random.rand(100)*1000
#100种颜色
color=np.random.rand(100)
#绘制图
plt.scatter(x,y,s=size,c=color,alpha=0.7) #s 大小  c 颜色  alpha 透明度
#显示图
plt.show()