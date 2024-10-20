'''
函数定义
'''
def print_content(content):
    print('ChatGIS:', content)

print_content('Number One')

'''
默认参数
'''
def print_default_param(name='ChatGIS'):
    print(name, 'Number One')
print_default_param()
print_default_param('China')

'''
多参数
'''
def calculate_area(width, height):
    print(width, height)
    return width * height
print(calculate_area(2, 3))
print(calculate_area(height=4, width=5))
print(calculate_area(4, height=5))
# print(calculate_area(width=4, 5))

'''
变量作用域
'''
name = 'gChatGIS'
def show_name():
    name = 'ChatGIS'
    print('in:', name)
show_name()
print('out: ', name)

'''
匿名函数
'''
# 常规函数
def double(x):
    return x * 2
print(double(2))
# 匿名函数
doubx = lambda x: x * 2
print(doubx(2))

'''
生成器
'''
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
