类就是对具有相同**属性和行为**的对象的抽象描述。  
比如，创建一个 “动物” 类，其中包含 “生命状态”“移动方式”“进食方法” 等**属性和方法**，来概括各种具体动物的共同特性。  
这样，通过类的定义，就把现实世界中复杂多样的动物抽象为程序中的一个概念模型，方便进行统一的管理和操作。  
面向对象的抽象性引出了**类和对象**两个最重要的概念。  

## 1. 类与对象
示例：
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student("张三", 7, "一年级")
student2 = Student("李四", 8, "二年级")
print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
```
### 1.1. 类
class是声明类的关键字，其中`Student`是自定义的类名;  
object 类是所有类的基类，默认情况下，所有类都会隐式继承 object 类；此处自定义类没有显式继承其他类，所以父类可以省略；

### 1.2. 对象
student1和student2都是Student类的实例化对象；

## 2. 构造方法与实例变量
类的构造方法是面向对象编程中一个重要的概念，它主要用于初始化对象的属性，在创建对象时自动调用。  
默认构造方法是 `__init__` ，当创建类的实例时，`__init__` 方法会自动被调用，用于初始化对象的属性。  
构造方法中的第一个参数是self，self是指当前实例，表示这个方法与当前实例绑定，self后的参数是用来初始化实例变量的，**调用构造方法时不需要传入self**。   
实例变量就是某个实例（或对象）个体特有的“数据”，示例中，通过 self.name 和 self.age 来初始化实例的属性。
## 3. 实例方法
在 Python 的面向对象编程中，实例方法是类中最常见的方法类型。
### 3.1. 实例方法的定义与调用
实例方法需要通过实例对象来调用。
```python
class Student:
    student_num = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_num += 1
    def instroduce(self):
        return f"我的名字叫{self.name}， 我今年{self.age}岁啦"
student1 = Student("张三", 7)
student2 = Student("李四", 8)
print(student1.instroduce())
print(student2.instroduce())
```
### 3.2. 实例方法的使用场景
实例方法常被用于访问和修改实例的属性, 此处通过该实例方法实现对实例变量`name`的修改。
```python
    def change_name(self, new_name):
        self.name = new_name
student1.change_name("张三丰")
print(student1.instroduce())
```

## 4. 类变量
类变量是属于类本身的变量，被该类的所有实例共享。
### 4.1. 类变量的定义
类变量通常在类的内部，但在类的所有方法之外定义。  
此处可以理解为所有学生的名称、年龄和年级各不相同，但是所在的学校名称是相同的。
```python
class Student:
    # 定义类变量
    school = '集思小学'
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
```
### 4.2. 类变量的访问
类变量既可以通过类名直接访问，也可以通过类的实例访问。
```python
# 通过类名访问类变量
print(Student.school)
# 通过实例对象访问类变量
student1 = Student("张三", 7, "一年级") 
print(student1.school)
```
### 4.3. 类变量的修改
当通过类名修改类变量时，所有实例访问该类变量时都会得到修改后的值。
此处可以理解为学校进行了校名变更；
```python
Student.school = '吉斯小学'
print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student1.school)
print(student2.school)
```
当通过实例修改类变量时，实际上是给该实例创建了一个同名的实例变量，而不会影响类变量本身以及其他实例对类变量的访问。
此处可以理解为李四同学进行了转学；
```python
student1 = Student("张三", 7, "一年级")
student2 = Student("李四", 8, "二年级")
print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
student2.school = '吉斯小学'
print(student1.school)
print(student2.school)
```
### 4.4. 类变量的应用场景
类变量可以用于共享数据，当多个实例需要共享某些数据时，可以使用类变量。例如，统计学生类创建的实例数量。
```python
class Student:
    student_num = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_num += 1
student1 = Student("张三", 7, "一年级")
student2 = Student("李四", 8, "二年级")
print(Student.student_num)
```
## 5. 类方法
类方法是绑定到类而不是类的实例的方法。它可以通过类名直接调用，也可以通过类的实例调用。类方法使用 @classmethod 装饰器来定义，其第一个参数通常为 cls，代表类本身。
### 5.1. 类方法的定义
```python
class Student:
    school = '集思小学'
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_num += 1
    @classmethod
    def get_school_name(cls):
        return cls.school
```
`get_school_name`是一个类方法，使用 `@classmethod` 装饰器进行修饰，第一个参数 `cls` 代表类本身，通过 `cls` 可以访问类的属性和调用其他类方法。
### 5.2. 类方法的调用
类方法既可以通过类名直接调用，也可以通过类的实例调用。
```python
# 通过类名调用类方法
print(Student.get_school_name())
# 通过实例调用类方法
print(student1.get_school_name())
```
### 5.3. 类方法的应用场景
**工厂方法**  
类方法可以作为工厂方法，用于创建类的实例。例如，定义一个类方法根据不同的输入格式创建实例。
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_num += 1
    @classmethod
    def from_string(cls, infos):
        name, age, grade = infos.split(',')
        return cls(name, int(age), grade)
student3 = Student.from_string("王五, 9, 三年级")
print(student3.name, student3.age, student3.grade)
```
**修改类变量**  
类方法可以用于修改类变量的值。
```python
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
```
## 6. 静态方法
静态方法是类中的一种特殊方法，它和类以及实例都没有紧密的关联，不会依赖类或实例的属性与方法。
### 6.1 静态方法的定义
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```
### 6.2 静态方法的调用
静态方法既可以通过类名直接调用，也能通过类的实例来调用。
```python
# 通过类名调用静态方法
result1 = MathUtils.add(3, 5)
print(result1)

# 创建类的实例
math_obj = MathUtils()
# 通过实例调用静态方法
result2 = math_obj.add(2, 4)
print(result2)
```
### 6.3 静态方法的使用场景
**封装通用工具函数**  
当有一些函数和类的属性、方法没有直接关联，但又和类在逻辑上有一定联系时，可以把这些函数定义为静态方法。  
例如，在一个日期处理类中，封装一个计算两个日期相差天数的静态方法。
```python
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
```
**避免不必要的实例化**  
如果一个方法不需要访问类或实例的属性和方法，将其定义为静态方法可以避免创建类的实例，从而节省资源。  
例如，在一个图形类中，定义一个计算两点之间距离的静态方法。
```python
import math

class Shape:
    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 调用静态方法
dist = Shape.distance(1, 2, 4, 6)
print(dist)
```