class ParentClass:
    def __init__(self):
        pass

    def parent_method(self):
        print("这是父类的方法")

class ChildClass(ParentClass):
    def __init__(self):
        # 调用父类的构造方法
        super().__init__()

    def child_method(self):
        print("这是子类的方法")

# 创建子类的实例
child = ChildClass()
# 调用父类的方法
child.parent_method()
# 调用子类的方法
child.child_method()


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} 正在进食")

    def sleep(self):
        print(f"{self.name} 正在睡觉")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} 喵喵叫")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} 汪汪叫")

# 创建猫和狗的实例
cat = Cat("咪咪", 2)
dog = Dog("旺财", 3)

# 调用继承的方法
cat.eat()
dog.sleep()
# 调用子类特有的方法
cat.meow()
dog.bark()


class ParentClass1:
    def method1(self):
        print("This is method from ParentClass1")


class ParentClass2:
    def method2(self):
        print("This is method from ParentClass2")


class ChildClass(ParentClass1, ParentClass2):
    pass


# 创建子类的实例
child = ChildClass()
# 调用父类 1 的方法
child.method1()
# 调用父类 2 的方法
child.method2()

class A:
    def method(self):
        print("A's method")


class B(A):
    def method(self):
        print("B's method")


class C(A):
    def method(self):
        print("C's method")


class D(B, C):
    pass


print(D.__mro__)
d = D()
d.method()