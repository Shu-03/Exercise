# 作者：shu qi
# 开发时间：2023/5/9 9:45
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"]=False


fr = open('三国人物出场次数.txt','r',encoding='gbk')
dic = {}
keys = []
for line in fr:
    v = line.strip().split(':')
    dic[v[0]] = v[1]
    keys.append(v[0])
fr.close()

list_name = list(dic.keys())
list_name_times = list(dic.values())
list_name_times = list(map(int,list_name_times))

for i in range(len(list_name)):
    plt.bar(list_name[i],list_name_times[i])
plt.title("三国人物出场次数")
plt.xlabel("姓名")
plt.ylabel("次数")
plt.show()

from pyecharts.charts import wordcloud
dic = dict(zip(list_name,list_name_times))
wc = WordCloud(font_path="C:\Windows\Fonts\msyh.ttc",width=500,height=400,mode="RGBA",background_color=None).fit_words(dic)
plt.imshow(wc)
plt.axis("off")
plt.show()
