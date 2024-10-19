## 语法
```python
def myPrint(content):
    print('ChatGIS: ', content)
```

- 使用def定义方法，类似与JavaScript中的function
- 传参和返回值等，都和JS一样

## 函数参数(默认值)
```python
def myPrintDefaultParam(name='ChatGIS'):
    print(name, 'Number One')
myPrintDefaultParam()
myPrintDefaultParam('China')
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
