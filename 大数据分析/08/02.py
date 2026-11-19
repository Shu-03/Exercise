# 作者：shu qi
# 开发时间：2023/6/5 19:22
import pandas as pd

df_score = pd.read_excel("综合成绩.xlsx")

bins = [0, 60, 70, 80, 90, 100]
labels = ['不及格', '及格', '中', '良', '优']
df_score['等级'] = pd.cut(df_score['综合成绩'], bins=bins, labels=labels)
df_count = df_score.groupby('等级')['学号'].count()
print(df_count)