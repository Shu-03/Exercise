# 作者：shu qi
# 开发时间：2023/5/8 19:32

import json

# 主程序，执行入口
if __name__ == '__main__':
    # try except Python的异常处理机制
    try:
        # with Python中的上下文管理器，会帮我们释放资源，比如 关闭文件句柄
        # open 函数为Python内建的文件读取函数，r代表只读
        with open(r'C:\Users\Shu\Documents\大学\大数据分析\2009106042\学生信息表.json', 'r',encoding='utf-8') as f:
            # 解析一个有效的JSON字符串并将其转换为Python字典
            data = json.loads(f.read())
        # 使用 ，连接列表中的值
        # data[0]是一个字典类型，一个星号代表展开键，两个星号（**）代表展开字典的值
        output = ','.join([*data[0]])
        # 遍历 字典列表data
        for obj in data:
            # 将结果转化为字符串，累加到output中
            # f 为f-string格式化，将大括号中的表达式替代
            output += f'\n{obj["姓名"]},{obj["学号"]},{obj["性别"]}，{obj["班级"]}'
        # 将结果写到到output.csv中
        with open(r'C:\Users\Shu\Documents\大学\大数据分析\2009106042\学生信息表.xlsx', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')