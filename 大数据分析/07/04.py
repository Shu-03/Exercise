# 作者：shu qi
# 开发时间：2023/6/4 20:40


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

bj_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='北京2021年度全年空气质量数据')
# 提取需要的列
bj= bj_data[['日期', 'PM2.5', 'PM10', 'So2', 'No2']]

# 将日期列转换为月份列
bj['月份'] = pd.to_datetime(bj['日期']).dt.month

# 按月份和指标分组，计算均值
grouped_bj =bj.groupby(['月份']).mean()

# 绘制折线图
plt.plot(grouped_bj.index, grouped_bj['PM2.5'], label='PM2.5')
plt.plot(grouped_bj.index, grouped_bj['PM10'], label='PM10')
plt.plot(grouped_bj.index, grouped_bj['So2'], label='So2')
plt.plot(grouped_bj.index, grouped_bj['No2'], label='No2')

# 添加图例和标签
plt.legend()
plt.xlabel('月份')
plt.ylabel('空气质量指数')
plt.title('2021年北京空气质量指数对比')
# 显示图像
plt.show()


sh_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='上海2021年度全年空气质量数据')
sh= sh_data[['日期', 'PM2.5', 'PM10', 'So2', 'No2']]

# 将日期列转换为月份列
sh['月份'] = pd.to_datetime(sh['日期']).dt.month

# 按月份和指标分组，计算均值
grouped_sh =sh.groupby(['月份']).mean()

# 绘制折线图
plt.plot(grouped_sh.index, grouped_sh['PM2.5'], label='PM2.5')
plt.plot(grouped_sh.index, grouped_sh['PM10'], label='PM10')
plt.plot(grouped_sh.index, grouped_sh['So2'], label='So2')
plt.plot(grouped_sh.index, grouped_sh['No2'], label='No2')

# 添加图例和标签
plt.legend()
plt.xlabel('月份')
plt.ylabel('空气质量指数')
plt.title('2021年上海空气质量指数对比')
# 显示图像
plt.show()

gz_data = pd.read_excel('2021年度广州市全年天气质量数据.xlsx')[['日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
gz= gz_data[['日期', 'PM2.5', 'PM10', 'SO2', 'NO2']]

# 将日期列转换为月份列
gz['月份'] = pd.to_datetime(gz['日期']).dt.month

# 按月份和指标分组，计算均值
grouped_gz =gz.groupby(['月份']).mean()

# 绘制折线图
plt.plot(grouped_gz.index, grouped_gz['PM2.5'], label='PM2.5')
plt.plot(grouped_gz.index, grouped_gz['PM10'], label='PM10')
plt.plot(grouped_gz.index, grouped_gz['SO2'], label='SO2')
plt.plot(grouped_gz.index, grouped_gz['NO2'], label='NO2')

# 添加图例和标签
plt.legend()
plt.xlabel('月份')
plt.ylabel('空气质量指数')
plt.title('2021年广州市空气质量指数对比')
# 显示图像
plt.show()