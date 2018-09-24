class Class:
    def method(self):
        print('I have a self')
def function():
    print('I do not ...')
instance = Class()
instance.method()
# 可以将属性关联到一个 11 普通函数，但这样就没有特殊的self参数了
instance.method = function
instance.method()