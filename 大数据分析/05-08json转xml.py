# 作者：shu qi
# 开发时间：2023/5/9 0:14

import os
import cv2
import json


def json_to_xml(data, img_path, xml_path):
    # 1.字典对标签中的类别进行转换
    dict = {
        '0': "background",
        '1': "Broken bottle cap",
        '2': "Bottle cap deformation",
        '3': "Broken edge of bottle cap",
        '4': "Bottle cap spinning",
        '5': "Cap breakpoint",
        '6': "Label skew",
        '7': "Label wrinkled",
        '8': "Label bubble",
        '9': "Code spraying is normal",
        '10': "Code spraying is not normal"
    }
    # 用于存储 "老图"
    pre_img_name = ''
    # 3.遍历文件夹
    for id, name in data_dic.items():
        print(name)
        img_name = name[:-4]
        pic = cv2.imread(img_path + name)
        # 获取图像大小信息
        Pheight, Pwidth, Pdepth = pic.shape
        for ann in data['annotations']:
            if id == ann['image_id']:
                # 遇到的是一张新图片
                if ann['image_id'] != pre_img_name:
                    # 6.新建xml文件
                    xml_file = open((xml_path + img_name + '.xml'), 'w')
                    xml_file.write('<annotation>\n')
                    xml_file.write('    <folder>VOC2007</folder>\n')
                    xml_file.write('    <filename>' + name + '</filename>\n')
                    xml_file.write('<source>\n')
                    xml_file.write('<database>orgaquant</database>\n')
                    xml_file.write('<annotation>organoids</annotation>\n')
                    xml_file.write('</source>\n')
                    xml_file.write('    <size>\n')
                    xml_file.write('        <width>' + str(Pwidth) + '</width>\n')
                    xml_file.write('        <height>' + str(Pheight) + '</height>\n')
                    xml_file.write('        <depth>' + str(Pdepth) + '</depth>\n')
                    xml_file.write('    </size>\n')
                    xml_file.write('            <segmented>0</segmented>\n')
                    xml_file.write('    <object>\n')
                    xml_file.write('<name>' + dict[str(ann['category_id'])] + '</name>\n')
                    xml_file.write('                    <pose>Unspecified</pose>\n')
                    xml_file.write('                    <truncated>0</truncated>\n')
                    xml_file.write('                    <difficult>0</difficult>\n')
                    xml_file.write('        <bndbox>\n')
                    xml_file.write('            <xmin>' + str(int(ann['bbox'][0])) + '</xmin>\n')
                    xml_file.write('            <ymin>' + str(int(ann['bbox'][1])) + '</ymin>\n')
                    xml_file.write('            <xmax>' + str(int(ann['bbox'][0] + ann['bbox'][2])) + '</xmax>\n')
                    xml_file.write('            <ymax>' + str(int(ann['bbox'][1] + ann['bbox'][3])) + '</ymax>\n')
                    xml_file.write('        </bndbox>\n')
                    xml_file.write('    </object>\n')
                    xml_file.close()
                    pre_img_name = ann['image_id']  # 将其设为"老"图
                else:  # 不是新图而是"老图"
                    # 7.同一张图片，只需要追加写入object
                    xml_file = open((xml_path + img_name + '.xml'), 'a')
                    xml_file.write('    <object>\n')
                    xml_file.write('<name>' + dict[str(ann['category_id'])] + '</name>\n')
                    xml_file.write('        <bndbox>\n')
                    xml_file.write('            <xmin>' + str(int(ann['bbox'][0])) + '</xmin>\n')
                    xml_file.write('            <ymin>' + str(int(ann['bbox'][1])) + '</ymin>\n')
                    xml_file.write('            <xmax>' + str(int(ann['bbox'][0] + ann['bbox'][2])) + '</xmax>\n')
                    xml_file.write('            <ymax>' + str(int(ann['bbox'][1] + ann['bbox'][3])) + '</ymax>\n')
                    xml_file.write('        </bndbox>\n')
                    xml_file.write('    </object>\n')
                    xml_file.close()

        # 8.读完txt文件最后写入</annotation>
        xml_file1 = open((xml_path + img_name + '.xml'), 'a')
        xml_file1.write('</annotation>')
        xml_file1.close()
    print("Done !")


# 修改成自己的文件夹 注意文件夹最后要加上/
if __name__ == '__main__':
    f = open('annotations.json', encoding='utf-8')
    data = json.load(f)
    data_dic = {}
    # 把图片名和id对应起来存到字典中
    for img in data['images']:
        data_dic[img['id']] = img['file_name'].strip()
    json_to_xml(data, "images/", "XML/")
