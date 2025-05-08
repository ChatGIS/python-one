# 定义
def add(a, b):
    """计算两个数的和"""
    return a + b

result = add(3, 5)
print(result)
print(add.__doc__)

# 参数
def hello(name="World"):
    print(f"Hello, {name}!")
hello("ChatGIS")
hello()

def introduce(name, age):
    print(f"{name} is {age} years old.")
introduce(name="Chat", age=5)
introduce(age=6, name="GIS")

def sum_all(*args):
    return sum(args)
total = sum_all(1, 2, 3, 4, 5)
print(total)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="ChatGIS", age=3, country="China")