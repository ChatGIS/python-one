# int 整数类型
int1 = 9
print(int1)
int2 = 0B11 # 二进制
print(int2)
int3 = 0O11 # 八进制
print(int3)
int4 = 0X11F # 十六进制
print(int4)

# float 浮点型
float1 = 0.2
print(float1)
float2 = 2e-2  # 科学计数法
print(float2)

# 复数类型

# 内置函数type()用来查看变量所指的对象类型
print(type(int1))
# 内置函数isinstance()也可以判断
print(isinstance(int1, int))

print(type(float1))