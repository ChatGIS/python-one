# if-else语句
age = int(input("输入年龄："))
if age > 18:
    print("成年人")
else:
    print("未成年人")
# if-elif-else语句
score = int(input("输入成绩："))
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
# for循环
for item in 'ChatGIS':
    print(item)
# while循环
count = 0
while count < 3:
    count += 1
    print(count)

# break
while True:
    user_input = input("输入 'q' 退出: ")
    if user_input == 'q':
        break  # 退出无限循环
# continue
for item in "ChatGIS":
    if item.isupper():
        continue  # 跳过大写字母
    print(item)
# pass
password = input("输入密码：")
if password != "":
    pass # 密码验证逻辑后续再写，pass占位，避免语法错误
else:
    print("空密码")