在 Python 中，流程控制用于控制程序的执行顺序，主要分为条件语句、循环语句和跳转语句。
## 1. 条件语句
根据条件判断执行不同的代码块，涉及三个关键字：if、else和elif。
### 1.1. if-else语句
```python
age = int(input("输入年龄："))
if age > 18:
    print("成年人")
else:
    print("未成年人")
```
交互结果：
```text
输入年龄：17
未成年人
输入年龄：20
成年人
```
### 1.2. if-elif-else语句 
```python
score = int(input("输入成绩："))
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
```
交互结果：
```text
输入成绩：90
A
输入成绩：70
B
输入成绩：10
C
```
## 2. 循环语句
### 2.1. for循环
```python
for item in 'ChatGIS':
    print(item)
```
输出结果：
```text
C
h
a
t
G
I
S
```
### 2.2. while循环
while语句是一种先判断的循环结构。
```python
count = 0
while count < 3:
    count += 1
    print(count)
```
输出
```python
1
2
3
```

## 3. 跳转语句
跳转语句用于改变程序的执行流程。
### 3.1. break
终止当前循环；
```python
while True:
    user_input = input("输入 'q' 退出: ")
    if user_input == 'q':
        break  # 退出无限循环
```
交互结果：
```text
输入 'q' 退出: a
输入 'q' 退出: b
输入 'q' 退出: q
```
### 3.2. continue
跳出当前循环的剩余部分，执行下一**次**循环；
```python
for item in "ChatGIS":
    if item.isupper():
        continue  # 跳过大写字母
    print(item)
```
交互结果：
```text
h
a
t
```
### 3.3. pass
空语句，用于占位，不执行任何操作：
```python
password = input("输入密码：")
if password != "":
    pass # 密码验证逻辑后续再写，pass占位，避免语法错误
else:
    print("空密码")
```