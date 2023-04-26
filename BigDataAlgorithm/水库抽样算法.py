# 作者：shu qi
# 开发时间：2022/9/12 19:21
import random
n=10
k=5
datas=[i for i in range(0,n)]
samples=datas[0:k]
for i in range(k+1,n):
    j=random.randint(0,i)
    if j<k:
        samples[j]=datas[i]