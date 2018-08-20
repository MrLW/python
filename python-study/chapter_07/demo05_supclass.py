# 超类
class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

# 继承超类
class SPAMFilter(Filter):
    def init(self): # 充血超类Filter的init方法
        self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1,2,3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])) # ['eggs', 'bacon']
# 判断一个类是否是另一个类子类
print(issubclass(SPAMFilter,Filter))
# 访问一个类的基类
print(SPAMFilter.__bases__)#(<class '__main__.Filter'>,)
#isInstance()
print(isinstance(f,Filter))# True
# 获取对象属于哪一个类
print(s.__class__) # <class '__main__.SPAMFilter'>
# 判断某个实例是否有某个方法/属性
print(hasattr(f,'filter'))
