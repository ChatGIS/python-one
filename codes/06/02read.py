file_object1 = open('my_file_multiline.txt', 'r', encoding='utf-8')
# 读取文件中所有数据
content1 = file_object1.read()
print(content1)
# 读取文件中部分数据
print('----------------------------------')
file_object1.seek(0)
content11 = file_object1.read(12)
print(content11)
# readline函数
print('----------------------------------')
file_object1.seek(0)
content_line1 = file_object1.readline(-1)
print(content_line1)
content_line2 = file_object1.readline(5)
print(content_line2)
content_line3 = file_object1.readline()
print(content_line3)
# readlines函数
print('----------------------------------')
file_object1.seek(0)
lines = file_object1.readlines()
print(lines)
file_object1.close()