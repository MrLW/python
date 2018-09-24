# 列表的方法
a = [1,2,3]
b = a
b[1] = 4
print(a)
# 下面看copy方法:两个实例
c = [4,5,6]
d = c.copy()
d[1] = 10
print(c)
# extend
a = [1, 2 ,3 ]
b = [4,5,6]
a.extend(b) # 等价于a = a + b 但是性能更好
print(a)

# 高级排序
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len,reverse=True) # 按照长度排序
print(x)