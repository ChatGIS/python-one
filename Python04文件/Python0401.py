fname1 = 'my_file.txt'
f = open(fname1, 'w+', encoding='utf-8', errors='ignore')
f.write('Hello World, Hello File')
f.close()
