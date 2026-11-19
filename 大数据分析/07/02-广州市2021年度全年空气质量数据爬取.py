# 作者：shu qi
# 开发时间：2023/6/4 17:47
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义爬虫函数


def get_data(city,i):

    url = f'http://www.tianqihoubao.com/aqi/{city}-2021{i}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    df = df.drop(df.index[0])
   #
    #df.set_index('日期', inplace=True)

    return df

gz_data = get_data("guangzhou","01")
gz_data.columns = ['日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
print(gz_data)
for i in range(11):
    dic = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    df = get_data("guangzhou",dic[i])
    gz_data = gz_data.append(df)
gz_data['日期'] = pd.to_datetime(gz_data['日期'])
gz_data.to_excel("2021年度广州市全年天气质量数据.xlsx",index=False)