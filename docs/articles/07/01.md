在 Python 中，模块（Module）和包（Package）是组织代码的重要方式，它们可以将大型程序拆分成更小、更易管理的部分。
## 1. 模块的定义
一个 .py 文件就是一个模块，用于封装代码（如函数、类、变量），实现复用和避免命名冲突。

## 2. 导入模块
导入方式：使用 `import` 或 `from ... import ...` 语句；
### 2.1. 导入整个模块
```python
import math
print(math.sqrt(4))  # 输出：2.0
```
### 2.2. 导入特定方法
```python
from math import sqrt
print(sqrt(9))  # 输出：3.0
```
### 2.3. 导入并起别名
```python
import math as m
print(m.sqrt(16))  # 输出：4.0
```
### 2.4. 导入所有内容
不推荐这种方式，因为可能导致命名冲突；
```python
from math import *
print(sqrt(25))  # 输出：5.0
```
