class Student:
    school = '集思小学'
    student_num = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_num += 1
student1 = Student("张三", 7, "一年级")
student2 = Student("李四", 8, "二年级")
print(Student.student_num)
print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
student2.school = '吉斯小学'
print(student1.school)
print(student2.school)