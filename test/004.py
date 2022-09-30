import os
# 函数中的name是新建文件的名字，msg是写入的内容，类型为str类型，可任意传参
desktop_path = "D:\\ 111"  # 新创建的txt文件的存放路径
full_path = desktop_path + "000" + '.txt'  # 也可以创建一个.doc的word文档
file = open(full_path, 'w')  # w 的含义为可进行读写
file.close()
