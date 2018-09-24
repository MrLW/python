# exec :将字符串作为代码执行
exec("print('Hello,python')")
# 命名空间的引入
from math import sqrt
scope = {}
exec('sqrt = 1 ',scope) # 参数2表示命名空间,有点类似sqrt为健,1为值,存入scope
print(sqrt(4))
print(scope['sqrt'])

# eval:计算用字符串表示 的Python表达式的值，并返回结果.有返回值.
print(eval(input("Enter an arithmetic expression: ")))

# 可以向exec或者eval提供命名空间,可在使用这个命名空间前加一些值
scope = {}
scope['x'] = 3
scope['y'] = 4
x = 1
y = 2
print(eval('x * y '),scope)