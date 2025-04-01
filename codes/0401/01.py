f = open('my_file.txt', 'rt', encoding='utf-8', errors='ignore')
txt = f.read()
f.close()
print(txt)