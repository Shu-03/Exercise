# 作者：shu qi
# 开发时间：2022/9/27 14:55

#多次调用函数并不为默认值参数赋值，默认值参数只会在第一次调用时进行解释
#出现这种情况是因为列表、字典这种可变序列改变形参的值会改变实参的值。
'''def demo(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list
print(demo('5',[1,2,3,4]))        #[1, 2, 3, 4, '5']
print(demo('aaa',['a','b']))        #['a', 'b', 'aaa']
print(demo('a'))          #['a']
print(demo('b'))         #['a', 'b']
'''
def demo(newitem,old_list=None):
    if old_list is None:
        old_list=[]
    old_list.append(newitem)
    return old_list
print(demo('5',[1,2,3,4]))        #[1, 2, 3, 4, '5']
print(demo('aaa',['a','b']))        #['a', 'b', 'aaa']
print(demo('a'))          #['a']
print(demo('b'))          #['b']