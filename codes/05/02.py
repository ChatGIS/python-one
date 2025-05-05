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