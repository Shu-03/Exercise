# 作者：shu qi
# 开发时间：2023/6/5 15:25

import pandas as pd
import numpy as np

# 读取考勤数据
attendance_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='考勤情况统计',header=1);
#print(attendance_data.head())
# 删除重复值
attendance_data.drop_duplicates(subset = '学号', inplace = True)
#处理缺失值和异常值
mean_absent = attendance_data['缺勤'].mean()
attendance_data['缺勤'] = attendance_data['缺勤'].fillna(mean_absent).clip(lower=0)
attendance_data['缺勤'] = attendance_data['缺勤'].where(attendance_data['缺勤'] <= 16, mean_absent)
# 处理缺勤情况
attendance_data['attendance_score'] = 100 - attendance_data['缺勤'] * 5
attendance_data.set_index('学号', inplace=True)
print(attendance_data)

# 处理作业数据
homework_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='作业情况统计',header=1);
# 删除重复值
homework_data.drop_duplicates(subset='学号',inplace=True)
print(homework_data.shape)
# 处理异常值
for col in homework_data.columns[2:]:
    homework_data[col] = pd.to_numeric(homework_data[col], errors='coerce')  # 将字符串转换为数字，无法转换的设为缺失值
    mean = homework_data[col].mean()
    homework_data[col] = homework_data[col].apply(lambda x: mean if x < 0 or x > 100 or pd.isna(x) else x)
# 将异常值用均值填充
for col in homework_data.columns[2:]:
    mean = homework_data[col].mean()
    homework_data[col] = homework_data[col].apply(lambda x: mean if x < 0 or x > 100 else x)
homework_data['Average'] = homework_data[['作业1', '作业2', '作业3', '作业4', '作业5', '作业6', '作业7']].mean(axis=1)
homework_data.set_index('学号', inplace=True)
print(homework_data)

# 处理实验数据
experiment_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='实验情况统计',header=1);
# 删除重复值
experiment_data.drop_duplicates(subset='学号',inplace=True)
print(experiment_data.shape)
# 处理异常值
for col in experiment_data.columns[2:]:
    experiment_data[col] = pd.to_numeric(experiment_data[col], errors='coerce')  # 将字符串转换为数字，无法转换的设为缺失值
    mean = experiment_data[col].mean()
    experiment_data[col] = experiment_data[col].apply(lambda x: mean if x < 0 or x > 100 or pd.isna(x) else x)
# 将异常值用均值填充
for col in experiment_data.columns[2:]:
    mean =experiment_data[col].mean()
    experiment_data[col] = experiment_data[col].apply(lambda x: mean if x < 0 or x > 100 else x)
experiment_data['Average'] = experiment_data[['实验1', '实验2', '实验3', '实验4', '实验5', '实验6', '实验7','实验8']].mean(axis=1)
experiment_data.set_index('学号', inplace=True)
print(experiment_data)

#处理期末成绩数据
exam_data = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='期末成绩',header=1);
#print(attendance_data.head())
# 删除重复值
exam_data.drop_duplicates(subset = '学号',inplace = True)
exam_data.set_index('学号', inplace=True)
print(exam_data.shape)
print(exam_data.isnull().sum())

df_total = pd.DataFrame()
df_total['姓名'] = attendance_data['姓名']
df_total['综合成绩'] = attendance_data['attendance_score'] * 0.1 + homework_data['Average'] * 0.1 +experiment_data['Average']* 0.2 + exam_data['期末成绩'] * 0.6
print(df_total)
df_total.to_excel("综合成绩.xlsx")

'''
import pandas as pd

# 读取excel文件
df_attendance = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='考勤情况统计',header=1)
df_homework = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='考勤情况统计',header=1)
df_experiment = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='考勤情况统计',header=1)
df_exam = pd.read_excel('《计算机网络》课程成绩数据.xlsx', sheet_name='考勤情况统计',header=1)

# 处理重复值
df_attendance.drop_duplicates(inplace=True)
df_homework.drop_duplicates(inplace=True)
df_experiment.drop_duplicates(inplace=True)
df_exam.drop_duplicates(inplace=True)

# 处理异常值
df_attendance['考勤'] = df_attendance['考勤'].apply(lambda x: 100 if x > 100 else x)
df_attendance['考勤'] = df_attendance['考勤'].apply(lambda x: x - 5 * (20 - x) if x < 80 else x)
df_homework.replace(0, pd.NaT, inplace=True)
df_homework.fillna(df_homework.mean(), inplace=True)
df_experiment.replace(0, pd.NaT, inplace=True)
df_experiment.fillna(df_experiment.mean(), inplace=True)

# 计算综合成绩
df_attendance.set_index('学号', inplace=True)
df_homework.set_index('学号', inplace=True)
df_experiment.set_index('学号', inplace=True)
df_exam.set_index('学号', inplace=True)
df_total = df_attendance * 0.1 + df_homework * 0.1 + df_experiment * 0.2 + df_exam * 0.6
df_total.reset_index(inplace=True)

# 输出结果
print(df_total)
'''