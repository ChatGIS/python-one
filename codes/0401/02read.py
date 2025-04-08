file_object1 = open('my_file_multiline.txt', 'r', encoding='utf-8')
# 读取文件中所有数据
content1 = file_object1.read()
print(content1)
# 读取文件中部分数据
file_object1.seek(0)
content11 = file_object1.read(12)
print(content11)