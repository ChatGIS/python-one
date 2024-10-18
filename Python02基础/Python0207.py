# 决策语句
# age = input("Enter your age: ")
# if int(age) < 18:
#     print('未成年人')
# elif 18 <= int(age) < 60:
#     print('中年人')
# elif int(age) >= 60:
#     print('老年人')

# while语句
count = 0
while count < 3:
    count = count + 1
    print(count)

# for 语句
for item in 'ChatGIS':
    print(item)

# for循环break
for item in 'ChatGIS':
    print(item)
    if item == 'G':
        break

# for循环continue
for item in 'ChatGIS':
    if item == 'G':
        continue
    print(item)