class Student:
    school = '集思小学'
    student_num = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_num += 1
    def instroduce(self):
        return f"我的名字叫{self.name}， 我今年{self.age}岁啦"
    def change_name(self, new_name):
        self.name = new_name
    @classmethod
    def get_school_name(cls):
        return cls.school
    @classmethod
    def from_string(cls, infos):
        name, age = infos.split(',')
        return cls(name, int(age))
    @classmethod
    def reset_num(cls):
        cls.student_num = 0
student1 = Student("张三", 7)
student2 = Student("李四", 8)
print(Student.student_num)
print(student1.name, student1.age)
print(student2.name, student2.age)
student2.school = '吉斯小学'
print(student1.school)
print(student2.school)
print(Student.get_school_name())
print(student1.get_school_name())
student3 = Student.from_string("王五, 9")
print(student3.name, student3.age)

Student.reset_num()
print(Student.student_num)

print(student1.instroduce())
print(student2.instroduce())

student1.change_name("张三丰")
print(student1.instroduce())