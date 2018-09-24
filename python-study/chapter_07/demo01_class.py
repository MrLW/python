_metaclass_=type # 如果使用python2,需要加此行
class Person:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello,world,I am  {}".format(self.name))

foo = Person()
bar = Person()
foo.set_name('Jack')
bar.set_name('Bob')
foo.greet() # 等价于Person.greet(foo)
bar.greet()
# 通过外部访问属性
print(foo.name)
print(bar.name)