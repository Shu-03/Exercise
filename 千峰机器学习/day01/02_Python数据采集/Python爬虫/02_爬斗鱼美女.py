# 作者：shu qi
# 开发时间：2023/4/10 19:25

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def douyu(page=1):

    url = f'https://www.douyu.com/wgapi/ordnc/live/web/room/yzList/{page}'


    response = requests.get(url,headers=headers)
    #print(type(response.text)) #json字符串

    #json解析：josn字符串==>json字典
    d = response.json()
    #print(d)

    #自动创建文件夹

    import os

    if not os.path.exists('douyu'):
        os.mkdir('douyu')

    #拿到所有的主播
    meinv_list=d['data']['rl']
    #遍历每一个美女
    for meinv in meinv_list:
        name = meinv['nn'] #拿到名字
        img = meinv['rs16'] #图片url

        #print(name,img)

        #下载图片
        from urllib import request
        request.urlretrieve(img,f'douyu/{name}.png')


#爬取4页
douyu(1)
douyu(2)
douyu(3)
douyu(4)