
## 1. 理解
堆栈跟踪就像你站在高楼上，楼下有一层层台阶。当你往下走时，每走一步都会留下一个记录，这就像堆栈中的函数调用记录。
如果你下楼时迈错了一步，你可能会跌倒，就像程序中出现错误一样。堆栈跟踪记录了你从楼顶走到楼底并跌倒的过程，以帮助你找到问题出在哪里。
## 2. 示例
```python
import traceback

def func_a():
    print('在func_a中')
    func_b()
def func_b():
    print('在func_b中')
    x = 1 / 0

try:
    func_a()
except Exception:
    traceback.print_exc()
```
## 3. 结果分析
打印内容：
```
Traceback (most recent call last):
  File "\python-one\codes\04\02.py", line 11, in <module>
    func_a()
    ~~~~~~^^
  File "\python-one\codes\04\02.py", line 5, in func_a
    func_b()
    ~~~~~~^^
  File "\python-one\codes\04\02.py", line 8, in func_b
    x = 1 / 0
        ~~^~~
ZeroDivisionError: division by zero
```
从结果可以看出：  
1）首先调用了func_a，然后func_a调用了func_b。  
2）在func_b中发生了除零错误。  
3）通过打印的堆栈信息可以看出错误的确切位置在“\python-one\codes\04\02.py”的第8行，即func_b函数中。
通过异常堆栈，可以非常清楚地看到错误发生的位置和完整的调用链。    
这可以帮助我们快速定位和修复bug。