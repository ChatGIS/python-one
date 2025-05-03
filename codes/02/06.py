# 算数运算符
a = 5
b = 3
print("5 + 3 = ", a + b)
print("5 - 3 = ", a - b)
print("5 * 3 = ", a * b)
print("5 / 3 = ", a / b)
print("5 // 3 = ", a // b)
print("5 % 3 = ", a % b)
print("5 ** 3 = ", a ** b)
# 比较运算符
print("5 == 3 ? ", a == b)
print("5 != 3 ? ", a != b)
print("5 > 3 ? ", a > b)
print("5 < 3 ? ", a < b)
print("5 <= 3 ? ", a <= b)
print("5 >= 3 ? ", a >= b)
# 赋值运算符
a += b
print("a += b 运算后a的值：", a)
a -= b
print("a -= b 运算后a的值：", a)
a *= b
print("a *= b 运算后a的值：", a)
a /= b
print("a /= b 运算后a的值：", a)
a /= b
print("a /= b 运算后a的值：", a)
a = 5
a //= b
print("a //= b 运算后a的值：", a)
a %= b
print("a %= b 运算后a的值：", a)
a **= b
print("a **= b 运算后a的值：", a)
# 逻辑运算符
print("(1 < 2) and (3 < 4) ", (1 < 2) and (3 < 4))
print("(1 > 2) or (3 < 4) ", (1 > 2) or (3 < 4))
print("not(3 < 4) ", not(3 < 4))
# 位运算符
print("5 & 3 = ", 5 & 3)
print("5 | 3 = ", 5 | 3)
print("5 ^ 3 = ", 5 ^ 3)
print("~5 = ", ~5)
print("5 << 1 = ", 5 << 1)
print("5 >> 1 = ", 5 >> 1)
# 成员运算符
print("3 in [1, 2, 3]", 3 in [1, 2, 3])
print("3 not in [1, 2, 3]", 3 not in [1, 2, 3])
# 身份运算符
print("a is b : ", a is b)
print("a is not b : ", a is not b)