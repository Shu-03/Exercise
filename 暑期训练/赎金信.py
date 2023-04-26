# 作者：shu qi
# 开发时间：2022/7/20 16:12

本题解答有错
'''给你两个字符串：ransomNote和magazine,判断
    ransomNote能不能由magazine里面的字符构成。
    如果可以，返回true;否则返回false。
    magazine里面的字符每次只能在ransomNote中使用一次。'''
#列表（线性列表）一种数据项构成的有限序列，即按照一定的线性序列，排列而成的数据项的集合。
#列表特征
#   顺序
#   长度可变
#常见形式数组和链表，栈和队列是两种特殊类型的列表。
#数组是列表的实现方式之一，一种数据结构。
#python数组（list）中的元素类型可以不保持一致。
#数组具有列表的特征，也有自己独有的特征
#如何从宏观上区分列表和数组？------索引（标识每项数据在数组中的具体位置）列表没有索引  这是数组与列表最大的不同。
#数组中的元素在内存中连续存储，每个元素占用相同大小的内存。
#相反列表的元素在内存中可能相邻，也可能不相邻。如列表的另一种实现方式---链表，它的元素在内存中则不一定相邻。
#数组的四种操作
#   读取元素---通过访问索引的方式读取。 找到索引0的内存地址后加上索引值，找到目标元素。时间复杂度O(1)
#   查找元素---逐步往后查找。 时间复杂度O(N)
#   插入元素
#   删除元素---时间复杂度O(N)
#python定义数组
#   直接定义---matrix=[0,1,2,3]
#   间接定义---matrix=[0 for i in range(4)]
#             print(matrix)         结果：[0,0,0,0]
#ransonNote=list(inpute("ransomNote:").split(','))
#定义两个字符串
ransonNote=input("ransomNote:")
magazine=input("magazine:")
#定义两个字典
dict1={}
dict2={}
#计算字典里key的value
for str in magazine:
    dict1[str]=magazine.count(str)
for str in ransonNote:
    dict2[str]=ransonNote.count(str)
for key1 in dict1:
    for key2 in dict2:
        if key2==key1:
            if dict2[key2]<=dict1[key1]:
                flig=True
            else:
                flig=False
        else:
            flig=False
print(flig)
#   print(f'{key}:{dict1[key]}')
#==>print('a={},b={},c={}'.format(a,b,c))
#{:nf}控制小数点位数
'''import numpy as np
a=np.sqrt(2)
b=np.sqrt(3)
c=np.sqrt(5)
print(f'a={a:1f},b={b:2f},c={c:3f}')'''

