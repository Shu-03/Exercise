# 作者：shu qi
# 开发时间：2023/4/11 10:40

import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.12022 SLBChan/30'
}

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8090255589137196110&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%8E%9F%E7%A5%9E%E5%9B%BE%E7%89%87&queryWord=%E5%8E%9F%E7%A5%9E%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a&1681180734020='

response = requests.get(url,headers=headers)


d = response.json()

#print(d)

import os
if not os.path.exists('yuanshen'):
    os.mkdir('yuanshen')
ys_list = d['data']

for ysimg in ys_list:
    name = ysimg['fromPageTitle']
    img = ysimg['hoverURL']

    #下载图片
    from urllib import request
    request.urlretrieve(img,f'yuanshen/{name}.png')
