class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b ,self.a + self.b
        return self.a
    def __iter__(self):
        return self
# 创建迭代器对象
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
# 使用迭代器创建序列
class TestI :
    value = 0
    def __next__(self):
        self.value += 1
        if self.value >= 10 :
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

t  = TestI()
print(list(t))
