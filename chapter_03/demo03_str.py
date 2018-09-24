# 使用format
print("{},{} and {}".format("first","second","third") )
print("{0}, {1} and {2}".format("first", "second", "third"))

from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="π")) # .2f表示使用包含2位小数的浮点数格式

# 如果变量与替换字段同名，还可使用一种简写。在这种情况下，可 使用f字符串——在字符串前面加上f。
from math import e
print(f"Euler constant is roughly {e}") # 等价于"Euler's constant is roughly {e}.".format(e=e)