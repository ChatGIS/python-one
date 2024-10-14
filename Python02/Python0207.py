# 决策语句
age = input("Enter your age: ")
if int(age) < 18:
    print('未成年人')
elif 18 <= int(age) < 60:
    print('中年人')
elif int(age) >= 60:
    print('老年人')


import sys

print(sys.getdefaultencoding())