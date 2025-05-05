class Student:
    student_num = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_num += 1
    @classmethod
    def reset_num(cls):
        cls.student_num = 0

student2 = Student("李四", 8, "二年级")
print(Student.student_num)
Student.reset_num()
print(Student.student_num)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
# 通过类名调用静态方法
result1 = MathUtils.add(3, 5)
print(result1)

# 创建类的实例
math_obj = MathUtils()
# 通过实例调用静态方法
result2 = math_obj.add(2, 4)
print(result2)


from datetime import datetime

class DateUtils:
    @staticmethod
    def days_between_dates(date1, date2):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)

# 调用静态方法
date1 = "2023-01-01"
date2 = "2023-01-10"
days = DateUtils.days_between_dates(date1, date2)
print(days)


import math

class Shape:
    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 调用静态方法
dist = Shape.distance(1, 2, 4, 6)
print(dist)