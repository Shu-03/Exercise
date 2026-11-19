# 作者：shu qi
# 开发时间：2023/6/5 19:31
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
total_score= pd.read_excel("综合成绩.xlsx")
total_score.set_index('学号',inplace=True)
exam_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='期末成绩',header=1);
exam_data.drop_duplicates(subset = '学号',inplace = True)
exam_data.set_index('学号', inplace=True)
bins = [0, 60, 70, 80, 90, 100]
labels = ['不及格', '及格', '中', '良', '优']
exam_data['等级'] = pd.cut(exam_data['期末成绩'], bins=bins, labels=labels)
total_score['等级'] = pd.cut(total_score['综合成绩'], bins=bins, labels=labels)
df_count = pd.DataFrame()
df_count['期末成绩'] =exam_data.groupby('等级')['姓名'].count()
df_count['综合成绩'] = total_score.groupby('等级')['姓名'].count()
print(df_count)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.pie(df_count['期末成绩'], labels=labels, autopct='%1.1f%%')
ax1.set_title('全班期末成绩等级分布')
ax2.pie(df_count['综合成绩'], labels=labels, autopct='%1.1f%%')
ax2.set_title('全班综合成绩等级分布')
plt.show()