# map() 示例：对列表每个元素应用函数
numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出 [1, 4, 9]

# sorted() 示例：使用自定义排序规则
students = [("Alice", 25), ("Bob", 20)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # 输出 [('Bob', 20), ('Alice', 25)]