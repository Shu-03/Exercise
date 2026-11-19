# 作者：shu qi
# 开发时间：2023/6/4 20:00


import pandas as pd
bj_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='北京2021年度全年空气质量数据')
sh_data = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='上海2021年度全年空气质量数据')
gz_data = pd.read_excel('2021年度广州市全年天气质量数据.xlsx')[['日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]

bj_monthly_avg = bj_data.groupby(bj_data['日期'].dt.month).mean()
sh_monthly_avg = sh_data.groupby(sh_data['日期'].dt.month).mean()
gz_monthly_avg = gz_data.groupby(gz_data['日期'].dt.month).mean()

# 输出结果
print('北京市2021年度1~12月各项指标每个月的平均值：')
print(bj_monthly_avg)
print('上海市2021年度1~12月各项指标每个月的平均值：')
print(sh_monthly_avg)
print('广州市2021年度1~12月各项指标每个月的平均值：')
print(gz_monthly_avg)

# 生成北京、上海、广州2021年度1~12月各月空气质量指数AQI_PM2.5历史数据
bj_aqi_pm25 = bj_data[['AQI指数', 'PM2.5']]
sh_aqi_pm25 = sh_data[['AQI指数', 'PM2.5']]
gz_aqi_pm25 = gz_data[['AQI指数', 'PM2.5']]
bj_aqi_pm25.to_csv('北京市2021年度1~12月各月空气质量指数AQI_PM2.5历史数据.csv')
sh_aqi_pm25.to_csv('上海市2021年度1~12月各月空气质量指数AQI_PM2.5历史数据.csv')
gz_aqi_pm25.to_csv('广州市2021年度1~12月各月空气质量指数AQI_PM2.5历史数据.csv')
