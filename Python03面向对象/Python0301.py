'''
函数定义
'''
def myPrint(content):
    print('ChatGIS:', content)

myPrint('Number One')

'''
默认参数
'''
def myPrintDefaultParam(name='ChatGIS'):
    print(name, 'Number One')
myPrintDefaultParam()
myPrintDefaultParam('China')

'''
多参数
'''
def calculateArea(width, height):
    print(width, height)
    return width * height
print(calculateArea(2, 3))
print(calculateArea(height=4, width=5))
print(calculateArea(4, height=5))
# print(calculateArea(width=4, 5))
