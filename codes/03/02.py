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