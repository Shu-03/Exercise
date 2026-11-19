# 作者：shu qi
# 开发时间：2023/9/23 15:26
import PyPDF2

local = r'D:\PythonDemo\Exercise\数据挖掘'
pdf_file = open("Fake News Identification Using Regression Analysi.pdf","rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)
# 遍历每一页
for page_num in range(num_pages):
    # 获取当前页对象
    page_obj = pdf_reader.pages[page_num]
    # 获取当前页中的所有对象
    page_objs = page_obj['/Resources']['/XObject'].get_object()
    # 遍历每个对象
    for obj_name in page_objs:
        # 判断对象是否为图片
        if page_objs[obj_name]['/Subtype'] == '/Image':
            # 获取图片对象
            img_obj = page_objs[obj_name]
            # 获取图片数据
            img_data = img_obj.get_data()
            # 将图片数据保存为文件
            with open(local+obj_name + '.jpg', 'wb') as img_file:
                img_file.write(img_data)