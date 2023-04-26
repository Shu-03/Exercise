# 作者：shu qi
# 开发时间：2023/4/10 18:52

import requests

#模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

#request:请求
#response:响应
response = requests.get('https://www.qq.com',headers=headers)
print(response.text)

