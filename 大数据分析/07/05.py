# 作者：shu qi
# 开发时间：2023/6/4 20:57


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
bj_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='北京2021年度全年空气质量数据')
sh_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='上海2021年度全年空气质量数据')
gz_data = pd.read_excel('2021年度广州市全年天气质量数据.xlsx')[['日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]


bj_data['城市'] = '北京'
sh_data['城市'] = '上海'
gz_data['城市'] = '广州'
# 合并数据
df = pd.concat([bj_data, sh_data,gz_data])

# 筛选出2021年6月份的数据
df_june = df[df['日期'].dt.month == 6]

# 绘制柱状图
plt.bar(df_june['城市'], df_june['PM2.5'])
plt.title('2021年6月份三个城市PM2.5指标变化对比')
plt.xlabel('城市')
plt.ylabel('PM2.5')
plt.show()