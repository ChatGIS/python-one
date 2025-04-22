在 Python 中，try-except 语句是用于异常处理的核心机制，它可以帮助你捕获并处理程序运行过程中出现的异常，
避免程序因异常而崩溃，增强程序的健壮性和稳定性。
## 1. 基本语法
```python
try:
    # 可能会抛出异常的代码块
    pass
except ExceptionType:
    # 当发生指定类型的异常时执行的代码块
    pass
```
- try 块：包含可能会引发异常的代码，Python 会尝试执行这个代码块中的所有语句。
- except 块：用于捕获并处理特定类型的异常。当 try 块中的代码抛出 ExceptionType 类型的异常时，程序会跳转到对应的 except 块中执行相应的处理代码。

示例：
```python
try:
    num1 = int(input("请输入一个整数: "))
    num2 = int(input("请再输入一个整数: "))
    result = num1 / num2
    print(f"结果是: {result}")
except ValueError:
    print("输入无效，请输入有效的整数。")
except ZeroDivisionError:
    print("错误: 除数不能为零。")
```
`try `语句块的主要作用是包裹可能会抛出异常的代码。
一旦其中某条语句触发了异常，Python 解释器会**中断后续代码的执行**，然后根据异常类型寻找匹配的 except 语句块进行处理。
## 2. 捕获多个异常
可以在一个 except 语句中捕获多个异常，使用元组来指定异常类型：
```python
try:
    num = int("abc")
    result = 1 / 0
except (ValueError, ZeroDivisionError):
    print("发生了值错误或除零错误。")
```
这种形式可以简化代码结构、统一处理相似异常，适用于统一处理的异常逻辑
## 3. 捕获所有异常
要捕获所有类型的异常，可以使用 except 语句而不指定异常类型，但这种做法不推荐，因为它会掩盖一些潜在的问题，使调试变得困难：
```python
try:
    num = 1 / 0
except:
    print("发生了一个异常。")
```
更推荐的做法是指定具体的异常类型，或者捕获 Exception 基类：
```python
try:
    num = 1 / 0
except Exception as e:
    print(f"发生了异常: {e}")
```
## 4. else子句
try-except 语句还可以包含一个 else 子句，当 try 块中没有发生任何异常时，会执行 else 块中的代码。
```python
try:
    num1 = int(input("请输入一个整数: "))
    num2 = int(input("请再输入一个整数: "))
    result = num1 / num2
except ValueError:
    print("输入无效，请输入有效的整数。")
except ZeroDivisionError:
    print("错误: 除数不能为零。")
else:
    print(f"结果是: {result}")
```
else 子句提高了代码的可读性和可维护性，开发者可以一目了然地知道哪些代码是在无异常时执行的，便于后续的修改和扩展。

## 5. finally子句
无论 try 块中是否发生异常，finally 块中的代码都会被执行。因此，通常用于执行一些清理操作，如关闭文件、释放资源等。
```python
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件未找到。")
finally:
    if 'file' in locals():
        file.close()
```
在这个示例中，无论是否成功打开文件并读取内容，finally 块中的代码都会尝试关闭文件，确保资源被正确释放。