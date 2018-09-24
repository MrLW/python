def foo() : x = 42 # 这行代码会创建新的命名空间
x = 1
# 访问全局变量和修改全局变量
external = 'test'
def combine(parameter):print(parameter + external) # 全局变量尽量不要这样访问
combine('python ')
# 当全局变量和局部变量同名时
def combine2(external):print(external + globals()['external'])
combine2('python2 ')
# 告诉函数内变量为全局变量
x = 1
def change_global():
    global x
    x = x + 1
change_global()
print(x)
# 作用域嵌套
def foo():
    def bar():
        print('Hello,world!')
    bar()
# 作用域嵌套的例子
def multiplier(factor):
    def multiplyByFactor(number):
         return number * factor
    return multiplyByFactor
print(multiplier(2)(5))
