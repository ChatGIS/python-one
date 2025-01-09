# 决策语句
Python中的条件语句涉及3个关键字：if、else和elif，这3个关键字对应条件语句的3种结构。

## if 语句
```python
age = input("Enter your age: ")
if int(age) < 18:
    print('未成年人')
elif 18 <= int(age) < 60:
    print('中年人')
elif int(age) >= 60:
    print('老年人')
```
# 循环语句
## while 语句
```python
count = 0
while count < 3:
    count = count + 1
    print(count)
```
输出
```python
1
2
3
```

## for 语句
```python
for item in 'ChatGIS':
    print(item)
```
输出
```python
C
h
a
t
G
I
S
```
