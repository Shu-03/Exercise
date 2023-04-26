# 作者：shu qi
# 开发时间：2023/4/23 16:58


def main():
    ftele1=open("TeleAddressBook.txt","rb")
    ftele2=open("EmailAddressBook.txt","rb")
    ftele1.readline()
    ftele2.readline()
    lines1=ftele1.readlines()
    lines2=ftele2.readlines()
    #建立空列表用于存储姓名电话Email
    list1_name=[]
    list1_tele=[]
    list2_name=[]
    list2_email=[]
    #获取TeleAddressBook
    for line in lines1:
        elements=line.split()
        list1_name.append(str(elements[0].decode("utf-8")))
        list1_tele.append(str(elements[1].decode("utf-8")))
    #获取EmailAddressBook
    for line in lines2:
        elements=line.split()
        list2_name.append(str(elements[0].decode("utf-8")))
        list2_email.append(str(elements[1].decode("utf-8")))
    lines=[]
    lines.append("姓名\t电话\t\t邮箱\n")
    #按索引方式遍历姓名列表
    for i in range(len(list1_name)):
        s=''
        if list1_name[i] in list2_name:
            j=list2_name.index(list1_name[i])
            s="\t".join([list1_name[i],list1_tele[i],list2_email[j]])
            s+="\n"
        else:
            s="\t".join([list1_name[i],list1_tele[i],str("-----------")])
            s+="\n"
        lines.append(s)
    for i in range(len(list2_name)):
        s=""
        if list2_name[i] not in list1_name:
            s="\t".join([list2_name[i],str("-----------"),list2_email[i]])
            s+="\n"
        lines.append(s)
    #将新生成的合并数据写入新的文件中
    ftele3=open("AddressBook.txt","w")
    ftele3.writelines(lines)
    #关闭文件
    ftele3.close()
    ftele1.close()
    ftele2.close()
    print("The addressBooks are merged!")
main()