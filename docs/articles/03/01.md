## 语法
```python
def print_content(content):
    print('ChatGIS: ', content)
```

- 使用def定义方法，类似与JavaScript中的function
- 按照PEP8的建议，函数名称应全部使用小写字母，并使用下划线分隔单词
- 避免使用驼峰命名法（CamelCase），例如，CalculateArea或findMaxValue，除非是为了兼容某些库或框架

## 函数参数(默认值)
```python
def print_default_param(name='ChatGIS'):
    print(name, 'Number One')
print_default_param()
print_default_param('China')
```
输出
```
ChatGIS Number One
China Number One
```
## 多参数函数
```python
def calculateArea(width, height):
    print(width, height)
    return width * height
print(calculateArea(2, 3))
print(calculateArea(height=4, width=5))
print(calculateArea(4, height=5))
# print(calculateArea(width=4, 5))
```
最后一个语法错误

输出
```
2 3
6
5 4
20
4 5
20
```

## 函数变量作用域
- 局部变量：在函数中声明的变量，它的作用域是当前的代码块，超出这个范围则变量失效
- 全局变量：在模块中声明的变量，它的作用域是整个模块
```python
name = 'gChatGIS'
def show_name():
    name = 'ChatGIS'
    print('in:', name)
show_name()
print('out: ', name)
```
输出
```
in: ChatGIS
out:  gChatGIS
```
## 匿名函数与lambda函数
```python
# 常规函数
def double(x):
    return x * 2
print(double(2))
# 匿名函数
doubx = lambda x: x * 2
print(doubx(2))
```
- 匿名函数没有def关键词

## 生成器
生成器（Generator）是Python中的一种特殊函数，它可以用来创建迭代器。
生成器函数不同于普通函数，它包含yield关键字。
调用生成器函数不会立即执行，而是返回一个生成器对象。
每次调用这个对象的next()方法，函数会执行到下一个yield语句，返回对应的结果。
```python
def my_generator():
    yield 1
    yield 2
    yield 3
print(next(my_generator()))
print(next(my_generator()))
print(next(my_generator()))
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
```
输出
```
1
1
1
1
2
3
```
- 将方法赋值给一个变量，否则会执行yield;
- 惰性计算，这种方式不需要一次姓准备全部结果，可以一点一点生成，节省了大量内存空间。