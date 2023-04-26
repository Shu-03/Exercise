# 作者：shu qi
# 开发时间：2022/9/7 16:50
#导入模块
from matplotlib import pyplot as plt
import numpy as np
#创建0-10之间100个等差数
x=np.linspace(0,10,100)
#使用subplot划分画布 2行2列 画在区1
plt.subplot(2,2,1)
plt.plot(x,np.sin(x))
#画在区3
plt.subplot(2,2,3)
plt.plot(x,np.cos(x))
#显示图
plt.show()