# 定义函数
def hello(name):
    return 'Hello, ' + name + '!'
print(hello('Bob'))
# 给函数添加文档
def square(x):
    'Calculates the square of the number x'
    return x * x
# 访问文档字符串
print(square.__doc__)
# print(hello(square)) 只能在交互式解释器中运行
print(square(3))
