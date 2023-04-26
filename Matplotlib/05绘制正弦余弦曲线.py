# 作者：shu qi
# 开发时间：2022/9/7 16:34
#导入matplotlib numpy模块
from matplotlib import pyplot as plt
import numpy as np
#从0-10之间中找到100个等差数列值
x=np.linspace(0,10,100)
sin_y=np.sin(x)
cos_y=np.cos(x)
#绘制图
plt.plot(x,sin_y)
plt.plot(x,cos_y)
#保存图
plt.savefig("sin_cos.jpg")
#显示图
plt.show()