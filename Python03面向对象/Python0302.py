# 声明Employee员工类
class Employee:
    pass

# 多态
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.length = length

    def area(self):
        return self.length ** 2
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
square = Square(5)
print('正方形面积：', square.area())
circle = Circle(3)
print('圆的面积：', circle.area())