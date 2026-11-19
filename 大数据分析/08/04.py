# 作者：shu qi
# 开发时间：2023/6/5 19:52

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
total_score= pd.read_excel("综合成绩.xlsx")
exam_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='期末成绩',header=1);
exam_data.drop_duplicates(subset = '学号',inplace = True)
# 以学号为横轴，以期末考试成绩为纵轴生成散点图
plt.scatter(exam_data['学号'], exam_data['期末成绩'])
plt.xlabel('学号')
plt.ylabel('期末考试成绩')
plt.show()

# 以学号为横轴，以综合成绩为纵轴生成散点图
plt.scatter(total_score['学号'], total_score['综合成绩'])
plt.xlabel('学号')
plt.ylabel('综合成绩')
plt.show()