# 作者：shu qi
# 开发时间：2023/6/4 14:36


import pandas as pd
from scipy import integrate


bj_data = pd.read_excel('2021年度北京上海全年天气质量数据.xlsx','北京2021年度全年空气质量数据')
sh_data = pd.read_excel('2021年度北京上海全年天气质量数据.xlsx','上海2021年度全年空气质量数据')

print(bj_data.isnull().sum())
print(sh_data.isnull().sum())

# 线性插值
bj_data_linear = bj_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='linear')
sh_data_linear = sh_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='linear')

# 多项式插值
bj_data_poly = bj_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='polynomial', order=2)
sh_data_poly = sh_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='polynomial', order=2)

# 样条插值
bj_data_spline = bj_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='spline', order=2)
sh_data_spline = sh_data[['PM2.5','PM10','So2','No2','Co','O3']].interpolate(method='spline', order=2)

# 读取原始数据
bj_data_original = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='北京2021年度全年空气质量数据')[['PM2.5','PM10','So2','No2','Co','O3']]
sh_data_original = pd.read_excel('2021年度北京上海全年天气质量数据（原.xlsx', sheet_name='上海2021年度全年空气质量数据')[['PM2.5','PM10','So2','No2','Co','O3']]




# 对比插补后的数据与原始数据是否一致
print('北京市线性插值后数据是否与原始数据一致：', bj_data_linear.equals(bj_data_original))
print('上海市线性插值后数据是否与原始数据一致：', sh_data_linear.equals(sh_data_original))
print('北京市多项式插值后数据是否与原始数据一致：', bj_data_poly.equals(bj_data_original))
print('上海市多项式插值后数据是否与原始数据一致：', sh_data_poly.equals(sh_data_original))
print('北京市样条插值后数据是否与原始数据一致：', bj_data_spline.equals(bj_data_original))
print('上海市样条插值后数据是否与原始数据一致：', sh_data_spline.equals(sh_data_original))

