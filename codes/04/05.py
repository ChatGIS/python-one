class Animal:
    def speak(self):
        print("动物发出声音")

class Dog(Animal):
    def speak(self):
        print("狗汪汪叫")

class Cat(Animal):
    def speak(self):
        print("猫喵喵叫")

# 定义一个函数，接收 Animal 类型的对象
def make_animal_speak(animal):
    animal.speak()

# 创建不同动物的实例
dog = Dog()
cat = Cat()

# 调用函数，传入不同的对象
make_animal_speak(dog)
make_animal_speak(cat)

class Duck:
    def quack(self):
        print("嘎嘎嘎")

class Person:
    def quack(self):
        print("我模仿鸭子嘎嘎嘎")

# 定义一个函数，接收具有 quack 方法的对象
def make_quack(obj):
    obj.quack()

# 创建不同类型的对象
duck = Duck()
person = Person()

# 调用函数，传入不同的对象
make_quack(duck)
make_quack(person)

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

# 创建学生对象列表
students = [
    Student("张三", 80),
    Student("李四", 90),
    Student("王五", 70)
]

# 对学生列表进行排序
sorted_students = sorted(students)

# 输出排序结果
for student in sorted_students:
    print(f"{student.name}: {student.score}")