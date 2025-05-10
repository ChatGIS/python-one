# 语法：lambda 参数: 表达式
add = lambda a, b: a + b
print(add(3, 5))  # 输出 8

# 结合高阶函数使用
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出 [1, 4, 9, 16]