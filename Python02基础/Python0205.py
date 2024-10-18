## 列表
list1 = ['C', 'H', 'A', 'T', 'G', 'I', 'S']
print(list1)
print(type(list1))
# 访问元素
print('list1[0]', list1[0])
print('list1[-1]', list1[-1])
# 列表切片
print('list1[0:6:2]', list1[0:6:2])
# 修改元素
list1.append('@')
print(list1)
list1 += ['C', 'O', 'M']
print(list1)
list1.insert(0, '%%')
print(list1)
list1.remove('C')  # 从左向右搜索，删除找到的第一个元素
print(list1)
list1[0] = 'C'
print(list1)

## 元组
tuple1 = 1,2,3,4
print(tuple1)
print(type(tuple1))

tuple2 = (1, 2, '中')
print(tuple2)
print(type(tuple2))

## 集合
set = {'C', 'H', 'A', 'T', 'G', 'I', 'S'}
print(set)
print(type(set))

## 字典
dict = {'name': 'ChatGIS'}
print(dict)
print(type(dict))
