# 作者：shu qi
# 开发时间：2022/10/15 15:43
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
sns.set_style('whitegrid', {'font.sans-serif': ['simhei', 'Arial']})

df_train = pd.read_csv('http://fdp.csmar.com:7092/group1/M00/10/2C/wKhlJmMqhc6AW8ltAAEIlAciyjo965.csv',index_col=0)

#print(df_train.info())
#print(df_train.isna().sum())

#切片
X=df_train.iloc[:,:-1]
Y=df_train.iloc[:,-1]
import numpy as np
size=np.arange(0.6,1,0.1)
scorelist=[[],[],[],[],[],[]]
for i in range(0,4):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=size[i],random_state=5)
    #tree
    tree=DecisionTreeClassifier().fit(X_train,Y_train)
    tree_pred=tree.predict(X_test)
    tree_score=accuracy_score(Y_test,tree_pred)
    scorelist[0].append(tree_score)

    #Knn
    Knn=KNeighborsClassifier().fit(X_train,Y_train)
    Knn_pred=Knn.predict(X_test)
    Knn_score=accuracy_score(Y_test,Knn_pred)
    scorelist[1].append(Knn_score)

    #LR
    lr=LogisticRegression().fit(X_train,Y_train)
    lr_pred=lr.predict(X_test)
    lr_score=accuracy_score(Y_test,lr_pred)
    scorelist[2].append(lr_score)

    #Random_Forest
    from sklearn.ensemble import RandomForestClassifier
    forest=RandomForestClassifier().fit(X_train,Y_train)
    forest_pred=forest.predict(X_test)
    forest_score=accuracy_score(Y_test,forest_pred)
    scorelist[3].append(forest_score)

    #SVC
    from sklearn.svm import SVC
    svc=SVC().fit(X_train,Y_train)
    svc_pred=svc.predict(X_test)
    svc_score=accuracy_score(Y_test,svc_pred)
    scorelist[4].append(svc_score)

    #Bayes
    from sklearn.naive_bayes import GaussianNB
    bayes=GaussianNB().fit(X_train,Y_train)
    bayes_pred=bayes.predict(X_test)
    bayes_score=accuracy_score(Y_test,bayes_pred)
    scorelist[5].append(bayes_score)

color_list=('red','blue','lightgreen','yellow','cornflowerblue','black')
for i in range(0,6):
    plt.plot(size,scorelist[i],color=color_list[i])
plt.legend(['tree','Knn','LR','RandomForest','SVC','Bayes'])
plt.xlabel('训练集占比')
plt.ylabel('准确率')
plt.title('不同模型随着训练集占比变化曲线')
plt.show()

