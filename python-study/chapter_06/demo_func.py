# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
seq = [1,2,3]
def f1(x) :
    return x * x
print(list(map(f1, [1,2,3])))
# filter
def f2(x):
    return x % 2 == 0
print(list(filter(f2,[1,2,3,4,5])))
# 需要注意的是:这里的reduce返回的不是iterable
from functools import reduce
def f3(x,y) :
    return x + y
print(reduce(f3,[1,2,3,4,5]))
# apply

