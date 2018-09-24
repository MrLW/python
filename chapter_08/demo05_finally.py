x = None
try:
    x = 1 / 0
    print('try code')
finally:
    print('一定会执行的代码',x)
    del x