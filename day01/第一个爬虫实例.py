#导入模块，从urllib(网络库)里的request(请求)中找到urlopen.
#输入百度网址

from urllib.request import urlopen
url = "http://www.baidu.com"
resp = urlopen(url)


with open("mybaidu.html",mode="w",encoding="utf_8") as f:
    f.write(resp.read().decode("utf-8"))

print("over!")