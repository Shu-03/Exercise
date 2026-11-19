import os
import numpy as np
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

#import cv2
import time


def MakeTxt2Xml(txt_path,xml_path,png_path):
    data = np.loadtxt(txt_path,dtype=np.str_)
    if data.size == 0:
        output = "Begin process, " + txt_path + " is null!!!"
        print(output)
    if data.ndim == 1:
        data = np.array([data])
    doc_root = ET.Element('doc')
    tree = ET.ElementTree(doc_root)

    img_path_element = ET.Element('path')
    img_path_element.text = png_path
    doc_root.append(img_path_element)

    outputs_element = ET.Element('outputs')
    object_element = SubElement(outputs_element,'object')
    # element.append(SubElement) 与  subelement = SubElement(main_element,'subelement') 是相同的意思
    for i in range(data.shape[0]):

        item_element = SubElement(object_element, 'item')


        name_element = SubElement(item_element, 'name')
        name_element.text = data[i][0]

        bndbox_element = SubElement(item_element, 'bndbox')

        xmin_element = SubElement(bndbox_element, 'xmin')
        xmin_element.text = str(data[i][1])

        ymin_element = SubElement(bndbox_element, 'ymin')
        ymin_element.text = str(data[i][2])

        xmax_element = SubElement(bndbox_element, 'xmax')
        xmax_element.text = str(data[i][3])

        ymax_element = SubElement(bndbox_element, 'ymax')
        ymax_element.text = str(data[i][4])


    doc_root.append(outputs_element)

    time_element = ET.Element('time_labeled')
    # time_element.text = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    time_element.text = str(int(round(time.time() * 1000)))
    doc_root.append(time_element)

    labeled_element = ET.Element('labeled')
    if (os.path.exists(txt_path)):
        labeled_element.text = str("true")
    else:
        labeled_element.text = str("false")
    doc_root.append(labeled_element)

    size_element = ET.Element('size')
    width_element = SubElement(size_element, 'width')
    img = cv2.imread(png_path)
    # width_element.text = str(img.shape[1])
    # height_element = SubElement(size_element, 'height')
    # height_element.text = str(img.shape[0])
    # depth_element = SubElement(size_element, 'depth')
    # depth_element.text = str(img.shape[2])
    width_element.text = str(1920)
    height_element = SubElement(size_element, 'height')
    height_element.text = str(1080)
    depth_element = SubElement(size_element, 'depth')
    depth_element.text = str(3)

    doc_root.append(size_element)

    xml = tostring(doc_root)
    dom = parseString(xml)

    # xml_name = pic_name.replace(".jpg", "")
    # xml_name = os.path.join(save_xml_path, xml_name + '.xml')
    with open(xml_path, 'wb') as f:
        f.write(dom.toprettyxml(indent='\t', encoding='utf-8'))
    print(xml_path+" is writed!")



if __name__ == "__main__":
    labeltxt = "/media/wxf/Elements/data/video/label_txt"
    labelxml = "/media/wxf/Elements/data/video/label_xml"
    img_path = "."


    for txt in sorted(os.listdir(labeltxt)):
        txt_path = os.path.join(labeltxt,txt)
        name = txt.split(".")[-2]
        xml_path = labelxml + os.sep + name + ".xml"
        png_path = img_path + os.sep + name + ".png"
        if os.path.exists(txt_path):
            # print(txt_path)
            MakeTxt2Xml(txt_path,xml_path,png_path)