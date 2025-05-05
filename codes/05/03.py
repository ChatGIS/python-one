# try:
#     num1 = int(input("请输入一个整数: "))
#     num2 = int(input("请再输入一个整数: "))
#     result = num1 / num2
#     print(f"结果是: {result}")
# except ValueError:
#     print("输入无效，请输入有效的整数。")
# except ZeroDivisionError:
#     print("错误: 除数不能为零。")

# try:
#     num = int("abc")
#     result = 1 / 0
# except (ValueError, ZeroDivisionError):
#     print("发生了值错误或除零错误。")

# try:
#     num = 1 / 0
# except:
#     print("发生了一个异常。")

# try:
#     num = 1 / 0
# except Exception as e:
#     print(f"发生了异常: {e}")

# try:
#     num1 = int(input("请输入一个整数: "))
#     num2 = int(input("请再输入一个整数: "))
#     result = num1 / num2
# except ValueError:
#     print("输入无效，请输入有效的整数。")
# except ZeroDivisionError:
#     print("错误: 除数不能为零。")
# else:
#     print(f"结果是: {result}")

try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件未找到。")
finally:
    if 'file' in locals():
        file.close()