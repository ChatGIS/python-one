# 读取文件内容
f = open('my_file.txt', 'rt', encoding='utf-8', errors='ignore')
txt = f.read()
f.close()
print(txt)
# 创建文件并添加文本
f = open('my_file_new.txt', 'wt', encoding='utf-8', errors='ignore')
f.write('使用write函数新增一行文本；')
f.close()
# 在原有文件末尾追加内容
f1 = open('my_file.txt', 'a+', encoding='utf-8', errors='ignore')
f1.write('追加内容；')
f1.close()