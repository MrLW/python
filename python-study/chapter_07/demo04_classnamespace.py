# 两行代码等价
def foo(x):return x*x
foo = lambda x : x*x

class C:
    print('Class C being defined...')

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print(m1.members)
m2 = MemberCounter()
m2.init()
print(m2.members)
m1.members = 'Three'
m1.init()
print(m1.members)
print(MemberCounter.members)
print(m2.members)
