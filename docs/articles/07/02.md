## 1. 包的定义
- 包：一个包含多个模块的文件夹，必须包含 __init__.py 文件（Python 3.3+ 后可为空文件）。
- 多层结构：包内可嵌套子包，形成层级组织。

示例：
```text
my_package/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```
## 2. 导入包中的模块
```python
# 导入包内模块
import my_package.module1
my_package.module1.func()

# 从包导入特定模块
from my_package import module1
module1.func()

# 从模块导入特定内容
from my_package.module1 import func
func()

# 导入子包中的模块
from my_package.subpackage import module2
module2.sub_func()
```
## 3. __init__.py 的作用
- 初始化包：可包含包级别的初始化代码。
- 控制导入行为：通过 __all__ 变量指定 from package import * 导入的模块。