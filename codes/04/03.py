class MyClass:
    def __init__(self):
        self.__private_variable = 10

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

# 创建类的实例
obj = MyClass()
# 在类内部访问私有变量
print(obj.get_private_variable())

# 在类内部修改私有变量
obj.set_private_variable(20)
print(obj.get_private_variable())

# 创建类的实例
obj = MyClass()
# 通过名称修饰后的名称访问私有变量
print(obj._MyClass__private_variable)


class BankAccount:
    def __init__(self, balance):
        # 私有变量，账户余额
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount} 元，当前余额：{self.__balance} 元。")
        else:
            print("存入金额必须大于 0。")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount} 元，当前余额：{self.__balance} 元。")
        else:
            print("取款失败，金额无效或余额不足。")

    def get_balance(self):
        return self.__balance

# 创建银行账户实例
account = BankAccount(1000)
# 存款操作
account.deposit(500)
# 取款操作
account.withdraw(300)
# 获取账户余额
print(account.get_balance())


class MyClass:
    def __init__(self):
        # 受保护变量
        self._protected_variable = 5
        # 私有变量
        self.__private_variable = 10

# 创建类的实例
obj = MyClass()
# 可以访问受保护变量
print(obj._protected_variable)
# 可以通过名称修饰访问私有变量
print(obj._MyClass__private_variable)


class MyClass:
    def __init__(self):
        pass

    def __private_method(self):
        return "这是一个私有方法"

    def public_method(self):
        # 在类内部调用私有方法
        result = self.__private_method()
        return result

# 创建类的实例
obj = MyClass()
# 通过公共方法间接调用私有方法
print(obj.public_method())

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def __preprocess_data(self):
        # 复杂的预处理逻辑
        return [i * 2 for i in self.data]

    def process_data(self):
        # 调用私有方法进行预处理
        preprocessed_data = self.__preprocess_data()
        # 最终处理逻辑
        result = [i + 1 for i in preprocessed_data]
        return result

# 创建数据处理实例
data = [1, 2, 3, 4, 5]
processor = DataProcessor(data)
# 调用公共方法进行数据处理
print(processor.process_data())