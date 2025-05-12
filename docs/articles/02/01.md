## 1. 注释
注释用于给代码添加必要的文字说明，注释内容会被Python解释器忽略。
```python
# 单行注释
# 快捷键 Ctrl + /
```
```python
'''
多行注释(块注释),使用3个单引号或者3个双引号
'''
"""
多行注释(块注释),使用3个单引号或者3个双引号
"""
```
注释行#coding=utf-8用来设置Python代码文件的编码集，该注释语句必须放在文件的第一行或第二行才能有效。
```python
# 中文编码注释
#coding=utf-8
```
Python2，默认使用 ASCII 格式，Python3 默认使用 utf-8 格式；所以，python3如果不指定中文编码，打印出的中文也是正确的。
## 2. 标识符
在程序代码中由程序员自定义的名称都成为标识符，例如：变量、常量、函数名、属性、类、模块和包等；

命名基本命名规范：
1. 字符区分大小写；
2. 使用字母、数字和下划线组成，其他字符不行；
3. 首字符一般是字母，也可以是下划线，但一定不能是数字；
4. 不能使用关键字作为标识符；
5. 不要使用Python内置函数；

## 3. 关键字
Python 中一共有 35 个关键字，分别是：  
False、None、True、and、as、assert、async、await、break、class、continue、def、del、elif、else、except、finally、for、from、global、if、import、in、is、lambda、nonlocal、not、or、pass、raise、return、try、while、with、yield
