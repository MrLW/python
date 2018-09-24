# 简单推导
x1 = [x*x for x in range(10)]
print(x1)
x2 = [x * x for x in range(10) if x % 4 == 0 ]
print(x2)
x3 = [(x , y ) for x in range(3) for y in range(3)]
print(x3)



girls=['alice','bernice','clarice']
boys = ['chris', 'arnold', 'bob']
# // 实现方法1F
print( [b+'+'+g for b in boys for g in girls if b[0] == g[0]])
# 实现方法2
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
print(letterGirls)

# 字典推导
sauares = {i : "{} squared is {},cubic is {}".format(i,i**2,i**3) for i in range(10)}
print(sauares)

# del 语句
x4 = 1
del x4