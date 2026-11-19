# 作者：shu qi
# 开发时间：2023/5/9 9:07


'''
import jieba

txt = open('三国演义.txt', 'r', encoding='gbk').read()
words = jieba.lcut(txt)
count = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word, 0) + 1

items = list(count.items())
items.sort(key=lambda x: x[1], reverse=True)

for word in words:
    if len(word)==1:
        continue
    elif word=='孔明' or word=='孔明曰':
        word='诸葛亮'
    elif word=='关公' or word=='云长':
        word='关羽'
    elif word=='玄德' or word=='玄德曰':
        word='刘备'
    elif word == '曹躁' or word == '孟德曰':
        word = '曹操'
    elif word == '孟德' or word == '丞相':
        word = '曹操'
    else:
        word=word

ex={'将军','却说','丞相','二人','不可','荆州','不能','如此','商议','如何',\
    '主公','军士','左右','军马','引兵','次日','大喜','天下','东吴','于是',\
    '今日','不敢','魏兵','陛下','一人','都督','人马','不知'}
for word in ex:
    del count[word]


for i in range(20):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))
'''

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

txt = open('三国演义.txt', 'r', encoding='gbk').read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == '孔明' or word == '孔明曰':
        word = '诸葛亮'
    elif word == '关公' or word == '云长':
        word = '关羽'
    elif word == '玄德' or word == '玄德曰':
        word = '刘备'
    elif word == '曹躁' or word == '孟德曰':
        word = '曹操'
    elif word == '孟德' or word == '丞相':
        word = '曹操'
    else:
        word = word
    counts[word] = counts.get(word, 0) + 1

ex = {'将军', '却说','二人', '不可', '荆州', '不能', '如此', '商议', '如何', \
      '主公', '军士', '左右', '军马', '引兵', '次日', '大喜', '天下', '东吴', '于是', \
      '今日', '不敢', '魏兵', '陛下', '一人', '都督', '人马', '不知','汉中','众将',\
      '只见','后主','蜀兵','大叫','上马','此人','先主','太守','天子','后人',\
      '背后','城中','一面','何不','大军','忽报','先生','何故','然后','先锋','夫人',\
      '不如','赶来','原来','令人','江东','徐州','正是','忽然','下马','喊声','成都',\
      '因此','百姓','未知','大败','大事','引军','之后','一军','不见','起兵','接应',\
      '大惊','军中','心中','进兵','可以','大怒','以为','不得','下文','追赶','粮草',\
      '一声','分解','分付'}
for word in ex:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))

'''
f = open("三国人物出场次数.txt",'a',encoding='gbk')
for i in range(20):
    word,count = items[i]
    word = str(word)
    count = str(count)
    f.write(word)
    f.write(':')
    f.write(count)
    f.write('\n')
f.close()
'''
