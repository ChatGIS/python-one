在 Python 中，函数是组织好的、可重复使用的代码块，用于执行特定任务。
函数是 Python 编程的核心概念之一，它可以提高代码的复用性、可维护性和可读性。

Python官方提供的函数称为内置函数，如：print()，此外，我们还可以自定义函数。
## 1. 定义与调用
函数通过 def 关键字定义，格式为：
```python
def 函数名(参数列表):
    """文档字符串（可选）"""
    函数体
    return 返回值  # 可选
```
- 函数名：遵循标识符规则（如小写字母、下划线）。
- 参数列表：可包含零个或多个参数，用逗号分隔。
- 文档字符串：描述函数功能，可通过 `函数名.__doc__` 访问。
- 返回值：通过 return 语句返回结果，若无则默认返回 None。

示例：
```python
def add(a, b):
    """计算两个数的和"""
    return a + b

result = add(3, 5)
print(result)
print(add.__doc__)
```
输出结果：
```text
8
计算两个数的和
```
## 2. 函数参数
### 2.1. 必需参数
调用时必须提供的参数，否则会报错;
```python
def hello(name):
    print(f"Hello, {name}!")
hello("ChatGIS")
hello()
```
输出结果：
```text
Hello, ChatGIS!
Traceback (most recent call last):
  File "E:\python-one\codes\03\01.py", line 12, in <module>
    hello()
    ~~~~~^^
TypeError: hello() missing 1 required positional argument: 'name'
```
其中，函数`hello()`因为没有传参而报错。

### 2.2. 默认参数
定义时指定默认值，调用时可省略；
```python
def hello(name="World"):
    print(f"Hello, {name}!")
hello("ChatGIS")
hello()
```
输出结果：
```text
Hello, ChatGIS!
Hello, World!
```
### 2.3. 关键字参数
调用时通过参数名指定值，可忽略参数顺序;
```python
def introduce(name, age):
    print(f"{name} is {age} years old.")
introduce(name="Chat", age=5)
introduce(age=6, name="GIS")
```
输出结果：
```text
Chat is 5 years old.
GIS is 6 years old.
```
### 2.4. 可变参数
- `*args`：接收任意数量的位置参数，以元组形式存储。
```python
def sum_all(*args):
    return sum(args)
total = sum_all(1, 2, 3, 4, 5)
print(total) # 15
```
- `**kwargs`：接收任意数量的关键字参数，以字典形式存储。
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="ChatGIS", age=3, country="China")
```
输出结果：
```text
name: ChatGIS
age: 3
country: China
```
## 3. 函数返回值
函数通过 return 语句返回值，支持返回任意类型的对象：
```python
def get_name_and_age():
    return "Bob", 25  # 返回元组

name, age = get_name_and_age()  # 元组解包
print(name, age)  # 输出 "Bob 25"
```
- 多个返回值：实际返回一个元组，可通过解包获取多个值。
- 无返回值：若不写 return，函数默认返回 None。

## 4. 函数的作用域
函数内部的变量属于局部作用域，外部无法访问；全局变量可在函数内部读取，但修改需用 global 声明；
```python
x = 10  # 全局变量

def modify_x():
    global x  # 声明要修改全局变量
    x = 20

modify_x()
print(x)  # 输出 20
```
